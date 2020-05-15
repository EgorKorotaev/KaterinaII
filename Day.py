class Day:
    def __init__(self, month, day, weekday):
        self.month = month
        self.day = day
        self.weekday = weekday
        self.event = []

    def addEvent(self, event):
        self.event.append(event)

    def __str__(self):
        output = f'месяцъ: {self.month}, день: {self.day}, день недели: {self.weekday}\n' \
               f'события:\n'
        for event in self.event:
            output += str(event)
        return output
