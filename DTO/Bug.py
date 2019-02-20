class Bug:
    def __init__(self, name, location, description, sell, rare_sell):
        self.name = name
        self.location = location
        self.description = description
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

    #DESCRIPTION
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
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
        msg =  'Name: ' + self.name + ', Location: ' + self.location + ', Description: ' + self.description + ', Sell: ' + self.sell + ', Rare Sell: ' + self.rare_sell
        return msg

    def json(self):
        json = '{\n\t"name":"' + self.name + '", "location":"' + self.location + '", "description":"' + self.description + '", "sell":"' + self.sell + '", "rare_sell":"' + self.rare_sell + '"\n},\n'
        return json
