from  base_object import BaseObject

class Room(BaseObject):
    def __init__(self, name):
        super().__init__(name)
        self._linked_rooms = {}
        self._character = None

    # One way to use Property
    def set_char(self, char):
        self._character = char

    def get_char(self):
        return self._character

    character = property(get_char, set_char)

    def link_room(self, room_to_link, direction):
        self._linked_rooms[direction] = room_to_link

    def get_details(self):
        print ('The ' + self.name)
        print ('--------------------')
        self.describe()
        for direction in self._linked_rooms:
            room = self._linked_rooms[direction]
            print( "The " + room.name + " is " + direction)

    def move(self, direction):
        if direction in self._linked_rooms:
            return self._linked_rooms[direction]
        else:
            print ("You can't go that way")
            return self