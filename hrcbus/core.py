#!/usr/bin/env python

'''
busmonitor.py: Create trending plots for the Chandra/HRC Primary bus
using data from the Ska engineering telemetry archive.
'''

__author__ = "Dr. Grant R. Tremblay"

import sys
import os

import time

import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import spline


def check_environment():
    '''Ensure that the Ska environment variable is set.'''

    if "SKA" in os.environ:
        testfile = str(os.environ["SKA"]) + "/bin/flt_envs"
        if os.path.isfile(testfile):
            print("Now connected to the Ska telemetry archive.")
        else:
            print("The $SKA environment variable is set to", os.environ["SKA"])
            print("... but no data can be found there. Please check this.")
            sys.exit()
    else:
        print("The $SKA environment variable is not set! Please try again.")
        sys.exit()


def fetch_msids():
    '''Fetch the MSIDs from the Ska Archive'''

def main():
    '''Make the plots.'''

    check_environment()


if __name__ == '__main__':
    start_time = time.time()
    main()
    runtime = round((time.time() - start_time), 3)
    #print("Finished in    |  {} seconds".format(runtime))

    #print("Showing plots  |")

    #plt.show()
