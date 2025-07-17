from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

def search_tv_shows(query):
    """Search for TV shows using TMDB API intake a query"""
    url = "https://api.themoviedb.org/3/search/tv"
    params = {
        "api_key": api_key,
        "query": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results")

def search_movies(query):
    """Search for Movies using TMDB API intake a query
    Keys: dict_keys('page', 'results', 'total_pages', 'total_results')"""
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": query
    }

    response = requests.get(url, params=params)
    data = response.json()
    # dict_keys(['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'title', 'video', 'vote_average', 'vote_count']),
    print(data["results"][0]["backdrop_path"])
    return data.get("results")

print(search_movies("Inception"))