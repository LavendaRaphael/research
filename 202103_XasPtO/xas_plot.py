#!/bin/env python
import from_xas_modules
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

pic=[]
for int_i in range(100):
    pic.append('')
pic[1]=[str_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/', 'xas_tm']

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)

if (pic[1]):
    str_workdir = pic[1][0]
    #---------------------------------------------[]
    plt.figure(1)
    str_abname='a90_b45'
    str_savefig = pic[1][1]+'.'+str_abname+'.pdf'
    os.chdir( str_workdir )

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[1] )
    label='Theory O-11 X_Y'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = 'xas_tm.a20_b90.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[2] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[3] )
    label='TM O-11 X_Y'
    plt.plot( array2d_xdata, array2d_ydata, 'o', label=label)

    _, array2d_kb = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0,1], dtype=int)
    float_onset = 531
    array2d_xdata, array2d_ydata, _ = from_xas_modules.def_xas_findtm( array2d_xdata=array2d_xdata, array2d_ydata=array2d_ydata, array2d_kb=array2d_kb, float_onset=float_onset, str_abname=str_abname)
    plt.plot( array2d_xdata, array2d_ydata, 's', mfc='none')

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()
    #---------------------------------------------[]
    plt.figure(2)
    str_abname='a0_b90'
    str_savefig = pic[1][1]+'.'+str_abname+'.pdf'

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[2] )
    label='Theory O-11 Z'
    plt.plot( array2d_xdata, array2d_ydata, label=label )

    str_datfile = 'xas_tm.a20_b90.csv'
    _, array2d_xdata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[2] )
    _, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[4] )
    label='TM O-11 Z'
    plt.plot( array2d_xdata, array2d_ydata, 'o', label=label)

    _, array2d_kb = from_xas_modules.def_xas_extract( str_datfile=str_datfile, list1d_column=[0,1], dtype=int)
    float_onset = 530
    array2d_xdata, array2d_ydata, _ = from_xas_modules.def_xas_findtm( array2d_xdata=array2d_xdata, array2d_ydata=array2d_ydata, array2d_kb=array2d_kb, float_onset=float_onset, str_abname=str_abname)
    plt.plot( array2d_xdata, array2d_ydata, 's', mfc='none')

    plt.xlim( 527,540 )
    plt.ylim( 0,10 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

if (pic[0]):
    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='20210924.Pt.110.a20.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 20$\degree$' )

    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='20210924.Pt.110.a41.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 41$\degree$' )

    str_xheader, list_yheaders, array2d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='xas_exp.xyfit.csv', list1d_column=[1] )
    plt.plot( array2d_xdata, array2d_ydata,label=r'Exp. 90$\degree$ fit' )

    plt.xlim( 527,540 )
    plt.ylim( bottom=0 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( 'xas_exp.xyfit.pdf',bbox_inches='tight' )
    plt.show()
