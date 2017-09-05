from room import Room


kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies."

dining_hall = Room("Dining Hall")
dining_hall.description = "A formal dining room with ornate golden decorations on every wall"

ball_room = Room("Ball Room")
ball_room.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ball_room, "west")
dining_hall.link_room(kitchen, "north")
ball_room.link_room(dining_hall, "east")
