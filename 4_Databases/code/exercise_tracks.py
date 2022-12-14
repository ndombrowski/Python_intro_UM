import xml.etree.cElementTree as ET
import sqlite3

#make a db connection
conn = sqlite3.connect('trackdb_ex.sqlite')
cur = conn.cursor()

#make some fresh tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

#get the data we will use to populate our tables
fname = '../data/Library.xml'

#the syntax for our data looks as follows
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

#lookup function that looks up the key for an object
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

#parse the filename string returning an xml object
stuff = ET.parse(fname)

#going into the 3rd dict levels gives us the tracks
#so for each key id we want all the track information
all = stuff.findall('dict/dict/dict')
print('Dict count', len(all))

#extract data using the lookup function
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    #print(name, artist, album, count, rating, length, genre)

    #populate our tables
    #INSERT OR INGORE says only put row if text is not there
    #only works since when we generate the table with `name TEXT UNIQUE`
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))

    #the above can have missing values, so we need to deal with his
    row = cur.fetchone() 
    if row is not None: 
        genre_id = row[0]

    #since artist_id is the foreign id for the album title, then we can deal with the next table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES(?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()

print('DB created successfully')
