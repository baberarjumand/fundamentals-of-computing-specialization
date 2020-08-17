# http://www.codeskulptor.org/#user47_RfwliOq092_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game(rangeLimit):
    # initialize global variables used in your code here
    global secret_number
    global my_frame
    global num_of_guesses
    
    if rangeLimit == 100:    
        secret_number = random.randrange(0,100)
        num_of_guesses = 7
        print 'New game started'
        print 'Guess the number in range [0,100)'
        print 'Remaining Guesses:', num_of_guesses
        my_frame.start()
    elif rangeLimit == 1000:
        secret_number = random.randrange(0,1000)
        num_of_guesses = 10
        print 'New game started'
        print 'Guess the number in range [0,1000)'
        print 'Remaining Guesses:', num_of_guesses
        my_frame.start()
    else:
        print 'Invalid range input'
    print ' '

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(1000)
    
def input_guess(guess):
    # main game logic goes here
    guess_int = int(guess)
    global num_of_guesses
    
    print 'Guess was', guess_int
    if (guess_int > secret_number) and num_of_guesses > 1:
        num_of_guesses -= 1
        print 'Lower! Remaining Guesses:', num_of_guesses
    elif (guess_int < secret_number) and num_of_guesses > 1:
        num_of_guesses -= 1
        print 'Higher! Remaining Guesses:', num_of_guesses
    elif (guess_int == secret_number):
        print 'Correct! Player wins!'
        print 'Starting new game...\n'
        new_game(100)
    elif (num_of_guesses <= 1):
        print 'Sorry, you ran out of guesses!'
        print 'Starting new game...\n'
        new_game(100)
    else:
        print 'Something went wrong'
    print ''
    
# create frame
my_frame = simplegui.create_frame("Home", 300, 200)

# register event handlers for control elements and start frame
my_frame.add_button("Set Range to [0,100)", range100)
my_frame.add_button("Set Range to [0,1000)", range1000)
my_frame.add_input('Enter Number', input_guess, 50)

# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
