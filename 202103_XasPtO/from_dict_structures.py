#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

dict_structures = {}

str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
list2d_atom = []
list2d_atom.append([ 1,2.0])
list2d_atom.append([ 3,2.0])
list2d_atom.append([ 5,2.0])
list2d_atom.append([ 7,2.0])
list2d_atom.append([ 9,2.0])
list2d_atom.append([11,1.0])

str_chdir = str_110 + str_workdir

dict_structures[ str_workdir ] = class_structures()
dict_structures[ str_workdir ].list2d_atom = list2d_atom
dict_structures[ str_workdir ].str_chdir = str_chdir
