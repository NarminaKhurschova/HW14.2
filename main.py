from functions import search_data_by_title, view_in_json, search_by_realise_year, search_by_genre
from flask import Flask, jsonify, request, render_template, Blueprint
from rating.views import rating_blueprint

app = Flask(__name__)


app.register_blueprint(rating_blueprint)


@app.route("/search")
def searching_by_title():
    title = request.args.get('s')
    list_param = ['title', 'country', 'release_year', 'listed_in', 'description']
    found = search_data_by_title(title, list_param)
    all_found_dict = view_in_json(found[0], list_param)
    return jsonify(all_found_dict)


@app.route('/movie/<title>')
def about_movie(title):
    list_param = ['title', 'country', 'release_year', 'listed_in', 'description']
    all_about_movie = search_data_by_title(title, list_param)
    all_about_movie_dict = view_in_json(all_about_movie[0], list_param)
    return render_template('about_movie.html', about_movie=all_about_movie_dict)


@app.route('/movie/year/to/year')
def search_by_realise():
    min_year = request.args.get('s')
    max_year = request.args.get('d')
    list_param = ['title', 'release_year']
    list_mov = []
    all_movies = search_by_realise_year(min_year, max_year, list_param)
    for movie in all_movies:
        movie_dict = view_in_json(movie, list_param)
        list_mov.append(movie_dict)
    return render_template('all_by_year.html', min_year=min_year, max_year=max_year, list_mov=list_mov)


@app.route('/genre/<genre>')
def search_with_genre(genre):
    list_of_movies_dict = []
    list_param = ['title', 'description']
    all_movies = search_by_genre(list_param, genre)
    for movie in all_movies:
        movie_dict = view_in_json(movie, list_param)
        list_of_movies_dict.append(movie_dict)

    return render_template('by_genre.html', genre=genre, list_of_movies_dict=list_of_movies_dict)








app.run(port=8000, debug=True)
