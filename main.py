import ui 
import artwork_db 

while True:
    
    task = input('What task') 

    if task == '1':
        add_artist()
    elif task == '2':
        add_artwork()
    else:
        print("Quit") 


def add_artist():
    # get input 
    name = ui.get_non_empty_string('Artist name?')
    email = ui.get_non_empty_string('Artist email?')
    artwork_db.add_artist(name, email)

def add_artwork():
     art_name = input('Enter art name:')
     artist_primary_id = ui.check_if_artwork_exist(art_name)
     try:
         new_artwork = ui.get_art_work_content(artist_primary_id)
         new_artwork.save()
     except:
        print('Error has occurred ')

            

