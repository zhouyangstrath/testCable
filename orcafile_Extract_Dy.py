#CableX/scripts/orcafileExtractDy.py

"""
Function: Used in each loading space for orcaflex files extraction
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import sys
import os

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileOperation.orcaflex_files import orcaflexfiles
import globals
import json

def main():
    
    print("Extract File Name for OrcaFlex Running")
    
    cablex_folder = globals.update_globals()[-1]
    
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        LoadingSpace = json.load(f)
    
    directrory_path = os.path.join(cablex_folder, 'LS_Dy')
    # List all the files
    lay_folders = [folder for folder in os.listdir(directrory_path) if os.path.isdir(os.path.join(directrory_path, folder)) and folder.startswith('Lay')]

    outputfile = f'{cablex_folder}/Ls_Dy/Filelist.lst'
    with open(outputfile, 'w') as txt_file:
        txt_file.write("") 
        
    for folder in lay_folders:
        datafile = 'Data'
        angles = ['0deg', '15deg', '-15deg' ]
        for angle in angles:
            folder_path = os.path.join(f'{cablex_folder}/LS_Dy/{folder}/{angle}', datafile)
            #print(folder_path)
            if os.path.exists(folder_path):
                yaml = orcaflexfiles()
                path = f'{folder}/{angle}/Data'
                yaml.write_yamlfiles(yaml.find_yamlfiles(folder_path), path, outputfile)
            else:
                print("No yaml files founded")            
                             
if __name__ == "__main__":
    main()