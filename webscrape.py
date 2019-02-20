import urllib.request
from bs4 import BeautifulSoup
from DAO import Data
import functions

from DTO.BaffleBoard import BaffleBoard

page = functions.scrapeUrl(Data.WEB_LINK)
tableHead = page.find('span', {"id": "Yo-kai_Watch_3"})
table = tableHead.find_parent().find_next_sibling()
tableRows = table.find_all('tr')


rowCount = 0
for row in tableRows:
    rowCount = rowCount + 1
    if rowCount is not 1:

        rowData = row.find_all('td')
        dataCount = 0

        for data in rowData:
            dataCount = dataCount + 1

            ## GET LOCATION
            if dataCount is 1:
                location = data.text
            ## GET CLUES
            if dataCount is 2:
                clues = data.find_all('li')
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
                solution = data.text

            ## GET EFFECT
            if dataCount is 4:
                effect = data.text

        #print(location)
        #print('Location: ' + location + ', Clue 1: ' + clue_1 + ', Clue 2: ' + clue_2 + ', Clue 3: ' + clue_3 + ', Solution: ' + solution + ', Effect: ' + effect)
        baffleBoard = BaffleBoard( location.rstrip(), clue_1.rstrip(), clue_2.rstrip(), clue_3.rstrip(), solution.rstrip(), effect.rstrip())

        test = functions.addBaffleBoardToFile(baffleBoard, "baffleBoard3.js")
        print(test)
