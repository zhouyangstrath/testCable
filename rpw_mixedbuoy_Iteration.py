#CableX/scripts/rpwIteration.py

"""
Function: For RCDC loadingSpace Iterations
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import datetime
from time import process_time
import sys
import os
import json

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cableIteration.rpw_cable_mixedbuoy import rpw_cable_mixedbuoy
import globals

def main():
    print ("Base model Iterating:")
    
    cablex_folder = globals.update_globals()[-1]
    
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)
        
    if loadingspace_folder == 'LS4':
        LoadingSpace = 4
    elif loadingspace_folder == 'LS5':
        LoadingSpace = 5
    else:
        print('Error in LoadingSpace Selection')
        
    now = datetime.datetime.now()
    print('Initiating batch for analyses')
    print("Time : ", now)
    to = process_time()

    rpwcable = rpw_cable_mixedbuoy('../basemodel/RCDC_Basemodel.yml', 'LW_SOL', 'LW_EOL', 'RPW_SOL', 'RPW_EOL', 'Tether_SOL_1', 'Tether_SOL_2', 'Tether_EOL_1', 'Tether_EOL_2', 
                                    'Clamp_SOL', 'Clamp_EOL', '1000kg_SOL', '1000kg_EOL', 'Clamp ref')
    rpwcable.generate_models(LoadingSpace)
    rpwcable.print_results()

    now = datetime.datetime.now()
    print("Time : ", now)
    tf = process_time()
    print("Elapsed time :", tf, to)
    print("Total elapsed time:", tf - to, '[s]')

if __name__ == "__main__":
    main()