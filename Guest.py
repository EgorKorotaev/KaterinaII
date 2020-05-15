class Guest:
    def __init__(self, title, surname, name, patronymic, sequenceNumber):
        self.title = title
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.sequenceNumber = sequenceNumber

    def __str__(self):
        output = f'   {self.title} {self.surname} {self.name} {self.patronymic} {self.sequenceNumber}\n'
        return output
