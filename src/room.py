# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def _printing(self):
        return self.__dict__

    def __str__(self):
        return '{self.name}, Descripition: {self.description}'.format(self=self)
