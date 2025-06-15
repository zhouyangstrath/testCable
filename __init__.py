# CableX/__init__.py

"""
CABLEX Package of FOWT power cable configuration Design and Optimisation
Version: CABLEX v1.6.5
Author Name: Yang Zhou

Modules:
- file_operations: Folder Copy, AllpassFile Read for LazyWave, AllpassFile Read for RCDC
- cable_iteration: lazywaveCable, rcdcCable 

"""

from .cableIteration import fulllazywave_cable, fulllazywave_cable_mixedbuoy, lazywave_cable, lazywave_cable_mixedbuoy
from .cableIteration import rcdc_cable, rcdc_cable_mixedbuoy, rpw_cable, rpw_cable_mixedbuoy, rcdc_cable_dynamic
from .fileOperation import folder_copy, folder_clean, input_parser, allpass_parser_lw, allpass_parser_rcdc, orcaflex_files, copy_gui_files, output_merge
from .orcaMPI import orca_py_mpi
from .postProcessing import datasum_static, datasum_dynamic
from .initialSetting import sea_current