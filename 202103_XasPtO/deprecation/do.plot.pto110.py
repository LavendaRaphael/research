#!/bin/env python
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
from XasPtO import local_dict_structure
from XasPtO import local_class_structure
from tf_xas_kit import io

str_exp = os.environ['dir_pto_exp']
str_work_110 = os.path.join( os.environ['dir_pto_shtu'], 'Pt.110_O_vac')
dict_structure = local_dict_structure.def_dict_structure()

matplotlib.rcParams['font.size']=20
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)

#---------------------------------------------------------------------------------------------
def def_plt_exp(
        obj_ax,
        str_datfile,
        str_label,
        list1d_column = [0,1]
        ):
    _, array2d_xdata = io.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata = io.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
    obj_ax.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=str_label )
    return obj_ax

def def_plt_theory(
        obj_ax,
        str_datfile,
        str_label,
        list1d_column,
        ):
    _, array2d_xdata = io.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[0] ] )
    _, array2d_ydata = io.def_extract( str_datfile=str_datfile, list1d_column=[ list1d_column[1] ] )
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

#------------------------------------------------------------
def def_pic_pto110(
        str_workdir,
        str_savefig,
        list2d_data, 
    ):

    os.chdir( str_workdir )
    print(os.getcwd())

    fig, obj_ax = plt.subplots()
    def_plt_exp(
        obj_ax = obj_ax,
        str_datfile = os.path.join( str_exp, '20210924.pto110_a20_postscaling.csv'),
        str_label=r'Exp. 20$\degree$',
        list1d_column = [ 1, 2]
    )
    for list1d_data in list2d_data:
        def_plt_theory(
            obj_ax = obj_ax,
            str_datfile = os.path.join( list1d_data[0], 'xas.alpha.csv'),
            list1d_column = [ 0, 1 ],
            str_label = r'Theory 20$\degree$ '+ list1d_data[1]
        )
    def_plt_save(
        fig,
        obj_ax,
        str_savefig +'.a20.pdf',
        tuple_xlim = (527,540),
        tuple_ylim = (None,5)
    )

    list2d_loop = [
        [ 'z',[0,2],[0,3] ,'out-of-plane'],
        [ 'x_y',[0,1],[0,2], 'in-plane']
        ]

    for list1d_loop in list2d_loop:
        fig, obj_ax = plt.subplots()
        def_plt_exp(
            obj_ax = obj_ax,
            str_datfile = os.path.join(str_exp,'20210924.pto110_xyzfit.csv'),
            str_label=r'Exp. fit '+list1d_loop[3],
            list1d_column = list1d_loop[1]
        )
        for list1d_data in list2d_data:
            def_plt_theory(
                obj_ax = obj_ax,
                str_datfile = os.path.join(list1d_data[0],'xas.alpha.csv'),
                list1d_column = list1d_loop[2],
                str_label = r'Theory '+list1d_loop[3]+' '+ list1d_data[1]
            )
        def_plt_save(
            fig,
            obj_ax,
            str_savefig +'.'+list1d_loop[0]+'.pdf',
            tuple_xlim = (527,540),
            tuple_ylim = (None,5)
        )

    plt.show()

if ('t'):
    def_pic_pto110(
        str_workdir = os.path.join( str_work_110, 'Pt.110.x2y12_O22_vac'),
        str_savefig = 'vasp_sch.gw',
        list2d_data = [
            ['vasp_sch/', 'Before'],
            ['vasp_sch_new.gw/', 'Metal Pot-GW'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.neighbor_mix_1',
        list2d_data = [
            [ dict_structure['110.x2y3_O4.v56'].str_chdir,'a'],
            [ dict_structure['110.x2y4_O6.v56'].str_chdir,'b'],
            [ dict_structure['110.x2y1_O2_a1b3'].str_chdir, 'c'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.neighbor_xy',
        list2d_data = [
            [ dict_structure['110.x2y3_O2.14'].str_chdir, 'a'],
            [ dict_structure['110.x2y4_O3.148'].str_chdir,'b'],
            [ dict_structure['110.x2y2_O2.14_a1b2'].str_chdir,'c'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.neighbor_y',
        list2d_data = [
            [ dict_structure['110.x2y3_O2.13'].str_chdir, 'a'],
            [ dict_structure['110.x2y4_O3.137'].str_chdir,'b'],
            [ dict_structure['110.x2y1_O1_a1b3'].str_chdir,'c'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.neighbor_x',
        list2d_data = [
            [ dict_structure['110.x2y3_O1'].str_chdir, 'a'],
            [ dict_structure['110.x2y3_O2.12'].str_chdir,'b'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.vasp_feff',
        list2d_data = [
            [ dict_structure['110.x2y1_O2_a1b3'].str_chdir, 'VASP SCH'],
            [ dict_structure['110.x2y1_O2_feffk'].str_chdir,'FEFF Kspace'],
        ],
    )
if (''):
    def_pic_pto110(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.mixture',
        list2d_data = [
            [ dict_structure['110.x2y1_O1_a1b3'].str_chdir, 'a'],
            [ dict_structure['110.x2y2_O2.14_a1b2'].str_chdir, 'b'],
            [ dict_structure['110.x2y1_O2_a1b3'].str_chdir,'c'],
        ],
    )
