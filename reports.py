#!/usr/bin/env python
# Report functions


def file_processing(file_name):
    games_list = []
    with open(file_name, "r") as file:
        for line in file:
            games_list.append(line.strip().split("\t"))
    return games_list


def count_games(file_name):
    games_list = file_processing(file_name)
    games_amount = len(games_list)
    return games_amount


def decide(file_name, year):
    games_list = file_processing(file_name)
    for item in games_list:
        if item[2] == str(year):
            return True
    return False


def get_latest(file_name):
    games_list = file_processing(file_name)
    latest = 0
    for item in games_list:
        if int(item[2]) > latest:
            latest = int(item[2])
    for item in games_list:
        if int(item[2]) == latest:
            return item[0]


def count_by_genre(file_name, genre):
    games_list = file_processing(file_name)
    games_of_spec_genre = []
    for item in games_list:
        if item[3] == genre:
            games_of_spec_genre.append(item[0])
    return len(games_of_spec_genre)


def get_line_number_by_title(file_name, title):
    games_list = file_processing(file_name)
    for item in games_list:
        if item[0] == title:
            return games_list.index(item) + 1
    raise ValueError
    return


def sort_abc(file_name):
    games_list = file_processing(file_name)
    titles = []
    for item in games_list:
        titles.append(item[0])
    iterations = 1
    while iterations < len(titles):
        j = 0
        while j <= len(titles)-2:
            if titles[j] > titles[j+1]:
                temporary = titles[j]
                titles[j] = titles[j+1]
                titles[j+1] = temporary
            j += 1
        else:
            iterations += 1
    return titles


def get_genres(file_name):
    games_list = file_processing(file_name)
    genres = []
    for item in games_list:
        if item[3] not in genres:
            genres.append(item[3])
        else:
            continue
    return sorted(genres, key=lambda item: item.lower())


def when_was_top_sold_fps(file_name):
    games_list = file_processing(file_name)
    copies_sold_fps = []
    for item in games_list:
        if item[3] == "First-person shooter":
            copies_sold_fps.append(float(item[1]))
    if not copies_sold_fps:
        raise ValueError
        return
    max_sold = max(copies_sold_fps)
    for item in games_list:
        if float(item[1]) == max_sold:
            return int(item[2])
