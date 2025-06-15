    
#CableX/scripts/pyOrcMultiProcessingDy.py

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

from orcaMPI.orca_py_mpi_dy import WorkerDy
from fileOperation.input_parser import input_parser
from fileOperation.orcaflex_files import orcaflexfiles 

def main():

    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.WARNING)

    input = input_parser('Input.dat')
    MpiCount = int(input['MpiCount'])            
    corecount = MpiCount # edit this value to the number of cores you want to use on your computer
    
    print("Iterated Models Running in Orcaflex")
    print ("OrcaFlex Modelling is using", MpiCount, "Cores to Run in parallel!")
    
    fileList = []
    WorkerDys = []
    # for datfile in glob.glob('*.yml'): # edit this to *.sim, *.dat, *.yml or other filter to select the files you want to run
    #     fileList.append(datfile)
    yaml = orcaflexfiles()
    fileList = yaml.read_filelist('Filelist.lst')
    chunkSize = int(len(fileList) / corecount)
    chunkRemainder = int(len(fileList) % corecount)
    #print('%s jobs found, dividing across %s WorkerDys - %s each remainder %s' % (str(len(fileList)), str(corecount), chunkSize, chunkRemainder))

    start = 0
    for coreNum in range(0, corecount):
        WorkerDy = WorkerDy()
        WorkerDys.append(WorkerDy)
        end = start + chunkSize
        if chunkRemainder>0:
            chunkRemainder -= 1
            end += 1
        if end>len(fileList):
            end = len(fileList)
        WorkerDy.setJobs(fileList[start:end])
        WorkerDy.start()
        start = end
        if start>=len(fileList):
            break

    for WorkerDy in WorkerDys:
        WorkerDy.join()
    print('Simulation Accomplished...')
    print ("--------------------------------------------------------------------------")
    
if __name__=='__main__':
    main()
