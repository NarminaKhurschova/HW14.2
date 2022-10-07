from functions import data_from_netflix


def movies_with_rating_order(list_param):
    """Все фильмы отсортированный по рейтингу"""
    search_by_rating_netflix = data_from_netflix(f"""SELECT {','.join(list_param)}
                                                FROM netflix
                                                WHERE rating != ''
                                                ORDER BY rating
                                                """)

    return search_by_rating_netflix


def movies_from_selected_rating_list(dict_movie, list_of_rating):
    """Фильмы из выбранного рейтинга"""
    selected_movies = []
    for movie in dict_movie:
        if movie['rating'] in list_of_rating:
            selected_movies.append(movie)

    return selected_movies