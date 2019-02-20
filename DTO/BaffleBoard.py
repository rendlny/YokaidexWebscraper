class BaffleBoard:
    def __init__(self, location='', clue_1='', clue_2='', clue_3='', solution='', effect=''):
        self.location = location
        self.clue_1 = clue_1
        self.clue_2 = clue_2
        self.clue_3 = clue_3
        self.solution = solution
        self.effect = effect

    #LOCATION
    def get_location(self):
        return self.idea

    def set_location(self, location):
        self.location = location
        return

    #CLUE_1
    def get_clue_1(self):
        return self.clue_1

    def set_clue_1(self, clue_1):
        self.clue_1 = clue_1
        return

    #CLUE_2
    def get_clue_2(self):
        return self.clue_2

    def set_clue_2(self, clue_2):
        self.clue_2 = clue_2
        return

    #CLUE_3
    def get_clue_3(self):
        return self.clue_3

    def set_clue_3(self, clue_3):
        self.clue_3 = clue_3
        return

    #SOLUTION
    def get_solution(self):
        return self.solution

    def set_solution(self, solution):
        self.solution = solution
        return

    #EFFECT
    def get_effect(self):
        return self.effect

    def set_effect(self, effect):
        self.effect = effect
        return

    def display(self):
        msg =  'Location: ' + self.location + ', Clue 1: ' + self.clue_1 + ', Clue 2: ' + self.clue_2 + ', Clue 3: ' + self.clue_3 + ', Solution: ' + self.solution + ', Effect: ' + self.effect
        return msg

    def json(self):
        json =  '{\n\t"location":"' + self.location + '", "clue_1":"' + self.clue_1 + '", "clue_2":"' + self.clue_2 + '", "clue_3":"' + self.clue_3 + '", "solution":"' + self.solution + '", "effect":"' + self.effect + '"\n},\n'
        return json
