from turtlebot import Turtlebot,Rate, get_time



def rotate(turtle = None, angle=0,speed = 1, verbose = False):
    corection = 0.3
    rate = Rate(10)

    movement_time = abs(angle)/speed
    moved_angle=0

    turtle.cmd_velocity(linear=0, angular=0)
    turtle.reset_odometry()
    _, _, off = turtle.get_odometry() 

    if verbose:
        print("Rotating for : " + str(movement_time) + " seconds")
        print("Offset:" + str(off))

    if angle < 0:
        speed = -speed
        corection = -corection

    t = get_time()
    while abs(moved_angle) < abs(angle + off - corection):

	    print("moved_angle: " + str(moved_angle))
	    [x,y,a] = turtle.get_odometry()
	    print("odometry: " + str(a))
	    moved_angle= moved_angle + a
	    turtle.reset_odometry()
	    turtle.cmd_velocity(linear=0, angular=speed)
        print("Angle : " + str(moved_angle))
	    rate.sleep()

    turtle.cmd_velocity(linear=0,angular=0)
    if verbose:
	    print("rotation done")


def translate(turtle = None, linear=2, speed = 1, verbose = False):

    corection = 0
    rate = Rate(10)

    movement_time = abs(angle) / speed
    moved_angle = 0

    turtle.cmd_velocity(linear=0, angular=0)
    turtle.reset_odometry()
    _, _, off = turtle.get_odometry()

    if verbose:
        print("Translating for : " + str(movement_time) + " seconds")
        print("Offset:" + str(off))

    if linear < 0:
        speed = -speed
        corection = -corection

    t = get_time()
    moved_distance = 0

    while abs(moved_distance) < abs(linear + off - corection):

        print("Something gonna happen here soon")




