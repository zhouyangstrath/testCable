#CableX/scripts/rcdcDyIteration.py

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

from cableIteration.rcdc_cable_dynamic import rcdc_cable_dynamic
import globals

def main():
    
    print ("Base model Iterating for Dynamics:")
          
    now = datetime.datetime.now()
    print('Initiating batch for analyses')
    print("Time : ", now)
    to = process_time()

    generator = rcdc_cable_dynamic('../basemodel/DynamicPre/TetraSub_constraint.dat', 'LW_SOL', 'LW_EOL', 'RPW_SOL', 'RPW_EOL', 'Tether_SOL_1', 'Tether_SOL_2', 'Tether_EOL_1', 'Tether_EOL_2', 
                                    'Clamp_SOL', 'Clamp_EOL', '1000kg_SOL', '1000kg_EOL', 'Clamp ref')
    generator.generate_models()
    generator.print_results()

    now = datetime.datetime.now()
    print("Time : ", now)
    tf = process_time()
    print("Elapsed time :", tf, to)
    print("Total elapsed time:", tf - to, '[s]')
    
    print ("--------------------------------------------------------------------------")


if __name__ == "__main__":
    main()