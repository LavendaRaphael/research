#!/bin/env python

import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
from XasPtO import local_dict_structure
from XasPtO import local_class_structure
from tf_xas_kit import io

str_exp = os.environ['dir_pto_exp']
str_work_111 = os.path.join( os.environ['dir_pto_shtu'], 'Pt.111_O_vac')
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
def def_pic_pto111(
        str_workdir,
        str_savefig,
        list2d_data,
        tuple_ylim = (None,4)
    ):

    os.chdir( str_workdir )
    print(os.getcwd())

    list2d_loop = [
        [ '20$\degree$',1 ],
        [ 'z',3 ],
        [ 'x_y',2]
        ]

    for list1d_loop in list2d_loop:
        fig, obj_ax = plt.subplots()

        def_plt_exp(
            obj_ax = obj_ax,
            str_datfile = os.path.join( str_exp, '20210926.pto111_a20_postscaling.csv'),
            str_label=r'Exp. 20$\degree$',
            list1d_column = [1,2]
            )

        for list1d_data in list2d_data:
            def_plt_theory(
                obj_ax = obj_ax,
                str_datfile = list1d_data[0],
                list1d_column = [ 0, list1d_loop[1] ],
                str_label = r'Theory '+list1d_loop[0]+' '+ list1d_data[1]
            )
        def_plt_save(
            fig,
            obj_ax,
            str_savefig +'.'+ str(list1d_loop[1])+'.pdf',
            tuple_xlim = (527,540),
            tuple_ylim = tuple_ylim
        )
    plt.show()

if ('t'):
    def_pic_pto111( 
        str_workdir = os.path.join( str_work_111, 'Pt.111.x4y4_O4_vac'),
        str_savefig = 'vasp_sch.gw', 
        list2d_data = [
            ['vasp_sch/xas.alpha.csv', 'Before'],
            ['vasp_sch.gw/xas.alpha.csv', 'Pot-GW'],
            ['vasp_sch_new.gw/xas.alpha.csv', 'Metal Pot-GW'],
        ],
        tuple_ylim = (None, 5)
    )
if (''):
    def_pic_pto111(
        str_workdir = dict_structure['111.x4y4_O4'].str_chdir,
        str_savefig = 'xas.boradening_1',
        list2d_data = [
            [ 'xas.alpha.csv', 'CH_SIGMA 0.45'],
            [ 'xas.gaussian_sigma0.4.alpha.csv', 'Gaussian Sigma 0.4'],
        ],
        tuple_ylim = (0, 7)
    )
if (''):
    def_pic_pto111(
        str_workdir = dict_structure['111.x4y4_O4'].str_chdir,
        str_savefig = 'xas.boradening',
        list2d_data = [
            [ 'xas.alpha.csv', 'CH_SIGMA 0.45'],
            [ 'xas.gaussian_hwhm0.225.alpha.csv', 'Gaussian FWHM 0.45'],
            [ 'xas.lorentzian_hwhm0.225.alpha.csv', 'Lorentzian FWHM 0.45'],
        ],
        tuple_ylim = (0, 7)
    )
if (''):
    def_pic_pto111( 
        str_workdir = str_work_111+'Pt.111.x4y4_O4_vac/',
        str_savefig = 'vasp_sch.corehole', 
        list2d_data = [
            ['vasp_sch/xas.alpha.csv', '1.0 corehole'],
            ['vasp_sch.hch/xas.alpha.csv', '0.5 corehole'],
        ],
        tuple_ylim = (None, 6)
    )

if (''):
    def_pic_pto111(
        str_workdir = str_work_111,
        str_savefig = 'picture/xas.vasp_feff',
        list2d_data = [
            [ dict_structure['111.x4y4_O4'].str_chdir, 'VASP SCH'],
            [ dict_structure['111.a2b2_O1_feffk'].str_chdir, 'FEFF K-Space'],
        ],
    )
if (''):
    def_pic_pto111(
        str_workdir = dict_structure['111.x4y4_O4'].str_chdir,
        str_savefig = 'xas.exp_theory',
        list2d_data = [
            [ 'xas.alpha.csv', ''],
        ],
    )

