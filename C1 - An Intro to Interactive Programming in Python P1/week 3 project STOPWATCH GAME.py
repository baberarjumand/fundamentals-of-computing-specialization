# http://www.codeskulptor.org/#user47_2i5a43DWAo_0.py

# template for "Stopwatch: The Game"

import simplegui

# define global variables
TIMER_INTERVAL = 100
counter = 0
score = 0
attempts = 0
scoreStr = '0/0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(input):
    global formattedCounterStr
    num_of_mins = input // 600
    seconds = (input % 600) / 10.0
    if (seconds < 9.9):
        return str(num_of_mins) + ':0' + str(seconds)        
    else:
        return str(num_of_mins) + ':' + str(seconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startTimer():
    timer.start()

def stopTimer():
    timer.stop()
    global score, attempts, scoreStr
    attempts += 1
    if counter % 10 == 0:
        score += 1
    scoreStr = str(score) + '/' + str(attempts)

def resetTimer():
    if timer.is_running():
        timer.stop()
    global counter, score, attempts, scoreStr
    counter = 0
    score = 0
    attempts = 0
    scoreStr = str(score) + '/' + str(attempts)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), [100, 100], 36, 'red')
    canvas.draw_text(scoreStr, [200, 50], 36, 'green')

    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200)
frame.set_draw_handler(draw)
frame.add_button("Start", startTimer)
frame.add_button("Stop", stopTimer)
frame.add_button("Reset", resetTimer)

# register event handlers
timer = simplegui.create_timer(TIMER_INTERVAL, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric