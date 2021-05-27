import requests
import os
import urllib
from pathlib import Path
from os import path
import getpass
import concurrent.futures
import sys
import time
import getopt

MAX_THREADS = 30

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


def downloadImages(amount, url):
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


def downloadFiles(amount, url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(downloadImages(amount, url))


def main(argv):
    print(argv)
    if argv[1:] != "":
        tag = ''
        amount = 0
        try:
            opts, args = getopt.getopt(argv[1:], "ta", ["tags", "amount"])
        except getopt.GetoptError:
            print('main.py -t <tags> -a <number>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('main.py -t <tag> -a <number>')
                sys.exit()
            elif opt in ("-t", "--tags"):
                tag = arg
            elif opt in ("-a", "--amount"):
                stramount = arg
                amount = int(stramount)
        url = (f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={tag}')
        downloadFiles(amount, url)
    
    else:
        tag = input("Enter the tags you would like to search for:\n")

        amount = int(input("Enter the amount of pictures you would like to install:\n"))

        url = (f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={tag}')

        directory()
        downloadFiles(amount, url)


if __name__ == '__main__':
    main(sys.argv[1:])


print("Finished.")
