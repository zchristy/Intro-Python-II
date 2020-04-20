# Implement a class to hold item information. This should have name and
# description attributes.

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def _printing(self):
        return self.__dict__

    def __str__(self):
        return '{self.name}, Descripition: {self.description}'.format(self=self)
