#!/usr/bin/env python
# Printing functions
from reports import *


# prints the most played game
def print_get_most_played(file_name):
    answer1 = get_most_played(file_name)
    print ("Which is the most played game?\n", answer1, end="\n"*2)


# prints the total copies sold
def print_sum_sold(file_name):
    answer2 = sum_sold(file_name)
    print ("How many copies have been sold in total?\n", answer2, end="\n"*2)


# prints the average of sold copies
def print_get_selling_avg(file_name):
    answer3 = get_selling_avg(file_name)
    print ("How many copies have been sold on the average?\n", round(answer3, 3), end="\n"*2)


# prints the length of the longest game title
def print_count_longest_title(file_name):
    answer4 = count_longest_title(file_name)
    print ("How long is the longest title?\n", answer4, end="\n"*2)


# prints
def print_get_date_avg(file_name):
    answer5 = get_date_avg(file_name)
    print ("What is the average of the releasing dates?\n", answer5, end="\n"*2)


# prints the properties of the given game
def print_get_game(file_name, title):
    try:
        answer6 = get_game(file_name, title)
        for i, item in enumerate(answer6):
            answer6[i] = str(item)
        properties = ["name", "copies sold", "release date", "genre", "publisher"]
        print ("The properties of {} are the following:".format(title))
        for i, prop in enumerate(properties):
            print ("{}: {}".format(properties[i], answer6[i]))
        print ("\n")
    except TypeError:
        print ("Game not found\n")


# prints genres and the number of games rated in that genre
def print_count_grouped_by_genre(file_name):
    answer7 = count_grouped_by_genre(file_name)
    print ("How many games are there by genre?")
    for key, value in answer7.items():
        print ("{}: {}".format(key, value), end="\n")
    print ("\n")


# prints the list of the games ordered by their release date (descending)
def print_get_date_ordered(file_name):
    answer8 = get_date_ordered(file_name)
    print ("The date-ordered (descending) list of games is the following:")
    print ("\n".join(answer8), end="\n"*2)


def main():
    data_file = input("Give name of data file (e.g. game_stat.txt): \n")
    title = input("Enter title for question 6 (e.g. Diablo II): \n")
    print_get_most_played(data_file)
    print_sum_sold(data_file)
    print_get_selling_avg(data_file)
    print_count_longest_title(data_file)
    print_get_date_avg(data_file)
    print_get_game(data_file, title)
    print_count_grouped_by_genre(data_file)
    print_get_date_ordered(data_file)


if __name__ == "__main__":
    main()
