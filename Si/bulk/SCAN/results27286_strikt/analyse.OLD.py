#!/usr/bin/python

# Input:
# - The current directory contains directories with names key1_key2.
#   Those are enlisted in stdin (ls -1 | script).
# - Names of parameters to plot as arguments
# Output:
# - A plot containing a 2D convergence plot for each parameter

# use example: ls -1 | ./analyze.py acell

import sys
import matplotlib.pyplot as plt
import subprocess
import numpy as np
import re
from mpl_toolkits.mplot3d import axes3d, Axes3D

def get_number(param):
    return float(re.sub("[^0-9E+-.]", "", param))

def get_param_val(param, file):
    command = "grep -o '" + param + "  *[^ ]*' '" + file + "' | tail -n1"
    output = subprocess.check_output(command, shell=True).decode()
    return get_number(output)

if __name__ == "__main__":
    # parse parameter info
    nbr_param = len(sys.argv) - 1
    params = sys.argv[1:]

    # initialize and fill X, Y and Z arrays
    X = []; Y = []; Z = []
    for line in sys.stdin:
        if line.count("_") == 1:
            # parse directory, x and y
            directory = line.rstrip()
            x_in, y_in = directory.split("_")
            x = get_number(x_in); y = get_number(y_in)
            # extract corresponding z (actual parameter value)
            z = get_param_val(params[0], directory + "/opt.out")
            X.append(x); Y.append(y); Z.append(z)
    
    print(X, Y, Z)
    
    X = np.array(X);  Y = np.array(Y);  Z = np.array(Z)

    # initialize subplot
    fig = plt.figure()
    # for ii in range(nbr_param):
    # ax = fig.add_subplot(111, projection='3d')
    ax = Axes3D(fig)

    # ax.set_zlim3d(np.min(Z), np.max(Z))

    ax.scatter(X, Y, Z)
    
    # show plot
    plt.show()
