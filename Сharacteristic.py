from Guest import Guest


class Characteristic(Guest):
    def __init__(self):
        self.visiting = []

    def addVisiting(self, visiting):
        self.visiting.append(visiting)
