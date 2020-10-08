import urllib.request
from bs4 import BeautifulSoup
from assets import data
from assets import functions

from models.Fish import Fish

page = functions.scrape_url(data.WEB_FISH_LINK)
table = page.find('table', {"class": "wikitable"})

tableRows = table.find_all('tr')
rowCount = 0
for row in tableRows:
    rowCount = rowCount + 1
    if rowCount is not 1:

        rowData = row.find_all('td')
        dataCount = 0

        for dataCol in rowData:
            dataCount = dataCount + 1

            ## NAME
            if dataCount is 1:
                fishName = dataCol.text
                print(fishName)

            ## LOCATION
            if dataCount is 2:
                fishLocation = dataCol.text

            ## TIME
            if dataCount is 3:
                fishTime = dataCol.text

            ## RARITY
            if dataCount is 4:
                fishRarity = dataCol.text

            ## BUY
            if dataCount is 5:
                fishBuy = dataCol.text

            ## SELL
            if dataCount is 6:
                fishSell = dataCol.text

            ## RARE SELL
            if dataCount is 6:
                fishRareSell = dataCol.text

        print( '-------' )

        fish = Fish(fishName.rstrip(), fishLocation.rstrip(), fishTime.rstrip(), fishRarity.rstrip(), fishBuy.rstrip(), fishSell.rstrip(), fishRareSell.rstrip())
        functions.add_object_json_to_file(fish, "fish.json")
