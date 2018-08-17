from pymongo import MongoClient
from bs4 import BeautifulSoup
from requests import get
import json
from unidecode import unidecode


from sys import argv
import datetime
from urllib.request import urlopen
import time

def get_urls_from_search(attempt=0):
    # driver = webdriver.PhantomJS()
    now = datetime.datetime.now()

    search_terms = [
        'nintendo+switch'
    ]

    num_pages = 1

    urls = set()
    worked = False
    for term in search_terms:
        for page in range(1, num_pages+1):
            url = "https://liquipedia.net/dota2/Dota_Pro_Circuit/Rankings/Teams"

            # Get the html from the site and create a BeautifulSoup object from it
            # driver.get(url)
            source = urlopen(url).read()
            soup = BeautifulSoup(source, 'html.parser')
            # import pdb; pdb.set_trace()
            # import pdb; pdb.set_trace()
            try:
                # Get the number of search results.  If greater than 10 we'll need to
                # loop through subsequent pages to get the additional urls
                articles = soup.findAll('span', class_="team-template-text")
                for tag in articles:
                    # import pdb; pdb.set_trace()
                    if tag.find('a') != None:
                        article = str(tag.find('a').get('title'))
                        urls.add(article)
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
    file_path = 'data/teams.txt'
    f = open(file_path, 'w')
    f.write(json.dumps(list(urls)))
    f.close()
    # else:
    #     print("Didn't work")
