#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_work_110=os.environ['goto_pto_work_110']

dict_structures = {}

str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
list_atoms = []
list_atoms.append([ 1,2.0])
list_atoms.append([ 3,2.0])
list_atoms.append([ 5,2.0])
list_atoms.append([ 7,2.0])
list_atoms.append([ 9,2.0])
list_atoms.append([11,1.0])

str_chdir = str_work_110 + str_workdir

dict_structures[ str_workdir ] = class_structures()
dict_structures[ str_workdir ].list_atoms = list_atoms
dict_structures[ str_workdir ].str_chdir = str_chdir
