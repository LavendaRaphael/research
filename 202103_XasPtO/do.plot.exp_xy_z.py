#!/bin/env python

import xas_module
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import local_module

str_exp=os.environ['goto_pto_exp']
str_work_110=os.environ['goto_pto_work_110']
str_work_111=os.environ['goto_pto_work_111']

dict_structure = local_module.def_dict_structure()

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)
list1d_color = list(mcolors.TABLEAU_COLORS)

#---------------------------------------------------------------------------------------------
def def_plt_exp(
        obj_ax,
        str_datfile,
        str_label,
        list1d_column = [0,1]
        ):
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
    obj_ax.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=str_label )
    return obj_ax

def def_plt_theory(
        obj_ax,
        str_datfile,
        str_label,
        list1d_column,
        ):
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
    obj_ax.plot( array2d_xdata, array2d_ydata, label=str_label )
    return obj_ax

def def_plt_save(
        fig,
        obj_ax,
        str_savefig,
        tuple_xlim = (None, None),
        tuple_ylim = (None, None),
        ):
    obj_ax.set_xlim( tuple_xlim )
    obj_ax.set_ylim( tuple_ylim )
    obj_ax.set_xlabel( 'Energy (eV)' )
    obj_ax.set_ylabel( 'Intensity (Arb. Units)' )
    obj_ax.legend()
    fig.savefig( str_savefig, bbox_inches='tight' )

#----------------------------------------------------------------------------------
def def_pic_exp_theory(
        str_workdir,
        str_savefig,
        list1d_exp,
        list2d_data,
        ):

    os.chdir( str_workdir )
    print(os.getcwd())

    fig, obj_ax = plt.subplots()
    def_plt_exp(
        obj_ax = obj_ax,
        str_datfile = str_exp + list1d_exp[0],
        str_label=r'Exp. '+list1d_exp[2],
        list1d_column = list1d_exp[1]
        )
    for list1d_data in list2d_data:
        def_plt_theory(
            obj_ax = obj_ax,
            str_datfile = list1d_data[0],
            list1d_column = list1d_data[1],
            str_label = r'Theory '+ list1d_data[2]
        )
    def_plt_save(
        fig,
        obj_ax,
        str_savefig+'.pdf',
        tuple_xlim = (527,540),
        tuple_ylim = (None,None)
        )
    plt.show()

if (''):
    def_pic_exp_theory(
        str_workdir = dict_structure[ '110.x2y12_O22' ].str_chdir,
        str_savefig = 'xas.exp_xy_z',
        list1d_exp = [ '20210924.pto110_a20_postscaling.csv',[1,2],'20$\degree$' ],
        list2d_data = [
            ['xas.alpha.csv',[0,2],'X_Y'],
            ['xas.alpha.csv',[0,3],'Z']
            ]
        )
