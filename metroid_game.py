#!/usr/bin/python3

#The first line ever read...
print('"The last Metroid is in captivity. The galaxy is at peace..."')

player_info = []

#Function to run the intro of the game.
def intro():
    print('Congratulations! You are now the owner of a new baby Metroid!')
    print('Please fill out the following information to keep on record with the Metroid Ownership Agency.')
    print('Your Name:')
    player_name = input()
    print('Your Age:')
    player_age = input()
    print('What will you name your new Metroid?')
    metroid_name = input()
    player_info.append(player_name)
    player_info.append(player_age)
    player_info.append(metroid_name)

    print("player_info", player_info)

    confirm(player_name, player_age, metroid_name)

#Function to run the confirmation sequeunce/loop.
def confirm(player_name, player_age, metroid_name):
    print('Are you sure? Y/N')
    answer = input().lower()
    if answer == ('y'):
        print ('Your name: ' + player_name)
        print ('Your age: ' + player_age)
        print ('Metroid name: ' + metroid_name)
    elif answer == ('n'):
        intro()
    else:
        print('I did not understand. Could you repeat that?')
        confirm(player_name, player_age, metroid_name)
        
#The Game

    feed = 0
    print(feed)

    while feed < 2:
        print('Feed Metroid? Y/N')
        feed_answer = input().lower()
        if feed_answer == 'y':
            print('Metroid has been fed!')
            feed += 1
            print("The metroid has been fed {} times!".format(feed))
        else:
            print("You're a monster!")

intro()


    

