import os
import requests

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")
GOOGLE_PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def get_restaurant_recommendations(location, cuisine):
    """Fetches restaurant recommendations from Google Places API."""
    if not GOOGLE_PLACES_API_KEY:
        return "Error: Google Places API key is missing."

    params = {
        "query": f"{cuisine} restaurants in {location}",
        "key": GOOGLE_PLACES_API_KEY
    }

    try:
        response = requests.get(GOOGLE_PLACES_URL, params=params)
        data = response.json()

        if "error_message" in data:
            return f"Google API Error: {data['error_message']}"

        if not data.get("results"):
            return "No restaurants found for this query."

        return [
            {
                "name": place.get("name", "Unknown"),
                "address": place.get("formatted_address", "No address available")
            }
            for place in data["results"][:5]
        ]

    except requests.RequestException as e:
        return f"API Request failed: {e}"