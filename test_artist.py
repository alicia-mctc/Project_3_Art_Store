import sqlite3
import unittest 
from unittest import TestCase

# replace the database path
import db_config
db_config.database_path = 'test_artist_database.db'

# then import your code
import artwork_db
from artist import Artist


class TestArtistLast(TestCase):
    
    # def test_last(self):
    #     # Checking last name of artist
    #     self.assertEqual(Lowry, last(Peterson )) 

    # def test_first(self):
    #     # Checking first name of artist
    #     with self.assertRaises(ValueError):
    #      first(Claude, Sam)   


    def setUp(self):
        self.clear_database()   # remove all data from db before each test so you know what data you are starting with

    def clear_database(self):
        with sqlite3.connect(db_config.database_path) as con:
            con.execute('delete from artists')
            con.execute('delete from artworks')
        con.close()


    def test_add_artist(self):
        # new artist data 
        artist = Artist('Alicia', 'email@example.com')
        artwork_db.insert_artist(artist)
        # check if artist in DB
        with sqlite3.connect(db_config.database_path) as c:
            all_data = c.execute('select * from artists').fetchall()
            self.assertEqual(1, len(all_data))  # one row 
            first_row = all_data[0]
            # first column is the id
            self.assertEqual('Alicia', first_row[1])   # 2nd column is the name
            self.assertEqual('email@example.com', first_row[2])   # 3rd column is the email
        c.close()


    def test_add_artist_no_email(self):
        # new artist data - no email. This test fails - check the constraints in your DB, don't allow empty emails
        name = 'Alicia'
        artist = Artist(name, None)
        with self.assertRaises(sqlite3.IntegrityError):  
            artwork_db.insert_artist(artist)


    # Can you write a test adding an artist with no name?

    # Can you write a similar test for adding an artwork?

    # What about a test for adding an artwork with no artist?


if __name__ == '__main__':
    unittest.main()