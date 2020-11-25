from pathlib import Path
import requests
import os
import urllib
from os import path
import getpass

def directory():
    try:

        os.makedirs("GelWaifuScraper")
        print("Created directory.")

    except FileExistsError:
        print("GelWaifuScraper directory in use.")
        pass

directory()
username = getpass.getuser()

path = f"/home/{username}/GelWaifuScraper/"



tag = input("Enter the tags you would like to search for:\n")

amount = int(input("Enter the amount of pictures you would like to install:\n"))


url = (f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={tag}')

search = requests.get(url)
downloaded = 0
json = search.json()

for image in json:

    get = image.get("file_url")
    split = get.rsplit('/', 1)[1]
    fpath = os.path.join(path, split)
    
    
    trya = os.path.join(f"//home//{username}//GelWaifuScraper//" + split)
    
    if trya not in fpath:
        tryout = requests.get(get)

        if get.find('/'):
            print(f"Downloading {get}....")
            downloaded += 1
            with open(trya, 'wb') as l:
                
                l.write(tryout.content)
                
    
        if amount == int(downloaded):
            print("Finished downloading images.")
            break 
    
    

print("Finished.")