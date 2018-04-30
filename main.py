from turtlebot import Turtlebot
from depth_processing import image2cloud

def main:

    turtle = Turtlebot(pc=True,depth=True)
    K = turtle.get_depth_K()
    while not turtle.is_shutting_down():

        # Process depth image to pointcloud
        depth = turtle.get_depth_image()
        if depth is None:
            print("Depth image is None")
            continue

        # Pointcloud
        pcl = p2c(depth, K, True)








