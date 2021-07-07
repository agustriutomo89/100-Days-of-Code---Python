def turn_around():
    turn_left()
    turn_left()

def gogo():
    move()
    turn_left()
    move()
    turn_left()
    turn_around()
    move()
    turn_around()
    turn_left()
    move()
    turn_left()

while at_goal() == False:
    gogo()





