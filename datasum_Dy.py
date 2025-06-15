#CableX/scripts/orcafileExtract.py

"""
Function: Used in each loading space for orcaflex files extraction
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import sys
import os
import json

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from postProcessing.datasum_dynamic import datasum_dynamic
from fileOperation.input_parser import input_parser 
import globals


def main():
    
    print("Results Summarising:")

    input = input_parser('Input.dat')
    CableLayout = int(input['CableLayout'])
    MixedBuoy = int((input['MixedBuoy']))
    print(CableLayout)
    dataSum = datasum_dynamic()
    marinegrowth = ['EOL', 'SOL']
    cablex_folder = globals.update_globals()[-1]
    
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    # with open(folder_file, 'r') as f:
    #     LoadingSpace = json.load(f)
    directrory_path = os.path.join(cablex_folder, "LS_Dy")
    # List all the files
    lay_folders = [folder for folder in os.listdir(directrory_path) if os.path.isdir(os.path.join(directrory_path, folder)) and folder.startswith('Lay')]

    for folder in lay_folders:
        angles = ['0deg', '15deg', '-15deg' ]
        marinegrowth = ['EOL', 'SOL']

        for angle in angles:
            for mg in marinegrowth:
                if CableLayout == 4:
                    dataSum.datasum_fulllazywave_dynamic(folder, angle, mg)
                else:
                    dataSum.datasum_rcdc_dynamic(folder, angle, mg)
                #print(folder, angle, mg)
        for angle in angles:
            for mg in marinegrowth: 
                print ('Summarizing Configuration: ' + folder + ' Marine Growth: ' + mg + ' Azumith: '+ angle)
                input_file = f'{angle}_{mg}.txt'
                folder_path = f'{cablex_folder}/LS_Dy/{folder}/{angle}'
                output_folder = f'{cablex_folder}/LS_Dy'
                if os.path.exists(os.path.join(folder_path, input_file)):
                    #print('Yes')
                    with open(os.path.join(folder_path, input_file), 'r') as infile:
                        data = infile.read()
                    with open(os.path.join(output_folder, f'Dynamic_LSDy_{mg}.txt'), 'a') as outfile:
                        outfile.write(data)
                else:
                    printer = "Error in" + folder_path + "file Loading"
                    print(printer)
    
    file_path_eol = f'{cablex_folder}/LS_Dy/Dynamic_LSDy_EOL.txt'
    file_path_sol = f'{cablex_folder}/LS_Dy/Dynamic_LSDy_SOL.txt'
    if CableLayout == 4:
        dataSum.add_header_fulllazywave(file_path_eol)
        dataSum.add_header_fulllazywave(file_path_sol)
    else: 
        dataSum.add_header_rcdc(file_path_eol)
        dataSum.add_header_rcdc(file_path_sol)       
    print ("--------------------------------------------------------------------------")
                
    
if __name__ == "__main__":
    main()