class Artwork:
    """An example of Artwork class"""
    def __init__(self, artist_id, art_name, price, available, artwork_id=None):
        self.artist_id = artist_id
        self.art_name = art_name
        self.price = price
        self.available = available
        self.artwork_id = artwork_id
      
    def __repr__(self):
        return "Artwork('{}', '{}', '{}', '{},'{}')".format(self.artist_id, 
        self.art_name, self.price, self.available, self.artwork_id)        
