from unittest import TestCase
import artist

class TestArtistLast(TestCase):
    
    def test_last(self):
        # Checking last name of artist
        self.assertEqual(Lowry, last(Peterson )) 

    def test_first(self):
        # Checking first name of artist
        with self.assertRaises(ValueError):
         first(Claude, Sam)   
