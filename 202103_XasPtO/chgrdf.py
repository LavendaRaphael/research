#!/usr/bin/env python
# coding: utf-8

from ase.calculators.vasp import VaspChargeDensity
import os
import numpy
import from_xas_modules
import math
import matplotlib.pyplot as plt

str_comput_110=os.environ['goto_pto_comput_110']

str_chdir = str_comput_110+'Pt.110.x2y3z4.5_O1_vac15/vasp_sch/atom_1/'
os.chdir(str_chdir)
print(os.getcwd())

obj_chgcar = VaspChargeDensity(filename='peak_1/WFN_SQUARED_B0271_K0006.vasp')


plt.plot( array1d_r, array1d_rdf )
