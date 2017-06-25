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
