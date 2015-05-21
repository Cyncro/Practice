#The first line ever read...
print('"The last Metroid is in captivity. The galaxy is at peace..."')

#Function to run the intro of the game.
def intro():
    print('Congratulations! You are now the owner of a new baby Metroid!')
    print('Please fill out the following information to keep on record with the Metroid Ownership Agency.')
    print('Your Name:')
    global player_name
    player_name = input()
    print('Your Age:')
    global player_age
    player_age = input()
    print('What will you name your new Metroid?')
    global metroid_name
    metroid_name = input()
    confirm()

#Function to run the confirmation sequeunce/loop.
def confirm():
    print('Are you sure? Y/N')
    answer = input()
    if answer is ('Y'):
        print ('Your name: ' + player_name)
        print ('Your age: ' + player_age)
        print ('Metroid name: ' + metroid_name)
    elif answer is ('N'):   
        intro()
    else:
        print('I did not understand. Could you repeat that?')
        confirm()
        
#The Game

    metroid_names = ['Jim', 'Joe-bob', 'Ricardo', ('nested list whoaaaaa', 'omg i cant take it :O')]
    print (metroid_names)
    #print (" | ".join(metroid_names))
    print (metroid_names[0])
    metroid_names.append(metroid_name)
    print (metroid_names)
    print (metroid_names[3][0]) 
    feed = 0
    print(feed)

    while feed < 2:
        print('Feed Metroid? Y/N')
        feed_answer = input().lower()
        if feed_answer == 'y':
            print('Metroid has been fed!')
            feed += 1
            print("The metroid has been fed {} times!".format(feed))

intro()


    

