#!/bin/env python

from from_xas_modules import *
import os
sys.path.append(r'./')
from from_dict_structures import dict_structures 

list_workdirs=[]
#----------------------------------[Pt.110]
list_workdirs.append('Pt.110.x12y2z4.5_O22_vac15/')

#----------------------------------[loop]

for str_workdir in list_workdirs:
    str_chdir = dict_structures[ str_workdir ].str_chdir
    str_chdir = str_chdir+'vasp_sch/'

    os.chdir(str_chdir)
    print(os.getcwd())

    list_atoms = dict_structures[ str_workdir ].list_atoms
    os.chdir(list_atoms[5][0])
    print(os.getcwd())

    def_xas_extract_tm()