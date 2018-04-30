from turtlebot import Turtlebot
import numpy as np

turtle = Turtlebot(pc=True, rgb=True, depth=True)

while not turtle.is_shutting_down():

    depth = turtle.get_depth_image()
    rgb = turtle.get_rgb_image()
    point_cloud = turtle.get_point_cloud()
    rgb_K = turtle.get_rgb_K()
    depth_K = turtle.get_depth_K()

    if rgb is None:
        continue
    if depth is None:
        continue
    if point_cloud is None:
        continue
    if rgb_K is None:
        continue
    if depth_K is None:
        continue

    np.save('exports/depth.npy', depth)
    np.save('exports/rgb.npy', rgb)
    np.save('exports/point_cloud.npy', point_cloud)
    np.save('exports/rgb_K.npy', rgb_K)
    np.save('exports/depth_K.npy', depth_K)

    exit(0)
