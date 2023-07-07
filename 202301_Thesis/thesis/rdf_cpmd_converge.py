import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import pandas as pd
import matplotlib.ticker as mticker

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/rdf/'

def run(
    ax,
    dict_data,
    pair,
    text,
) -> None:

    plot.plt_compare(
        ax,
        dict_data = dict_data,
        float_lw = 1,
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.2, 0.9): text,
        },
        transform = ax.transAxes
    )

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def get_dict_data(pair):

    return {
        '0-4 ps'  : rdfcsv(dir_data+f'rdf.{pair}.0000000_0008269.csv'),
        '4-12 ps' : rdfcsv(dir_data+f'rdf.{pair}.0008269_0024807.csv'),
        '12-20 ps': rdfcsv(dir_data+f'rdf.{pair}.0024807_0041345.csv'),
        '20-28 ps': rdfcsv(dir_data+f'rdf.{pair}.0041345_0057883.csv'),
    }

def fig_a(ax):

    pair = 'cc_h_oh.o_w'
    run(
        ax,
        dict_data = get_dict_data(pair),
        text = r'H$_{OH}$-O$_W$',
        pair = pair,
    )
    ax.legend(
        frameon = False,
    )
    ax.set_ylabel('g(r)')
    ax.set_xlim(1,6)
    ax.set_ylim(0,4)
    ax.tick_params(labelbottom=False)
    ax.yaxis.set_major_locator(mticker.MultipleLocator(1))

def fig_b(ax):
    pair = 'cc_o_oh.h_w'
    run(
        ax,
        dict_data = get_dict_data(pair),
        text = r'O$_{OH}$-H$_W$',
        pair = pair,
    )
    ax.tick_params(labelbottom=False, labelleft=False)

def fig_c(ax):
    pair = 'cc_o_nyl.h_w'
    run(
        ax,
        dict_data = get_dict_data(pair),
        text = r'$^=$O-H$_W$',
        pair = pair,
    )
    ax.set_xlabel('r (Å)')
    ax.set_ylabel('g(r)')

def fig_d(ax):
    pair = 'o_w.o_w'
    run(
        ax,
        dict_data = get_dict_data(pair),
        text = r'O$_W$-O$_W$',
        pair = pair,
    )
    ax.set_xlabel('r (Å)')
    ax.tick_params(labelleft=False)

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (10*cm, 10*cm))

    gs = fig.add_gridspec(2, 2, left=0.1, right=0.99, bottom=0.1, top=0.97, wspace=0.1, hspace=0.1)

    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1], sharex=ax0, sharey=ax0)
    ax2 = fig.add_subplot(gs[1,0], sharex=ax0, sharey=ax0)
    ax3 = fig.add_subplot(gs[1,1], sharex=ax0, sharey=ax0)
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)
    fig_d(ax3)

    plot.save(
        fig,
        file_save = 'rdf_cpmd_converge',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

