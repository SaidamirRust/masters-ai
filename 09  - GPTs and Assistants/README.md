# 1. API Key Security
## Risk:
Exposing API keys in the codebase can lead to unauthorized access and potential abuse.

## Countermeasure:

We store API keys using environment variables instead of hardcoding them in the source code.
Example: os.getenv("OPENAI_API_KEY") in agent.py
This prevents accidental exposure if the code is pushed to a public repository.
API rate limits and restrictions should be set in the respective API provider dashboards.

# 2. Data Leakage Prevention
## Risk:
Sending the entire restaurant review dataset to the LLM could expose sensitive business information.

## Countermeasure:

We limit the data sent to the LLM by extracting only relevant chunks from restaurant_reviews.csv using sampling (df.sample(5)).
This ensures that the LLM only processes a subset of the data instead of the full dataset.
If using a database in the future, we can implement query-based extraction rather than loading the entire table.

# 3. User Input Sanitization (Prompt Injection Prevention)
## Risk:
Malicious users could craft prompts that manipulate the AI into returning unintended or harmful responses.

## Countermeasure:

We strictly define the system prompt in agent.py to ensure the AI stays within its scope:

    system_message = "You are a restaurant insights assistant. Use the provided review data to answer user queries accurately."
We log user queries (in utils.py) to track potential misuse and detect anomalies.
In the future, additional measures like regex filtering and predefined query formats can be implemented to sanitize user input.

# 4. Secure External API Calls
## Risk:
Unverified or incorrectly formatted API requests could cause service failures or unexpected behavior.

## Countermeasure:

We validate user inputs before sending them to external APIs (api_tools.py):

    if not location or not cuisine:
        return "Error: Location and cuisine type must be provided."

Exception handling ensures that failures in API calls do not crash the application:

    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        return f"Error: {e}"
Rate limiting & retries can be added to avoid API request flooding.

# 5. Logging & Monitoring
## Risk:
Undetected errors or attacks can cause prolonged downtime or data breaches.

## Countermeasure:

We implemented logging in utils.py, which tracks API interactions, errors, and user queries:

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
Logging helps detect suspicious activities, such as repeated failed API calls or anomalous user input patterns.
Logs can be stored and analyzed for debugging and security audits.

# 6. Streamlit Session Security
## Risk:
Session-based attacks (e.g., Cross-Site Scripting) could manipulate UI elements.

## Countermeasure:

Session state is initialized properly (st.session_state), reducing unexpected session behavior.
User inputs are not executed as code, preventing code injection vulnerabilities.
