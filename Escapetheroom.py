def room():
    room = 1
    while room < 4:    
        room = 1
        if room == 1:
            print "You are now in room 1."
            action1 = input("Choose. (Type forward with quotation marks)")
            if action1 == "forward":
                room = 2
            else:
                room = 2
        if room == 2:   
            print "You are now in room 2."
            action2 = input("Choose. (Type forward with quotation marks)")
            if action2 == "forward":
                room = 3
            else:
                room = 3
        if room == 3:   
            print "You are now in room 3."
            action3 = input("Choose. (Type forward with quotation marks)")
            if action3 == "forward":
                room = 1
            else:
                room = 1

room()
