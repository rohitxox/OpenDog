#!/usr/bin/env python3
'''Animates distances and measurment quality'''
from rplidar import RPLidar
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

PORT_NAME = 'COM5'
DMAX = 2500
IMIN = 0
IMAX = 50
#buffer = 500

def update_line(num, iterator, line):
    scan = next(iterator)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in scan])
    line.set_array(intens)
    return line,

def run():
    lidar = RPLidar(PORT_NAME)
    fig = plt.figure('MechaDog 2D scanning')
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=8, c=[IMIN, IMAX],
                           cmap=plt.cm.Reds_r, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)

    iterator = lidar.iter_scans() #buffer
    ani = animation.FuncAnimation(fig, update_line,fargs=(iterator, line), interval=50)
    plt.show()
    lidar.stop()
    lidar.disconnect()



run()
# if __name__ == '__main__':
#