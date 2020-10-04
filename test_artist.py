import sqlite3
import unittest
from unittest import TestCase
import db_config

db_config.database_path = 'test_artist_database.db'


import artwork_db
from artist import Artist


class TestArtistLast(TestCase):
    
    def setUp(self):
        self.clear_database() #To show starting data,we need to clear out all data in database 
 
    def clear_database(self):
        with sqlite3.connect(db_config.database_path) as con:
            con.execute('delete from artist')
            con.execute('delete from artworks')
        con.close()

    def test_add_artist(self):
        #new artist data
        artist = Artist('Ryan', 'email@example.com')
        artwork_db.insert_artist(artist)
        #check if artist in DB
        with sqlite3.connect(db_config.database_path) as con:
            all_data = c.execute('select * from artists').fetchall()
            self.assertEqual(1, len(all_data)) # one row
            first_row = all_data[0]
            self.assertEqual('Ryan', first_row[1]) #2nd column is the name
            self.assertEqual('email@example.com', first_row[2]) #3rd is the email
        con.close()

    def test_add_artist_no_email(self):
        #new artist data - no email. This test fails - check the constraints in your DB,
        # must provide email 
        name = 'Ryan'
        artist = Artist(name, None)
        with self.assertRaises(sqlite3.IntegrityError):
            artwork_db.insert_art(artist)
        con.close()            

    def test_add_artist_no_name(self):
        #new artist data - no name
        name = 'Ryan'   
        artist = Artist(name, '')
        with self.assertRaises(sqlite3.IntegrityError):
            artwork_db.insert_art(artist)
        con.close()

    def test_add_artwork(self):
        #new artwork 
        artwork = Artwork('The Last Supper', '1000', True)
        artwork_db.insert_artwork(artwork)
        #check if artwork in DB
        with sqlite3.connect(db_config.database_path) as c:
            all_data = c.execute('select * from artworks').fetchall()
            self.assertEqual(1, len(all_data)) # one row
            first_row = all_data[0]
            #first and second columns are for id
            self.assertEqual('The Last Supper', first_row[2]) #3nd column is the name of artwork
            self.assertEqual('1000', first_row[3]) #4rd column is the price
            self.assertEqual(True, first_row[4]) # 5th column is the artwork availability 
            
        con.close()

    def test_add_artwork_no_artist(self):
        #new artwork without artist
        art_name = ''
        artwork = Artwork(art_name, None)
        with self.assertRaises(sqlite3.IntegrityError):  
            artwork_db.insert_artist(artwork)
        
        con.close()    

if __name__ == '__main__':
    unittest.main()       
