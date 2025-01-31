import openai
import os
import pandas as pd
from utils import LOGGER

# Load API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    LOGGER.error("OpenAI API key is missing.")

# Load Restaurant Reviews CSV
DATA_PATH = "restaurant_reviews.csv"
df = pd.read_csv(DATA_PATH)
LOGGER.info("Loaded restaurant reviews dataset in agent.")

def get_relevant_reviews(user_query, num_reviews=5):
    """
    Retrieves reviews relevant to the user's query.
    If no relevant reviews are found, fallback to random samples.
    """
    query_keywords = user_query.lower().split()

    filtered_df = df[
        df.apply(lambda row: any(keyword in str(row["Review"]).lower() for keyword in query_keywords), axis=1)]

    if not filtered_df.empty:
        relevant_reviews = filtered_df.sample(min(num_reviews, len(filtered_df))).to_dict(orient="records")
    else:
        relevant_reviews = df.sample(num_reviews).to_dict(orient="records")

    return relevant_reviews


def query_agent(user_query, conversation_history=""):
    """
    Processes user query using GPT-4o with memory and relevant restaurant review data.
    """
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing."

    # Extract relevant reviews based on query
    relevant_reviews = get_relevant_reviews(user_query)
    context = "\n".join(
        [f"{r['Restaurant Name']} ({r['Country']}): {r['Sentiment']} - {r['Review']}" for r in relevant_reviews])

    system_message = (
            "You are a restaurant insights assistant. "
            "Use the following review data to answer user questions:\n\n" + context
    )

    # Build message history for memory
    messages = [{"role": "system", "content": system_message}]

    if conversation_history:
        messages.append({"role": "user", "content": conversation_history})

    messages.append({"role": "user", "content": user_query})

    try:
        LOGGER.info("Sending query to OpenAI API.")
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=200
        )
        LOGGER.info("Received response from OpenAI API.")
        return response.choices[0].message.content.strip()

    except openai.APIError as e:
        LOGGER.error(f"OpenAI API Error: {e}")
        return f"OpenAI API Error: {e}"
