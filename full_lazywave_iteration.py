#CableX/scripts/lazywaveIteration.py

"""
Function: For Full lazywave loadingSpace Iterations
Version: CABLEX v1.6.5
Author Name: Yang Zhou
"""

import datetime
from time import process_time
import sys
import os
import json


# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cableIteration.fulllazywave_cable import full_lazywave_cable
import globals

def main():
    
    print ("Base model Iterating:")
    
    cablex_folder = globals.update_globals()[-1]
    
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)
        
    if loadingspace_folder == 'LS1':
        LoadingSpace = 1
    elif loadingspace_folder == 'LS2':
        LoadingSpace = 2
    else:
        LoadingSpace = 3
    
    now = datetime.datetime.now()
    print('Initiating batch for analyses')
    print("Case Iteration for Loading Space", LoadingSpace) 
    print("Time : ", now)
    to = process_time()

    lazywavecable = full_lazywave_cable('../basemodel/Full_LW_BaseModel.yml', 'LW_SOL','LW_EOL', 'Clamp ref', '1000kg_SOL')
    lazywavecable.generate_models(LoadingSpace)
    lazywavecable.print_results()

    now = datetime.datetime.now()
    print("Time : ", now)
    tf = process_time()
    print("Elapsed time :", tf, to)
    print("Total elapsed time:", tf - to, '[s]')

if __name__ == "__main__":
    main()