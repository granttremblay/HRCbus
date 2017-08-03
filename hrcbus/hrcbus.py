#!/usr/bin/env python

'''
busmonitor.py: Create trending plots for the Chandra/HRC Primary bus
using data from the Ska engineering telemetry archive.
'''

__author__ = "Dr. Grant R. Tremblay"

import time

import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import spline



def check_environment():
    '''Ensure that the Ska environment variable is set.'''




if __name__ == '__main__':
    start_time = time.time()
    main()
    runtime = round((time.time() - start_time), 3)
    print("Finished in    |  {} seconds".format(runtime))

    print("Showing plots  |")

    plt.show()
