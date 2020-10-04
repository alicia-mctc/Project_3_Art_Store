class Artist:
    """An example of Artist class"""
    
    def __init__(self, name, email, artist_id=None): #default if id is not know
        self.name = name
        self.email = email
        self.artist_id = artist_id
    
    def artist(self):
        return '{}'.format(self.artist_id)    
            
    def __repr__(self):
        return "Artist('{}', '{}', '{}')".format(self.artist_id,self.name, self.email)