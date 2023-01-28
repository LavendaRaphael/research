import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
from XasPtO import local_dict_structure
from XasPtO import local_class_structure

str_exp = os.environ['goto_pto_exp']
str_work_110 = os.path.join( os.environ['dir_pto_shtu'], 'Pt.110_O_vac')
str_work_111 = os.path.join( os.environ['dir_pto_shtu'], 'Pt.111_O_vac')

dict_structure = local_dict_structure.def_dict_structure()

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)
list_color = list(mcolors.TABLEAU_COLORS)

if (''):
    fig, ax = plt.subplots()
    str_workdir = local_class_structure.def_class_structure_basic( dict_structure[ '110.x2y12_O22' ] ).str_chdir
    str_savefig = 'xas.alpha.pdf'
    os.chdir( str_workdir )
    print(os.getcwd())

    float_plus = 2

    str_datfile = os.path.join( str_exp, '20210924.pto110_a20_postscaling.csv')
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label=r'Exp. 20$\degree$'
    ax.plot( array2d_xdata, array2d_ydata+float_plus, 'o', mfc='none', label=label)

    str_datfile = 'xas.alpha.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    label=r'Theory 20$\degree$'
    ax.plot( array2d_xdata, array2d_ydata+float_plus, label=label, color=list1d_color[0] )

    str_datfile = str_exp+'20210924.pto110_a41_postscaling.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[1] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[2] )
    label=r'Exp. 41$\degree$'
    ax.plot( array2d_xdata, array2d_ydata, 'o', mfc='none', label=label)

    str_datfile = 'xas.alpha.csv'
    _, array2d_xdata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[0] )
    _, array2d_ydata = xas_module.def_extract( str_datfile=str_datfile, list1d_column=[4] )
    label=r'Theory 41$\degree$'
    ax.plot( array2d_xdata, array2d_ydata, label=label, color=list1d_color[1] )

    ax.set_xlim( 527,540 )
    #plt.ylim( 0,6 )
    ax.tick_params(
        axis = 'y',
        which = 'both',
        labelleft = False,
        )
    ax.set_xlabel( 'Energy (eV)' )
    ax.set_ylabel( "Intensity (Arb. Units)" )
    ax.legend()
    fig.savefig( str_savefig,bbox_inches='tight' )
    plt.show()

