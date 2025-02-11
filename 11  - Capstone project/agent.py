import json
import openai
import os
import sqlite3
from utils import LOGGER

# Load API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    LOGGER.error("OpenAI API key is missing.")

# Database connection
DB_PATH = "restaurant_reviews.db"

def execute_sql_query(query, params=()):
    """Executes an SQL query on the SQLite database."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
    except sqlite3.Error as e:
        LOGGER.error(f"Database error: {e}")
        return []


def query_agent(user_query, conversation_history=""):
    """
    Processes user query using GPT-4o with memory, relevant restaurant review data, OpenAI's function calling for SQL-based data retrieval.
    """
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing."

    system_message = (
        "You are a knowledgeable restaurant review assistant. "
        "Analyze SQL query results and generate insightful, structured responses. "
        "Do not return raw database results—interpret them naturally. "
        "Summarize overall sentiment, highlight key trends, and suggest relevant insights. "
        "If the reviews mention recurring themes (e.g., great service, bad food), point them out."
    )

    # Build message history for memory
    messages = [{"role": "system", "content": system_message}]

    if conversation_history:
        messages.append({"role": "user", "content": conversation_history})

    messages.append({"role": "user", "content": user_query})

    try:
        LOGGER.info("Sending query to OpenAI API with function calling.")
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=[
                {
                    "name": "execute_sql_query",
                    "description": "Execute an SQL query on the restaurant review database.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "The SQL query to execute."},
                            "params": {"type": "array", "items": {"type": "string"}, "description": "Query parameters."}
                        },
                        "required": ["query"]
                    }
                }
            ],
            function_call="auto",
            max_tokens=500
        )

        LOGGER.info("Received response from OpenAI API.")
        response_message = response.choices[0].message

        if hasattr(response_message, "function_call") and response_message.function_call:
            func_name = response_message.function_call.name
            func_args = json.loads(response_message.function_call.arguments)

            if func_name == "execute_sql_query":
                query = func_args.get("query")
                params = func_args.get("params", [])
                results = execute_sql_query(query, params)

                # Pass results back to OpenAI for AI-generated response
                ai_context = f"Here are the restaurant reviews: {results}. Based on this, summarize the insights."
                messages.append({"role": "assistant", "content": ai_context})

                ai_response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    max_tokens=500
                )

                return ai_response.choices[0].message.content.strip()

        return response_message.content.strip() if response_message.content else "No valid response."

    except openai.APIError as e:
        LOGGER.error(f"OpenAI API Error: {e}")
        return f"OpenAI API Error: {e}"
    except json.JSONDecodeError as e:
        LOGGER.error(f"Error decoding JSON from OpenAI response: {e}")
        return "Error: Failed to parse OpenAI function call arguments."
    except Exception as e:
        LOGGER.error(f"Unexpected error: {e}")
        return "An unexpected error occurred."
