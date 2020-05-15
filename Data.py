import json

from Day import Day
from Event import Event
from Guest import Guest


class Data:
    def __init__(self):
        self.data = {}
        rawData = json.load(open(r'data.json', 'r', encoding="utf-8"))
        for day in rawData:
            tempDay = Day(day['month'], day['day'], day['weekday'])
            for event in day['event']:
                tempEvent = Event(event['time'], event['place'], event['celebration'], event['description'])
                for guest in event['aGuestList']:
                    tempGuest = Guest(guest['title'], guest['surname'], guest['name'], guest['patronymic'], guest['sequenceNumber'])
                    tempEvent.addAGuestList(tempGuest)
                tempDay.addEvent(tempEvent)
            self.data[str(day['day']) + ' ' + day['month']] = tempDay
