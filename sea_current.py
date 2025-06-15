#CableX/scripts/sea_current.py

"""
Function: Use for the sea current generation 
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from initialSetting.sea_current import preset_current 
from fileOperation.input_parser import input_parser
import globals

def main():
    
    input = input_parser('Input.dat')
    CableLayout = int(input['CableLayout'])
    #MixedBuoy = int(input['MixedBuoy'])
    
    cable_mapping = {
        1: (f"../basemodel/LW_Basemodel_org.yml"),
        2: (f"../basemodel/RCDC_Basemodel_org.yml"),
        3: (f"../basemodel/RCDC_Basemodel_org.yml"),
        4: (f"../basemodel/Full_LW_Basemodel_org.yml")
    }
    
    org_model = cable_mapping.get(CableLayout) 
    #print(org_model)
    rev_model = org_model.replace("_org", "") if org_model else None
    preset_current(org_model, rev_model)
        
    lw_model = f"../basemodel/LW_Basemodel_org.yml"
    lw_rev_model = f"../basemodel/LW_Basemodel.yml"
    preset_current(lw_model, lw_rev_model)
    
    # lw_smeared_model = f"../basemodel/LW_Smeared_Basemodel_org.yml"
    # lw_smeared_rev_model = f"../basemodel/LW_Smeared_Basemodel.yml"
    # rcdc_smeared_model = f"../basemodel/RCDC_Smeared_Basemodel_org.yml"
    # rcdc_smeared_rev_model = f"../basemodel/RCDC_Smeared_Basemodel.yml"
    
    print("***************************************************************************")
    print ("                User Defined Current Profile Settled")
    #print(     rev_model, "model Updated")

if __name__ == "__main__":
    main()