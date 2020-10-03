class Artist:
    """An example of Artist class"""
    
    def __init__(self, name, email, artist_id=None):   # default for id if it's not known. 
        # When creating Artist and Artwork objects from the database, make sure you use the 
        # correct order of parameters
        self.artist_id = artist_id
        self.name = name
        self.email = email
        #self.email = first + '.' + last + '@company.com'

    def artist(self):
        return '{}'.format(self.artist_id)    
            
    def __repr__(self):
        return "Artist('{}', '{}', '{}')".format(self.artist_id,self.name, self.email)