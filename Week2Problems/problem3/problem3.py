movies = []

try:
    with open("text_files/FavoriteMovies.txt") as FavMovies:
        lines = FavMovies.readlines()
        for line in lines:
            movies.append(line)
except FileNotFoundError:
    pass

try:
    with open("text_files/FavoriteMoviesupdated.txt", "w") as FavMovies1:
        for count in range(0,len(movies)):
            FavMovies1.write(f"{lines[count].rstrip()} is a movie I like.\n")
except FileNotFoundError:
    pass

