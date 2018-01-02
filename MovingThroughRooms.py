import time
def room():
    room = 0
    blueKey = 0
    redKey = 0
    whiteKey = 0
    silverKey = 0
    goldKey = 0
    timesBasementDoorOpened = 0
    timesStairwellDoorOpened = 0
    timesBedroomDoorOpened = 0
    timesBathroomDoorOpened = 0
    timesLivingRoomDoorOpened = 0
    while room <= 6:
        print 'You wake up in a dark and dreary basement. You are worried that you are trapped. You must find a way out! There is a blue door, a grandfather clock, a set of drawers, and a lamp.'
        print ''
        time.sleep(1)
        while room == 0: #Basement
            basementAction = input('Type, "Open the basement door" to try opening the door or type, "Search the ..." to search the item you want to interact with.')
            print ''
            if basementAction == 'Open the basement door' or 'open the basement door':
                timesBasementDoorOpened += 1
                if blueKey == 1:
                    if timesBasementDoorOpened <= 1:
                        print 'You are now in a stairwell. Up the stairs is a red door. 5 paintings grace the walls, each with a rusty name plate. The paintings are labeled "Seth", "Sean", "Kevin", "Dylan", and "McDonough".'
                        print ''
                        time.sleep(1)
                    room = 1
                else:
                    print 'The door is locked.'
                    print ''
                    time.sleep(1)
            elif basementAction == 'Search the grandfather clock' or 'search the grandfather clock':
                blueKey = 1
                print 'You found a blue key!'
                print ''
                time.sleep(1)
            elif basementAction == 'Search the set of drawers' or 'search the set of drawers':
                print "The drawers won't open. They seem to be sealed shut from rust."
                print ''
                time.sleep(1)
            elif basementAction == 'Search the lamp' or 'search the lamp':
                print 'There is nothing attached to or in the lamp.'
                print ''
                time.sleep(1)
            else:
                print "That isn't an available option."
                print ''
                time.sleep(1)
        while room == 1: #Stairwell
            stairwellAction = input('Type, "Open the stairwell door" to try opening top stairwell door, type, "Open the basement door" to reenter the basement, or type "Search the painting labeled ..." to search the painting you want to interact with.')
            print ''
            if stairwellAction == 'Open the stairwell door' or 'open the stairwell door':
                timesStairwellDoorOpened += 1
                if redKey == 1:
                    if timesStairwellDoorOpened <= 1:
                        print 'You unlock the stairwell door and enter a dimly lit bedroom. You see the light of the bathroom gleaming in the corner. You also see a white door on the opposite side of the bathroom. In the room is a bed, a dresser, a nightstand, and a wardrobe.'
                        print ''
                        time.sleep(1)
                    room = 2
                else:
                    print 'The door is locked.'
                    print ''
                    time.sleep(1)
            elif stairwellAction == 'Open the basement door' or 'open the basement door':
                print 'You reenter the basement from the stairwell.'
                print ''
                time.sleep(1)
                room = 1
            elif stairwellAction == 'Search the painting labeled Seth' or 'search the painting labeled Seth':
                print "You flip the painting around and find nothing."
                print ''
                time.sleep(1)
            elif stairwellAction == 'Search the painting labeled Kevin' or 'search the painting labeled Kevin':
                print 'No dice after searching this painting.'
                print ''
                time.sleep(1)
            elif stairwellAction == 'Search the painting labeled Sean' or 'search the painting labeled Sean':
                print "Behind the painting is a hole in the wall. Unfortunately, the hole is empty."
                print ''
                time.sleep(1)
            elif stairwellAction == 'Search the painting labeled Dylan' or 'search the painting labeled Dylan':
                print "He's beautiful, but there is nothing behind the painting."
                print ''
                time.sleep(1)
            elif stairwellAction == 'Search the painting labeled McDonough' or 'search the painting labeled McDonough':
                redKey = 1
                print "You bash his face in and discover a hole in the wall. A red key is inside!"
                print ''
                time.sleep(1)
            else:
                print "That isn't an available option."
                print ''
                time.sleep(1)
        while room == 2: #Bedroom
            bedroomAction = input('Type, "Open the bedroom door" to try opening the bedroom door, type, "Open the stairwell door" to reenter the basement, type, "Open the bathroom door" to try entering the bathroom, or type "Search the ..." to search the item you want to interact with.')
            print ''
            if bedroomAction == 'Open the bedroom door' or 'open the bedroom door':
                timesBedroomDoorOpened += 1
                if whiteKey == 1:
                    if timesBedroomDoorOpened <= 1:
                        print 'You unlock the bedroom door and enter a brightly lit living room. Inside the room is a TV cabinet, a couch, a coffee table, and a lamp.'
                        print ''
                        time.sleep(1)
                    room = 4
                else:
                    print "The door is locked."
                    print ''
                    time.sleep(1)
            elif bedroomAction == 'Search the bed' or 'search the bed':
                print "You search the sheets on the bed and find nothing. You'd sleep, but you have to get out of the house!"
                print ''
                time.sleep(1)
            elif bedroomAction == 'Search the dresser' or 'search the dresser':
                print "Don't get too excited, as nothing is inside."
                print ''
                time.sleep(1)
            elif bedroomAction == 'Search the nightstand' or 'search the nightstand':
                whiteKey = 1
                print "In the nightstand drawer, you find a white key!"
                print ''
                time.sleep(1)
            elif bedroomAction == 'Search the wardrobe' or 'search the wardrobe':
                print 'Sadly, nothing is inside.'
                print ''
                time.sleep(1)
            elif bedroomAction == 'Open the bathroom door' or 'open the bathroom door':
                timesBathroomDoorOpened += 1
                if timesBathroomDoorOpened <= 1:
                    print 'You enter a mostly white bathroom. Inside is a shower, a sink, a medicine cabinet, and a toilet.'
                room = 3
            else:
                print "That isn't an available option."
                print ''
                time.sleep(1)
        while room == 3: #Bathroom
            bathroomAction = input('Type, "Open the bathroom door" to exit the bathroom or type "Search the ..." to search the item you want to interact with.')
            print ''
            if bathroomAction == 'Open the bathroom door':
                print 'You reenter the bedroom from the bathroom.'
                print ''
                time.sleep(1)
                room = 2
            elif bathroomAction == 'Search the shower' or 'search the shower':
                print 'Nothing is on the floor of the shower.'
                print ''
                time.sleep(1)
            elif bathroomAction == 'Search the sink' or 'search the sink':
                print 'Nothing is in the sink.'
                print ''
                time.sleep(1)
            elif bathroomAction == 'Search the medicine cabinet' or 'search the medicine cabinet':
                goldKey = 1
                print 'You find a golden key behind some pills in the medicine cabinet!'
                print ''
                time.sleep(1)
            elif bathroomAction == 'Search the toilet' or 'search the toilet':
                print "Don't even think about it. That thing looks disgusting."
                print ''
                time.sleep(1)
            elif bathroomAction == 'Open the bathroom door' or 'open the bathroom door':
                print 'You reenter the bedroom from the bathroom.'
                print ''
                time.sleep(1)
                room = 2
            else:
                print "That isn't an available option."
                print ''
                time.sleep(1)
        while room == 4: #Living Room
            livingRoomAction = input('Type, "Open the living room door" to try opening the living room door, type, "Open the bedroom door" to reenter the bedroom, or type "Search the ..." to search the item you want to interact with.')
            print ''
            if livingRoomAction == 'Open the living room door' or 'open the living room door':
                timesLivingRoomDoorOpened += 1
                if silverKey == 1:
                    if timesLivingRoomDoorOpened <= 1:
                        print 'You unlock the living room door and enter a dank foyer room. Inside the room is a set of paintings, a flower vase, and an eagle setpiece.'
                        print ''
                        time.sleep(1)
                    room = 5
                else:
                    print "The door is locked."
                    print ''
                    time.sleep(1)
        while room == 5: #Foyer


room()
