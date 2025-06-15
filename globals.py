#CableX/fileOperations/globals.py

"""
Function: Settings for Global parameters Global folder settings 
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileOperation.input_parser import input_parser

# Global parameters settings
def update_globals():
    input = input_parser('Input.dat')
    # Specify the Cable and Buoy Type in the Input.dat file
    layout = int(input['CableLayout'])
    mixedbuoy = int(input['MixedBuoy'])
    cable = int(input['CableType'])
    buoy = int(input['BuoyType'])
    WD = int(input['WtrDpth'])
    offset = int(input['Offset'])
    #print("offset is ", offset)
    cablexCode = f'..'
    cablemapping = {
        1: "PinLW" ,
        2: "RCDC" ,
        3: "RPW" ,
        4: "FullLW"
    }
    buoymapping = {
        1: "Single",
        2: "Dual"
    }
    cablenaming = cablemapping.get(layout)
    buoynaming = buoymapping.get(mixedbuoy)
    #print (cablenaming)
    cablexFolder = f'../../{cablenaming}{buoynaming}{WD}Wtrdpth{offset}Offset{cable}Cable{buoy}Buoy' 
    #print(cablexFolder)
    return cable, buoy, WD, cablexFolder
