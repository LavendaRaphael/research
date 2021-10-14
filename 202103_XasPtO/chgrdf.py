#!/usr/bin/env python
# coding: utf-8

import from_xas_modules
import os
import matplotlib.pyplot as plt

str_comput_110=os.environ['goto_pto_comput_110']

str_chdir = str_comput_110+'Pt.110.x2y3z4.5_O1_vac15/vasp_sch/atom_1/'
os.chdir(str_chdir)
print(os.getcwd())

array1d_r, array1d_rdf = from_xas_modules.def_chgrdf(
    str_chgfile = 'CHG'
    )
plt.plot( array1d_r, array1d_rdf )
plt.show()