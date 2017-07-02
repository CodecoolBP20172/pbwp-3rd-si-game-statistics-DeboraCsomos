#!/usr/bin/env python
# Export functions
from reports import *


def exporting_results_to_file(export_file="reports.txt"):
    data_file = input("Give name of data file (e.g. game_stat.txt): \n")
    title = input("Enter title for question 5 (e.g. Diablo II): \n")
    with open(export_file, "w") as file:
        file.write(str(get_most_played(data_file)) + "\n"*2)
        file.write(str(round(sum_sold(data_file), 3)) + "\n"*2)
        file.write(str(round(get_selling_avg(data_file), 3)) + "\n"*2)
        file.write(str(count_longest_title(data_file)) + "\n"*2)
        file.write(str(get_date_avg(data_file)) + "\n"*2)
        file.write("\n".join([str(item) for item in get_game(data_file, title)]) + "\n"*2)
        file.write("\n".join({"{}: {}".format(k, str(v)) for k, v in count_grouped_by_genre(data_file).items()})
                   + "\n"*2)
        file.write("\n".join([str(item) for item in get_date_ordered(data_file)]) + "\n"*2)


def main():
    exporting_results_to_file()
    print ("Check your new reports.txt file.")


if __name__ == "__main__":
    main()
