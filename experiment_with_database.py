# I moved these from the artwork_db class - these are for seeing if the functions work?
# so they can go in their own file 
# the artwork_db should have the final code used by the application 


from artist  import Artist
from artwork import Artwork


def add_artist(art):
    # you don't need with con. THe insert_art method will handle the db connection
    art_1 = Artist( 1, 'L. S.', 'Lowry')
    art_2 = Artist(2,'Claude', 'Monet' )
    art_3 = Artist(3,'Vincent Van', 'Gogh')
    insert_art(art_1)
    insert_art(art_2)
    insert_art(art_3)

def add_artwork():
    artw_1 = Artwork(1, 1, 'The Beach', 100, available = True)
    artw_2 = Artwork(2, 2, 'Water Lily Pond', 500, available = True)
    artw_3 = Artwork(3, 3, 'Almond Blossom', 500, available = True)
    insert_art(artw_1)
    insert_art(artw_2)
    insert_art(artw_3)

        

arts = get_arts_by_name('Lowry')
print(arts)

update_price([1], 700)
remove_art([0])

arts = get_arts_by_name('Lowry')
print(arts)
