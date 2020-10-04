import sqlite3
from artist import Artist
from artwork import Artwork
import db_config

conn = sqlite3.connect(db_config.database_path)# connect to database

c = conn.cursor()

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS artists
(artist_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, 
 email TEXT UNIQUE NOT NULL)""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS 
artworks(artist_id INTEGER, art_name, price REAL CHECK(price > 0), 
available Boolean, artwork_id INTEGER PRIMARY KEY NOT NULL,
FOREIGN KEY(artist_id) REFERENCES artists(artist_id))""")

conn.commit()

conn.close()

def insert_artist(art): #insert an artist
    with sqlite3.connect(db_config.database_path) as c:  # create a new connection in each function
        c.execute("INSERT INTO artists (name, email ) VALUES (?, ?)", 
        (art.name, art.email ))
    c.close()  #close connection after each function
        
def get_arts_by_name(lastname):
    with sqlite3.connect(db_config.database_path) as c: 
        c.execute("SELECT * FROM artists WHERE name= ?", (lastname,))
        return c.fetchall()
    c.close()          

def update(price):
    with conn:
        c.execute("""UPDATE artworks SET price = price 
                    WHERE (?, ?, ?, ?)""",
                   (price.artwork_id, price.artist_id, price.price, price.available))

def remove_art(art):
    with conn:
        c.execute("DELETE from artists WHERE name=? , ?",
        art.name, art.email)

def add_artist(art):
    with conn:

        art_1 = Artist( 1, 'L. S.', 'Lowry')
        art_2 = Artist(2,'Claude', 'Monet' )
        art_3 = Artist(3,'Vincent Van', 'Gogh')
        insert_art(art_1)
        insert_art(art_2)
        insert_art(art_3)

def add_artwork(new_artwork):
    with conn:
        artw_1 = Artwork(1, 1, 'The Beach', 100, available = True)
        artw_2 = Artwork(2, 2, 'Water Lily Pond', 500, available = True)
        artw_3 = Artwork(3, 3, 'Almond Blossom', 500, available = True)
        insert_art(artw_1)
        insert_art(artw_2)
        insert_art(artw_3)
        

        

arts = get_arts_by_name('Lowry')
print(arts)

update_price([1], 700)
remove_art([0])

arts = get_arts_by_name('Lowry')
print(arts)


conn.close()
