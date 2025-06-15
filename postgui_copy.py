#CableX/scripts/postGuiCopy.py

"""
Function: Used in Extracting Postprocessing LS files to GUI folder
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import sys
import os

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileOperation.gui_copy import copy_gui_files
import globals

def main():
        
    print ("##############Post GUI source file preparing#############")
    print ("PostProcessing to setup GUI working directory")
    
    cablex_folder = globals.update_globals()[-1]
    
    # Define the source and destination directories
    source_directory = f'{cablex_folder}'
    destination_directory = f'{cablex_folder}/PostUI/Data'

    # Call the function to copy the files
    copy_gui_files(source_directory, destination_directory)

if __name__ == "__main__":
    main()