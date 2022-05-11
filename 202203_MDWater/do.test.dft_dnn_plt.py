import numpy
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['font.size']=15
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]

# setup
int_natom = 192

# common
array_e = numpy.genfromtxt("dptest.e.out").transpose()
array_e /= int_natom
array_e -= numpy.average( array_e[0] )
array_e *= 1000

array_f = numpy.genfromtxt('dptest.f.out').transpose()
array_f_norm = numpy.zeros( shape = (2, array_f.shape[1]) )
array_f_norm[0] = numpy.linalg.norm( array_f[0:3], axis=0 )
array_f_norm[1] = numpy.linalg.norm( array_f[3:6], axis=0 )
array_f_norm -= numpy.average( array_f_norm[0] )

def def_plt(
        array_data,
        str_efv,
        float_rmse,
        ):
    
    if (str_efv=='e'):
        str_label = f"Energy RMSE = {float_rmse:.2f} meV/atom"
        str_xlabel = 'DFT energy (meV/atom)'
        str_ylabel = 'DNN energy (meV/atom)'
    elif (str_efv=='f'):
        str_label = f"Force RMSE = {float_rmse:.2f} meV/Å"
        str_xlabel = 'DFT force (eV/Å)'
        str_ylabel = 'DNN force (eV/Å)' 
    else:
        raise

    fig, ax = plt.subplots()

    ax.plot(
        array_data[0],
        array_data[1],
        label = str_label,
        marker='o',
        linestyle = '',
        markersize=2,
        )

    ax.axline([0, 0], [1, 1], color='black', linestyle='--')

    ax.legend()
    ax.set_xlabel(str_xlabel)
    ax.set_ylabel(str_ylabel)
    #fig.set_size_inches(4, 4)
    plt.savefig('dptest.'+str_efv+'.pdf', bbox_inches='tight')
    plt.show()

def_plt(
    array_data = array_e,
    str_efv = 'e',
    float_rmse = 0.6552798,
    )
def_plt(
    array_data = array_f_norm,
    str_efv = 'f',
    float_rmse = 64.24218,
    )
