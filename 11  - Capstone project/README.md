# Restaurant Insights Agent

## Overview

The Restaurant Insights Agent is an AI-powered application that provides insights into restaurant reviews and recommendations. It utilizes OpenAI's GPT-4o for natural language processing and interacts with external APIs for restaurant data retrieval. The user interface is built using Streamlit.

## Features

- AI-Powered Chat: Ask questions about restaurant reviews and get insights.

- Restaurant Recommendations: Retrieve top restaurants based on location and cuisine.

- Business Insights Dashboard: Displays key metrics such as total reviews, average sentiment, and top restaurants.

- Logging: All interactions are logged for monitoring and debugging.

## Installation Prerequisites

Ensure you have Python 3.12 installed.

## Create a Virtual Environment

    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows

## Install Dependencies

    pip install -r requirements.txt

## Configuration

Create a .env file in the project root and add the following keys:

    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_PLACES_API_KEY=your_google_places_api_key

## Running the Application

Start the Streamlit app with: 

    streamlit run main.py

