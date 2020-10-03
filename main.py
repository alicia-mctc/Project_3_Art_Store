import ui 
import artwork_db 


def main():
    while True:
        
        task = input('What task') 

        if task == '1':
            add_artist()
        elif task == '2':
            add_artwork()
        else:
            print("Quit") 
            break   # break out of loop, end program


def add_artist():
    # get input 
    # name = ui.get_non_empty_string('Artist name?')  
    # email = ui.get_non_empty_string('Artist email?')
    artist = ui.get_artist_content()  # is this the method to use? 
    artwork_db.insert_artist(artist)
    # artwork_db.insert_artist(name, email)  # be careful with function names and make sure your arguments match
    # this function expects an artist object

def add_artwork():
     art_name = input('Enter art name:')
     artist_primary_id = ui.check_if_artwork_exist(art_name)
     try:
         new_artwork = ui.get_art_work_content(artist_primary_id)
        #  new_artwork.save()
        # call the method in artwork_db to save the artwork 
     except:
        print('Error has occurred ')

            
if __name__ == '__main__':
    main()