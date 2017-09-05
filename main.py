from room import Room
import character 

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

dave = character.Enemy("Dave", "A smelly zombie")
dave.conversation = "Hnnnng! Hnnnngry.. Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"

dining_hall.character = dave

current_room = kitchen          

dead = False;

while dead == False:     
    print("\n")         
    current_room.get_details()         

    inhabitant = current_room.character
    if inhabitant != None:
        inhabitant.describe()

    command = input("> ")    
    if command in ['north', 'south', 'east','west']:
        current_room = current_room.move(command)  
    elif command == 'talk':
        if inhabitant:
            inhabitant.talk()
        else:
            print ("You shout at the night... no one answers.")
    elif command == 'fight':
        if inhabitant:
            print("What will you fight with?")
            weapon = input()
            dead = not inhabitant.fight(weapon)
        else:
            print ("You swing wildly about and fall flat on your face. ")
    elif command == 'quit':
        print ("You give up and go home.  The End")
        quit();
    else:
        print ("Sorry, I don't know how to " + command)
