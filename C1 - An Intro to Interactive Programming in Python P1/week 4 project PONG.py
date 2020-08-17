# http://www.codeskulptor.org/#user47_nPGtx6IPDHE5pox.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

BALL_LINE_WIDTH = 5

paddle1_pos = HEIGHT / 2 # left paddle
paddle2_pos = HEIGHT / 2 # right paddle

paddle1_vel = 0 # left
paddle2_vel = 0 # right

score1 = 0 # left
score2 = 0 # right

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if (direction):    
#         ball_vel = [2, 2]
        ball_vel = [random.randrange(3, 6), -1 * random.randrange(1, 5)]
    else:
#         ball_vel = [-2, 2]
        ball_vel = [(-1 * random.randrange(3, 6)), -1 * random.randrange(1, 5)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    ## draw mid line and gutters
    # mid line
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    # left gutter
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    # right gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    ## update ball
    # bounce off right paddle OR left paddle scores    
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        if (ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
        
    # bounce off left paddle OR right player scores
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):        
        if (ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) and (ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    ball_pos[0] += ball_vel[0] # update ball's x coord
    # bounce off top
    if ball_pos[1] <= (0 + BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    # bounce off bottom
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
        
    ball_pos[1] += ball_vel[1] # update ball's y coord
       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, BALL_LINE_WIDTH, 'white', 'white')
    
    ## update paddle's vertical position, keep paddle on the screen
    # left paddle
    if ((paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT) and  ((paddle1_pos + paddle1_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle1_pos += paddle1_vel
    # right paddle
    if ((paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT) and ((paddle2_pos + paddle2_vel) <= (HEIGHT - HALF_PAD_HEIGHT)):
        paddle2_pos += paddle2_vel
    
    ## draw paddles
    # left paddle
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 1, 'white', 'red')
    # right paddle
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 1, 'white', 'green')
    
    # draw scores
    canvas.draw_text(str(score1), (0.25 * WIDTH, 0.20 * HEIGHT), 50, 'red')
    canvas.draw_text(str(score2), (0.75 * WIDTH, 0.20 * HEIGHT), 50, 'green')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    # left paddle
    if key == simplegui.KEY_MAP["w"]:            
        paddle1_vel = -7
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 7
        
    # right paddle
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -7
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 7

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    # left paddle
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    # right paddle
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart Game', new_game)


# start frame
new_game()
frame.start()
