#CableX/scripts/directSetup.py

"""
Function: PreProcess Directory Setup for following CABLEX workflows
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import os
import shutil
import sys
#
# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fileOperation.folder_copy import Folder
from fileOperation.input_parser import input_parser
import globals

def main():
    
    cablex_folder = globals.update_globals()[-1]
    input = input_parser('Input.dat')
    CableLayout = int(input['CableLayout'])
    MixedBuoy = int(input['MixedBuoy'])
    
    if not os.path.exists(cablex_folder):
        os.makedirs(cablex_folder)     

    if CableLayout == 4 or CableLayout == 1:
        LoadingSpaces = ['LS1', 'LS2', 'LS3', 'LS_Dy',  "PostUI"]
    else:
        LoadingSpaces = ['LS1', 'LS2', 'LS3', 'LS4', 'LS5', 'LS_Dy', "PostUI"]
    
    for space in LoadingSpaces:
        condition_folder = f'{cablex_folder}/{space}'
        if not os.path.exists(condition_folder):
            os.makedirs(condition_folder)
    #print(space)
    for space in LoadingSpaces:
        if space in ['LS1', 'LS2', 'LS3']:
            if CableLayout == 4 and MixedBuoy == 1:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/Full_LW_Basemodel.yml', '../postProcessing/PostProcessFullLazywaveStatic.py']
            elif CableLayout == 4 and MixedBuoy == 2:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/Full_LW_Basemodel.yml', '../postProcessing/PostProcessFullLazywaveStatic_MixedBuoy.py']
            elif MixedBuoy == 1:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/LW_Basemodel.yml', '../postProcessing/PostProcessLazywaveStatic.py']
            elif MixedBuoy == 2:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/LW_Basemodel.yml', '../postProcessing/PostProcessLazywaveStatic_MixedBuoy.py']
            else:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/LW_Smeared_Basemodel.yml', '../postProcessing/PostProcessLazywaveStatic.py']
              
        elif space in ['LS4', 'LS5']:
            if MixedBuoy == 1:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/RCDC_Basemodel.yml', '../postProcessing/PostProcessRCDCStatic.py']
            elif MixedBuoy == 2:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/RCDC_Basemodel.yml', '../postProcessing/PostProcessRCDCStatic_MixedBuoy.py']
            else:
                postprocess_filename = ['../scripts/Input.dat', '../basemodel/RCDC_Smeared_Basemodel.yml', '../postProcessing/PostProcessRCDCStatic.py']   
        
        elif space in ['LS_Dy']: 
            postprocess_filename = ['Input.dat'] 
            folderdynamic = '../basemodel/DynamicPre'
            Folder.copyFolder(folderdynamic, f'{cablex_folder}/{space}')
            continue
        else:
            postprocess_filename = ['Input.dat']
            folderbmp = '../basemodel/postGui'   
            Folder.copyFolder(folderbmp, f'{cablex_folder}/{space}')   
            continue
        
        for file in postprocess_filename:
            shutil.copy(file,f'{cablex_folder}/{space}')
    print("***************************************************************************")
    print ("               PreProcessing to setup working directory")
    print("Work file path:", cablex_folder, "Created" )
    print("***************************************************************************")
    print("")
                
if __name__ == "__main__":
    main()
        