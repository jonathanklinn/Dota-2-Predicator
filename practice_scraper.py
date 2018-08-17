from pymongo import MongoClient
from bs4 import BeautifulSoup
from requests import get
import json
from unidecode import unidecode
from load_data import load_urls, get_file_name
from sys import argv
import datetime
from urllib.request import urlopen
import time
# from selenium import webdriver


def get_urls_from_search(attempt=0):
    # driver = webdriver.PhantomJS()

    search_terms = [
        'TI'
    ]

    num_pages = 1

    urls = set()
    worked = False
    for term in search_terms:
        for page in range(1, num_pages+1):
            url = "https://cybersport.com/tags/dota-2"

            # Get the html from the site and create a BeautifulSoup object from it
            # driver.get(url)
            source = urlopen(url).read()
            soup = BeautifulSoup(source, 'html.parser')
            # import pdb; pdb.set_trace()
            # import pdb; pdb.set_trace()
            try:
                # Get the number of search results.  If greater than 10 we'll need to
                # loop through subsequent pages to get the additional urls
                articles = soup.findAll('h3', class_='margin-bottom--0 margin-top--10 card-vertical__title')
                for tag in articles:
                    # import pdb; pdb.set_trace()
                    if tag.find('a') != None:
                        article = str(tag.find('a').get('href'))
                        urls.add('https://cybersport.com'+article)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                # import pdb; pdb.set_trace()
                if attempt < 3:
                    attempt += 1
                    get_urls_from_search(date, attempt)
            time.sleep(5)
    return worked, urls




if __name__ == '__main__':
    ''' This script should be called in the following way:
    $ python jons_all_urls3.py
    '''

    print('Scraping BB')
    # Initialize empty lists for urls to be appended to

    did_it_work, urls = get_urls_from_search()

    print('Game Article Scraping Done...')
    print('There were a total of {0} urls'.format(len(urls)))

    # if did_it_work:
    # Convert good_urls set to a list and write to a txt file
    file_path = 'jons_urls/urls.txt'
    f = open(file_path, 'w')
    f.write(json.dumps(list(urls)))
    f.close()
