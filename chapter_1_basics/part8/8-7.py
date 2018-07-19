def make_album(artist, album, tracks=''):
    album_name = {'artist': artist, 'album': album} 
    if tracks:
        album_name['tracks'] = tracks
    return album_name
print(make_album('rammstein', 'mutter'))
print(make_album('the white stripes', 'elephant'))
print(make_album('noize mc', 'hard reboot', tracks=12))
