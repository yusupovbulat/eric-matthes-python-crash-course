def make_album(artist, album, tracks=''):
    album_name = {'artist': artist.title(), 'album': album.title()} 
    if tracks:
        album_name['tracks'] = tracks
    return album_name

while True:
    print("\nPlease enter information about the artist's album")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    a_a = make_album(artist, album)
    for key, response in a_a.items():
        print(key + ' ' + response)
