#!/bin/env python
  
import xas_module
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import local_module

dict_structure = local_module.def_dict_structure()

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)
list1d_color = list(mcolors.TABLEAU_COLORS)
list1d_marker = matplotlib.markers.MarkerStyle.filled_markers
def def_plt(
        obj_ax,
        str_datfile,
        list1d_column,
        str_label,
        str_marker
        ):
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[list1d_column[0]] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[list1d_column[1]] )
    obj_ax.plot( array2d_xdata, array2d_ydata, marker=str_marker, mfc='none', label=str_label )
    obj_ax.legend()
    return obj_ax

def def_test(
        list2d_data, 
        ):
    fig, obj_ax = plt.subplots()

    for int_j in range(len(list2d_data)):
        list1d_data = list2d_data[ int_j ]
        def_plt(
            obj_ax = obj_ax,
            str_datfile = list1d_data[0],
            list1d_column = list1d_data[1],
            str_label = list1d_data[0],
            str_marker = list1d_marker[int_j]
            )
    plt.show()

str_homedir = os.environ['HOME']
os.chdir(str_homedir+'/group/202103_XasPtO/server/Pt.111_O_vac/Pt.111.a2b2c4_O1_vac/feff_kspace/')

def_test(
    list2d_data = [
        ['xas.ave.csv', [0,2] ],
        ['atom_1/ellipticity_z/xmu.dat', [0,3] ],
    ]
    )
