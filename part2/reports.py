#!/usr/bin/env python
# Report functions

import math


# processes the given database so the other functions can use it
def file_processing(file_name):
    try:
        with open(file_name, "r") as file:
            games_list = [line.strip().split("\t") for line in file]
        return games_list
    except FileNotFoundError:
        print ("Cannot locate file. Run script again and give an existing datafile!")
        exit()


# returns the list of sold_copies as many other function need info from it
def get_sold_copies(games_list):
    sold_copies = [float(item[1]) for item in games_list]
    return sold_copies


# returns the title of the most played game in the database
def get_most_played(file_name):
    games_list = file_processing(file_name)
    sold_copies = get_sold_copies(games_list)
    most_sold_copies = max(sold_copies)
    most_played_games = [item[0] for item in games_list if float(item[1]) == most_sold_copies]
    return most_played_games[0]


# returns the total of copies sold according to the database
def sum_sold(file_name):
    games_list = file_processing(file_name)
    sold_copies = get_sold_copies(games_list)
    return sum(sold_copies)


# returns the average of copies sold according to the database
def get_selling_avg(file_name):
    games_list = file_processing(file_name)
    sold_copies = get_sold_copies(games_list)
    return sum(sold_copies) / len(sold_copies)


# finds the game with the longest title in the database and returns its length
def count_longest_title(file_name):
    games_list = file_processing(file_name)
    titles = []
    for item in games_list:
        titles.append(item[0])
    return len(max(titles, key=len))


# returns the average of releasing dates according to the database
def get_date_avg(file_name):
    games_list = file_processing(file_name)
    release_dates = [int(item[2]) for item in games_list]
    return math.ceil(round(sum(release_dates) / len(release_dates)))


# gets all available info about the given game
def get_game(file_name, title):
    games_list = file_processing(file_name)
    for item in games_list:
        if item[0] == title:
            item[1] = float(item[1])
            item[2] = int(item[2])
            return item


# counts how many games are in the given database by genre
def count_grouped_by_genre(file_name):
    games_list = file_processing(file_name)
    group_by_genre = {}
    for item in games_list:
        if item[3] not in group_by_genre:
            group_by_genre[item[3]] = 1
        else:
            group_by_genre[item[3]] += 1
    return group_by_genre


# gives the alphabetically- and descending date-ordered list of games in the database
def get_date_ordered(file_name):
    games_list = file_processing(file_name)
    games_by_date = {}
    for item in games_list:
        games_by_date[item[0]] = item[2]
    sorted_list_of_games_by_date = sorted(sorted(games_by_date, key=lambda item: item.lower()),
                                          key=games_by_date.__getitem__, reverse=True)
    return sorted_list_of_games_by_date
