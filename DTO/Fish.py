class Fish:
    def __init__(self, name, location, time, rarity, buy, sell, rare_sell):
        self.name = name
        self.location = location
        self.time = time
        self.rarity = rarity
        self.buy = buy
        self.sell = sell
        self.rare_sell = rare_sell

    #NAME
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return

    #LOCATION
    def get_location(self):
        return self.idea

    def set_location(self, location):
        self.location = location
        return

    #TIME
    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        return

    #RARITY
    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity):
        self.rarity = rarity
        return

    #BUY
    def get_buy(self):
        return self.buy

    def set_buy(self, buy):
        self.buy = buy
        return

    #SELL
    def get_sell(self):
        return self.sell

    def set_sell(self, sell):
        self.sell = sell
        return

    #RARE_SELL
    def get_rare_sell(self):
        return self.rare_sell

    def set_rare_sell(self, rare_sell):
        self.rare_sell = rare_sell
        return

    def display(self):
        msg =  'Name: ' + self.name + ', Location: ' + self.location + ', Time: ' + self.time + ', Rarity: ' + self.rarity + ', Buy: ' + self.buy + ', Sell: ' + self.sell + ', Rare Sell: ' + self.rare_sell
        return msg

    def json(self):
        json =  '{\n\t"name":"' + self.name + '", "location":"' + self.location + '", "time":"' + self.time + '", "rarity":"' + self.rarity + '", "buy":"' + self.buy + '", "sell":"' + self.sell + '", "rare_sell":"' + self.rare_sell + '"\n},\n'
        return json
