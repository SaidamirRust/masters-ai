import streamlit as st
from agent import query_agent
from api_tools import get_restaurant_recommendations
from utils import LOGGER
import pandas as pd

st.set_page_config(page_title="Restaurant Insights Agent", layout="wide")
LOGGER.info("Streamlit app started.")

st.title("🍽️ Restaurant Insights Agent")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = []  # Ensure it is initialized as a list

# Sidebar - Restaurant Finder
st.sidebar.header("Find Restaurants")
location = st.sidebar.text_input("Enter Location", placeholder="e.g., New York")
cuisine = st.sidebar.text_input("Cuisine Type", placeholder="e.g., Italian")

if st.sidebar.button("Get Recommendations"):
    LOGGER.info(f"Fetching recommendations for location: {location}, cuisine: {cuisine}")
    recommendations = get_restaurant_recommendations(location, cuisine)
    if isinstance(recommendations, str):  # If an error message is returned
        st.error(recommendations)
    else:
        st.subheader("Top Restaurant Recommendations:")
        for r in recommendations:
            st.write(f"**{r['name']}** - {r['address']}")

# Sidebar - Chat with AI
st.sidebar.header("Chat with the AI")
user_query = st.sidebar.text_area("Ask about restaurant insights", placeholder="e.g., What are common sentiments for a restaurant in Paris?")

if st.sidebar.button("Ask AI"):
    if user_query.strip():
        # Prepare conversation history as context
        conversation_history = "\n".join(
            [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state["messages"]])
        LOGGER.info(f"User query: {user_query}")
        response = query_agent(user_query, conversation_history)  # Pass history to agent
        LOGGER.info(f"AI Response: {response}")
        # Store user message and AI response in session state
        st.session_state["messages"].append({"role": "user", "content": user_query})
        st.session_state["messages"].append({"role": "assistant", "content": response})
    else:
        LOGGER.warning("User submitted an empty query.")
        st.warning("Please enter a question.")

# Display chat history
st.subheader("AI Conversation")
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"👤 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **AI:** {msg['content']}")

# Sidebar Business Insights Section
st.sidebar.subheader("📊 Business Insights")

# Load the restaurant reviews dataset
df = pd.read_csv("restaurant_reviews.csv")
LOGGER.info("Loaded restaurant reviews dataset.")

# Convert sentiment to numeric values
sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
df["Sentiment"] = df["Sentiment"].map(sentiment_mapping)

# Handle missing values after mapping
df = df.dropna(subset=["Sentiment"])

col1, col2, col3 = st.columns(3)
with col1:
    total_reviews = df.shape[0]
    st.sidebar.metric(label="Total Reviews", value=total_reviews)

with col2:
    avg_sentiment = df["Sentiment"].mean()  # Assuming Sentiment is numerical (-1 to 1)
    st.sidebar.metric(label="Avg Sentiment Score", value=round(avg_sentiment, 2))

with col3:
    top_restaurant = df.groupby("Restaurant Name")["Sentiment"].mean().idxmax()
    st.sidebar.metric(label="🏆 Top Restaurant", value=top_restaurant)
