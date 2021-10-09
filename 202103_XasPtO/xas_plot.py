#!/bin/env python
import from_xas_modules
import os
import matplotlib.pyplot as plt
import matplotlib

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

pic=[]
for int_i in range(100):
    pic.append('')
pic[1]=[str_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11/', 'xas.tm.pdf']

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)


if (pic[1]):
    str_workdir = pic[1][0]
    str_savefig = pic[1][1]
    os.chdir( str_workdir )

    str_datfile = str_exp+'20210924.Pt.110.a20.csv'
    _, _, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )
    label=r'Exp. 20$\degree$'
    plt.plot( array1d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.a20_b90.csv'
    _, _, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )
    label='Theory O-11 X_Y'
    plt.plot( array1d_xdata, array2d_ydata, label=label )

    list2d_kb=['',]
    list2d_kb.append([1200])
    list2d_kb.append([10])
    list2d_kb.append([500])

    for int_k in range(1):
        int_k += 1
        str_datfile = 'xas_tm.a20_b90.K'+str(int_k)+'.csv'
        _, _, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )
        array2d_ydata *= 5
        label='TM O-11 X_Y'+str(int_k)
        plt.plot( array1d_xdata, array2d_ydata, 'o', label=label)
        list1d_kb = list2d_kb[int_k]
        print( array1d_xdata[list1d_kb], array2d_ydata[list1d_kb] )
        plt.plot( array1d_xdata[list1d_kb], array2d_ydata[list1d_kb], 's', mfc='none', label=label)

    plt.xlim( 527,540 )
    plt.ylim( bottom=0 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

if (pic[0]):
    str_xheader, list_yheaders, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='20210924.Pt.110.a20.csv', int_xcolumn=0, list1d_ycolumn=[1] )
    plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 20$\degree$' )

    str_xheader, list_yheaders, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='20210924.Pt.110.a41.csv', int_xcolumn=0, list1d_ycolumn=[1] )
    plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 41$\degree$' )

    str_xheader, list_yheaders, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile='xas_exp.xyfit.csv', int_xcolumn=0, list1d_ycolumn=[1] )
    plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 90$\degree$ fit' )

    plt.xlim( 527,540 )
    plt.ylim( bottom=0 )
    plt.xlabel( 'Energy (eV)' )
    plt.ylabel( "Intensity (Arb. Units)" )
    plt.legend()
    plt.savefig( 'xas_exp.xyfit.pdf',bbox_inches='tight' )
    plt.show()
