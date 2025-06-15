#CableX/scripts/postprocess_update.py

"""
Function: Use for updating the postprocess scripts for the cablex 
Version: CABLEX v1.6.4
Author Name: Yang Zhou
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from initialSetting.pre_postprocessing import postprocess_define, postprocess_update

def main():
    print("***************************************************************************")
    print(" Orcaflex PostProcessing Scripts Updated based on User Specified Complete! ")
    #print("***************************************************************************")
    #print("")
    postprocess_update()

if __name__ == "__main__":
    main()