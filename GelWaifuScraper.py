import requests
import os
import urllib
from pathlib import Path
from os import path
import getpass


username = getpass.getuser()
directorypath = f"//home//{username}//GelWaifuScraper//"
imagepath = f'/home/{username}/GelWaifuScraper/'


def directory():
    try:
        os.makedirs(directorypath)
        print("Created directory.")

    except FileExistsError:
        print("GelWaifuScraper directory in use.")
        pass


directory()

tag = input("Enter the tags you would like to search for:\n")

amount = int(input("Enter the amount of pictures you would like to install:\n"))

url = (f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={tag}')

search = requests.get(url)
json = search.json()

downloaded = 0

for image in json:

    get = image.get("file_url")
    split = get.rsplit('/', 1)[1]
    fpath = os.path.join(imagepath, split)

    filename = os.path.join(directorypath + split)
    if filename not in fpath:
        tryout = requests.get(get)

        if get.find('/'):
            print(f"Downloading {get}....")
            downloaded += 1
            with open(filename, 'wb') as writeFile:
                writeFile.write(tryout.content)

        if amount == int(downloaded):
            print("Finished downloading images.")
            break


print("Finished.")
