def songDictionary(title, artist="Unknown"):
    dictionaryItem = {'title': title, 'artist': artist}
    return dictionaryItem
def printSongEntries(songInfo):
    print("Here are all the song entries in the list:")
    for song in songInfo:
        print(song)