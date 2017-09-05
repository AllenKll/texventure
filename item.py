from base_object import BaseObject

class Item(BaseObject):
    def __init__(self, name):
        super().__init__(name)
    
    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)