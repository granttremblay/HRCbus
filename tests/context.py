#/usr/bin/env python

'''
Make sure my tests can see my module. 
'''

import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import hrcbus
