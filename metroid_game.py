#The first line ever read...
print('"The last Metroid is in captivity. The galaxy is at peace..."')

#Function to run the intro of the game.
def Intro():
    print('Congratulations! You are now the owner of a new baby Metroid!')
    print('Please fill out the following information to keep on record with the Metroid Ownership Agency.')
    print('Your Name:')
    global PlayerName
    PlayerName = input()
    print('Your Age:')
    global PlayerAge
    PlayerAge = input()
    print('What will you name your new Metroid?')
    global MetroidName
    MetroidName = input()
    Confirm()

#Function to run the confirmation sequeunce/loop.
def Confirm():
    print('Are you sure? Y/N')
    Answer = input()
    if Answer is ('Y'):
        print ('Your name: ' + PlayerName)
        print ('Your age: ' + PlayerAge)
        print ('Metroid name: ' + MetroidName)
    elif Answer is ('N'):   
        Intro()
    else:
        print('I did not understand. Could you repeat that?')
        Confirm()
        
#The Game
Intro()
print('Changes')

    
    
