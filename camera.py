#!/usr/bin/env python

from turtlebot import Turtlebot
import numpy as np
import cv2
from numpy.linalg import inv
import matplotlib.pyplot as plt

x_range = (-0.3, 0.3)
z_range = (0.3, 3.0)
WINDOW = 'obstacles'

def main():

    turtle = Turtlebot(pc=True)
    cv2.namedWindow(WINDOW)

    while not turtle.is_shutting_down():
        # get point cloud
        pc = turtle.get_point_cloud()

	    if pc is None:
 	        continue

        # mask out floor points
        mask = pc[:,:,1] > x_range[0]

        x = pc[:,:,1] > x_range[0]


        # mask point too far and close
    	mask = np.logical_and(mask, pc[:,:,2] > z_range[0])
        mask = np.logical_and(mask, pc[:,:,2] < z_range[1])


        if np.count_nonzero(mask) <= 0:
            continue


        valid_depth = np.sum(~np.isnan(data['depth']))
        points = np.zeros((3, valid_depth))
        points_depths = np.zeros((1, valid_depth))
        cnt = 0
        for u in range(0, 480):
            for v in range(0, 640):
            # create coordinates vector
            if ~np.isnan(depth[u][v]):
                points[0, cnt] = v * depth[u][v]
                points[1, cnt] = u * depth[u][v]
                points[2, cnt] = 1 * depth[u][v]
            # points_depths[0,cnt] = depth[u][v]
            cnt = cnt + 1

        pointcloud = inv(turtle.get_depth_K(self)).dot(points)


        Ry = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])
        pointcloud = Ry.dot(pointcloud)


        vec = ((pointcloud[2, :] < 0.3) & (pointcloud[2, :] > -0.3) & (pointcloud[0, :] > 0.2) & (pointcloud[0, :] < 3))


        pointcloud = pointcloud[:, vec]

        fig = plt.figure(frameon=True)
        ax = fig.gca()
        ax.axis('equal')

        ax.scatter(pointcloud[1, :], pointcloud[0, :], s=1)  # Need to swap the coordinates to plot it nicely
        ax.invert_xaxis()  # Invert the y axis (which is now x), to have it the way robot sees it. Sadly there is not nicer way in matplotlib
        ax.scatter([0], [0], c='r')

        plt.show()
        # empty image
        image = np.zeros(mask.shape)

        # assign depth i.e. distance to image
        image[mask] = np.int8(pc[:,:,2][mask] / 3.0 * 255)
        im_color = cv2.applyColorMap(255 - image.astype(np.uint8), cv2.COLORMAP_JET)

        # show image
        cv2.imshow(WINDOW, im_color)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()

