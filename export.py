#!/usr/bin/env python
# Export functions
from reports import *


def exporting_results_to_file(export_file="reports.txt"):
    data_file = input("Give name of data file (e.g. game_stat.txt): \n")
    year = int(input("Enter year for question 2 (e.g. 1999):\n"))
    genre = input("Enter genre for question 4 (e.g. RPG): \n")
    title = input("Enter title for question 5 (e.g. Diablo II): \n")
    with open(export_file, "w") as file:
        file.write(str(count_games(data_file)) + "\n"*2)
        file.write(str(decide(data_file, year)) + "\n"*2)
        file.write(get_latest(data_file) + "\n"*2)
        file.write(str(count_by_genre(data_file, genre)) + "\n"*2)
        file.write(str(get_line_number_by_title(data_file, title)) + "\n"*2)
        file.write("\n".join(sort_abc(data_file)) + "\n"*2)
        file.write("\n".join(get_genres(data_file)) + "\n"*2)
        file.write(str(when_was_top_sold_fps(data_file)) + "\n"*2)


exporting_results_to_file()
print ("Check your new reports.txt file, and finally let me watch the new Silicon Valley episode!")
