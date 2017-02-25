# apotheosis
pull info from last.fm to populate an artist page on NW

* Add similar artists
* Add missing artist bio
* Add missing artist image
* Add missing cover art for all albums in artist's discography (!)
* All images, new or existing, are rehosted on ptpimg if on a bad host

There are still bugs to be found. Please add any you come across to Issues.


1. clone the github repo

2. install pylast and contextlib2 <code>$ pip install --user pylast contextlib2</code>

3. make a [last.fm API account](https://www.last.fm/api) (you'll need the auth keys for the config)

4. If you are a PTP member you can make a [ptpimg account](https://ptpimg.me) to take advantage of the rehosting feature.

5. copy and fill out the config file (remember to quote all strings!) <code>$ cp config.py.template config.py</code>

Example Usage: <code>$ ./apotheosis 1234 </code>
Runs script on artist with id=1234

# This is a work in progress

Forked from the original apotheosis https://github.com/Suit-Of-Sables/apotheosis
