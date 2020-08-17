# http://www.codeskulptor.org/#user47_fYEo0NdcnX_1.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer = None
player = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        strA = 'Current hand: '
        for card in self.hand:
            strA += str(card) + ' '
        return strA

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        score = 0
        flag = False
        for card in self.hand:
            rank = card.get_rank()
            if rank == "A":
                flag = True
            score += VALUES[rank]
        if flag:
            if score + 10 <= 21:
                return score + 10
            else:
                return score
        else:
            return score
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]


# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = [Card(suit,rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        strA = 'Current deck: '
        for card in self.deck:
            strA += str(card) + ' '
        return strA


#define event handlers for buttons
def deal():
    global outcome, in_play, score, deck, dealer, player
    
    if in_play:
        score -= 1
        
    in_play = True
    outcome = "Do you want to HIT or STAND?"
        
    deck = Deck()
    deck.shuffle()
    
    dealer = Hand()
    player = Hand()
    
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global in_play, player, deck, outcome, score
 
    # if the hand is in play, hit the player   
    if in_play:        
        outcome = "Do you want to HIT or STAND?"
        player.add_card(deck.deal_card())
        
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "Player BUSTED and lost. Deal Again?"
            in_play = False
            score -= 1

def stand():
    global in_play, outcome, deck, dealer, player, score
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            outcome = "Dealer BUSTED and lost. Deal again?"            
            score += 1
        elif player.get_value() <= dealer.get_value():
            outcome = "Dealer wins. Deal again?"            
            score -= 1
        else:
            outcome = "Player wins. Deal again?" 
            score += 1
        in_play = False

# draw handler    
def draw(canvas):
    global dealer, player, outcome, score, in_play
    
    canvas.draw_text("Blackjack", (200, 50), 48, 'black')
    
    canvas.draw_text(outcome, (30, 300), 36, 'white')
    
    canvas.draw_text("Dealer", (30, 140), 48, 'black')
    dealer.draw(canvas, [30, 150])
    dealer_pos = [30, 150]
    
    if in_play:
        card_location = (CARD_CENTER[0] + CARD_SIZE[0], CARD_CENTER[1] + CARD_SIZE[1])
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [dealer_pos[0] + CARD_CENTER[0],
                                                              dealer_pos[1] + CARD_CENTER[1]], CARD_SIZE)
    else:
        card_location = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(dealer.hand[0].get_rank()), CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(dealer.hand[0].get_suit()))
        canvas.draw_image(card_images, card_location, CARD_SIZE, [dealer_pos[0] + CARD_CENTER[0], dealer_pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    canvas.draw_text("Player: "+ str(player.get_value()), (30, 370), 48, 'black')
    player.draw(canvas, [30, 380])
    
    canvas.draw_text("Score: "+ str(score), (350, 140), 48, 'white')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric