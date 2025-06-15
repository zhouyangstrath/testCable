#CableX/initialSettings

"""
Functions: Used to transfer the excel file to the input.dat file 
Version: v1.6
Author: Yang Zhou
"""

import pandas as pd
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fileOperation.input_parser import input_parser 

def main():
    # Load the excel file 
    excel_file_path = 'CableX_Input.xlsx'
    df_summarysheet = pd.read_excel(excel_file_path, sheet_name='Summary', header=None)
    df_environmentsheet = pd.read_excel(excel_file_path, sheet_name='Environment', header=None)
    df_statichecksheet = pd.read_excel(excel_file_path, sheet_name='Static_Check', header=None)
    df_cablexsheet = pd.read_excel(excel_file_path, sheet_name= 'CableX_DS', header=None)

    # Load the input.dat file
    input_file_path = 'Input_org.dat'
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        
    # print(df_summarysheet)

    # Value Extract in Summary Sheet
    cable_layout = int(df_summarysheet.iloc[9, 4]) # Cell E10 for CableLayout Value
    cable_type = int(df_summarysheet.iloc[10, 4]) # Cell E11 for CableType Value
    mixed_buoy = int(df_summarysheet.iloc[11, 4]) # Cell E12 for mixedBuoy Value
    buoy_type1 = str(df_summarysheet.iloc[12, 4]) # Cell E13 for First Type of Buoyancy Module
    buoy_type2 = str(df_summarysheet.iloc[13, 4]) # Cell E14 for Second Type of Buoyancy Module
    hang_off = int(df_summarysheet.iloc[16, 4]) # Cell E17 for hangoff positions Value
    clamp_init = int(df_summarysheet.iloc[17, 4]) # Cell E18 for clamp init Value
    marine_growth1 = int(df_summarysheet.iloc[20, 4]) # Cell E21 for marine growth from 2 to -40m 
    marine_growth2 = int(df_summarysheet.iloc[21, 4]) # Cell E22 for marine growth below -40m 
    mpi_count = int(df_summarysheet.iloc[24, 4]) # Cell E24 for cores used for parallel running 
    # Replace Lines with Summary/DIAC system Files 
    lines[10] = lines[10].replace('1', str(cable_layout), 1)
    lines[11] = lines[11].replace('800', str(cable_type), 1)
    lines[12] = lines[12].replace('3', str(mixed_buoy), 1)
    lines[13] = lines[13].replace('730_800', str(buoy_type1), 1)
    lines[14] = lines[14].replace('500', str(buoy_type2), 1)
    lines[16] = lines[16].replace('10', str(hang_off), 1)
    lines[17] = lines[17].replace('12', str(clamp_init), 1)
    lines[18] = lines[18].replace('25', str(marine_growth1), 1)
    lines[22] = lines[22].replace('4', str(mpi_count), 1)

    # Value Extract in Environment Sheet
    water_depth = int(df_environmentsheet.iloc[5, 4]) # Cell E6 for waterdepth Value
    offset = int(df_environmentsheet.iloc[6, 4]) # Cell E7 for offset Value
    tidal_current = str(df_environmentsheet.iloc[7, 4]) # Cell E8 tidal current Value
    wind_current = str(df_environmentsheet.iloc[8, 4]) # Cell E9 wind driven current Value
    dev_depth = int(df_environmentsheet.iloc[9, 4]) # Cell E10 dev depth Value 
    # Replace Lines with Environment system Files
    lines[25] = lines[25].replace('93', str(water_depth), 1) 
    lines[26] = lines[26].replace('35', str(offset), 1) 
    lines[27] = lines[27].replace('1.00', str(tidal_current), 1) 
    lines[28] = lines[28].replace('0.36', str(wind_current), 1)
    lines[29] = lines[29].replace('40', str(dev_depth), 1)

    # Value Extract in Static Check Sheet
    sag_clear = int(df_statichecksheet.iloc[5, 4]) # Cell E6 for Sag Clearance Value
    hog_clear = int(df_statichecksheet.iloc[6, 4]) # Cell E7 for Hog Clearance Value
    sag_mbr = float(df_statichecksheet.iloc[7, 4]) # Cell E8 for Sag MBR Value
    hog_mbr = float(df_statichecksheet.iloc[8, 4]) # Cell E9 for Sag MBR Value
    lwtdp_mbr = float(df_statichecksheet.iloc[9, 4]) # Cell E10 for full lazywave Tdp MBR Value
    top_angle = float(df_statichecksheet.iloc[10, 4]) # Cell E11 for Top Angle Value
    top_tension = float(df_statichecksheet.iloc[11, 4]) # Cell E12 for Top Tension Value
    clamp_mbr = float(df_statichecksheet.iloc[13, 4]) # Cell E14 for clamp MBR Value
    tdp_mbr = float(df_statichecksheet.iloc[14, 4]) # Cell E15 for TDP MBR Value
    # Replace Lines with static check system Files
    lines[33] = lines[33].replace('12', str(sag_clear), 1)
    lines[34] = lines[34].replace('12', str(hog_clear), 1)
    lines[35] = lines[35].replace('9', str(sag_mbr), 1)
    lines[36] = lines[36].replace('9', str(hog_mbr), 1)
    lines[37] = lines[37].replace('9', str(lwtdp_mbr), 1)
    lines[38] = lines[38].replace('360', str(top_angle), 1)
    lines[39] = lines[39].replace('550', str(top_tension), 1)
    lines[41] = lines[41].replace('8', str(clamp_mbr), 1)
    lines[42] = lines[42].replace('8', str(tdp_mbr), 1)

    # Value Extract in CableX Workflows
    layback_min = int(df_cablexsheet.iloc[5, 4]) # Cell E6 for Layback Min Value 
    layback_max = int(df_cablexsheet.iloc[6, 4]) # Cell E7 for Layback Max Value 
    layback_delta = int(df_cablexsheet.iloc[7, 4]) # Cell E8 for Layback Delta Value 
    total_min = int(df_cablexsheet.iloc[9, 4]) # Cell E10 for Total Min Value 
    total_max = int(df_cablexsheet.iloc[10, 4]) # Cell E11 for Total Max Value 
    total_delta = int(df_cablexsheet.iloc[11, 4]) # Cell E12 for Total Delta Value 
    buoy_min = int(df_cablexsheet.iloc[13, 4]) # Cell E14 for Buoy1 Min Value 
    buoy_max = int(df_cablexsheet.iloc[14, 4]) # Cell E15 for Buoy1 Max Value 
    buoy_delta = int(df_cablexsheet.iloc[15, 4]) # Cell E16 for Buoy1 Delta Value 
    buoy2_min = int(df_cablexsheet.iloc[16, 4]) # Cell E17 for Buoy2 Min Value 
    buoy2_max = int(df_cablexsheet.iloc[17, 4]) # Cell E18 for Buoy2 Max Value 
    buoy2_delta = int(df_cablexsheet.iloc[18, 4]) # Cell E19 for Buoy2 Delta Value 
    buoycc_min = int(df_cablexsheet.iloc[20, 4]) # Cell E21 for Buoy Adj Cen Min Value 
    buoycc_max = int(df_cablexsheet.iloc[21, 4]) # Cell E22 for Buoy Adj Cen Max Value 
    buoycc_delta = int(df_cablexsheet.iloc[22, 4]) # Cell E23 for Buoy Adj Cen Delta Value
    buoy1st_fix = int(df_cablexsheet.iloc[24, 4]) # Cell E25 for Buoy 1st fix Value 
    buoy1st_min = int(df_cablexsheet.iloc[25, 4]) # Cell E26 for Buoy 1st Min Value
    buoy1st_max = int(df_cablexsheet.iloc[26, 4]) # Cell E27 for Buoy 1st Max Value 
    buoy1st_delta = int(df_cablexsheet.iloc[27, 4]) # Cell E28 for Buoy 1st Delta Value
    rcdc_an = str(df_cablexsheet.iloc[29, 4]) # Cell E30 for Amplification for RCDC Anchor compared with layback
    rpw_an = str(df_cablexsheet.iloc[30, 4]) # Cell E31 for Amplification for Rpw Anchor compared with layback
    rcdcl_min = int(df_cablexsheet.iloc[32, 4]) # Cell E33 for rcdc Length Min Value
    rcdcl_max = int(df_cablexsheet.iloc[33, 4]) # Cell E34 for rcdc Length Max Value 
    rcdcl_delta = int(df_cablexsheet.iloc[34, 4]) # Cell E35 for rcdc Length Delta Value
    rpwl_min = int(df_cablexsheet.iloc[35, 4]) # Cell E36 for rpw Length Min Value
    rpwl_max = int(df_cablexsheet.iloc[36, 4]) # Cell E37 for rpw Length Max Value 
    rpwl_delta = int(df_cablexsheet.iloc[37, 4]) # Cell E38 for rpw Length Delta Value
    tethera_min = int(df_cablexsheet.iloc[39, 4]) # Cell E40 for tether anchor Min Value
    tethera_max = int(df_cablexsheet.iloc[40, 4]) # Cell E41 for rpw tether anchor Max Value 
    tethera_delta = int(df_cablexsheet.iloc[41, 4]) # Cell E42 for rpw tether anchor Delta Value
    tetherl_min = int(df_cablexsheet.iloc[43, 4]) # Cell E44 for tether length Min Value
    tetherl_max = int(df_cablexsheet.iloc[44, 4]) # Cell E45 for rpw tether length Max Value 
    tetherl_delta = int(df_cablexsheet.iloc[45, 4]) # Cell E46 for rpw tether length Delta Value
    # Replace Lines with CableX workflow Files
    lines[47] = lines[47].replace('160', str(layback_min), 1)
    lines[48] = lines[48].replace('181', str(layback_max), 1)
    lines[49] = lines[49].replace('10', str(layback_delta), 1)
    lines[51] = lines[51].replace('210', str(total_min), 1)
    lines[52] = lines[52].replace('241', str(total_max), 1)
    lines[53] = lines[53].replace('10', str(total_delta), 1)
    lines[55] = lines[55].replace('20', str(buoy_min), 1)
    lines[56] = lines[56].replace('27', str(buoy_max), 1)
    lines[57] = lines[57].replace('1', str(buoy_delta), 1)
    lines[58] = lines[58].replace('6', str(buoy2_min), 1)
    lines[59] = lines[59].replace('21', str(buoy2_max), 1)
    lines[60] = lines[60].replace('1', str(buoy2_delta), 1)
    lines[62] = lines[62].replace('4', str(buoycc_min), 1)
    lines[63] = lines[63].replace('5', str(buoycc_max), 1)
    lines[64] = lines[64].replace('1', str(buoycc_delta), 1)
    lines[66] = lines[66].replace('3', str(buoy1st_fix), 1)
    lines[67] = lines[67].replace('60', str(buoy1st_min), 1)
    lines[68] = lines[68].replace('221', str(buoy1st_max), 1)
    lines[69] = lines[69].replace('5', str(buoy1st_delta), 1)
    lines[73] = lines[73].replace('1.7', str(rcdc_an), 1)
    lines[74] = lines[74].replace('1.7', str(rpw_an), 1)
    lines[76] = lines[76].replace('4', str(rcdcl_min), 1)
    lines[77] = lines[77].replace('21', str(rcdcl_max), 1)
    lines[78] = lines[78].replace('4', str(rcdcl_delta), 1)
    lines[79] = lines[79].replace('4', str(rpwl_min), 1)
    lines[80] = lines[80].replace('20', str(rpwl_max), 1)
    lines[81] = lines[81].replace('4', str(rpwl_delta), 1)
    lines[83] = lines[83].replace('9', str(tethera_min), 1)
    lines[84] = lines[84].replace('4', str(tethera_max), 1)
    lines[85] = lines[85].replace('3', str(tethera_delta), 1)
    lines[87] = lines[87].replace('12', str(tetherl_min), 1)
    lines[88] = lines[88].replace('15', str(tetherl_max), 1)
    lines[89] = lines[89].replace('1', str(tetherl_delta), 1)

    # Value Extract in Static Check Sheet for specified range 
    specified_min = int(df_statichecksheet.iloc[19, 4]) # Cell E6 for Sag Clearance Value
    specified_max = int(df_statichecksheet.iloc[20, 4]) # Cell E7 for Hog Clearance Value
    specified_mbr = float(df_statichecksheet.iloc[21, 4]) # Cell E7 for Hog Clearance Value
    
    # Value Replace for the specified reigon
    lines[93] = lines[93].replace('5', str(specified_min), 1)
    lines[94] = lines[94].replace('1', str(specified_max), 1)
    lines[95] = lines[95].replace('5', str(specified_mbr), 1)    

    output_file_path = 'Input.dat'

    with open(output_file_path, 'w') as file:
        file.writelines(lines)

    #print("***************************************************************************") 
    #print("")

def input_check():
    input = input_parser('Input.dat')
    # Cable Layout Check
    CableLayout = int(input['CableLayout'])
    valid_cablelayout =  {1, 2, 3, 4}
    if CableLayout not in valid_cablelayout:
        print(f"Error: Specifying wrong Cable Layout: Type '{CableLayout}', Double Check Input File")
        sys.exit(1)
    # Cable Type Check
    CableType = int(input['CableType'])
    valid_cable = {300, 800}
    if CableType not in valid_cable:
        print(f"Error: Specifying wrong Cable Type: Type {CableType}, Double Check Input File")
        sys.exit(1)
    # MixedBuoy Check
    MixedBuoy = int(input['MixedBuoy'])
    valid_mixedbuoy = {1, 2}
    if MixedBuoy not in valid_mixedbuoy:
        print(f"Error: Specifying wrong Cable Type: Type {MixedBuoy}, Double Check Input File")
        sys.exit(1)
    # Buoyancy Module Check
    BuoyType = int(input['BuoyType'])
    Buoy2Type = int(input['Buoy2Type'])
    
    buoy_mapping = {
        500: "500kg",
        600: "600kg",
        700: "700kg",
        800: "800kg",
        900: "900kg",
        1000: "1000kg",
        300300: "300kg_300mm2",
        420300: "420kg_300mm2",
        570300: "570kg_300mm2",
        300800: "300kg_800mm2",
        500800: "500kg_800mm2",
        730800: "730kg_800mm2"
        }
    
    if BuoyType not in buoy_mapping:
        print(f"Error: Specifying wrong 1st Buoyancy Module Type: Type {BuoyType}, Double Check Input File")
        sys.exit(1)
    if Buoy2Type not in buoy_mapping:
        print(f"Error: Specifying wrong 2nd Buoyancy Module Type: Type {Buoy2Type}, Double Check Input File")
        sys.exit(1)
    print ("                    Input File Check Complete")
    
if __name__ == "__main__":
    main()