def up():
    turn_left()
    move()

# Challenge 1: Turn right function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
move()
up()
right()
down()

# Challenge 2 : Robot should move in square and return
# to original position
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()