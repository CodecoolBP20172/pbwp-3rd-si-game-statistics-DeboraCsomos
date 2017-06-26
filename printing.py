#!/usr/bin/env python
# Printing functions
from reports import *


# asking for input from Judy to be able to answer her annoyingly ignorant questions instead of watching the new
# episode of Silicon Valley
data_file = input("Give name of data file (e.g. game_stat.txt): \n")
year = int(input("Enter year for question 2 (e.g. 1999):\n"))
genre = input("Enter genre for question 4 (e.g. RPG): \n")
title = input("Enter title for question 5 (e.g. Diablo II): \n")


# prints the number of games in database
def print_count_games(file_name):
    answer1 = count_games(file_name)
    print ("How many games are in the file?\n", answer1, end="\n"*2)


# prints True if there is a game from the given year in the database, False otherwise
def print_decide(file_name, year):
    answer2 = decide(file_name, year)
    print ("Is there a game from {}?\n".format(year), answer2, end="\n"*2)


# prints the title of tha latest game in the database
def print_get_latest(file_name):
    answer3 = get_latest(file_name)
    print ("Which was the latest game?\n", answer3, end="\n"*2)


# prints the number of games by the given genre
def print_count_by_genre(file_name, genre):
    answer4 = count_by_genre(file_name, genre)
    print ("How many {} games do we have?\n".format(genre.lower()), answer4, end="\n"*2)


# prints the line number of the game by the given title
def print_get_line_number_by_title(file_name, title):
    answer5 = get_line_number_by_title(file_name, title)
    print ("What is the line number of {}?\n".format(title), answer5, end="\n"*2)


# prints the alphabetically sorted list of games
def print_sort_abc(file_name):
    answer6 = sort_abc(file_name)
    print ("Alphabetically sorted list of games: ")
    print ("\n".join(answer6), end="\n"*2)


# prints the alphabetically sorted list of genres in the database without duplicates
def print_get_genres(file_name):
    answer7 = get_genres(file_name)
    print ("The genres of games are: ")
    print ("\n".join(answer7), end="\n"*2)


# prints the name of the top sold first-person shooter game
def print_when_was_top_sold_fps(file_name):
    answer8 = when_was_top_sold_fps(file_name)
    print ("When was the top sold first-person shooter game was published?\n", answer8, end="\n"*2)


print_count_games(data_file)
print_decide(data_file, year)
print_get_latest(data_file)
print_count_by_genre(data_file, genre)
print_get_line_number_by_title(data_file, title)
print_sort_abc(data_file)
print_get_genres(data_file)
print_when_was_top_sold_fps(data_file)
