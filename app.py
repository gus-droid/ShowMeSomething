from flask import Flask, redirect, url_for, render_template, request
from movie_api import search_tv_shows, search_movies
from db.db_operations import *
from gemini_api import generate_recommendation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_message = request.form.get("message")
        response = generate_recommendation(user_message)
    return render_template("chat.html", response=response)

@app.route("/media")
def media():
    movies = get_all_movies()
    shows = get_all_shows()
    return render_template("media.html", movies=movies, shows=shows)


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    content = []

    if request.method == "POST":
        query = request.form.get("content")
        search_type = request.form.get("type")

        if query:
            if search_type == "tv":
                content = search_tv_shows(query)
            elif search_type == "movie":
                content = search_movies(query)

    return render_template("recommend.html", content=content)

'''Logic to add movie/show to table'''
@app.route("/add_liked", methods=["POST"])
def add_liked():
    title = request.form.get("title")
    image = request.form.get("image")
    tmdb_id = request.form.get("tmdb_id")
    media_type = request.form.get("media_type")

    if title and tmdb_id and media_type:
        add_liked_content(title, image, tmdb_id, media_type)

    return redirect(url_for("recommend"))

'''Logic to delete movie/show from table'''
@app.route("/delete_liked", methods=["POST"])
def delete_liked():
    tmdb_id = request.form.get("tmdb_id")
    media_type = request.form.get("media_type")

    if tmdb_id and media_type:
        delete_liked_content(tmdb_id, media_type)

    return redirect(url_for("media"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
