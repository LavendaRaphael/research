from ase.calculators.vasp import VaspChargeDensity
import os
import numpy
import from_xas_modules

str_comput_110=os.environ['goto_pto_comput_110']

str_chdir = str_comput_110+'Pt.110.x2y3z4.5_O1_vac15/vasp_sch/atom_1/'
os.chdir(str_chdir)

vchg = VaspChargeDensity(filename='peak_1/WFN_SQUARED_B0271_K0006.vasp')
atoms = vchg.atoms[0]
print(atoms)

array3d_chg=vchg.chg[0]
float_chg=numpy.sum(array3d_chg)
from_xas_modules.def_print_paras( locals(), ['float_chg'] )

tup_shape=numpy.shape(array3d_chg)
from_xas_modules.def_print_paras( locals(), ['tup_shape'] )

int_ngrid = 1
for int_i in tup_shape:
    int_ngrid *= int_i
from_xas_modules.def_print_paras( locals(), ['int_ngrid'] )

float_volume=atoms.get_volume()
from_xas_modules.def_print_paras( locals(), ['float_volume'] )

float_volslice = float_volume/int_ngrid
from_xas_modules.def_print_paras( locals(), ['float_volslice'] )

float_chg_volslice = float_chg*float_volslice
from_xas_modules.def_print_paras( locals(), ['float_chg_volslice'] )

float_chg_volume = float_chg*float_volume
from_xas_modules.def_print_paras( locals(), ['float_chg_volume'] )