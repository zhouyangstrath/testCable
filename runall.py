# CableX/scripts/runall.py

'''
Code Functions: Operate all the running in sequence for a cablexworkflow
Version: CABLEX v1.6.0
Author Name: Yang Zhou
'''
# Python modules
import subprocess
import os
import sys
import json
import shutil

# Cablex modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Presettings of prepare the initial Input.dat file 
import input_excel    
input_excel.main()
#from initialSetting.sea_current import preset_current
from fileOperation.input_parser import input_parser 
import globals, sea_current, output_merge, config_check, marine_growth
import scripts.datasum_St as datasum_St, scripts.datasum_Dy as datasum_Dy
import scripts.direct_Setup as direct_Setup, scripts.orcafile_Extract as orcafile_Extract, scripts.orcafile_Extract_Dy as orcafile_Extract_Dy, scripts.passcheck_St as passcheck_St, scripts.postgui_copy as postgui_copy
import scripts.lazywave_Iteration as lazywave_Iteration, scripts.lazywave_mixedbuoy_Iteration as lazywave_mixedbuoy_Iteration, full_lazywave_iteration, scripts.rcdc_Iteration as rcdc_Iteration, scripts.rcdc_mixedbuoy_Iteration as rcdc_mixedbuoy_Iteration, scripts.rpw_Iteration as rpw_Iteration, scripts.rpw_mixedbuoy_Iteration as rpw_mixedbuoy_Iteration, scripts.rcdc_Iteration_Dy as rcdc_Iteration_Dy
import scripts.full_lazywave_mixedbuoy_iteration as fulllazywave_mixedbuoy_Iteration
import scripts.orcafile_Clean as orcafile_Clean
import scripts.orca_py_Mpi as orca_py_Mpi
import scripts.orca_py_Mpi_Dy as orca_py_Mpi_Dy
import scripts.postprocess_update as postprocess_update
import scripts.userspecify_output as userspecify_output

# Main
def main():

        
    currentdir = os.path.abspath(os.path.dirname(__file__))
    mpirunning = os.path.join(currentdir, 'pyOrcMultiProcessing.py') # Multi-processer Running
    mpirunningDy = os.path.join(currentdir, 'pyOrcMultiProcessingDy.py')
    

    # CABLEX folders and the Loading Space folders set up
    cablex_folder = globals.update_globals()[-1]
    index = 0
    # Get the inputdata
    input = input_parser('Input.dat')
    CableLayout = int(input['CableLayout'])
    DynamicRun = int(input['DynamicRun'])
    MixedBuoy = int(input['MixedBuoy'])
    
    # Determine the workfolders based on the the cable layout
    if CableLayout == 1 or CableLayout == 4:
        workfolders = ['LS1', 'LS2', 'LS3']
    else:
        workfolders = ['LS1', 'LS2', 'LS3', 'LS4', 'LS5', 'LS6']
    
    for folder in workfolders:
        # Static folder workflows
        if folder in ['LS1', 'LS2', 'LS3', 'LS4', 'LS5']:
            index = index + 1
            print ("####################Static Loading Space", index, "processing######################")
            # save the current folder status in json file
            folder_file = os.path.join(f'{cablex_folder}', 'folder.json')
            with open(folder_file, 'w') as f:
                json.dump(folder, f)
            
            # Main CableX workflows    
            if folder in ['LS1', 'LS2', 'LS3']:
                if CableLayout == 1 or CableLayout == 2 or CableLayout == 3:
                    if MixedBuoy == 1:
                    # lazywave iteration
                        lazywave_Iteration.main()
                    elif MixedBuoy == 2:
                        lazywave_mixedbuoy_Iteration.main()
                    else:
                        print('Buoy Selection method Error')
                if CableLayout == 4:
                    if MixedBuoy == 1:
                        full_lazywave_iteration.main()
                    else: 
                        fulllazywave_mixedbuoy_Iteration.main()
                      
            elif folder in ['LS4', 'LS5']:
                if CableLayout == 2:
                    if MixedBuoy == 1:
                    # rcdc iteration
                        rcdc_Iteration.main()
                    else: 
                        rcdc_mixedbuoy_Iteration.main()
                elif CableLayout == 3:
                    # rpw iteration
                    if MixedBuoy == 1:
                        rpw_Iteration.main()
                    else:
                        rpw_mixedbuoy_Iteration.main()
                else:
                    print("CableLayout setting Error in Input.dat")
            else:
                print("Error on Loading Space selection")
            
            # Extract orcaflex files used for simulation
            orcafile_Extract.main()
            
            # mpi running 
            orca_py_Mpi.main()
            #mpirunning_run = subprocess.run(['python', mpirunning], cwd=f'{cablex_folder}/{folder}',capture_output=True, text=True)
            #print(mpirunning_run.stdout)
            
            # dataSumStatic to summarise the results obtained
            datasum_St.main()
            # passCheck
            passcheck_St.main()  
            # Check if there are passed configurations, if not, exit the cablex loop
            config_check.main()         
        
        # Dynamic folder workflows   
        elif folder in ['LS6']:
            
            index = index + 1
            
            print ("##################Extreme Dynamic Loading Space", index, "processing####################")
            
            folder_file = os.path.join(f'{cablex_folder}', 'folder.json')
            with open(folder_file, 'w') as f:
                json.dump(folder, f)

            if DynamicRun == 1:
                # rcdc Iteration in Dynamics
                rcdc_Iteration_Dy.main()
                # orcaflex files extraction
                orcafile_Extract_Dy.main()
            
                mpirunningDy_run = subprocess.run(['python', mpirunningDy], cwd=f'{cablex_folder}/{folder}',capture_output=True, text=True)
                print(mpirunningDy_run.stdout)
                # datasumDynamic
                datasum_Dy.main()
            else:
                ("User Select to run Extreme Dynamic Analysis maunally")
        else:
            print("Error in loading space selection")
            
if __name__ == '__main__':
        
    print("""
--------------------------------------------------------------------------- 
CABLEX: FOWT Power Cable Configuration Tool 
Version: v1.6.5
Copyright (C) Yang Zhou TechnipFMC/University of Strathclyde
---------------------------------------------------------------------------

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            CABLEX Configuration Screening WorkFlow Initiated 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         """)
    
    print("***************************************************************************")  
    print("          Transferred User Input Excel Sheet to CableX dat file")
    # # Transfer the excel sheet to dat file
    # Website: https://cablex-api.readthedocs.io/en/latest/
    # input_excel.main()
    input_excel.input_check()
    # Add user specified output in the documentaion
    userspecify_output.main()
    # Update the postprocess scripts
    postprocess_update.main()    
    # PreSetting of the Current Profile in the base model
    sea_current.main()    
    # Setup the basic directory before cablex running
    direct_Setup.main()
    # CableX workflows
    main()
    # Copy the postprocess GUI to the postUI folder
    postgui_copy.main()
    # merge the data for the output excel sheet
    output_merge.main()
    
    print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            CABLEX Configuration Screening WorkFlow Accomplished  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
          """)
