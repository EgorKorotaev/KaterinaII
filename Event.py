class Event:
    def __init__(self, time, place, celebration, description):
        self.time = time
        self.place = place
        self.celebration = celebration
        self.description = description
        self.aGuestList = []

    def addAGuestList(self, guest):
        self.aGuestList.append(guest)

    def __str__(self):
        output = f'   время: {self.time}, место: {self.place}, празднество: {self.celebration}, \n' \
               f'   описание: {self.description}\n' \
               f'   гости:\n'
        for guest in self.aGuestList:
            output += str(guest)
        return output
