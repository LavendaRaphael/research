import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import pandas as pd

homedir = os.environ['homedir']
str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/01.rmse_trn/'

def fig_a(
    ax
):

    train.dptest_parity_plt(
        ax,
        file_out = str_dir+'dptest.e.out',
        int_natoms = 384,
        float_lw = 0.75,
        energy_sep = True,
        #list_ticks = [-5, 0, 5],
    )

def fig_b(
    ax
):

    train.dptest_parity_plt(
        ax,
        file_out = str_dir+'dptest.f.out',
        float_lw = 0.75,
        #list_ticks = [-5, 0, 5],
    )

def fig_c(
    ax
):

    train.dptest_hist_plt(
        ax,
        file_out = str_dir+'dptest.e.out',
        int_natoms = 384,
        float_lw = 0.75,
    )

def fig_d(
    ax
):

    train.dptest_hist_plt(
        ax,
        file_out = str_dir+'dptest.f.out',
        float_lw = 0.75,
        xlim = (-0.5, 0.5)
    )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, 8*cm) )

    gs = fig.add_gridspec(2, 2, left=0.13, right=0.99, bottom=0.13, top=0.97, wspace=0.35, hspace=0.3)

    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    fig_a(ax0)
    fig_b(ax1)

    ax2 = fig.add_subplot(gs[1,0])
    ax3 = fig.add_subplot(gs[1,1])
    fig_c(ax2)
    fig_d(ax3)

    plot.save(
        fig,
        file_save = 'dft_dp_train',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

