import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd
import matplotlib.ticker as mticker

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/CC/'

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def fig_a(ax):

    plot.plt_error(
        ax,
        dict_data = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': rdfcsv(dir_data+'hbonds.h_0_1.o_w.ave.temperature.new.nhbonds.csv'),
        },
        bool_error = False,
        dict_ls = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': 'dotted'
        }
    )

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('n(H-bonds)')
    ax.legend(
        frameon = False,
    )
def fig_b(ax):

    plot.plt_error(
        ax,
        dict_data = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': rdfcsv(dir_data+'hbondslength.o_0_2.o_w.OhWaterDistance.ave.csv'),
        },
        bool_error = False,
        dict_ls = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': 'dotted'
        }
    )

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Distance (Å)')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.005))

def fig_c(ax):

    plot.plt_error(
        ax,
        dict_data = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': rdfcsv(dir_data+'hbondslength.o_0_2.o_w.OhWaterAngle.ave.csv'),
        },
        bool_error = False,
        float_scale = 180/np.pi,
        dict_ls = {
            r'O$_{OH}$-H$_{OH}$···O$_W$': 'dotted'
        }
    )

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Angle (°)')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (14*cm, 4*cm))

    gs = fig.add_gridspec(1, 3, left=0.1, right=0.99, bottom=0.2, top=0.97, wspace=0.35)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2])
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'hbonds_temperature',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

