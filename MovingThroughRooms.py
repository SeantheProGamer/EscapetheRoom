def room():
    room = 1
    while room < 4:    
        key = 0
        gold = 0
        room = 1
        while room == 1:
            print "You are now in the basement. A cold, dark room underneath the house. It smells like rust. There is a door to the north, a rusty grandfather clock, a rusty drawer, and a rusty lamp."
            action1 = input("(Type the direction you want to go or the item you want to interact with with quotation marks)")
            if action1 == "north":
                if key == 1:
                    room = 2
                else:
                    print "It's locked."
            else:
                print "That is a wall."
            if action1 == "Search the grandfather clock":
                key = 1
                print "You found a rusty key... sick."
            if action1 == "Search the drawer":
                print "Doesn't open, too rusty."
            if action1 == "Search the lamp":
                print "It's a lamp, it doesn't have storage space."
            else:
                print "That aint an option."
        while room == 2:   
            print "You are now on the stairs. To the north is a door. 5 paintings grace the walls, each with a rusty name plate and a description. Seth: A handsome boy. Kevin: Cries himself to slept every night. Sean: Timid individual. Dylan: The best teacher. McDonough: A vile toadstool who isn't particularly good at teaching."
            action2 = input("Choose.")
            if action2 == "north":
                if key == 2:
                    room = 3
                else:
                    print "That door is also locked. Geez, two in a row."
            if action2 == "Search Seth":
                print "You gently look behind the painting... nothing."
            if action2 == "Search Kevin":
                print "Nope."
            if action2 == "Search Sean":
                print "Behind the painting is a hole in the wall. It's empty."
            if action2 == "Search Dylan":
                print "He's beautiful."
            if action2 == "Search McDonough":
                print "You bash his face in and find a key. Bonus!"
                key = 2
            else:
                print "You sit down and think about death."
        while room == 3:   
            print "You are now in a bedroom with a rusty bed, a rusty dresser, a rusty nightstand, and a rusty wardrobe. There is also a door to the north. There is a bathroom to the east."
            action3 = input("Choose.")
            if action3 == "north":
                if key == 3:
                    room = 5
                else:
                    print "It's too locked."
            if action3 == "Search bed":
                print "You'd go to sleep, but it smells like rust."
            if action3 == "Search dresser":
                print "Don't get too excited."
            if action3 == "Search nightstand":
                print "Wow, that's alot of pills. Oh, there's also a strange golden key."
                gold = 1
            if action3 == "Search wardrobe":
                print "That's alot of skeletons."
            if action3 == "east":
                room = 4
                while room == 4:
                    print "Your in a bathroom. Oh god, your drowning in rust. Search it, search the bathroom."
                    action4 = input("Choose.")
                    if action3 == "Search the bathroom.":
                        print "Oooooo, boy. Another rusty key. DELICIOUS!"
                        room = 3
                    else:
                        print "Search the batheroom, Shawn."
            else:
                "Your getting tired of all this rust."
        while room == 5:
            print "Aw dang it! A rusty living room!"

room()
