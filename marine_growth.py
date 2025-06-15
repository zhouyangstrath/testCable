#CableX/initialSetting/marine_growth.py

"""
Functions: Sea Current implementation on quasi-static analysis
Version: v1.6.5
Author: Yang Zhou
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import logging
import OrcFxAPI as orcws

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser # type: ignore
from scripts import globals

cablex_folder = globals.update_globals()[-1]

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=f'../../seacurrent_creation.log',
                    filemode='w')


input = input_parser('Input.dat') 
depth = int(input['WtrDpth'])

# Parameter def
marine_growth = float(input['MarineGrowth'])

if marine_growth == 100:
    # 300mm Cable
    below40_300mm_OD = 0.2709
    below40_300mm_mass = 0.10624
    over40_300mm_OD = 0.3709
    over40_300mm_mass = 0.17303
    # 800mm Cable
    below40_800mm_OD = 0.2942
    below40_800mm_mass = 0.12715
    over40_800mm_OD = 0.3942
    over40_800mm_mass = 0.19879
elif marine_growth == 50:
    # 300mm Cable
    below40_300mm_OD = 0.2209
    below40_300mm_mass = 0.08065
    over40_300mm_OD = 0.2709
    over40_300mm_mass = 0.10624
    # 800mm Cable
    below40_800mm_OD = 0.2442
    below40_800mm_mass = 0.09914
    over40_800mm_OD = 0.2942
    over40_800mm_mass = 0.12715
elif marine_growth == 25:
    # 300mm Cable
    below40_300mm_OD = 0.1959
    below40_300mm_mass = 0.06980
    over40_300mm_OD = 0.2209
    over40_300mm_mass = 0.08065
    # 800mm Cable
    below40_800mm_OD = 0.2192
    below40_800mm_mass = 0.08708
    over40_800mm_OD = 0.2442
    over40_800mm_mass = 0.09914  
elif marine_growth == 0:
    # 300mm Cable
    below40_300mm_OD = 0.1709
    below40_300mm_mass = 0.06026
    over40_300mm_OD = 0.1709
    over40_300mm_mass = 0.06026
    # 800mm Cable
    below40_800mm_OD = 0.1942
    below40_800mm_mass = 0.07632
    over40_800mm_OD = 0.1942
    over40_800mm_mass = 0.07632     
else: 
    print("Marine Growth Selection Error")
    
    
# Define the main functions for distributiing current
def preset_marine_growth(model, savemodel):
    input = input_parser('Input.dat') 
    WaterDepth = int(input['WtrDpth'])
    model = orcws.Model(model)
    
    # 800mm
    line800_below40_name = "800mm_MG_below_40m"
    line800_below40 = model[line800_below40_name]
    line800_below40.OD = below40_800mm_OD
    line800_below40.MassPerUnitLength = below40_800mm_mass
    
    line800_over40_name = "800mm_MG_+2m_to-40m"
    line800_over40 = model[line800_over40_name]
    line800_over40.OD = over40_800mm_OD
    line800_over40.MassPerUnitLength = over40_800mm_mass
    
    # 300mm
    line300_below40_name = "300mm_MG_below_40m"
    line300_below40 = model[line300_below40_name]
    line300_below40.OD = below40_300mm_OD
    line300_below40.MassPerUnitLength = below40_300mm_mass
    
    line300_over40_name = "300mm_MG_+2m_to-40m"
    line300_over40 = model[line300_over40_name]
    line300_over40.OD = over40_300mm_OD
    line300_over40.MassPerUnitLength = over40_300mm_mass
    
    logging.debug(f"Model Saving")    
    model.SaveData(savemodel)

# if __name__ == '__main__':
#     model = "BaseModel.yml"
#     main(model)