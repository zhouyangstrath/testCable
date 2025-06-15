    
#CableX/scripts/pyOrcMultiProcessing.py

"""
Function: Used in each loading space for orcaflex files extraction
Version: CABLEX v1.6.0
Author Name: Yang Zhou
"""

import glob
import sys
import os
import multiprocessing
import logging

# Add the parent directory of 'offshore_wind_turbine' to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from orcaMPI.orca_py_mpi import Worker
from fileOperation.input_parser import input_parser
from fileOperation.orcaflex_files import orcaflexfiles 
import globals
import json

def main():
    
    cablex_folder = globals.update_globals()[-1]

    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.WARNING)

    input = input_parser('Input.dat')
    MpiCount = int(input['MpiCount'])            
    corecount = MpiCount # edit this value to the number of cores you want to use on your computer
    
    print("Iterated Models Running in Orcaflex")
    print ("OrcaFlex Modelling is using", MpiCount, "Cores to Run in parallel!")
    
    fileList = []
    workers = []
    # for datfile in glob.glob('*.yml'): # edit this to *.sim, *.dat, *.yml or other filter to select the files you want to run
    #     fileList.append(datfile)
    yaml = orcaflexfiles()
    #fileList = yaml.readFilelist(f'{cablex_folder}/Filelist.lst')
    # Load the current loading spaces
    folder_file = os.path.join(cablex_folder, 'folder.json')
    with open(folder_file, 'r') as f:
        loadingspace_folder = json.load(f)
    
    outputfile = f'{cablex_folder}/{loadingspace_folder}/Filelist.lst'
    print(outputfile)
    fileList = yaml.read_filelist(outputfile)
    chunkSize = int(len(fileList) / corecount)
    chunkRemainder = int(len(fileList) % corecount)
    #print('%s jobs found, dividing across %s workers - %s each remainder %s' % (str(len(fileList)), str(corecount), chunkSize, chunkRemainder))

    start = 0
    for coreNum in range(0, corecount):
        worker = Worker()
        workers.append(worker)
        end = start + chunkSize
        if chunkRemainder>0:
            chunkRemainder -= 1
            end += 1
        if end>len(fileList):
            end = len(fileList)
        worker.setJobs(fileList[start:end])
        worker.start()
        start = end
        if start>=len(fileList):
            break

    for worker in workers:
        worker.join()
    print('Simulation Accomplished...')
    print ("--------------------------------------------------------------------------")
    
if __name__=='__main__':
    main()
