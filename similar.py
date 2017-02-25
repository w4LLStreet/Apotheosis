from config import max_to_add, min_score, artist_page, nw_auth

def find(artist, lastfm):
    # get list of current similar artists on NW
    cur_similar = artist.similar_artists

    # get list of at most max_to_add similar artist from last.fm
    new_similar = lastfm.get_artist(artist.name).get_similar(limit=max_to_add)

    # find all artists that meet min_score
    new_similar = [a[0].name for a in new_similar if a[1] >= min_score]

    # but don't don't try to add one if already there
    new_similar = [a for a in new_similar if a not in cur_similar]

    return new_similar

def add(artist, new_similar, nw):

    data = {'action' : 'add_similar',
            'auth' : nw_auth,
            'artistid' : artist.id,
            'artistname': ''}

    for artist in new_similar:
        data['artistname'] = artist
        r = nw.session.post(artist_page, data=data)
