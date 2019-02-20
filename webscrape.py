import urllib.request
from bs4 import BeautifulSoup
from assets import data
from assets import functions

from DTO.BaffleBoard import BaffleBoard

page = functions.scrapeUrl(data.WEB_LINK)
tableHead = page.find('span', {"id": "Yo-kai_Watch_3"})
table = tableHead.find_parent().find_next_sibling()
tableRows = table.find_all('tr')


rowCount = 0
for row in tableRows:
    rowCount = rowCount + 1
    if rowCount is not 1:

        rowData = row.find_all('td')
        dataCount = 0

        for dataCol in rowData:
            dataCount = dataCount + 1

            ## GET LOCATION
            if dataCount is 1:
                location = dataCol.text
            ## GET CLUES
            if dataCount is 2:
                clues = dataCol.find_all('li')
                clueCount = 0
                for clue in clues:

                    clueCount = clueCount + 1
                    if clueCount is 1:
                        clue_1 = clue.text
                    if clueCount is 2:
                        clue_2 = clue.text
                    if clueCount is 3:
                        clue_3 = clue.text

            ## GET SOLUTION
            if dataCount is 3:
                solution = dataCol.text

            ## GET EFFECT
            if dataCount is 4:
                effect = dataCol.text

        #print(location)
        #print('Location: ' + location + ', Clue 1: ' + clue_1 + ', Clue 2: ' + clue_2 + ', Clue 3: ' + clue_3 + ', Solution: ' + solution + ', Effect: ' + effect)
        baffleBoard = BaffleBoard( location.rstrip(), clue_1.rstrip(), clue_2.rstrip(), clue_3.rstrip(), solution.rstrip(), effect.rstrip())

        test = functions.addBaffleBoardToFile(baffleBoard, "test.js")
        print(test)
