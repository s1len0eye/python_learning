def make_album(name, title, n_tracks=0):
    if n_tracks:
        return {'name': name.title(), 
        'album title': title.title(),
        'number of tracks': n_tracks}
    else:
        return {'name': name.title(), 
        'album title': title.title()}
    
while True:
    print("Press 'q' to quit.")
    name = input("Enter the name of artist: ")
    if name == 'q':
        break
    title = input("Enter the title of album: ")
    if title == 'q':
        break
        
    album = make_album(name, title)
    print(album)
