#CableX/scripts/orcafileExtract.py

"""
Function: Used in each loading space for orcaflex files extraction
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import sys
import os
import json

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from postProcessing.datasum_static import datasum_static
from fileOperation.input_parser import input_parser 
import globals


def main():
    
    input = input_parser('Input.dat')
    CableLayout = int(input['CableLayout'])
    MixedBuoy = int((input['MixedBuoy']))
    
    dataSum = datasum_static()
    marinegrowth = ['EOL', 'SOL']
    
    cablex_folder = globals.update_globals()[-1]
    
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        LoadingSpace = json.load(f)

    # LazyWave Loading Spaces
    if LoadingSpace == 'LS1':
        conditions = ['Nominal']
        for condition in conditions:
            for esol in marinegrowth:
                if CableLayout == 4 and MixedBuoy == 1:
                    dataSum.datasum_full_lazywave(condition, esol, LoadingSpace)
                elif CableLayout == 4 and MixedBuoy == 2:
                    dataSum.datasum_full_lazywave_mixedbuoy(condition, esol, LoadingSpace)
                elif MixedBuoy == 1:
                    dataSum.datasum_lazywave(condition, esol, LoadingSpace)
                else:
                    dataSum.datasum_lazywave_mixedbuoy(condition, esol, LoadingSpace)
    elif LoadingSpace in ['LS2', 'LS3']:
        conditions = ['Nominal', 'Near', 'Far', 'Cross']
        for condition in conditions:
            for esol in marinegrowth:
                if CableLayout == 4:
                    dataSum.datasum_full_lazywave(condition, esol, LoadingSpace)
                elif MixedBuoy == 1:
                    dataSum.datasum_lazywave(condition, esol, LoadingSpace)
                else:
                    dataSum.datasum_lazywave_mixedbuoy(condition, esol, LoadingSpace)
    # RCDC Loading Spaces
    elif LoadingSpace == 'LS4':
        conditions = ['Nominal']
        for condition in conditions:
            for esol in marinegrowth:
                if MixedBuoy == 1:
                    dataSum.datasum_rcdc(condition, esol, LoadingSpace)
                else: 
                    dataSum.datasum_rcdc_mixedbuoy(condition, esol, LoadingSpace)
    elif LoadingSpace == 'LS5':
        conditions = ['Nominal', 'Near', 'Far', 'Cross']
        for condition in conditions:
            for esol in marinegrowth:
                if MixedBuoy == 1:
                    dataSum.datasum_rcdc(condition, esol, LoadingSpace)
                else: 
                    dataSum.datasum_rcdc_mixedbuoy(condition, esol, LoadingSpace)
    else:
        print('Error on outputData')
    
if __name__ == "__main__":
    main()