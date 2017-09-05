from  base_object import BaseObject

class Room(BaseObject):
    def __init__(self, name):
        super().__init__(name)
        self.linked_rooms = {}

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print ('The ' + self.name)
        print ('--------------------')
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.name + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print ("You can't go that way")
            return self