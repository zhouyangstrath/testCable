#CableX/initialSettings/pre_postprocessing.py

"""
Functions: Used to modify the post-processing scripts in orcaflex running with user specified range 
Version: v1.6.5
Author: Yang Zhou
"""

import pandas as pd
import re
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser
from scripts import globals


def postprocess_define(cable_layout, buoy_layout):
    
    # Input data used to determine the postprocessing files
    input = input_parser(f'../scripts/Input.dat') 
    #cable_layout = int(input['CableLayout'])
    #buoy_layout = int(input['MixedBuoy'])
    
    # cable and buoyancy layout to determine postprocessing scripts
    cablex_mapping = {
        "1_1": (f'../postProcessing/PostProcessLazywaveStatic_org.py', 204, 205),
        "1_2": (f'../postProcessing/PostProcessLazywaveStatic_MixedBuoy_org.py', 208, 209), 
        "2_1": (f'../postProcessing/PostProcessRCDCStatic_org.py', 273, 274),
        "2_2": (f'../postProcessing/PostProcessRCDCStatic_MixedBuoy_org.py', 277, 278),
        "3_1": (f'../postProcessing/PostProcessRCDCStatic_org.py', 273, 274),
        "3_2": (f'../postProcessing/PostProcessRCDCStatic_MixedBuoy_org.py', 277, 278),
        "4_1": (f'../postProcessing/PostProcessFullLazywaveStatic_org.py', 222, 223),
        "4_2": (f'../postProcessing/PostProcessFullLazywaveStatic_MixedBuoy_org.py', 221, 222),
        }
    
    # Define the target files
    target_file_path, spec_min_line, spec_max_line = cablex_mapping.get(f"{cable_layout}_{buoy_layout}")
    target_file_path_out = target_file_path.replace("_org", "") if target_file_path else None
    
    #print(target_file_path)
    #print(target_file_path_out)
    
    return(target_file_path, target_file_path_out, spec_min_line, spec_max_line)
    

def postprocess_filesupdate(target_file_path, target_file_path_out,  spec_min_line, spec_max_line, specified_min, specified_max):
    # Create file is not exists
    if not os.path.exists(target_file_path_out):
        with open(target_file_path_out, "w", encoding="utf-8") as file:
            file.write("")
            
    with open(target_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    # print(spec_min_line, spec_max_line)
    # print(target_file_path, target_file_path_out)
    lines[spec_min_line] = lines[spec_min_line].replace("specifiedrange_min = Total_L - 2", f"specifiedrange_min = Total_L - {specified_min}")
    lines[spec_max_line] = lines[spec_max_line].replace("specifiedrange_max = Total_L - 0", f"specifiedrange_max = Total_L - {specified_max}")
    
    with open(target_file_path_out, "w", encoding="utf-8") as file:
        file.writelines(lines) 
    
def postprocess_update():

    #print(specified_min, specified_max)
    input = input_parser(f'../scripts/Input.dat') 
    specified_min = float(input['SpecifiedArcMin'])
    specified_max = float(input['SpecifiedArcMax'])
    cable_layout = int(input['CableLayout'])
    buoy_layout = int(input['MixedBuoy'])

    target_file_path, target_file_path_out,  spec_min_line, spec_max_line = postprocess_define(cable_layout, buoy_layout)  

    # target_file_path = f'../postProcessing/PostProcessLazywaveStatic_org.py'
    # target_file_path_out = f'../postProcessing/PostProcessLazywaveStatic.py'
    
    if cable_layout == 1 or cable_layout == 4:
        postprocess_filesupdate(target_file_path, target_file_path_out,  spec_min_line, spec_max_line, specified_min, specified_max)
    elif buoy_layout == 2:
        postprocess_filesupdate(target_file_path, target_file_path_out,  spec_min_line, spec_max_line, specified_min, specified_max)
        target_file_path2, target_file_path_out2,  spec_min_line2, spec_max_line2 = postprocess_define(1, 2)
        postprocess_filesupdate(target_file_path2, target_file_path_out2,  spec_min_line2, spec_max_line2, specified_min, specified_max)
    else:
        postprocess_filesupdate(target_file_path, target_file_path_out,  spec_min_line, spec_max_line, specified_min, specified_max)
        target_file_path2, target_file_path_out2,  spec_min_line2, spec_max_line2 = postprocess_define(1, 1)
        postprocess_filesupdate(target_file_path2, target_file_path_out2,  spec_min_line2, spec_max_line2, specified_min, specified_max)
    
postprocess_update()
# if __name__ == "__main__":
#     main()
