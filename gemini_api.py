import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sqlite3

def get_user_favorites():
    connection = sqlite3.connect("media.db")  # Add your DB path
    cursor = connection.cursor()

    cursor.execute("SELECT title FROM Movies")
    movie_results = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT title FROM Shows")
    show_results = [row[0] for row in cursor.fetchall()]

    connection.close()
    return movie_results + show_results


def generate_recommendation(user_message):
    load_dotenv()
    client = genai.Client()
    
    favorites = get_user_favorites()
    context = f"User's favorite movies/shows: {', '.join(favorites)}. Based on these, respond to the user's prompt: '{user_message}'"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a professional and kind movie/show recommender.",
        ),
        contents=context,
    )

    return response.text
