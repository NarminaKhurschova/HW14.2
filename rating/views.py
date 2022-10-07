from flask import Blueprint, render_template
from functions import view_in_json, data_from_netflix
from rating.functions import movies_with_rating_order, movies_from_selected_rating_list

rating_blueprint = Blueprint('rating_blueprint', __name__, template_folder='templates_r')


list_param = ['title', 'rating', 'description']


@rating_blueprint.route('/rating')
def rating_select():
    """Выбор рейтинга"""

    return render_template('all_ratings.html')


@rating_blueprint.route('/rating/children')
def rating_children():
    """Фильмы для просмотра с детьми"""
    list_of_movie_dicts = []
    list_of_rating_names = ['G']
    movies_from_netflix = movies_with_rating_order(list_param)
    for movie in movies_from_netflix:
        movie_in_dict = view_in_json(movie, list_param)
        list_of_movie_dicts.append(movie_in_dict)

    movies_for_children = movies_from_selected_rating_list(list_of_movie_dicts, list_of_rating_names)
    return render_template('for_childrens.html', movies_for_children=movies_for_children)


@rating_blueprint.route('/rating/family')
def rating_family():
    """Фильмы для семейного просмотра"""
    list_of_movie_dicts = []
    list_of_rating_names = ['G', 'PG', 'PG-13']
    movies_from_netflix = movies_with_rating_order(list_param)
    for movie in movies_from_netflix:
        movie_in_dict = view_in_json(movie, list_param)
        list_of_movie_dicts.append(movie_in_dict)

    movies_for_family = movies_from_selected_rating_list(list_of_movie_dicts, list_of_rating_names)
    return render_template('for_family.html', movies_for_family=movies_for_family)


@rating_blueprint.route('/rating/adults')
def rating_adult():
    """Фильмы для просмотра только взрослыми"""
    list_of_movie_dicts = []
    list_of_rating_names = ['R', 'NC-17']
    movies_from_netflix = movies_with_rating_order(list_param)
    for movie in movies_from_netflix:
        movie_in_dict = view_in_json(movie, list_param)
        list_of_movie_dicts.append(movie_in_dict)

    movies_for_adult = movies_from_selected_rating_list(list_of_movie_dicts, list_of_rating_names)
    return render_template('for_adult.html', movies_for_adult=movies_for_adult)

