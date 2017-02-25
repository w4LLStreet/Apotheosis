from HTMLParser import HTMLParser
import mechanize
import image
from classes import Album
from config import nw_auth
from cStringIO import StringIO

parser = HTMLParser()


def get_covers(artist, nw, lastfm):

    for album in artist.albums:
        album = Album(album)
        if not image.is_fine(album.image):
            print parser.unescape(album.name)
            image.fix(album, nw, lastfm)
