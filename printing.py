#!/usr/bin/env python
# Printing functions
from reports import *


def print_count_games(file_name):
    answer1 = count_games(file_name)
    print ("How many games are in the file?\n", answer1, end="\n"*2)


def print_decide(file_name, year):
    answer2 = decide(file_name, year)
    print ("Is there a game from {}?\n".format(year), answer2, end="\n"*2)


def print_get_latest(file_name):
    answer3 = get_latest(file_name)
    print ("Which was the latest game?\n", answer3, end="\n"*2)


def print_count_by_genre(file_name, genre):
    answer4 = count_by_genre(file_name, genre)
    print ("How many {} games do we have?\n".format(genre.lower()), answer4, end="\n"*2)


def print_get_line_number_by_title(file_name, title):
    answer5 = get_line_number_by_title(file_name, title)
    print ("What is the line number of {}?\n".format(title), answer5, end="\n"*2)


def print_sort_abc(file_name):
    answer6 = sort_abc(file_name)
    print ("Alphabetically sorted list of games: ")
    print ("\n".join(answer6), end="\n"*2)


def print_get_genres(file_name):
    answer7 = get_genres(file_name)
    print ("The genres of games are: ")
    print ("\n".join(answer7), end="\n"*2)


def print_when_was_top_sold_fps(file_name):
    answer8 = when_was_top_sold_fps(file_name)
    print ("When was the top sold first-person shooter game was published?\n", answer8, end="\n"*2)


print_count_games("game_stat.txt")
print_decide("game_stat.txt", 2011)
print_get_latest("game_stat.txt")
print_count_by_genre("game_stat.txt", "First-person shooter")
print_get_line_number_by_title("game_stat.txt", "Diablo III")
print_sort_abc("game_stat.txt")
print_get_genres("game_stat.txt")
print_when_was_top_sold_fps("game_stat.txt")
