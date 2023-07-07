import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/06.conformer/330K/beta_5/'

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def fig_a(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '2 ns'  : rdfcsv(dir_data+'sum_hills/dh_o_0_h_fes.1.dat'),
            '4 ns'  : rdfcsv(dir_data+'sum_hills/dh_o_0_h_fes.3.dat'),
            '6 ns'  : rdfcsv(dir_data+'sum_hills/dh_o_0_h_fes.5.dat'),
            '8 ns'  : rdfcsv(dir_data+'sum_hills/dh_o_0_h_fes.7.dat'),
            '10 ns' : rdfcsv(dir_data+'sum_hills/dh_o_0_h_fes.9.dat'),
        },
        bool_maxzero = True,
        bool_minus = True,
        float_lw = 1,
    )
    ax.legend(frameon=False)
    ax.set_xlabel(r'$\alpha$ (rad)')
    ax.set_ylabel('V (kJ/mol)')
    ax.set_xlim(-np.pi, np.pi)

def fig_b(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '2 ns' : rdfcsv(dir_data+'reweight/analysis.1.dhx_o_h_fes.grid'),
            '4 ns' : rdfcsv(dir_data+'reweight/analysis.3.dhx_o_h_fes.grid'),
            '6 ns' : rdfcsv(dir_data+'reweight/analysis.5.dhx_o_h_fes.grid'),
            '8 ns' : rdfcsv(dir_data+'reweight/analysis.7.dhx_o_h_fes.grid'),
            '10 ns': rdfcsv(dir_data+'reweight/dhx_o_h_fes.grid'),
        },
        bool_minzero = True,
        float_lw = 1,
    )
    ax.legend(frameon=False)
    ax.set_ylim(None,40)
    ax.set_xlabel(r"($\alpha$'+$\beta$')/2 (rad)")
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
        file_save = 'fes_converge_conformer',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

