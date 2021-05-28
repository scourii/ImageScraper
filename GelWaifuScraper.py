import requests
import os
import getpass
import concurrent.futures
import sys
import argparse

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
    print(amount)
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
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Downloads images from gelbooru.")
        parser.add_argument('-a', "--amount", help="Amount of images to install.", type=int)
        parser.add_argument('-t', "--tags", help="Tags to search for.")
        args = parser.parse_args()
        if args.amount:
            amount = args.amount
        if args.tags:
            tag = args.tags

        url = (f'https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags={tag}')
        directory()
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
