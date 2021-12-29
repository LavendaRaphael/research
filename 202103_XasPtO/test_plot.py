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
        ):
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[list1d_column[0]] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[list1d_column[1]] )
    obj_ax.plot( array2d_xdata, array2d_ydata, label=str_label )
    obj_ax.legend()
    return obj_ax

def def_test(
        list2d_data, 
        tuple_xlim = (None, None)
        ):
    fig, obj_ax = plt.subplots()

    for int_j in range(len(list2d_data)):
        list1d_data = list2d_data[ int_j ]
        def_plt(
            obj_ax = obj_ax,
            str_datfile = list1d_data[0],
            list1d_column = list1d_data[1],
            str_label = list1d_data[0],
            )
    obj_ax.set_xlim( tuple_xlim )
    plt.show()

str_homedir = os.environ['HOME']
os.chdir(str_homedir+'/research/202103_XasPtO/server/Pt.110_O_vac/Pt.110.x2y12_O22_vac/vasp_sch/')

def_test(
    list2d_data = [
        [ 'xas.alpha.csv', [0,3] ],
        [ 'xas.a20_b90.csv',[0,3] ],
    ],
    tuple_xlim = (527,540)
    )
