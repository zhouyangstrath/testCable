#CableX/scripts/sea_current.py

"""
Function: Use for the sea current generation 
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from initialSetting.marine_growth import preset_marine_growth

def main():
    
    lw_model = f"../basemodel/LW_Basemodel.yml"
    full_lw_model = f"../basemodel/Full_LW_Basemodel.yml"
    rcdc_model = f"../basemodel/RCDC_Basemodel.yml"
    preset_marine_growth(lw_model, lw_model)
    preset_marine_growth(full_lw_model, full_lw_model)
    preset_marine_growth(rcdc_model, rcdc_model)

if __name__ == "__main__":
    main()