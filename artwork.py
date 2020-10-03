class Artwork:
    """An example of Artwork class"""
    # You might not know the id when the Artwork is created. artwork=None is a default value
    def __init__(self, artist_id, art_name, price, available, artwork_id=None):
        self.artwork_id = artwork_id
        self.artist_id = artist_id
        self.art_name = art_name
        self.price = price
        self.available = available
      
    def __repr__(self):
        return "Artwork('{}', '{}', '{}', '{},'{}')".format(self.artwork_id,self.artist_id, 
        self.artist_id, self.price, self.available)        
