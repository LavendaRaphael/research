import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import pandas as pd

homedir = os.environ['homedir']

def fig_a(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        file_out = str_dir+'dptest.e.out',
        int_natoms = 384,
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
        bool_rmse = True,
        file_log = str_dir+'log'
    )

def fig_b(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        file_out = str_dir+'dptest.f.out',
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
        bool_rmse = True,
        file_log = str_dir+'log'
    )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, 4*cm) )

    gs = fig.add_gridspec(1, 2, left=0.1, right=0.99, bottom=0.2, top=0.99, wspace=0.3)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])

    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'dft_dp',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

