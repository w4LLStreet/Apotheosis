from re import sub
from config import nw_auth, artist_page

def missing(artist):
    return artist.bio == ''

def add(artist, lastfm, nw):
    bio = get(artist.name, lastfm)
    if bio == None:
        print "failed to get bio :("
        print "Perhaps there is no bio for this artist on last.fm right now.(?)\n"
        return          # failed to get bio
    artist.bio = to_bbcode(bio)
    edit(artist, nw)

def get(artist_name, lastfm):
    try:
        bio = lastfm.get_artist(artist_name).get_bio('content')
    except:
        return None
    print "found ...",
    return bio

def to_bbcode(bio):
    bio = sub('<a href="', '\n\n[url=', bio)
    bio = sub('">Read', ']Read', bio)
    bio = sub('</a>.', '[/url]\n', bio)
    s = 'User-contributed text is available under the Creative Commons By-SA License; additional terms may apply.'
    bio = bio.replace(s, '[size=1]' + s + '[/size]')
    return bio

def edit(artist, nw):
    data = {'action' : 'edit',
            'auth' : nw_auth,
            'artistid' : artist.id,
            'body' : artist.bio,
            'image' : artist.image,
            'summary' : 'added artist bio from last.fm'}
    r = nw.session.post(artist_page, data=data)
    print "added!\n"
