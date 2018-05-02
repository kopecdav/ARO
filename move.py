from turtlebot import Rate, get_time

rate = Rate(10)


def rotate(turtle = None, angle=0,speed = 1, verbose = False):
    movement_time = angle/speed
    if verbose:
        print("Rotating for : " + str(movement_time) + " seconds")

    t = get_time()
    while get_time() - t < movement_time:
        turtle.cmd_velocity(linear=0, angular=speed)
        if verbose:
            print("Rotation ready")
        rate.sleep()


