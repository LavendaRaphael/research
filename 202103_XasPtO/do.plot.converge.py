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

#------------------------------------------------------------
def def_pic_converge(
        str_workdir,
        str_savefig,
        list2d_data, #[
        #    [ str_datfile, str_label, list2d_column ],
        #]
        tuple_xlim=(None,None),
        tuple_ylim=(None,None)
    ):

    os.chdir( str_workdir )
    print(os.getcwd())

    fig, obj_ax = plt.subplots()
    for int_i in range( len( list2d_data ) ):
        list1d_data = list2d_data[ int_i ]
        def_plt_theory(
                obj_ax = obj_ax,
                str_datfile = list1d_data[0],
                list1d_column = list1d_data[2],
                str_label = list1d_data[1]
            )
    def_plt_save(
        fig,
        obj_ax,
        str_savefig + '.pdf',
        tuple_xlim,
        tuple_ylim
    )
    plt.show()

if (''):
    def_pic_converge(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.2013_jpcc_zhutianwei.f2.a20',
        list2d_data = [
            [ dict_structure['110.x2y2_O1_a1b2'].str_chdir+'xas.alpha.csv', 'Theory 0.25 ML',[0,1]],
            [ dict_structure['110.x2y2_O2.14_a1b2'].str_chdir+'xas.alpha.csv', 'Theory 0.5 ML',[0,1]],
            [ dict_structure['110.x2y2_O3_a1b2'].str_chdir+'xas.alpha.csv', 'Theory 0.75 ML',[0,1]],
            [ dict_structure['110.x2y1_O2_a1b3'].str_chdir+'xas.alpha.csv', 'Theory 1.0 ML',[0,1]],
        ],
        tuple_xlim=(527, 540),
        tuple_ylim=(None, 4)
    )
if (''):
    def_pic_converge(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.2013_jpcc_zhutianwei.f5.a20',
        list2d_data = [
            [ dict_structure['110.x1y1.a2b2_O2_a1b2'].str_chdir+'xas.alpha.csv', 'Theory 0.5 ML',[0,1]],
            [ dict_structure['110.x2y1_O2_a1b3'].str_chdir+'xas.alpha.csv', 'Theory 1.0 ML',[0,1]],
        ],
        tuple_xlim=(527, 540),
        tuple_ylim=(None, 4)
    )
if (''):
    def_pic_converge(
        str_workdir = str_exp,
        str_savefig = '20211113_20210924.pto110_a20',
        list2d_data = [
            [ '20210924.pto110_a20_postscaling.csv', r'Exp.0924 20$\degree$', [1,2] ],
            [ '20211113.Angel-Pt110-OXAS.csv', r'Exp.1113 25$\degree$',[0,1] ],
        ],
    )
if (''):
    def_pic_converge(
        str_workdir = str_exp,
        str_savefig = '20210924.pto110_xyzfit',
        list2d_data = [
            [ '20210924.pto110_xyzfit.csv', r'Fit. 0$\degree$', [0,2] ],
            [ '20210924.pto110_a20_postscaling.csv',r'Exp. 20$\degree$',[1,2] ],
            [ '20210924.pto110_a41_postscaling.csv',r'Exp. 41$\degree$',[1,2] ],
            [ '20210924.pto110_xyzfit.csv', r'Fit. 90$\degree$',[0,1] ],
        ],
        tuple_xlim = ( 527,540 ),
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feffk' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test_unfreezef',
        list2d_data = [
            [ 'chwidth0.45/xmu.dat', 'default',3 ],
            [ 'unfreezef/xmu.dat', 'unfreezef',3 ],
        ],
        tuple_xlim = ( 527,540 ),
        tuple_ylim = (0,0.02)
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff_kspace' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test_chbroading',
        list2d_data = [
            [ 'correction0.225/xmu.dat', 'correction 0.225',3 ],
            [ 'chbroading1/xmu.dat', 'chwidth 0.45 + chbroading 1',3 ],
        ],
        tuple_xlim = ( 527,540 ),
        tuple_ylim = (0,0.02)
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff_kspace' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test_correction',
        list2d_data = [
            [ 'correction0.225/xmu.dat', 'correction 0.225',3 ],
            [ 'chwidth0.45/xmu.dat',  'chwidth 0.45', 3 ],
        ],
        tuple_xlim = ( 527,540 ),
        tuple_ylim = (0,0.02)
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff_kspace' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test_exchange',
        list2d_data = [
            [ 'chwidth0.45/xmu.dat',   'chwidth 0.45', 3 ],
            [ 'exchange0.225/xmu.dat',  'exchange 0.225', 3  ],
        ],
        tuple_xlim = ( 527,540 ),
        tuple_ylim = (0,0.02)
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff_kspace' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test_chwidth',
        list2d_data = [
            [ 'chwidth0.0/xmu.dat',   'chwidth 0.0', 3 ],
            [ 'chwidth0.04/xmu.dat',  'chwidth 0.04', 3  ],
        ],
        tuple_xlim = ( 527,540 ),
        tuple_ylim = (0,0.02)
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r20_fms.converge_fms',
        list2d_data = [
            [ 'r20_fms.scf_7/xmu.dat',    'rfms 9', 3  ],
            [ 'r20_fms.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r20_fms.fms_11/xmu.dat',   'rfms 11', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r20_xanes.converge_fms',
        list2d_data = [
            [ 'r20_xanes.scf_7/xmu.dat',    'rfms 9', 3  ],
            [ 'r20_xanes.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r20_xanes.fms_11/xmu.dat',   'rfms 11', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r27.converge_fms.0',
        list2d_data = [
            [ 'r27.scf_7/xmu.dat',    'rfms 9', 3 ],
            [ 'r27.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r27.fms_11/xmu.dat',   'rfms 11', 3 ],
            [ 'r27.fms_12/xmu.dat',   'rfms 12', 3 ],
            [ 'r27.fms_13/xmu.dat',   'rfms 13', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r27.converge_fms.1',
        list2d_data = [
            [ 'r27.fms_14/xmu.dat',   'rfms 14', 3 ],
            [ 'r27.fms_15/xmu.dat',   'rfms 15', 3 ],
            [ 'r27.fms_16/xmu.dat',   'rfms 16', 3 ],
            [ 'r27.fms_17/xmu.dat',   'rfms 17', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )

if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r20.converge_fms',
        list2d_data = [
            [ 'r20.scf_7/xmu.dat',    'rfms 9', 3 ],
            [ 'r20.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r20.fms_11/xmu.dat',   'rfms 11', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )

if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'test',
        list2d_data = [
            [ 'r16.9_fix.scf_7/xmu.dat',    'rfms 9', 3 ],
            [ 'r16.9_fix.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r16.9_fix.fms_11/xmu.dat',   'rfms 11', 3 ],
            [ 'r27.fms_17/xmu.dat',   'rfms 17', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'r16.9_fix.converge_fms',
        list2d_data = [
            [ 'r16.9_fix.scf_7/xmu.dat',    'rfms 9', 3 ],
            [ 'r16.9_fix.fms_10/xmu.dat',   'rfms 10', 3 ],
            [ 'r16.9_fix.fms_11/xmu.dat',   'rfms 11', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '110.x2y1_O2_feffk' ].str_chdir + 'atom_1/',
        str_savefig = 'converge_kspace',
        list2d_data = [
            [ 'kmesh225/xmu.dat',    'KMESH 225', [0,3] ],
            [ 'kmesh400/xmu.dat',    'KMESH 400', [0,3] ],
            [ 'kmesh625/xmu.dat',    'KMESH 625', [0,3] ],
        ],
        tuple_xlim = ( 527,540 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.a2b2_O1_feff_kspace' ].str_chdir + 'atom_1/polarization_z/',
        str_savefig = 'converge_kspace',
        list2d_data = [
            [ 'kmesh10/xmu.dat',    'KMESH 10 10 1', 3 ],
            [ 'xmu.dat',            'KMESH 15 15 1', 3 ],
            [ 'kmesh20/xmu.dat',    'KMESH 20 20 1', 3 ],
        ],
        tuple_xlim = ( 527,540 )
    )

if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.x4y4_O4' ].str_chdir + 'atom_1/',
        str_savefig = 'converge_nbands',
        list2d_data = [
            [ 'xas.csv',           'NBANDS 664', [0,1] ],
            [ 'nbands1000/xas.csv', 'NBANDS 1000', [0,1] ],
        ],
        tuple_xlim = ( 512,525 )
    )
if (''):
    def_pic_converge(
        str_workdir = dict_structure[ '111.x4y4_O4' ].str_chdir + 'atom_1/',
        str_savefig = 'converge_kspace',
        list2d_data = [
            [ 'xas.csv',           'KSPACING 0.25', [0,1] ],
            [ 'kspace0.2/xas.csv', 'KSPACING 0.20', [0,1] ],
        ],
        tuple_xlim = ( 512,525 )
    )

