import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/05.metad/320K/CC/'

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def fig_a(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '3 ns'  : rdfcsv(dir_data+'sum_hills/dist_vp_o_1_2_fes.2.dat'),
            '6 ns'  : rdfcsv(dir_data+'sum_hills/dist_vp_o_1_2_fes.5.dat'),
            '9 ns'  : rdfcsv(dir_data+'sum_hills/dist_vp_o_1_2_fes.8.dat'),
            '12 ns' : rdfcsv(dir_data+'sum_hills/dist_vp_o_1_2_fes.11.dat'),
            '15 ns' : rdfcsv(dir_data+'sum_hills/dist_vp_o_1_2_fes.14.dat'),
        },
        bool_maxzero = True,
        bool_minus = True,
        float_lw = 1,
    )
    ax.legend(frameon=False)
    ax.set_xlabel('R(V$_P$O$_{CA}$) (Å)')
    ax.set_ylabel('V (kJ/mol)')

def fig_b(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '5 ns'  : rdfcsv(dir_data+'reweight/analysis.4.dist_vp_o_1_2_fes.grid'),
            '10 ns' : rdfcsv(dir_data+'reweight/analysis.9.dist_vp_o_1_2_fes.grid'),
            '15 ns' : rdfcsv(dir_data+'reweight/analysis.14.dist_vp_o_1_2_fes.grid'),
            '20 ns' : rdfcsv(dir_data+'reweight/analysis.19.dist_vp_o_1_2_fes.grid'),
            '25 ns' : rdfcsv(dir_data+'reweight/dist_vp_o_1_2_fes.grid'),
        },
        bool_minzero = True,
        float_lw = 1,
    )
    ax.set_ylim(None,60)
    ax.legend(frameon=False)
    ax.set_xlabel('R(V$_P$O$_{CA}$) (Å)')
    ax.set_ylabel('Free energy (kJ/mol)')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, 8*cm))

    gs = fig.add_gridspec(2, 1, left=0.13, right=0.99, bottom=0.13, top=0.97, wspace=0.35, hspace=0.3)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'fes_converge',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

