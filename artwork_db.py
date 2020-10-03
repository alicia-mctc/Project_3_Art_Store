import sqlite3
from artist import Artist
from artwork import Artwork

# set database path from configuration file. This is so the test can change the database path
import db_config
conn = sqlite3.connect(db_config.database_path)

c = conn.cursor()




c.execute("""CREATE TABLE IF NOT EXISTS artists
(artist_id INTEGER PRIMARY KEY NOT NULL, name TEXT NOT NULL, 
 email TEXT UNIQUE)""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS 
artworks(artwork_id INTEGER PRIMARY KEY NOT NULL, 
artist_id INTEGER, art_name, price REAL CHECK(price > 0), 
available Boolean,
FOREIGN KEY(artist_id) REFERENCES artists(artist_id))""")

conn.commit()

conn.close()



def insert_artist(art):   # is this to insert an artist? 
    with sqlite3.connect(db_config.database_path) as c:  # create a new connection in each function
        c.execute("INSERT INTO artists (name, email ) VALUES (?, ?)", 
        (art.name, art.email ))
    c.close()  # and close connection in each function
        
def get_arts_by_name(lastname):
    with sqlite3.connect(db_config.database_path) as c:  # create a new connection in each function
        c.execute("SELECT * FROM artists WHERE name= ?", (lastname,))
        return c.fetchall()
    c.close()  


def update_price(art, price):  # you don't need this 
    with conn:
        c.execute("""UPDATE artworks SET price = price 
                    WHERE artwork_id = artwork_id AND artist_id = artist_id""",   # use parameters, the ? syntax
                   ( art.artwork_id, art.artist_id, art.price, art.available))

def remove_art(art): 
    with conn:
        c.execute("DELETE from artists WHERE first = first AND last = last",  # make sure you use the right column names and use parameters - the ? syntax
        art.name, art.email, art.name_of_artwork)  # is email right? 


# Read the project requirements. There's a specfic set of features you need to implement 
# add a new artist
# search for all the artwork by an artist (everything - available and sold)
# display for all the available artwork by an artist
# add a new artwork. Make sure the artwork is associated with an artist. If needed, create an artist first. 
# delete an artwork
# change the availability status of an artwork, for example, change from available to sold



