#CableX/initialSetting/pre_calculation.py

"""
Pre Calculation for the Buoyancy Module and Power Cable Adapted with CableX v1.6.3
Author Name: Yang Zhou @TechnipFMC & Univ of Strathclyde
"""

# Data Pre-processing

import os
import sys
import logging
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=f'../../seacurrent_creation.log',
                    filemode='w')


# From Input.dat
input = input_parser('../scripts/Input.dat') 
depth = int(input['WtrDpth'])
CableType = int(input['CableType'])
BuoyCC = float(input['BuoyCC'])

# Read the initials
MarineGrowth = int(input['MarineGrowth'])

OD800CuCable = float(input['OD800CuCable'])
Mai800CuCable = float(input['Mai800CuCable'])
Mwa800CuCable = float(input['Mwa800CuCable'])

OD300CuCable = float(input['OD300CuCable'])
Mai300CuCable = float(input['Mai300CuCable'])
Mwa300CuCable = float(input['Mwa300CuCable'])

MassBuoy = float(input['MassBuoy']) 
NetBuoy = float(input['NetBuoy']) 
WtrDens = float(input['WtrDens'])
LenBuoy = float(input['LenBuoy'])
ODBuoy = float(input['ODBuoy'])
MBRCable = float(input['MBRCable'])
ClearBuoy = float(input['ClearBuoy'])

# OD & Mass for 800 Cable in Orcaflex Calculation
# SOL
OD800CuCable_calc = OD800CuCable
Mai800CuCable_calc = Mwa800CuCable/9.81 + np.pi/4 * np.square(OD800CuCable/1000) * 1025

#EOL
# OD & Mass for 800 Cable in Orcaflex Calculation +2 to -40m
OD800CuCable_mg40_calc = OD800CuCable + MarineGrowth/100 * 100 * 2
Mai800CuCable_mg40_calc = Mai800CuCable_calc + np.pi/4 * (np.square(OD800CuCable_mg40_calc) - np.square(OD800CuCable_calc)) * 1325 /1000000
# OD & Mass for 800 Cable in Orcaflex Calculation -40m to seabed
OD800CuCable_mgsb_calc = OD800CuCable + MarineGrowth/100 * 50 * 2
Mai800CuCable_mgsb_calc = Mai800CuCable_calc + np.pi/4 * (np.square(OD800CuCable_mgsb_calc) - np.square(OD800CuCable_calc)) * 1325 /1000000
#format = "{:.5f}".format(Mai800CuCable_calc) # data formating

# OD & Mass for 300 Cable in Orcaflex Calculation
# SOL
OD300CuCable_calc = OD300CuCable
Mai300CuCable_calc = Mwa300CuCable/9.81 + np.pi/4 * np.square(OD300CuCable/1000) * 1025

# EOL
# OD & Mass for 300 Cable in Orcaflex Calculation +2 to -40m
OD300CuCable_mg40_calc = OD300CuCable + MarineGrowth/100 * 100 * 2
Mai300CuCable_mg40_calc = Mai300CuCable_calc + np.pi/4 * (np.square(OD300CuCable_mg40_calc) - np.square(OD300CuCable_calc)) * 1325 /1000000
# OD & Mass for 300 Cable in Orcaflex Calculation -40m to seabed
OD300CuCable_mgsb_calc = OD300CuCable + MarineGrowth/100 * 50 * 2
Mai300CuCable_mgsb_calc = Mai300CuCable_calc + np.pi/4 * (np.square(OD300CuCable_mgsb_calc) - np.square(OD300CuCable_calc)) * 1325 /1000000


# SOL 
if CableType == 800:
    MassLinear = Mai800CuCable_calc # Linear mass, hoses/tubes water filled in air
    ODCuCable_calc = OD800CuCable
elif CableType == 300:
    MassLinear = Mai300CuCable_calc
    ODCuCable_calc = OD300CuCable
    
MBRCable_calc = MBRCable # MBR power cable (OP)
AngleElCC = np.arctan((LenBuoy/2)/(MBRCable_calc - (ODBuoy/2/1000))) * 180/np.pi  # Angle element centre to corner
MinCC = 2 * np.pi * MBRCable_calc * (2 * AngleElCC)/360 + 0.05 # Centre to centre min
MinFF = 0.26 * ODBuoy/1000 # Minimum clearance suggested (face to face)
MaxFF = 3.36 * ODBuoy/1000 # Maxmum clearance suggested (face to face)
VolBuoy = (MassBuoy + NetBuoy)/WtrDens # Buoy volume (1 module)
MassAverBuoy = MassBuoy/VolBuoy # Buoy (including foam, clamp, ...) (average) specific mass
MassCableEqv = (MassLinear * BuoyCC + MassBuoy)/BuoyCC # Equivalent mass per unit length (water filled in air)
BuoyTotal = (np.pi/4 * BuoyCC * np.square(ODCuCable_calc/1000) + VolBuoy) * WtrDens # Total buoyancy (not net, 1 pitch)
BuoyLinear = BuoyTotal/BuoyCC # Total linear buoyancy (not net)
ODCableEqv = 1000 * np.sqrt(4 * BuoyLinear/(np.pi * WtrDens)) # Equivalent diameter 


##########logging####################
logging.debug(f"Water Depth = {depth} m") 
logging.debug(f"OD800CuCable = {OD800CuCable} kg/m") 
logging.debug(f"800mm Cable Mass in Air = {Mai800CuCable_calc} kg/m") 
logging.debug(f"OD800CuCable_calc_mg40 = {OD800CuCable_mg40_calc} mm") 
logging.debug(f"Mai800CuCable_mg40_calc = {Mai800CuCable_mg40_calc} mm") 
logging.debug(f"OD800CuCable_calc_mgsb = {OD800CuCable_mgsb_calc} mm") 
logging.debug(f"Mai800CuCable_mgsb_calc = {Mai800CuCable_mgsb_calc} mm") 

logging.debug(f"OD300CuCable = {OD300CuCable} kg/m") 
logging.debug(f"300mm Cable Mass in Air = {Mai300CuCable_calc} kg/m") 
logging.debug(f"OD300CuCable_calc_mg40 = {OD300CuCable_mg40_calc} mm") 
logging.debug(f"Mai300CuCable_mg40_calc = {Mai300CuCable_mg40_calc} mm") 
logging.debug(f"OD300CuCable_calc_mgsb = {OD300CuCable_mgsb_calc} mm") 
logging.debug(f"Mai300CuCable_mgsb_calc = {Mai300CuCable_mgsb_calc} mm") 
logging.debug(f"Angle element centre to corner = {AngleElCC} mm") 
logging.debug(f"Minimum Center to Center Distance = {MinCC} mm") 
logging.debug(f"Minimum Face to Face Distance = {MinFF} mm") 
logging.debug(f"Volume of the Buoyancy = {VolBuoy} m3") 
logging.debug(f"Equivalent mass per unit length (water filled in air) = {MassCableEqv} kg/m") 
logging.debug(f"Total buoyancy (not net, 1 pitch) = {BuoyTotal} kg") 
logging.debug(f"Linear Buoyancy = {BuoyLinear} kg/m") 
logging.debug(f"Equivalent Cable Diameter = {ODCableEqv} kg/m") 
# All the Input

# class DataStorage:
#     def __init__(self, input_file)