#CableX/initialSetting/pre_calculation.py

"""
Pre Calculation for the Buoyancy Module and Power Cable Adapted with CableX v1.6.3
Author Name: Yang Zhou @TechnipFMC & Univ of Strathclyde
"""

# Data Pre-processing

import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser
#from fileOperation.input_parser import input_parser

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=f'../../pre_calculation.log',
                    filemode='w')

# From Input.dat
input = input_parser('Input.dat') 
depth = int(input['WtrDpth'])
logging.debug(f"Water Depth is {depth} m") 

# All the Input

# class DataStorage:
#     def __init__(self, input_file)