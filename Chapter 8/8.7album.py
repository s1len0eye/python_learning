def make_album(name, title, n_tracks=0):
    if n_tracks:
        return {'name': name.title(), 'album title': title.title(), 'number of tracks': n_tracks}
    else:
        return {'name': name.title(), 'album title': title.title()}
    
album = make_album('adam', 'test')
print(album)

album = make_album('bob', 'test2', 8)
print(album)
