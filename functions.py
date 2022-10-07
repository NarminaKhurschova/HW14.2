import sqlite3


def data_from_netflix(query):
    """
    query - sql запрос, формирующийся в каждой поисковой функции отдельно
    """
    con = sqlite3.connect('netflix.db')
    cur = con.cursor()
    query_data = query
    cur.execute(query_data)
    executed_query = cur.fetchall()
    return executed_query


def search_data_by_title(title_mult, list_param):
    """
    Поиска по названию
    :param title_mult: название фильма/сериала
    :param list_param: список столбцов формирующейся таблицы
    :return: кортеж значений столбцов
    """
    movie_in_tuple = data_from_netflix(f"""SELECT {",".join(list_param)}
                                    FROM netflix 
                                    WHERE title 
                                    LIKE \"%{title_mult.lower()}%\"
                                    GROUP BY title
                                    HAVING MAX(release_year) 
                                    """)

    return movie_in_tuple


def view_in_json(data, list_param):
    """Преобразование кортежа в словарь"""
    dict_mov = {}
    for index, param in enumerate(list_param):
        dict_mov[param] = data[index]
    return dict_mov


def search_by_realise_year(min_year, max_year, list_param):
    """
    Поиск фильмов/сериалов по диапазону лет
    :param min_year: начало диапазона
    :param max_year: конец
    :param list_param: список столбцов для sql запроса
    :return: список кортежей
    """
    data_search_by_realise_year = data_from_netflix(f"""SELECT {','.join(list_param)}
                                               FROM netflix
                                               WHERE release_year BETWEEN {min_year} AND {max_year}
                                               ORDER BY release_year ASC
                                               LIMIT 100
                                                """)
    return data_search_by_realise_year


def search_by_genre(list_param, name_of_genre):
    """
    Поиск по жанру
    :param list_param: список столбцов для sql запроса
    :param name_of_genre: жанр
    :return: кортеж
    """
    data_search_by_genre = data_from_netflix(f"""
                                            SELECT {','.join(list_param)}
                                            FROM netflix
                                            WHERE listed_in LIKE '%{name_of_genre}%'
                                            """)
    return data_search_by_genre


def search_by_type_release_date_genre(type, release_year, genre):
    """
    Поиск по типу, дате выпуска, жанру
    :param type: Тип
    :param release_year: дата выпуска
    :param genre: жанр
    :return: кортеж
    """
    data_search_by = data_from_netflix(f"""
                                        SELECT title, description, listed_in
                                        FROM netflix
                                        WHERE `type` LIKE '%{type}%'
                                        AND release_year = {int(release_year)}
                                        AND listed_in LIKE '%{genre}%'
                                        """)

    return data_search_by





def search_by_two_in_cast(first_name, second_name):
    """Поиск актеров, которые играли с выбранными актерами повторно"""
    data_search_by_names = data_from_netflix(f"""
                                            SELECT `cast`
                                            FROM netflix
                                            WHERE `cast` LIKE ('%{first_name}% %{second_name}%')
                                            """)
    actors = []
    is_actors = []
    dub_actors = set()

    for movie in data_search_by_names:
        for actor in movie:
            actors.extend(actor.split(','))

    for actor in actors:
        if actor not in is_actors:
            is_actors.append(actor)
        else:
            dub_actors.add(actor)

    return dub_actors



print(search_by_two_in_cast("Rose McIver", "Ben Lamb"))



    



