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

def def_plt_exp(
        obj_ax,
        str_datfile,
        str_label,
        ):
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
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

def def_pic_20degree(
        str_workdir,
        str_savefig,
        list2d_data, #[
        #    [ str_datfile, str_label ],
        #]
        str_expfile,    
    ):
    # exp, theory0, theory1
    # 20, x_y, z

    os.chdir( str_workdir )
    print(os.getcwd())

    list1d_column=[1,2,3]
    list1d_label=[ '20$\degree$', 'x_y', 'z' ]

    for int_i in range(len(list1d_column)):
        fig, obj_ax = plt.subplots()

        def_plt_exp(
            obj_ax = obj_ax,
            str_datfile = str_exp+str_expfile,
            str_label=r'Exp. 20$\degree$'
        )

        for int_j in range(len(list2d_data)):
            list1d_data = list2d_data[ int_j ]
            def_plt_theory(
                obj_ax = obj_ax,
                str_datfile = list1d_data[0]+'xas.a20_b90.csv',
                list1d_column = [ 0, list1d_column[int_i] ],
                str_label = r'Theory '+list1d_label[int_i]+' '+ list1d_data[1]
            )
        def_plt_save(
            fig,
            obj_ax,
            str_savefig +'.'+ str(list1d_column[int_i])+'.pdf',
            tuple_xlim = (527,540),
            tuple_ylim = (None,6)
        )
    plt.show()

if (''):
    def_pic_20degree(
        str_workdir = dict_structure['111.x4y4_O4'].str_chdir,
        str_savefig = 'xas.exp_theory',
        list2d_data = [
            [ '', ''],
        ],
        str_expfile = '20210926.Pt.111.a20.csv',
    )

if (''):
    def_pic_20degree(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.2013_jpcc_zhutianwei.f2',
        list2d_data = [
            [ dict_structure['110.x2y4_O2.15'].str_chdir, 'a'],
            [ dict_structure['110.x2y4_O4.1458'].str_chdir, 'b'],
            [ dict_structure['110.x2y1.a1b2_O3_a1b2'].str_chdir, 'c'],
            [ dict_structure['110.x2y3_O6'].str_chdir, 'd'],
        ],
        str_expfile = '20210924.Pt.110.a20.csv',
    )

if (''):
    def_pic_20degree(
        str_workdir = str_work_111,
        str_savefig = 'picture/xas.vasp_feff',
        list2d_data = [
            [ dict_structure['111.x4y4_O4'].str_chdir, 'VASP'],
            [ dict_structure['111.a2b2c4_O1_feff_kspace'].str_chdir, 'FEFF kspace'],
        ],
        str_expfile = '20210926.Pt.111.a20.csv',
    )

if (''):
    def_pic_20degree(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.2013_jpcc_zhutianwei.f5',
        list2d_data = [
            [ dict_structure['110.x1y1.a2b4_O4'].str_chdir, 'a'],
            [ dict_structure['110.x2y3_O6'].str_chdir, 'b'],
        ],
        str_expfile = '20210924.Pt.110.a20.csv',
    )

if (''):
    def_pic_20degree(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.correlation_xy',
        list2d_data = [
            [ dict_structure['110.x2y3_O1'].str_chdir,    'a'],
            [ dict_structure['110.x2y3_O2.14'].str_chdir, 'b'],
            [ dict_structure['110.x2y4_O2.16'].str_chdir, 'c'],
            [ dict_structure['110.x2y6_O2.18'].str_chdir, 'd'],
        ],
        str_expfile = '20210924.Pt.110.a20.csv',
    )

if (''):
    def_pic_20degree(
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.correlation_y',
        list2d_data = [
            [ dict_structure['110.x2y3_O1'].str_chdir,    'a'],
            [ dict_structure['110.x2y3_O2.13'].str_chdir, 'b'],
            [ dict_structure['110.x2y4_O2.15'].str_chdir, 'c'],
            [ dict_structure['110.x2y6_O2.17'].str_chdir, 'd'],
        ],
        str_expfile = '20210924.Pt.110.a20.csv',
    )

if (''):
    def_pic_20degree( 
        str_workdir = str_work_111+'Pt.111.x4y4_O4_vac/', 
        str_savefig = 'vasp_sch.corehole', 
        list2d_data = [
            ['vasp_sch/', 'FCH'],
            ['vasp_sch.hch/', 'HCH'],
        ],
        str_expfile = '20210926.Pt.111.a20.csv',
    )
if (''):
    def_pic_20degree( 
        str_workdir = str_work_110,
        str_savefig = 'neighbor/xas.useless',
        list2d_data = [
            ['Pt.110.x2y3_O3.136_vac/vasp_sch/', 'a'],
            ['Pt.110.x2y3_O5_vac/vasp_sch/', 'b'],
        ],
        str_expfile = '20210924.Pt.110.a20.csv',
    )

def def_pic_converge(
        str_workdir,
        str_savefig,
        list2d_data, #[
        #    [ str_datfile, str_label, int_column ],
        #]
        tuple_xlim,
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
                list1d_column = [ 0, list1d_data[2] ],
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
if ('t'):
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
        str_savefig = 'converge_kspace',
        list2d_data = [
            [ 'xas.csv',           'kspace 0.25', 3 ],
            [ 'kspace0.2/xas.csv', 'kspace 0.20', 3 ],
        ],
        tuple_xlim = ( 512,525 )
    )

'''
pic=[]
for int_i in range(100):
    pic.append([False])

pic[0]=[
    '',
    str_exp,
    [
        [
            '20211113.xyzfit',
            '20211113.xyzfit.csv',
            ['25', '50']
        ],
        [
            '20211113.xyzfit_m5',
            '20211113.xyzfit_m5.csv',
            ['20', '45']
        ],
        [
            '20211113.xyzfit_p5',
            '20211113.xyzfit_p5.csv',
            ['30', '55']
        ],
    ]
]
pic[1]=[
    '',
    dict_structure[ '110.x2y12_O22' ].str_chdir+'atom_11/', 
    'xas_tm'
]
pic[2]=[
    '',
    dict_structure[ '110.x2y12_O22' ].str_chdir+'atom_11/',
]
pic[3]=[
    '',
    dict_structure[ '110.x2y12_O22' ].str_chdir+'atom_11/wfn/',
]
pic[4]=[
    '',
    [
        dict_structure[ '110.x2y12_O22' ].str_chdir+'atom_11/',
        dict_structure[ '110.x2y12_O22' ].str_chdir,
        dict_structure[ '110.x2y12_O22_aimd' ].str_chdir,
    ],
    'xas.exp_xy_z.pdf'
]
pic[5]=[
    '',
    str_work_111+'Pt.111.x4y4_O4_vac/feff/',
    'xas.real_imag_exp.pdf'
]
pic[6]=[
    '',
    dict_structure['111.x4y4_O4'].str_chdir,
    'xas.exp_xy_z.pdf'
]
pic[7]=[
    '',
    [
        dict_structure[ '110.x2y12_O22' ].str_chdir,
        dict_structure[ '110.x2y12_O22_aimd' ].str_chdir,
    ],
    'xas.alpha.pdf'
]
pic[8]=[
    '',
    str_work_110+'neighbor/',
    [
        [   
            'xas.correlation_2column.',
            [   
                dict_structure[ '110.x2y3_O1' ].str_chdir,
                dict_structure[ '110.x4y3_O2.12' ].str_chdir,
            ]
        ],
        [   
            'xas.correlation_2column_1.',
            [   
                dict_structure[ '110.x2y3_O6'].str_chdir,
                dict_structure[ '110.x4y3_O6'].str_chdir
            ],
        ],
        [   
            'xas.correlation_y.',
            [   
                dict_structure[ '110.x2y3_O1' ].str_chdir,
                dict_structure[ '110.x2y3_O2.13' ].str_chdir,
                dict_structure[ '110.x2y4_O2.15' ].str_chdir,
            ]
        ],
        [
            'xas.correlation_xy.',
            [
                dict_structure[ '110.x2y3_O1' ].str_chdir,
                dict_structure[ '110.x2y3_O2.14' ].str_chdir,
                dict_structure[ '110.x2y4_O2.16' ].str_chdir,
            ]
        ],
        [
            'xas.neighbor_x.',
            [
                dict_structure[ '110.x2y3_O1' ].str_chdir,
                dict_structure[ '110.x2y3_O2.12' ].str_chdir
            ]
        ],
        [
            'xas.neighbor_y.',
            [
                dict_structure[ '110.x2y3_O1'].str_chdir ,
                dict_structure[ '110.x2y3_O2.13'].str_chdir ,
                dict_structure[ '110.x2y4_O3.137'].str_chdir,
                dict_structure[ '110.x2y3_O3.135'].str_chdir,
            ],
        ],
        [
            'xas.neighbor_xy.',
            [
                dict_structure[ '110.x2y3_O1'].str_chdir,
                dict_structure[ '110.x2y3_O2.14'].str_chdir,
                dict_structure[ '110.x2y4_O3.148'].str_chdir,
                dict_structure[ '110.x2y4_O4.1458'].str_chdir,
            ],
        ],
        [
            'xas.neighbor_mix.',
            [
                dict_structure[ '110.x2y3_O1'].str_chdir,
                dict_structure[ '110.x2y3_O3.123'].str_chdir,
                dict_structure[ '110.x2y4_O4.1237'].str_chdir,
            ],
        ],
        [
            'xas.neighbor_mix_1.',
            [
                dict_structure[ '110.x2y3_O4.v56'].str_chdir,
                dict_structure[ '110.x2y4_O6.v56'].str_chdir,
                dict_structure[ '110.x2y3_O6'].str_chdir,
            ],
        ],
        [
            'xas.coverage.',
            [
                dict_structure[ '110.x2y3_O1'].str_chdir,
                dict_structure[ '110.x2y4_O4.1458'].str_chdir,
                dict_structure[ '110.x2y3_O6'].str_chdir
            ]
        ],
        [
            'xas.distribution.',
            [
                dict_structure[ '110.x2y3_O2.12'].str_chdir,
                dict_structure[ '110.x2y3_O3.135'].str_chdir,
                dict_structure[ '110.x2y4_O4.1458'].str_chdir
            ]
        ],
    ]
]
pic[9]=[
    '',
    [
        str_work_111+'Pt.111.a2b2c4_O1_vac/feff/atom_1/polarization_z/',
        str_work_111+'Pt.111.a2b2c8_O1_vac/feff/atom_1/polarization_z/',
    ],
    [
        [
            'test_scf',
            [
                'scf_7/',
                'scf_8/',
            ],
            [
                'SCF 7.0',
                'SCF 8.0',
            ],
        ],
        [
            'test_fms',
            [
                'scf_7/',
                'fms_10/',
                'fms_11/',
                #'fms_12/',
                #'fms_13/',
            ],
            [
                'FMS 9.0',
                'FMS 10.0',
                'FMS 11.0',
                #'FMS 12.0',
                #'FMS 13.0',
            ],
        ],
    ]
]

list_pictemp = pic[9]
if (list_pictemp[0]):
    str_workdir = list_pictemp[1][1]
    list1d_out = list_pictemp[2][1]

    str_savefig = list1d_out[0] +'.pdf'
    list1d_datdir = list1d_out[1]
    list1d_title = list1d_out[2]

    os.chdir( str_workdir )
    print(os.getcwd())

    for int_j in range(len(list1d_datdir)):
        str_datfile = list1d_datdir[ int_j ]+'xmu.dat'
        _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
        _, array2d_ydata = xas_module.def_extract(
            str_datfile=str_datfile,
            list1d_column=[ 3 ]
        )
        plt.plot( 
            array2d_xdata, array2d_ydata, 
            label = list1d_title[ int_j ]
        )
    plt.xlim( 527,540 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig, bbox_inches='tight' )
    plt.show()

list_pictemp = pic[8]
if (list_pictemp[0]):
    #---------------------------------------------[]
    str_workdir = list_pictemp[1]
    list1d_out = list_pictemp[2][2]

    os.chdir( str_workdir )
    print(os.getcwd())

    str_outfile = list1d_out[0]
    list1d_datdir = list1d_out[1]

    list1d_abc = ['a','b','c','d','e','f']

    list1d_column=[1,2,3]
    list1d_label=[ '20$\degree$', 'x_y', 'z' ]

    for int_i in range(len(list1d_column)):
        plt.figure( int_i )
        
        str_datfile = str_exp+'20210924.Pt.110.a20.csv'
        _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
        _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
        label=r'Exp. 20$\degree$'
        plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

        for int_j in range(len(list1d_datdir)):
            str_datdir = list1d_datdir[ int_j ]
            str_datfile = str_datdir+'xas.a20_b90.csv'
            _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
            list1d_yheader, array2d_ydata = xas_module.def_extract( 
                str_datfile=str_datfile, 
                list1d_column=[ list1d_column[int_i] ] 
            )
            #label=r'Theory '+ list1d_label[int_i] +' '+list1d_abc[int_j]
            label=r'Theory '+ list1d_label[int_i] +' '+ list1d_abc[int_j]
            plt.plot( array2d_xdata, array2d_ydata, label=label )
        str_savefig = str_outfile + list1d_yheader[0] +'.pdf'
        plt.xlim( 527,540 )
        plt.ylim( 0,6 )
        plt.xlabel( 'Energy (eV)' )
        plt.ylabel( "Intensity (Arb. Units)" )
        plt.legend()
        plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

list_pictemp = pic[7]
if (list_pictemp[0]):
    #---------------------------------------------[]
    plt.figure(1)
    str_workdir = list_pictemp[1][1]
    str_savefig = list_pictemp[2]
    os.chdir( str_workdir )
    print(os.getcwd())

    float_plus = 3

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata+float_plus, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Theory 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata+float_plus, label=label, color=list1d_color[0] )
    
    str_datfile = str_exp+'20210924.Pt.110.a41.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 41$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[4] )
    label=r'Theory 41$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, label=label, color=list1d_color[1] )

    plt.xlim( 527,540 )
    #plt.ylim( 0,6 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

list_pictemp = pic[6]
if (list_pictemp[0]):
    #---------------------------------------------[]
    plt.figure(1)
    str_workdir = list_pictemp[1]
    str_savefig = list_pictemp[2]
    os.chdir( str_workdir )
    print(os.getcwd())

    str_datfile = str_exp+'20210926.Pt.111.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Theory 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label='Theory X_Y'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[3] )
    label='Theory Z'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    plt.xlim( 527,540 )
    plt.ylim( 0,6 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

list_pictemp = pic[5]
if (list_pictemp[0]):
    #---------------------------------------------[]
    plt.figure(1)
    str_workdir = list_pictemp[1]
    str_savefig = list_pictemp[2]
    os.chdir( str_workdir )
    print(os.getcwd())

    str_datfile = str_exp+'20210926.Pt.111.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.scaling.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label='FEFF realspace'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = str_work_111+'Pt.111.a2b2c4_O1_vac/feff_kspace/xas.scaling.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label='FEFF kspace'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    plt.xlim( 527,540 )
    plt.ylim( 0,5 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

list_pictemp = pic[4]
if (list_pictemp[0]):
    #---------------------------------------------[]
    plt.figure(1)
    str_workdir = list_pictemp[1][2]
    str_savefig = list_pictemp[2]
    os.chdir( str_workdir )

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label='Theory x_y'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[3] )
    label='Theory z'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

if (pic[3][0]):
    str_datdir = pic[3][1]
    os.chdir( str_datdir )
    print(os.getcwd())

    list2d_fig = []
    list2d_fig.append( ['wfn.chgrpd', 1, 'Charge radical probability distribution (e/\u00C5)'] )
    list2d_fig.append( ['wfn.chgrpi', 2, 'Charge radical probability integral (e)'] )
    list2d_fig.append( ['wfn.chgrdf', 3, 'Charge radical density funtion (e/\u00C5$^3$)'] )
    #---------------------------------------------[]
    for i in range( len(list2d_fig) ):
        plt.figure(i)
        str_savefig = list2d_fig[i][0] +'.pdf'
        list1d_column = [ list2d_fig[i][1] ]
        str_ylabel = list2d_fig[i][2]

        str_datfile = 'chgrdf.B1102_K0001.csv'
        _, array2d_xdata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = [0]
            )
        _, array2d_ydata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = list1d_column
            )
        label=r'Peak-1 (B-1102 K-1)'
        mask = (array2d_xdata >= 0) & (array2d_xdata <= 2)
        plt.plot( array2d_xdata[mask], array2d_ydata[mask], label=label )

        str_datfile = 'chgrdf.B1192_K0002.csv'
        _, array2d_xdata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = [0]
            )
        _, array2d_ydata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = list1d_column
            )
        label=r'Peak-2 (B-1192 K-2)'
        mask = (array2d_xdata >= 0) & (array2d_xdata <= 2)
        plt.plot( array2d_xdata[mask], array2d_ydata[mask], label=label )

        plt.xlim( 0,2 )
        plt.ylim( 0 )
        plt.xlabel( 'r (\u00C5)' )
        plt.ylabel( str_ylabel )
        plt.legend()
        plt.savefig( str_savefig, bbox_inches='tight' )
    
    plt.show()

if (pic[2][0]):
    str_datdir = pic[2][1]
    os.chdir( str_datdir )

    list2d_fig = []
    list2d_fig.append( ['parchg.chgrpd', 1, 'Charge radical probability distribution (e/\u00C5)'] )
    list2d_fig.append( ['parchg.chgrpi', 2, 'Charge radical probability integral (e)'] )
    list2d_fig.append( ['parchg.chgrdf', 3, 'Charge radical density funtion (e/\u00C5$^3$)'] )
    #---------------------------------------------[]
    for i in range( len(list2d_fig) ):
        plt.figure(i)
        str_savefig = list2d_fig[i][0] +'.pdf'
        list1d_column = [ list2d_fig[i][1] ]
        str_ylabel = list2d_fig[i][2]

        str_datfile = 'parchg.a0_b90/chgrdf.csv'
        _, array2d_xdata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = [0]
            )
        _, array2d_ydata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = list1d_column
            )
        label=r'Peak-1 (529.15 ~ 530.15)'
        mask = (array2d_xdata >= 0) & (array2d_xdata <= 2)
        plt.plot( array2d_xdata[mask], array2d_ydata[mask], label=label )

        str_datfile = 'parchg.a90_b45/chgrdf.csv'
        _, array2d_xdata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = [0]
            )
        _, array2d_ydata = xas_module.def_extract(
            str_datfile = str_datfile,
            list1d_column = list1d_column
            )
        label=r'Peak-2 (530.97 ~ 531.97)'
        mask = (array2d_xdata >= 0) & (array2d_xdata <= 2)
        plt.plot( array2d_xdata[mask], array2d_ydata[mask], label=label )

        plt.xlim( 0,2 )
        plt.ylim( 0 )
        plt.xlabel( 'r (\u00C5)' )
        plt.ylabel( str_ylabel )
        plt.legend()
        plt.savefig( str_savefig, bbox_inches='tight' )
    
    plt.show()

if (pic[1][0]):
    str_workdir = pic[1][1]
    #---------------------------------------------[]
    plt.figure(1)
    os.chdir( str_workdir )
    float_makersize=12
    float_linewidth=2

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label='Theory O-11 X_Y'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = 'xas_tm.a20_b90.csv'
    _, array2d_xdata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    list1d_header, array2d_ydata_tm = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[3] )
    label='TM O-11 X_Y'
    plt.plot( array2d_xdata_tm, array2d_ydata_tm, 'o', label=label)
    str_savefig = pic[1][2]+'.'+list1d_header[0]+'.pdf'

    float_onset = 531
    _, array2d_kb = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0,1], dtype=int)
    list1d_header, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[5] )
    array1d_index_topn = xas_module.def_tm_findmax(
        array1d_xdata = array2d_xdata_tm, 
        array1d_ydata = array2d_ydata, 
        array1d_kb = array2d_kb, 
        float_onset = float_onset, 
        str_abname = list1d_header[0]
        )
    plt.plot( 
        array2d_xdata_tm[ array1d_index_topn ], 
        array2d_ydata_tm[ array1d_index_topn ], 
        's', 
        markersize=float_makersize, 
        markeredgewidth =float_linewidth,
        mfc='none')
    list1d_header, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[6] )
    array1d_index_topn = xas_module.def_tm_findmax(
        array1d_xdata=array2d_xdata_tm, 
        array1d_ydata=array2d_ydata, 
        array1d_kb=array2d_kb, 
        float_onset=float_onset, 
        str_abname=list1d_header[0]
        )
    plt.plot( 
        array2d_xdata_tm[ array1d_index_topn ], 
        array2d_ydata_tm[ array1d_index_topn ], 
        's', 
        markersize=float_makersize,
        markeredgewidth =float_linewidth,
        mfc='none'
        )

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig, bbox_inches='tight' )
    #---------------------------------------------[]
    plt.figure(2)

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label='Theory O-11 Z'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = 'xas_tm.a20_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    list1d_header, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[4] )
    label='TM O-11 Z'
    plt.plot( array2d_xdata, array2d_ydata, 'o', label=label)
    str_savefig = pic[1][2]+'.'+list1d_header[0]+'.pdf'

    _, array2d_kb = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0,1], dtype=int)
    float_onset = 530
    array1d_index_topn = xas_module.def_tm_findmax( 
        array1d_xdata=array2d_xdata, 
        array1d_ydata=array2d_ydata, 
        array1d_kb=array2d_kb, 
        float_onset=float_onset, 
        str_abname=list1d_header[0]
        )
    plt.plot( 
        array2d_xdata[ array1d_index_topn ], 
        array2d_ydata[ array1d_index_topn ], 
        's', 
        markersize=float_makersize,
        markeredgewidth =float_linewidth,
        mfc='none'
        )

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )

    plt.show()

list_pictemp = pic[0]
if (list_pictemp[0]):
    str_chdir = list_pictemp[1]
    list1d_para  = list_pictemp[2][1]

    str_savefig = list1d_para[0]
    os.chdir(str_chdir)

    list1d_degree = list1d_para[2]
    str_datfile = '20211113.Angel-Pt110-OXAS.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile, [0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile, [1] )
    plt.plot( array2d_xdata, array2d_ydata, label=r'Exp. '+list1d_degree[0]+'$\degree$' )

    _, array2d_xdata = xas_module.def_extract( str_datfile, [0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile, [6] )
    plt.plot( array2d_xdata, array2d_ydata, label=r'Exp. '+list1d_degree[1]+'$\degree$' )

    str_datfile = list1d_para[1]
    _, array2d_xdata = xas_module.def_extract( str_datfile, [0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile, [1] )
    plt.plot( array2d_xdata, array2d_ydata, label=r'Exp. 90$\degree$ fit' )

    _, array2d_xdata = xas_module.def_extract( str_datfile, [0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile, [2] )
    plt.plot( array2d_xdata, array2d_ydata, label=r'Exp. 0$\degree$ fit' )

    plt.xlim( 527,540 )
    #plt.ylim( bottom=0 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig+'.pdf',bbox_inches='tight' )
    plt.show()
'''
