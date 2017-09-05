from room import Room
from item import Item
import character 

kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies."

dining_hall = Room("Dining Hall")
dining_hall.description = "A formal dining room with ornate golden decorations on every wall."

ballroom = Room("Ball Room")
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom, "west")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")

dave = character.Enemy("Dave", "A smelly zombie")
dave.conversation = "Hnnnng! Hnnnngry.. Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"
dining_hall.character = dave

# Add a new character
catrina = character.Friend("Catrina", "A friendly skeleton")
catrina.conversation = "Why hello there."
ballroom.character = catrina

# add some items
cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)



current_room = kitchen      
backpack = []    

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
    elif command == 'hug':
        if inhabitant:
            if isinstance(inhabitant, character.Friend):
                inhabitant.hug();
            else:
                print(inhabitant.name + " doesn't look that friendly." )
        else:
            print( "You wrap your arms around yourself and squeeze tight.")
    elif command == 'quit':
        print ("You give up and go home.  The End")
        quit();
    elif command == "take":
        item = current_room.get_item()
        if item is not None:
            print("You put the " + item.name + " in your backpack")
            backpack.append(item.name)
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print ("Sorry, I don't know how to " + command)
