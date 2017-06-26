#!/usr/bin/env python
# Report functions


# processes the given database so the other functions can use it
def file_processing(file_name):
    try:
        with open(file_name, "r") as file:
            games_list = [line.strip().split("\t") for line in file]
        return games_list
    except FileNotFoundError:
        print ("Cannot locate file. Run script again and give an existing datafile!")
        exit()


# counts the games in the given database
def count_games(file_name):
    games_list = file_processing(file_name)
    games_amount = len(games_list)
    return games_amount


# decides if there is a game from the given year in the database
def decide(file_name, year):
    games_list = file_processing(file_name)
    for item in games_list:
        if item[2] == str(year):
            return True
    return False


# returns the title of the latest game
def get_latest(file_name):
    games_list = file_processing(file_name)
    latest = 0
    for item in games_list:
        if int(item[2]) > latest:
            latest = int(item[2])
    for item in games_list:
        if int(item[2]) == latest:
            return item[0]


# returns the number of games by the given genre
def count_by_genre(file_name, genre):
    games_list = file_processing(file_name)
    games_of_spec_genre = []
    for item in games_list:
        if item[3] == genre:
            games_of_spec_genre.append(item[0])
    return len(games_of_spec_genre)


# searches for a game by title and returns its line number in database
def get_line_number_by_title(file_name, title):
    games_list = file_processing(file_name)
    for item in games_list:
        if item[0] == title:
            return games_list.index(item) + 1
    raise ValueError
    return


# returns an alphabetically sorted list of game titles
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


# returns the list of genres without duplicates in alphabetically order
def get_genres(file_name):
    games_list = file_processing(file_name)
    genres = []
    for item in games_list:
        if item[3] not in genres:
            genres.append(item[3])
        else:
            continue
    return sorted(genres, key=lambda item: item.lower())


# returns the top sold First-person shooter game from the given database
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
