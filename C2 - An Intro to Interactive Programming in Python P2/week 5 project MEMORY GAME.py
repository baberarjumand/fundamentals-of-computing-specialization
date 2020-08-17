# http://www.codeskulptor.org/#user47_IgQtuIGiS9B3AYB.py

# implementation of card game - Memory

import simplegui
import random

cards_deck = []
cards_expose_status = [False] * 16
turns = 0
game_state = 0 # 0 -> no card selected, 1 -> one card selected, 2 -> 2 cards selected
select_card_1 = -1
select_card_2 = -1


# helper function to initialize globals
def new_game():
    global cards_deck, cards_expose_status, turns, game_state
    cards_deck = range(0,8) + range(0,8)
    random.shuffle(cards_deck)
    cards_expose_status = [False] * len(cards_deck)
    game_state = 0
    turns = 0    
    label.set_text("Turns = " + str(turns))


# define event handlers
def mouseclick(pos):
    global cards_expose_status, cards_deck, turns, game_state, select_card_1, select_card_2
    
    clicked_card_index = pos[0] / 50
    
    if game_state == 0:
        game_state = 1
        cards_expose_status[clicked_card_index] = True
        select_card_1 = clicked_card_index
        turns = 1
    elif game_state == 1:
        if cards_expose_status[clicked_card_index] == False:
            cards_expose_status[clicked_card_index] = True
            game_state = 2
            select_card_2 = clicked_card_index
    else:
        if cards_expose_status[clicked_card_index] == False:
            cards_expose_status[clicked_card_index] = True
            if cards_deck[select_card_1] == cards_deck[select_card_2]:
                cards_expose_status[select_card_1] = True
                cards_expose_status[select_card_2] = True
            else:
                cards_expose_status[select_card_1] = False
                cards_expose_status[select_card_2] = False
            turns += 1                
            game_state = 1
            select_card_1 = clicked_card_index
            
    label.set_text("Turns = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards_deck
    for i in range(0,16):
        if cards_expose_status[i]:
            canvas.draw_text(str(cards_deck[i]), [9 + (50*i), 75], 72, "White")
        else:
            canvas.draw_polygon([(i*50, 0), (50 + (i*50), 0), (50 + (i*50), 100), (i*50, 100)], 2, "Red", "Green")        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric