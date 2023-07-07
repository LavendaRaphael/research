import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import numpy as np
import pandas as pd

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'

def fig_a(ax):

    plm.colvar_hist_plt(
        ax,
        file_data = dir_data+'COLVAR',
        header = 'dist_o_0_h',
        timerange = (0,28),
    )
    ax.set_xlabel(r'R(O$_0$H$_0$) (Å)')
    ax.set_xlim((0.9, 1.3))

def fig_b(ax):

    plm.colvar_hist_plt(
        ax,
        file_data = dir_data+'COLVAR',
        header = 'cnx_o_0_h',
        timerange = (0,28),
    )
    ax.set_xlabel(r"cn(O$_0$H$_W$)")
    ax.set_xlim(None, 0.03)

def fig_c(ax):

    plm.colvar_hist_plt(
        ax,
        file_data = dir_data+'COLVAR',
        header = 'dist_vp_o_1_2',
        timerange = (0,28),
    )
    ax.set_xlabel(r'R(V$_p$O$_{CA}$) (Å)')
    ax.set_xlim(1, 1.4)

def fig_d(ax):

    plm.colvar_hist_plt(
        ax,
        file_data = dir_data+'COLVAR',
        header = 'dhx_o_0_h',
        timerange = (0,28),
    )
    ax.set_xlabel(r"α'(O$_2$-C-O$_0$-H$_0$) (rad)")
    ax.set_xlim((None, 3))

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (10*cm, 10*cm))

    gs = fig.add_gridspec(2, 2, left=0.1, right=0.97, bottom=0.1, top=0.97, wspace=0.37, hspace=0.3)

    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    ax2 = fig.add_subplot(gs[1,0])
    ax3 = fig.add_subplot(gs[1,1])
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)
    fig_d(ax3)

    plot.save(
        fig,
        file_save = 'cv_prob_cpmd',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

