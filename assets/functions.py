import urllib.request
from bs4 import BeautifulSoup

def add_object_json_to_file(object, filename):
    f = open(filename, "a")
    f.write(object.json())
    return "added"

def change_spaces_to_html(url):
    html = url.replace(" ","%20")
    return html

#################################################################
# Function to return html details grabbed from given url ########
#################################################################
def scrape_url(url):
    webpage = urllib.request.urlopen(url)
    page = BeautifulSoup(webpage, "html.parser")
    return page

def scrape_file(filePath):
    page = BeautifulSoup(open(filePath), 'html.parser')
    return page
#################################################################
