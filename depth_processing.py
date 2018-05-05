
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt




def image2cloud(data, K_depth ,ploting = False):

    depth = data
    valid_depth = np.sum(~np.isnan(data))
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
                cnt = cnt + 1

    # Transform from Image to Origin coordinates
    pointcloud = inv(K_depth).dot(points)

    # Rotate
    Ry = np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]])
    pointcloud = Ry.dot(pointcloud)

    # Limit constrains
    vec = ((pointcloud[2, :] < 0.1) & (pointcloud[2, :] > -0.3) & (pointcloud[0, :] > 0.2) & (pointcloud[0, :] < 3))
    pointcloud = pointcloud[:, vec]

    # Plot the figure
    if ploting:

        fig = plt.figure(frameon=True)
        ax = fig.gca()
        ax.axis('equal')
        ax.scatter(pointcloud[1, :], pointcloud[0, :], s=1)  # Need to swap the coordinates to plot it nicely
        ax.invert_xaxis()  # Invert the y axis (which is now x), to have it the way robot sees it. Sadly there is not nicer way in matplotlib
        ax.scatter([0], [0], c='r')
        plt.show(block=False)

    # 3D pointCloud to 2D pointcloud
    pointcloud = np.delete(pointcloud, obj=2, axis=0)

    return pointcloud




