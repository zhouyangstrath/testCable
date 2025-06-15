# CableX/CodeSource/passCheckStatic.py

'''
Functions: Pass Case Filter based on the Summarised post-processing data files
Version: CABLEX v1.6.0
Author Name: Yang Zhou
'''

import time
import numpy as np
import sys
import os
import json
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from postProcessing.passCheck import cablex_data
from fileOperation import input_parser
import globals


def main():
    
    input = input_parser('Input.dat') 
    CableLayout = int(input['CableLayout'])
    MixedBuoy = int(input['MixedBuoy'])
    
    print("Pass Configuration Filtering:")

    cablexfile = cablex_data()
    
    cablex_folder = globals.update_globals()[-1]
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)

    if  loadingspace_folder == 'LS1':
        data_ls_solution = 1
    elif loadingspace_folder == 'LS2':
        data_ls_solution = 2
    elif loadingspace_folder == 'LS3':
        data_ls_solution = 3
    elif loadingspace_folder == 'LS4':
        data_ls_solution = 4
    elif loadingspace_folder == 'LS5':
        data_ls_solution = 5
    else: 
        print('error in loading space selection')
        
    ##################################USER DEFINED PASS CASE IN CABLEX####################################
    
    if data_ls_solution == 1:
        data_files = [f"{cablex_folder}/{loadingspace_folder}/Nominal_SOL_LS1.txt", f"{cablex_folder}/{loadingspace_folder}/Nominal_EOL_LS1.txt"]
    elif data_ls_solution == 2:
        data_files = [f"{cablex_folder}/{loadingspace_folder}/Nominal_SOL_LS2.txt", f"{cablex_folder}/{loadingspace_folder}/Nominal_EOL_LS2.txt",
                    f"{cablex_folder}/{loadingspace_folder}/Cross_SOL_LS2.txt", f"{cablex_folder}/{loadingspace_folder}/Cross_EOL_LS2.txt", 
                    f"{cablex_folder}/{loadingspace_folder}/Near_SOL_LS2.txt", f"{cablex_folder}/{loadingspace_folder}/Near_EOL_LS2.txt",
                    f"{cablex_folder}/{loadingspace_folder}/Far_SOL_LS2.txt", f"{cablex_folder}/{loadingspace_folder}/Far_EOL_LS2.txt"]
    elif data_ls_solution == 3:
        data_files = [f"{cablex_folder}/{loadingspace_folder}/Nominal_SOL_LS3.txt", f"{cablex_folder}/{loadingspace_folder}/Nominal_EOL_LS3.txt", 
                    f"{cablex_folder}/{loadingspace_folder}/Cross_SOL_LS3.txt", f"{cablex_folder}/{loadingspace_folder}/Cross_EOL_LS3.txt", 
                    f"{cablex_folder}/{loadingspace_folder}/Near_SOL_LS3.txt", f"{cablex_folder}/{loadingspace_folder}/Near_EOL_LS3.txt",
                    f"{cablex_folder}/{loadingspace_folder}/Far_SOL_LS3.txt", f"{cablex_folder}/{loadingspace_folder}/Far_EOL_LS3.txt"]
    elif data_ls_solution == 4:
        data_files = [f"{cablex_folder}/{loadingspace_folder}/Nominal_SOL_LS4.txt", f"{cablex_folder}/{loadingspace_folder}/Nominal_EOL_LS4.txt"]
    elif data_ls_solution == 5:
        data_files = [f"{cablex_folder}/{loadingspace_folder}/Nominal_EOL_LS5.txt", f"{cablex_folder}/{loadingspace_folder}/Nominal_SOL_LS5.txt", 
                    f"{cablex_folder}/{loadingspace_folder}/Cross_SOL_LS5.txt", f"{cablex_folder}/{loadingspace_folder}/Cross_EOL_LS5.txt",
                    f"{cablex_folder}/{loadingspace_folder}/Near_SOL_LS5.txt", f"{cablex_folder}/{loadingspace_folder}/Near_EOL_LS5.txt",
                    f"{cablex_folder}/{loadingspace_folder}/Far_SOL_LS5.txt", f"{cablex_folder}/{loadingspace_folder}/Far_EOL_LS5.txt"]

    # Load all data into a list
    if data_ls_solution < 4:
        if CableLayout == 4 and MixedBuoy == 1:
            all_data = [cablexfile.lazywave_full_passconfig_load(file) for file in data_files]
        elif CableLayout == 4 and MixedBuoy == 2:  
            all_data = [cablexfile.lazywave_full_mixedbuoy_passconfig_load(file) for file in data_files]         
        elif MixedBuoy == 1 or MixedBuoy == 3:
            all_data = [cablexfile.lazywave_passconfig_load(file) for file in data_files]
        else:
            all_data = [cablexfile.lazywave_mixedbuoy_passconfig_load(file) for file in data_files]
    # elif data_ls_solution < 5:
    #     all_data = [load_data_staticTether(file) for file in data_files]
    elif data_ls_solution < 6:
        if MixedBuoy == 1 or MixedBuoy == 3:
            all_data = [cablexfile.rcdc_passconfig_load(file) for file in data_files]
        else:
            all_data = [cablexfile.rcdc_mixedbuoy_passconfig_load(file) for file in data_files]
        
    # Get all pass cases into a list
    all_pass_cases = [cablexfile.get_passcases(data, data_ls_solution) for data in all_data]

    # Get identical pass case for all scenarios
    #start_time = time.time()
    matched_cases = all_pass_cases[0]
    for pass_case in all_pass_cases[1:]:
        matched_cases = cablexfile.case_matching(matched_cases, pass_case, data_ls_solution)
    file_path = f'{cablex_folder}/{loadingspace_folder}/allpass.txt'
    cablexfile.export_passcase(matched_cases, file_path, data_ls_solution)
    
    print ("--------------------------------------------------------------------------")
    
    passfile = f'{cablex_folder}/{loadingspace_folder}/allpass.txt'
    # copy the loading space pass file folder to the next loading space
    ls_part = int(loadingspace_folder[2:])
    

    if CableLayout == 1 or CableLayout == 4:
        if ls_part < 3:
            ls_new_part = ls_part + 1
            loadingspace_new_folder = "LS" + str(ls_new_part)
        else:
            loadingspace_new_folder = "LS_Dy"
    elif CableLayout == 2 or CableLayout == 3:
        if ls_part < 5:
            ls_new_part = ls_part + 1
            loadingspace_new_folder = "LS" + str(ls_new_part)
        else:
            loadingspace_new_folder = "LS_Dy"
    else: 
        print("Cable and Buoyancy Layout Selection Error")

    targetdir = f'{cablex_folder}/{loadingspace_new_folder}'
    targetfile = os.path.join(targetdir, 'allpass.txt')
    shutil.copy(passfile, targetfile)

    
    print("Transfer Pass Configurations to Loading Space", loadingspace_new_folder )
    print ("--------------------------------------------------------------------------")
    print ("*******************Staic Loading Space", loadingspace_folder , "Accomplished*******************")
    print (" ")

if __name__ == '__main__':
    main()