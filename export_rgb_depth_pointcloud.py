from turtlebot import Turtlebot
impot numpy as np

turtle = Turtlebot()
depth = turtle.get_depth_image()
rgb = turtle.get_rgb_image()
point_cloud = turtle.get_point_cloud()

np.save('depth.npy', depth)
np.save('rgb.npy', rgb)
np.save('point_cloud.npy', point_cloud)
