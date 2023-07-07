import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import numpy as np
import pandas as pd
import matplotlib.ticker as mticker

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/'

def fig_a(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'CC/0/COLVAR', dir_data+'CC/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (0, 400000): 'tab:blue',
            (0, 0): 'tab:blue',
            (1, 1): 'tab:orange',
            (3, 3): 'tab:green',
            (4, 4): 'tab:grey',
        },
        dict_label = {
            (0, 0): 'TT',
            (1, 1): 'CT',
            (3, 3): 'CC',
            (4, 4): r'HCO$_3^-$',
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_xlim(None, 2300)
    ax.set_ylabel(r'CN(O$_{CA}$H)')
    ax.legend(
        loc = 'lower right',
        frameon = False,
        markerscale = 3,
        labelspacing = 0.3,
    )
def fig_b(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'CC.0/0/COLVAR', dir_data+'CC.0/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (     0, 391700): 'tab:blue'
        },
        dict_label = {
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_ylabel(r'CN(O$_{CA}$H)')

def fig_c(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'CT/0/COLVAR', dir_data+'CT/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (     0,   3500): 'tab:orange',
            (  3500, 400000): 'tab:blue',
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_ylabel(r'CN(O$_{CA}$H)')
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.5))

def fig_d(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'CT.0/0/COLVAR', dir_data+'CT.0/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (     0,   16300): 'tab:orange',
            ( 16300,   79500): 'tab:blue',
            ( 91900,  143800): 'tab:orange',
            (146200,  186000): 'tab:orange',
            (190600,  194000): 'tab:blue',
            (232000,  400000): 'tab:orange',
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_ylabel(r'CN(O$_{CA}$H)')

def fig_e(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'TT/0/COLVAR', dir_data+'TT/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (     0,   4500): 'tab:green',
            (  4500,  62600): 'tab:orange',
            ( 65300,  84500): 'tab:orange',
            ( 87600, 112600): 'tab:orange',
            (117300, 129900): 'tab:orange',
            (138900, 142700): 'tab:green',
            (142700, 227100): 'tab:orange',
            (230400, 400000): 'tab:blue',
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_ylabel(r'CN(O$_{CA}$H)')
def fig_f(ax):

    plm.colvar_plt(
        ax,
        list_data = [dir_data+'TT.0/0/COLVAR', dir_data+'TT.0/1/COLVAR'],
        header = 'cn_o_h',
        dict_color = {
            (     0,   1700): 'tab:green',
            (  1700,  39900): 'tab:orange',
            ( 45200, 156600): 'tab:orange',
            (156600, 400000): 'tab:blue',
        },
        color = 'tab:grey',
        scatters = 1.0,
    )
    ax.set_ylabel(r'CN(O$_{CA}$H)')
    ax.set_xlabel('Time (ps)')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (12*cm, 18*cm))

    gs = fig.add_gridspec(6, 1, left=0.08, right=0.99, bottom=0.05, top=0.99, hspace=0.3)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2])
    ax3 = fig.add_subplot(gs[3])
    ax4 = fig.add_subplot(gs[4])
    ax5 = fig.add_subplot(gs[5])
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)
    fig_d(ax3)
    fig_e(ax4)
    fig_f(ax5)

    plot.save(
        fig,
        file_save = 'timeline_dpmd',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

