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

#--------------------------------------------------------------------------------------------------------
def def_pic_tm(
        ax,
        str_datfile,
        list1d_column,
        str_label,
        ):
    
    _, array2d_xdata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
    ax.plot( array2d_xdata_tm, array2d_ydata_tm, 'o', label=str_label)

    return ax, array2d_xdata_tm, array2d_ydata_tm
def def_pic_tm_select(
        ax,
        str_datfile,
        list1d_column,
        float_onset,
        float_xwidth = 0.5,
        int_ntm = 1,
        ):
    _, array2d_xdata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
    _, array2d_kb = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0,1], dtype=int)
    list1d_header, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[2] ] )
    array1d_index_topn = xas_module.def_tm_findmax(
        array1d_xdata = array2d_xdata_tm, 
        array1d_ydata = array2d_ydata, 
        array1d_kb = array2d_kb, 
        float_onset = float_onset, 
        str_abname = list1d_header[0],
        int_ntm = int_ntm,
        float_xwidth = float_xwidth,
        )
    ax.plot(
        array2d_xdata_tm[ array1d_index_topn ], 
        array2d_ydata_tm[ array1d_index_topn ], 
        's',
        markersize=12, 
        markeredgewidth =2,
        mfc='none',
        )

def def_pic_tm_flow(
        list1d_workdir,
        list1d_exp,
        list1d_theory,
        list1d_tm,
        list2d_tm_select,
        list1d_save,
    ):
    
    class_structure = dict_structure[ list1d_workdir[0] ]
    os.chdir( class_structure.str_chdir )
    os.chdir( class_structure.dict_atom[ list1d_workdir[1] ][1] )
    
    str_expfile = list1d_exp[0]
    str_alignfile = list1d_theory[0]
    str_tmalginfile = list1d_tm[0]

    fig,ax = plt.subplots()
    def_plt_exp(
        ax,
        str_datfile = str_exp + str_expfile,
        str_label = r'Exp. 20$\degree$',
        list1d_column = list1d_exp[1]
        )
    def_plt_theory(
        ax,
        str_datfile = str_alignfile,
        list1d_column = list1d_theory[1],
        str_label = list1d_theory[2],
        )
    def_pic_tm(
        ax,
        str_datfile = str_tmalginfile,
        list1d_column = list1d_tm[1],
        str_label = list1d_tm[2],
        )
    for list1d_tm_select in list2d_tm_select:
        def_pic_tm_select(
            ax,
            str_datfile = str_tmalginfile,
            list1d_column = list1d_tm_select[0],
            float_onset = list1d_tm_select[1],
            float_xwidth = list1d_tm_select[2],
            int_ntm = list1d_tm_select[3],
            )
    def_plt_save(
        fig,
        ax,
        str_savefig = list1d_save[0],
        tuple_xlim = list1d_save[1],
        tuple_ylim = list1d_save[2],
        )
    plt.show()

if (''):
    def_pic_tm_flow(
        list1d_workdir = ['111.x4y4_O4', 1],
        list1d_exp = ['20210926.pto111_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,2], 'Theory X_Y'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,4], 'TM X_Y'],
        list2d_tm_select = [
            [[2,4,7], 530.5, 1.0,1],
            [[2,4,8], 530.5, 1.0,1],
            ],
        list1d_save = ['xas_tm.xy.pdf', (527, 540), (0, 4)],
    )
if (''):
    def_pic_tm_flow(
        list1d_workdir = ['111.x4y4_O4', 1],
        list1d_exp = ['20210926.pto111_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,3], 'Theory Z'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,5], 'TM Z'],
        list2d_tm_select = [
            [[2,5,5], 530.5, 1.0,1],
            ],
        list1d_save = ['xas_tm.z.pdf', (527, 540), (0, 4)],
    )
 
if ('t'):
    def_pic_tm_flow(
        list1d_workdir = ['110.x2y12_O22', 11],
        list1d_exp = ['20210924.pto110_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,2], 'Theory O-11 X_Y'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,4], 'TM O-11 X_Y'],
        list2d_tm_select = [
            [[2,4,4], 531.5, 1.0, 5],
            ],
        list1d_save = ['test_tm.xy.pdf', (527, 540), (0, 6.2)],
    )
if (''):
    def_pic_tm_flow(
        list1d_workdir = ['110.x2y12_O22', 11],
        list1d_exp = ['20210924.pto110_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,3], 'Theory O-11 Z'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,5], 'TM O-11 Z'],
        list2d_tm_select = [
            [[2,5,5], 529.5, 1.0, 5],
            ],
        list1d_save = ['test_tm.z.pdf', (527, 540), (0, 6.2)],
    ) 

if (''):
    def_pic_tm_flow(
        list1d_workdir = ['110.x2y12_O22', 11],
        list1d_exp = ['20210924.pto110_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,3], 'Theory O-11 Z'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,5], 'TM O-11 Z'],
        list2d_tm_select = [
            [[2,5,5], 529.5, 1.0, 1],
            ],
        list1d_save = ['xas_tm.z.pdf', (527, 540), (0, 6.2)],
    )
if (''):
    def_pic_tm_flow(
        list1d_workdir = ['110.x2y12_O22', 11],
        list1d_exp = ['20210924.pto110_a20_postscaling.csv', [1,2]],
        list1d_theory = ['xas.a20_b90.align.csv', [0,2], 'Theory O-11 X_Y'],
        list1d_tm = ['xas_tm.a20_b90.align.csv', [2,4], 'TM O-11 X_Y'],
        list2d_tm_select = [
            [[2,4,7], 531, 0.5,1],
            [[2,4,8], 531, 0.5,1],
            ],
        list1d_save = ['xas_tm.xy.pdf', (527, 540), (0, 6.2)],
    ) 


