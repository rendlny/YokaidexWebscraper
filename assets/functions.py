import urllib.request
from bs4 import BeautifulSoup

def addObjectJsonToFile(object, filename):
    f = open(filename, "a")
    f.write(object.json())
    return "added"

def changeSpacesToHtml(url):
    html = url.replace(" ","%20")
    return html

#################################################################
# Function to return html details grabbed from given url ########
#################################################################
def scrapeUrl(url):
    webpage = urllib.request.urlopen(url)
    page = BeautifulSoup(webpage, "html.parser")
    return page

def scrapeFile(filePath):
    page = BeautifulSoup(open(filePath), 'html.parser')
    return page
#################################################################
