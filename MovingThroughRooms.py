#Escape the Room Program by Seth Williams, Sean Lessard, and Kevin Chambers
import time
import sys
def room():
    room = 0
    blueKey = 0
    redKey = 0
    whiteKey = 0
    silverKey = 0
    goldKey = 0
    timesIntroPlayed = 0
    timesBasementDoorOpened = 0
    timesStairwellDoorOpened = 0
    timesBedroomDoorOpened = 0
    timesBathroomDoorOpened = 0
    timesLivingRoomDoorOpened = 0
    while room <= 6:
        time.sleep(1)
        while room == 0: #Basement (Sean)
            if timesIntroPlayed == 0:
                print 'You wake up in a dark and dreary basement. You are worried that you are trapped. You must find a way out! There is a blue door, a grandfather clock, a set of drawers, and a lamp.'
                print ''
                timesIntroPlayed = 1
            basementAction = raw_input('Type, "Open the basement door" to try opening the door or type, "Search the ..." to search the item you want to interact with.')
            print ''
            if basementAction == 'Open the basement door' or basementAction == 'open the basement door':
                if blueKey == 1:
                    timesBasementDoorOpened += 1
                    if timesBasementDoorOpened <= 1:
                        print 'You are now in a stairwell. Up the stairs is a red door. 5 paintings grace the walls, each with a rusty name plate. The paintings are labeled "Seth", "Sean", "Kevin", "Dylan", and "McDonough".'
                        print ''
                        time.sleep(1)
                    room = 1
                else:
                    print 'The door is locked.'
                    print ''
            elif basementAction == 'Search the grandfather clock' or basementAction == 'search the grandfather clock':
                blueKey = 1
                print 'You found a blue key!'
                print ''
            elif basementAction == 'Search the set of drawers' or basementAction == 'search the set of drawers':
                print "The drawers won't open. They seem to be sealed shut from rust."
                print ''
            elif basementAction == 'Search the lamp' or basementAction == 'search the lamp':
                print 'There is nothing attached to or in the lamp.'
                print ''
            else:
                print "That isn't an available option."
                print ''
            time.sleep(1)
        while room == 1: #Stairwell (Sean)
            stairwellAction = raw_input('Type, "Open the stairwell door" to try opening top stairwell door, type, "Open the basement door" to reenter the basement, or type "Search the painting labeled ..." to search the painting you want to interact with.')
            print ''
            if stairwellAction == 'Open the stairwell door' or stairwellAction == 'open the stairwell door':
                if redKey == 1:
                    timesStairwellDoorOpened += 1
                    if timesStairwellDoorOpened <= 1:
                        print 'You unlock the stairwell door and enter a dimly lit bedroom. You see the light of the bathroom gleaming in the corner. You also see a white door on the opposite side of the bathroom. In the room is a bed, a dresser, a nightstand, and a wardrobe.'
                        print ''
                        time.sleep(1)
                    room = 2
                else:
                    print 'The door is locked.'
                    print ''
            elif stairwellAction == 'Open the basement door' or stairwellAction == 'open the basement door':
                print 'You reenter the basement from the stairwell.'
                print ''
                room = 1
            elif stairwellAction == 'Search the painting labeled Seth' or stairwellAction == 'search the painting labeled Seth':
                print "You flip the painting around and find nothing."
                print ''
            elif stairwellAction == 'Search the painting labeled Kevin' or stairwellAction == 'search the painting labeled Kevin':
                print 'No dice after searching this painting.'
                print ''
            elif stairwellAction == 'Search the painting labeled Sean' or stairwellAction == 'search the painting labeled Sean':
                print "Behind the painting is a hole in the wall. Unfortunately, the hole is empty."
                print ''
            elif stairwellAction == 'Search the painting labeled Dylan' or stairwellAction == 'search the painting labeled Dylan':
                print "He's beautiful, but there is nothing behind the painting."
                print ''
            elif stairwellAction == 'Search the painting labeled McDonough' or stairwellAction == 'search the painting labeled McDonough':
                redKey = 1
                print "You bash his face in and discover a hole in the wall. A red key is inside!"
                print ''
            else:
                print "That isn't an available option."
                print ''
            time.sleep(1)
        while room == 2: #Bedroom (Seth)
            bedroomAction = raw_input('Type, "Open the bedroom door" to try opening the bedroom door, type, "Open the stairwell door" to reenter the basement, type, "Open the bathroom door" to try entering the bathroom, or type "Search the ..." to search the item you want to interact with.')
            print ''
            if bedroomAction == 'Open the bedroom door' or bedroomAction == 'open the bedroom door':
                if whiteKey == 1:
                    timesBedroomDoorOpened += 1
                    if timesBedroomDoorOpened <= 1:
                        print 'You unlock the bedroom door and enter a brightly lit living room. Inside the room is a TV cabinet, a couch, a coffee table, and a lamp.'
                        print ''
                        time.sleep(1)
                    room = 4
                else:
                    print "The door is locked."
                    print ''
            elif bedroomAction == 'Search the bed' or bedroomAction == 'search the bed':
                print "You search the sheets on the bed and find nothing. You'd sleep, but you have to get out of the house!"
                print ''
            elif bedroomAction == 'Search the dresser' or bedroomAction == 'search the dresser':
                print "Don't get too excited, as nothing is inside."
                print ''
            elif bedroomAction == 'Search the nightstand' or bedroomAction == 'search the nightstand':
                whiteKey = 1
                print "In the nightstand drawer, you find a white key!"
                print ''
            elif bedroomAction == 'Search the wardrobe' or bedroomAction == 'search the wardrobe':
                print 'Sadly, nothing is inside.'
                print ''
            elif bedroomAction == 'Open the bathroom door' or bedroomAction == 'open the bathroom door':
                timesBathroomDoorOpened += 1
                if timesBathroomDoorOpened <= 1:
                    print 'You enter a mostly white bathroom. Inside is a shower, a sink, a medicine cabinet, and a toilet.'
                room = 3
            else:
                print "That isn't an available option."
                print ''
            time.sleep(1)
        while room == 3: #Bathroom (Kevin)
            bathroomAction = raw_input('Type, "Open the bathroom door" to exit the bathroom or type "Search the ..." to search the item you want to interact with.')
            print ''
            if bathroomAction == 'Open the bathroom door' or bathroomAction == 'open the bathroom door':
                print 'You reenter the bedroom from the bathroom.'
                print ''
                room = 2
            elif bathroomAction == 'Search the shower' or bathroomAction == 'search the shower':
                print 'Nothing is on the floor of the shower.'
                print ''
            elif bathroomAction == 'Search the sink' or bathroomAction == 'search the sink':
                print 'Nothing is in the sink.'
                print ''
            elif bathroomAction == 'Search the medicine cabinet' or bathroomAction == 'search the medicine cabinet':
                goldKey = 1
                print 'You find a golden key behind some pills in the medicine cabinet!'
                print ''
            elif bathroomAction == 'Search the toilet' or bathroomAction == 'search the toilet':
                print "Don't even think about it. That thing looks disgusting."
                print ''
            elif bathroomAction == 'Open the bathroom door' or bathroomAction == 'open the bathroom door':
                print 'You reenter the bedroom from the bathroom.'
                print ''
                room = 2
            else:
                print "That isn't an available option."
                print ''
            time.sleep(1)
        while room == 4: #Living Room (Sean)
            livingRoomAction = raw_input('Type, "Open the living room door" to try opening the living room door, type, "Open the bedroom door" to reenter the bedroom, or type "Search the ..." to search the item you want to interact with.')
            print ''
            if livingRoomAction == 'Open the living room door' or livingRoomAction == 'open the living room door':
                if silverKey == 1:
                    timesLivingRoomDoorOpened += 1
                    if timesLivingRoomDoorOpened <= 1:
                        print 'You unlock the living room door and enter a dank foyer room. Inside the room is a set of paintings, a flower vase, and an eagle setpiece.'
                        print ''
                        time.sleep(1)
                    room = 5
                else:
                    print "The door is locked."
                    print ''
            elif livingRoomAction == 'Search the TV cabinet' or livingRoomAction == 'search the TV cabinet':
                print "No luck in the TV cabinet. Unfortunately, there is no cable signal, so I can't watch The Room."
                print ''
            elif livingRoomAction == 'Search the couch' or livingRoomAction == 'search the couch':
                silverKey = 1
                print 'After searching the couch cushion, you find some roaches, as well as a silver key!'
                print ''
            elif livingRoomAction == 'Search the coffee table' or livingRoomAction == 'search the coffee table':
                print 'You find an empty Starbucks coffee cup inside the coffee table. But, there is no key...'
                print ''
            elif livingRoomAction == 'Search the lamp' or livingRoomAction == 'search the lamp':
                print "You don't find anything taped to the lamp."
                print ''
            else:
                print "That isn't an available option."
                print ''
            time.sleep(1)

        while room == 5: #Foyer (Seth and Kevin)
            print "Walking through the living room door, you see various Shawn P. McDonough portraits that line the walls so perfectly that you can't even see the walls. There's also a vase with a tree growing out of it, and a rusty, metal, life-sized statue of Shawn P. McDonough."
            print ''
            foyerAction = raw_input('Type, "Open the foyer door" to try opening the foyer door or type "Search the portraits, vase, or statue" to search the item you want to interact with.')
            print ''
            if foyerAction == 'Open the foyer door' or foyerAction == 'open the foyer door':
                print ''
                if goldKey == 1:
                    room = 6
                    time.sleep(1)
                    print "You step out into the light of the outside world. Once your eyes adjust, you see a car that you intend to use to make your escape. You freeze when you get up to it, because in the window's reflection looking back at you was the face of Shawn P. McDonough."
                    time.sleep(5)
                    sys.exit   
                else:
                    print "You need to search for gold key."
            elif foyerAction == 'Search the portraits' or foyerAction == 'search the portraits':
                print "You search each and every portrait over the course of five hours. No dice."
                print ''
            elif foyerAction == 'Search the vase' or foyerAction == 'search the vase':
                print "A fine tree, but no key."
                print ''
            elif foyerAction == 'Search the statue' or foyerAction == 'search the statue':
                print "How do you search a statue?"
                print ''
            else:
                print "That is not an available option."
            time.sleep(1)
room()
