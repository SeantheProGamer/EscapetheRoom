    while room == 6:
        print "Well I found the foyer. There's a nice rusty chandelier at the top lighting the horrific paintings of Shawn P. McDonough."
        action5 = input ("Would you like to search the room and possibly find the exit or go back to the living room?")
        if action5 == "Find exit":
            print "I am going to find the exit."
            room = 4
        else:
            print "You are going back to the living room."
