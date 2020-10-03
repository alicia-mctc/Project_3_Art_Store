class Artist:
    """An example of Artist class"""
    
    def __init__(self, artist_id, name, email):
        self.artist_id = artist_id
        self.name = name
        self.email = email
        #self.email = first + '.' + last + '@company.com'

    def artist(self):
        return '{}'.format(self.artist_id)    
            
    def __repr__(self):
        return "Artist('{}', '{}', '{}')".format(self.artist_id,self.name, self.email)