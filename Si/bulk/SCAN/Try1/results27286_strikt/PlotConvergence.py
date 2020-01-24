#!/bin/python

# Input:
# - The current directory contains directories with names key1_key2.
#   Those are enlisted in stdin (ls -1 | script).
# - Names of parameters to plot as arguments
# Output:
# - A plot containing a 2D convergence plot for each parameter

import sys
import matplotlib.pyplot as plt
import subprocess

# def add_tab(parameter, tab, X, Y):
#     tab.plot_surface(x, y, z)

def get_bash_output(bash_command):
    subbprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(stderr, error)
    return output

def get_key_ranges():
    X = []; Y = []
    #Z = [][]
    for line in sys.stdin:
        if line.count("_") == 1:
            x, y = line.split("_")
            X.append(x)
            Y.append(y)
        #Z[x, y] = get_param(param, line + "/opt.out")
    return X, Y

def get_param_val(param, X, Y):
    for x in X, y in Y:
        Z = []
        file = str(x) + "_" + str(y) + "/opt.out"
        bash_command = "grep \'" + param + " \'" + file + " | rev | cut -d\' \' -f1 | rev)"
        #subbprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        #output, error = proccess.communicate()
        Z[x, y] = get_bash_output(bash_command)
        #Z[x,y] = sys.command(grep param + " " file | rev | cut -d' ' -f1 | rev)
    return Z

if __name__ == "__main__":
    # parse parameter info
    nbr_param = len(sys.argv) - 1
    param = sys.argv[1:]

    # X and Y are common for all subplots
    X, Y = get_key_ranges()
    # initialize subplot
    fig, axs = plt.subplots(1, nbr_param) 
    for ii in range(nbr_param):
        Z = get_param_val(param[ii], X, Y)
        axs[0,ii].plot_surface(X, Y, Z)
        # add_tab(param[ii], axs[0,ii], X, Y)
    #plot
    plt.show()
