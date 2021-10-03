#!/bin/env python
from from_xas_modules import *
import os
sys.path.append(r'./')
from from_dict_structures import dict_structures 

list_workdirs=[]
#----------------------------------[Pt.110]
list_workdirs.append('Pt.110.x12y2z4.5_O22_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O1_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O6_vac15/')

#----------------------------------[Pt.111]

#----------------------------------[loop]

for str_workdir in list_workdirs:
    str_chdir = dict_structures[ str_workdir ].str_chdir
    str_cddir = str_chdir+'vasp_sch/'

    os.chdir(str_cddir)
    print(os.getcwd())

    list_atoms = dict_structures[ str_workdir ].list_atoms
    def_xas_ave( list_atoms)