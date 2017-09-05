from room import Room


kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies."

dining_hall = Room("Dining Hall")
dining_hall.description = "A formal dining room with ornate golden decorations on every wall."

ball_room = Room("Ball Room")
ball_room.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ball_room, "west")
dining_hall.link_room(kitchen, "north")
ball_room.link_room(dining_hall, "east")

current_room = kitchen          

from character import Character

dave = Character("Dave", "A smelly zombie")

dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("What's up, dude!")

# Trigger a conversation with Dave
dave.talk()


while True:     
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command)  