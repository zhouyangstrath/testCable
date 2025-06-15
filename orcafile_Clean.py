#CableX/scripts/orcafileClean.py

"""
Function: Folder Cleaness for all sim files after simulation  
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import os
import sys

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileOperation.folder_clean import folder_clean

def main():
    
    # Clean all the Nominal/Near/Far/Cross/* folders sim files
    folder_clean()

if __name__ == "__main__":
    main()