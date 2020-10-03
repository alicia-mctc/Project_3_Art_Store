def get_artist_content():
    name = input('Enter artist name: ')#ask user to provide artist name and save in name variable 
    email = input('enter artist email: ')
    return Artist(name=name, email=email)

def get_art_work_content(new_artist):# retrieve artwork information from new artist
    art_name = input('Enter art name: ')# get art name from user
    price = float(input('Enter art price: '))# ask user for art's price and convert price string to float data type
    return Artwork(artist=new_artist, art_name=art_name, price = price)


