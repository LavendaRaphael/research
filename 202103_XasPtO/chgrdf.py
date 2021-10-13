#!/usr/bin/env python
# coding: utf-8

import from_xas_modules
import os

str_comput_110=os.environ['goto_pto_comput_110']

str_chdir = str_comput_110+'Pt.110.x2y3z4.5_O1_vac15/vasp_sch/atom_1/peak_1/'
os.chdir(str_chdir)
print(os.getcwd())

from_xas_modules.def_xas_kb_chgrdf( int_k=6, int_b=271 )