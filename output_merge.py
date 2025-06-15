#CableX/fileOperation/output_merge.py

"""
Function: Used to merge the output data files from the cablex workflows
Version: CABLEX v1.6.5
Author Name: Yang Zhou
"""

import os
import pandas as pd
import re
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.output_merge import output_merge

def main():
    print("""
===========================================================================
         CABLEX Loading Space Results summarised in cablex_sum.xlsx  
===========================================================================
        """)
    output_merge()

if __name__ == "__main__":
    main()


