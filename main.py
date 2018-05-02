from turtlebot import Turtlebot
from depth_processing import image2cloud
from occupancy_grid import init_map
from time import sleep

def main():

    turtle = Turtlebot(pc=True,depth=True)
    K = turtle.get_depth_K()

    #Init map
    init_map()


    while not turtle.is_shutting_down():

        # Process depth image to pointcloud
        depth = turtle.get_depth_image()
        if depth is None:
            print("Depth image is None")
            continue

        # Pointcloud
        pcl = image2cloud(depth, K, True)

        move = True
        turtle.reset_odometry()
        while move:

            turtle.cmd_velocity(linear=0, angular=90)
            x,y,a = turtle.get_odometry()
            if a > 3.14:
                break

            sleep(0.1)


        # MAP STAGE

        # Plan trajectory, where to go next
        # Go some distance
        # Look around for tags
        # locate yourself with odometry and ICP -> Get Rotation and translation
        # Update Map


        # FINDING STAGE
        # Plan trajectory where to look for tags - detect some walls - define points where to look at them from specific angle
        # Move to those places ad mark the walls




if __name__ == "__main__":
    main()






