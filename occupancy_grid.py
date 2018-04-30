import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches



## Size of field 4x4m
_resolution = 0.1
_height = 4
_width = 4
_map = []
_initialized = False

def init_map():
    num_of_blocks_x = int(round(_width / _resolution))
    num_of_blocks_y = int(round(_height / _resolution))

    _map = np.zeros((num_of_blocks_y, num_of_blocks_x))
    _map[:, :] = -1
    print("Map initialized with height: " + str(num_of_blocks_y) + " width : " + str(num_of_blocks_x) + "and resolution of " + str(_resolution) + "meters")
    initialized = True


def update_map(pointcloud, coordinates, rotation):
    if not _initialized:
        print("Map has not been initialized yet")
        return

    # Line ploter with Bresenhasamelejshe(you know which one) algorithm from wiki
    # OMG PINDOUR A ZUZKA ARE FIGHTING AGAIN - I GONNA KILL MASELF



def get_map():
    if not _initialized:
        print("Map has not been initialized yet")
        return

    return _map


