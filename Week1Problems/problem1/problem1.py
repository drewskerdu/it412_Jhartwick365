from Functions.my_functions import *
playlist = []

while True:
    song = input("Enter a song or q to quit: ")
    if song == "q":
        break
    artist = input("Enter a artist for that song or q to quit: ")
    dictionarySong = songDictionary(song, artist)
    playlist.append(dictionarySong)
printSongEntries(playlist)