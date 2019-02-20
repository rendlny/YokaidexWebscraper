import urllib.request
from bs4 import BeautifulSoup
from assets import data
from assets import functions

from DTO.Bug import Bug


page = functions.scrapeFile("bug_html.html")
tableHead = page.find('span', {"id": "Yo-kai_Watch_2"})
table = tableHead.find_parent().find_next_sibling()
tableRows = table.find_all('tr')

for row in tableRows:
    rowData = row.find_all('td')
    dataCount = 0

    for dataCol in rowData:
        dataCount = dataCount + 1
        print(dataCount)
        print(dataCol)

        ##Name
        if dataCount is 1:
            bugName = dataCol.text
        ##SELL
        if dataCount is 2:
            bugSell = dataCol.text

        ##LOCATION
        if dataCount is 3:
            bugLocation = dataCol.text

        ##DESCRIPTION
        if dataCount is 4:
            bugDescription = dataCol.text

    print('--------------------')
    bug = Bug(bugName.rstrip(), bugLocation.rstrip(), bugDescription.rstrip(), bugSell.rstrip(), '')

    functions.addObjectJsonToFile(bug, "bug.js")
