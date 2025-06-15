#CableX/seacurrent/sea_current.py

"""
Functions: Sea Current implementation on quasi-static analysis
Version: v1.6.5
Author: Yang Zhou
"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import logging
import OrcFxAPI as orcws

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser # type: ignore
from scripts import globals

cablex_folder = globals.update_globals()[-1]

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
                    #filename=f'{cablex_folder}/seacurrent_creation.log',
                    #filemode='w')
logging.disable(logging.CRITICAL)

input = input_parser('Input.dat') 
depth = int(input['WtrDpth'])

# Parameter def
surface_tidal_speed = float(input['TidalCurrent']) 
wind_driven_speed_surface = float(input['WindCurrent'])
cutoff_depth = float(input['DevDepth'])
tidal_exponent = 1/7 
#cutoff_depth = 40.0        
#depth = np.linspace(0, 200, 100)  

# Tidal_current function
def tidal_current(depth, surface_speed, exponent):
    return surface_speed * (1 - depth/depth.max())**exponent

# Wind driven current function
def wind_driven_current(depth, surface_speed, cutoff_depth):
    current = np.maximum(surface_speed * (1 - depth/cutoff_depth), 0)
    return current

# Functions for plotting 
def seacurrent_plotting():
    
    # calculate total
    tidal = tidal_current(depth, surface_tidal_speed, tidal_exponent)
    wind = wind_driven_current(depth, wind_driven_speed_surface, cutoff_depth)
    total_current = tidal + wind
    
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(total_current * 100, depth, label='Current Profile (Total)', color='orange') 
    plt.plot(tidal * 100, depth, label='Tidal Current', linestyle='--', color='blue')      
    plt.plot(wind * 100, depth, label='Wind Driven Current', linestyle='--', color='green') 
    plt.gca().invert_yaxis() 
    plt.xlabel('Current Speed [cm/s]')
    plt.ylabel('Depth [m]')
    plt.title('Combined Current Profile')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define the main functions for distributiing current
def preset_current(model, savedmodel):
    input = input_parser('Input.dat') 
    WaterDepth = int(input['WtrDpth'])
    model = orcws.Model(model)
    model.environment.MultipleCurrentDataCanBeDefined = "Yes"
    model.environment.WaterDepth = WaterDepth
    model.environment.NumberOfCurrentDataSets = 13
    
    logging.info(f"start to distribute the name for current profile")
    for currentname in range (0, 13, 1):
        
        
        if currentname == 0:
            logging.debug(f"Distribute the name for current profile for 0(None)")
            model.environment.CurrentName[currentname] = "None" 
            model.environment.ActiveCurrent = model.environment.CurrentName[currentname]
            model.environment.SelectedCurrent = model.environment.CurrentName[currentname]
            model.environment.RefCurrentSpeed = 0
            model.environment.RefCurrentDirection = 180
        else:
            CurProfile = (currentname - 1) * 30
            CurName = f"{CurProfile}deg"
            logging.debug(f"Distribute the name for {CurName} current profiles")
            model.environment.CurrentName[currentname] = CurName 
            model.environment.ActiveCurrent = model.environment.CurrentName[currentname]
            model.environment.SelectedCurrent = model.environment.CurrentName[currentname]
            model.environment.RefCurrentSpeed = 1
            model.environment.RefCurrentDirection = CurProfile

    logging.info(f"Distribute the levels of each profile File")
    for currentindex in range(1, 13, 1):
        
        model.environment.ActiveCurrent = model.environment.CurrentName[currentindex]
        model.environment.SelectedCurrent = model.environment.CurrentName[currentindex]
        model.environment.NumberOfCurrentLevels = 22
        
        for levels in range(0, 20, 1):
            depth = levels * WaterDepth/20
            tidal = surface_tidal_speed * (1 - depth/WaterDepth)**tidal_exponent #tidal_current(depth, surface_tidal_speed, tidal_exponent)
            wind = wind_driven_current(depth, wind_driven_speed_surface, cutoff_depth)
            total_current = tidal + wind
            model.environment.RefCurrentSpeed = 1
            model.environment.CurrentDepth[levels] = depth
            model.environment.CurrentFactor[levels] = total_current
        
        # Distribute the current speed just above the seabed
        model.environment.CurrentDepth[20] = WaterDepth - 0.1 
        model.environment.CurrentFactor[20] = 0.1
        model.environment.CurrentDepth[21] = WaterDepth 
        model.environment.CurrentFactor[21] = 0
        model.environment.CurrentFactor[levels] = total_current
        
    logging.debug(f"Model Saving")    
    model.SaveData(savedmodel)

# if __name__ == '__main__':
#     model = "BaseModel.yml"
#     main(model)