import urllib.request
from bs4 import BeautifulSoup

def addBaffleBoardToFile(baffleBoard, filename):
    f = open(filename, "a")
    f.write(baffleBoard.json())
    return "added"

def changeSpacesToHtml(url):
    html = url.replace(" ","%20")
    return html

def getViewingInfoFromScripts(text):
    contents = text.split("strong")
    contents = contents[2]
    contents = contents[105:]
    contents = contents[:14]
    return contents

def getDirectionsFromScripts(text):
    contents = text.split("Directions")
    contents = contents[1]
    contents = contents[113:]
    contents = contents[:(len(contents)-37)]
    return contents

def getAccommodationInfoFromScripts(text):
    contents = text.split("unescape")
    contents = contents[1]
    contents = contents[2:]
    contents = contents[:(len(contents)-39)]
    if "}" in contents:
        contents = ""
    return contents

def getOtherInfoFromScripts(text):
    contents = text.split("unescape")
    contents = contents[1]
    contents = contents[2:]
    contents = contents[:(len(contents)-37)]
    return contents

def getCostFromScripts(text):
    contents = text.split("unescape")
    contents = contents[1]
    contents = contents.split(")")
    contents = contents[0]
    contents = contents[2:]
    contents = contents[:(len(contents)-1)]
    return contents

def getBedsFromScripts(text):
    contents = text.split("unescape")
    contents = contents[2]
    contents = contents.split(")")
    contents = contents[0]
    contents = contents[2:]
    contents = contents[:(len(contents)-1)]
    return contents

def getSaleStatusCode(text):
    if text is "Sale Agreed":
        code = "1"

    elif text is "For Sale by Private Treaty" :
        code = "2"

    elif text is "Sold":
        code = "3"

    elif text is "To Let":
        code = "4"

    elif text is "For Sale by Auction":
        code = "5"

    else:
        code = "0"

    return code

#################################################################
# Function to return html details grabbed from given url ########
#################################################################
def scrapeUrl(url):
    webpage = urllib.request.urlopen(url)
    page = BeautifulSoup(webpage, "html.parser")
    return page
#################################################################
