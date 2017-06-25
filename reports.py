#!/usr/bin/env python
# Report functions


def file_processing(file_name):
    games_list = []
    with open(file_name, "r") as f:
        for line in f:
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


# def get_latest(file_name):

# print (count_games("game_stat.txt"))
# print (decide("game_stat.txt", 2011))
