import sqlite3

"""Query to insert/like a movie"""
def insert_movie(title, image, tmdb_id):
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()
    cursor.execute('''
                   INSERT INTO Movies (image, title, TMDBid) VALUES (?, ?, ?)''', (image, title, tmdb_id))
    connection.commit()
    connection.close()

"""Query to insert/like a show"""
def insert_show(title, image, tmdb_id):
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()
    cursor.execute('''
                   INSERT INTO Shows (image, title, TMDBid) VALUES (?, ?, ?)''', (image, title, tmdb_id))
    connection.commit()
    connection.close()

"""Query to delete/unlike a movie"""
def delete_movie(title):
    connection = sqlite3.connect('media.db')
    cursor = connection.cursor()
    cursor.execute('''
                   DELETE FROM Movies WHERE title = ?
                   ''', (title,))
    connection.commit()
    connection.close()

"""Query to delete/unlike a show"""
def delete_show(title):
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()
    cursor.execute('''
                    DELETE FROM Shows WHERE title=?''', (title,))
    connection.commit()
    connection.close()

"""Query to return a list ofa ll movies added to user likes
Steps:
1.) Establish a connection
2.) Allow to curse
3.) execute a query
4.) fetch the query in results
5.) close connection
6.) return results"""
def get_all_movies():
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT * FROM Movies;''')
    results = cursor.fetchall()
    connection.close()
    return results


"""Query to return a list of all the shows added to user likes"""
def get_all_shows():
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT * FROM Shows;''')
    results = cursor.fetchall()
    connection.close()
    return results

"""Function to add to either the Movie or Show table"""
def add_liked_content(title, poster_path, tmdb_id, media_type):
    conn = sqlite3.connect("media.db")
    cursor = conn.cursor()

    if media_type == "movie":
        table = "Movies"
    else:  # tv shows
        table = "Shows"

    cursor.execute(
        f"INSERT OR IGNORE INTO {table} (image, title, TMDBid) VALUES (?, ?, ?)",
        (poster_path, title, tmdb_id),
    )
    conn.commit()
    conn.close()

"""Function to remove either the Movie or Show table"""
def delete_liked_content(tmdb_id, media_type):
    connection = sqlite3.connect("media.db")
    cursor = connection.cursor()

    if media_type == "movie":
        cursor.execute("DELETE FROM Movies WHERE TMDBid = ?", (tmdb_id,))
    elif media_type == "tv":
        cursor.execute("DELETE FROM Shows WHERE TMDBid = ?", (tmdb_id,))

    connection.commit()
    connection.close()