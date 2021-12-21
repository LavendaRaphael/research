#!/bin/env python
  
import xas_module
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import local_module
import numpy

dict_structure = local_module.def_dict_structure()

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)
list1d_color = list(mcolors.TABLEAU_COLORS)
list1d_marker = matplotlib.markers.MarkerStyle.filled_markers

fig, obj_ax = plt.subplots()
array1d_x = numpy.linspace(-10,10,1000)
array1d_g = xas_module.def_lineshape('gaussian',array1d_x,0.5)
array1d_l = xas_module.def_lineshape('lorentzian',array1d_x,0.5)

obj_ax.plot( array1d_x, array1d_g, label='Gaussian' )
obj_ax.plot( array1d_x, array1d_l, label='Lorentzian' )
obj_ax.legend()

obj_ax.set_xlim( -2,2 )
plt.show()

