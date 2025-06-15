# CableX/scripts/config_check.py

'''
Functions: Pass Case Check based on the Summarised post-processing data files
Version: CABLEX v1.6.5
Author Name: Yang Zhou
'''

import time
import numpy as np
import sys
import os
import json
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import globals
from postProcessing.config_check import check_allpass_file

def main():
    
    cablex_folder = globals.update_globals()[-1]
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)
        
    file_path = f'{cablex_folder}/{loadingspace_folder}/allpass.txt'
    #print(file_path)
    check_allpass_file(file_path)


if __name__ == '__main__':
    main()
    