addObjectJsonToFileimport urllib.request
from bs4 import BeautifulSoup
from assets import data
from assets import functions

from DTO.Bug import Bug


page = functions.scrapeFile("bug_html.html")
tableHead = page.find('span', {"id": "Yo-kai_Watch_1"})
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

        ##LOCATION
        if dataCount is 2:
            bugLocation = dataCol.text

        ##SELL
        if dataCount is 3:
            bugSell = dataCol.text

        ##RARE_SELL
        if dataCount is 4:
            bugRareSell = dataCol.text

    print('--------------------')
    bug = Bug(bugName.rstrip(), bugLocation.rstrip(), '', bugSell.rstrip(), bugRareSell.rstrip())

    functions.addObjectJsonToFile(bug, "bug_1.json")
