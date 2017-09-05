class Room():
    def __init__(self, name):
        self._name = name
        self._description = None
        self.linked_rooms = {}

    # One way to use Property
    def set_description(self, text):
        self._description = text

    def get_description(self):
        return self._description

    description = property(get_description, set_description)

    # another way to use Property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text

    # describe function
    def describe(self): 
        print( self.description )

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
