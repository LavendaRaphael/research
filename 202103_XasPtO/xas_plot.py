#!/bin/env python

import xas_module
import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors

str_exp=os.environ['goto_pto_exp']
str_work_110=os.environ['goto_pto_work_110']
str_work_111=os.environ['goto_pto_work_111']
str_comput_110=os.environ['goto_pto_comput_110']

pic=[]
for int_i in range(100):
    pic.append([False])
pic[1]=[
    False,
    str_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/', 
    'xas_tm'
    ]
pic[2]=[
    False,
    str_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/',
    ]
pic[3]=[
    False,
    str_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/wfn/',
    ]
pic[4]=[
    False,
    str_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/',
    'xas.exp_xy_z.pdf'
    ]
pic[5]=[
    False,
    str_work_111+'Pt.111.x4y4z4_O4_vac15/feff/',
    'xas.real_imag_exp.pdf'
    ]
pic[6]=[
    False,
    str_work_111+'Pt.111.x4y4z4_O4_vac15/vasp_sch/',
    'xas.exp_xy_z.pdf'
    ]
pic[7]=[
    True,
    str_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/',
    'xas.alpha.pdf'
    ]

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)
list_colors = list(mcolors.TABLEAU_COLORS)

list_pictemp = pic[7]
if (list_pictemp[0]):
    #---------------------------------------------[]
    plt.figure(1)
    str_workdir = list_pictemp[1]
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
    plt.plot( array2d_xdata, array2d_ydata+float_plus, label=label, color=list_colors[0] )
    
    str_datfile = str_exp+'20210924.Pt.110.a41.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 41$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a41_b90.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Theory 41$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, label=label, color=list_colors[1] )

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

    str_datfile = str_work_111+'Pt.111.a2b2c4_O1_vac15/feff_kspace/xas.scaling.csv'
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

if (pic[4][0]):
    #---------------------------------------------[]
    plt.figure(4)
    str_workdir = pic[4][1]
    str_savefig = pic[4][2]
    os.chdir( str_workdir )

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

    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label='Theory O-11 Z'
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
    plt.plot( array2d_xdata_tm[ array1d_index_topn ], array2d_ydata_tm[ array1d_index_topn ], 's', mfc='none')
    list1d_header, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[6] )
    array1d_index_topn = xas_module.def_tm_findmax(
        array1d_xdata=array2d_xdata_tm, 
        array1d_ydata=array2d_ydata, 
        array1d_kb=array2d_kb, 
        float_onset=float_onset, 
        str_abname=list1d_header[0]
        )
    plt.plot( array2d_xdata_tm[ array1d_index_topn ], array2d_ydata_tm[ array1d_index_topn ], 's', mfc='none')

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
    plt.plot( array2d_xdata[ array1d_index_topn ], array2d_ydata[ array1d_index_topn ], 's', mfc='none')

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )

    plt.show()
if (pic[0][0]):
    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = xas_module.def_extract( str_datfile='20210924.Pt.110.a20.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 20$\degree$' )

    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = xas_module.def_extract( str_datfile='20210924.Pt.110.a41.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 41$\degree$' )

    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = xas_module.def_extract( str_datfile='xas_exp.xyfit.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 90$\degree$ fit' )

    plt.xlim( 527,540 )
    plt.ylim( bottom=0 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( 'xas_exp.xyfit.pdf',bbox_inches='tight' )
    plt.show()
