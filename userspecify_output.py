#CableX/scripts/userspecify_output.py

"""
Function: Used to Transfer the User Specified output to Input.dat file
Version: CABLEX v1.6.4
Author Name: Yang Zhou
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from postProcessing.userspecify_output import spec_output_read

def main():
    spec_output_read()
    print("***************************************************************************")
    print("            User Specified Output Parameters Imported")
    #print("")
    
if __name__ == "__main__":
    main()