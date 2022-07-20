movies = []
with open("text_files/FavoriteMovies.txt") as FavMovies:
    lines = FavMovies.readlines()
    for line in lines:
        movies.append(line)


with open("text_files/FavoriteMoviesupdated.txt", "w") as FavMovies1:
    for count in range(0,5):
        FavMovies1.write(f"{lines[count]} is a movie I like.\n")

