class Artwork:
    """An example of Artwork class"""
    def __init__(self, artwork_id, artist_id, art_name, price, available):
        self.artwork_id = artwork_id
        self.artist_id = artist_id
        self.art_name = art_name
        self.price = price
        self.available = available
      
    def __repr__(self):
        return "Artwork('{}', '{}', '{}', '{},'{}')".format(self.artwork_id,self.artist_id, 
        self.artist_id, self.price, self.available)        
