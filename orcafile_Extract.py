#CableX/scripts/orcafileExtract.py

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
    
    print ("---------------------------------------------------------------------------")
    print("Extract File Name for OrcaFlex Running")
    
    cablex_folder = globals.update_globals()[-1]
    
    offsetfolder = ['Nominal', 'Near', 'Far', 'Cross']

    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)
    
    outputfile = f'{cablex_folder}/{loadingspace_folder}/Filelist.lst'
    with open(outputfile, 'w') as txt_file:
        txt_file.write("") 
            
    for folder in offsetfolder:
        folder_path = os.path.join(f'{cablex_folder}/{loadingspace_folder}', folder)
        if os.path.exists(folder_path):
            yaml = orcaflexfiles()
            #yaml_files =  yaml.findYamlFiles(folder_path)
            #yaml.writeYamlFiles(yaml.findYamlFiles(folder_path), folder, outputfile)
            yaml.write_yamlfiles(yaml.find_yamlfiles(folder_path), folder_path, outputfile)
        else:
            #print(f"skip {folder} file Extract: Quasistatic analysis not considered in current Loading Space")  
            filename = 0
    
    print("---------------------------------------------------------------------------")          
                             
if __name__ == "__main__":
    main()