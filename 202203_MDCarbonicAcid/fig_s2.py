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
    axs
):

    dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/DPMD/330K/CC/carbonicrdf/'
    dict_title = {
        'o_nyl.h_w': r'$^=$O-H$\mathregular{_W}$',
        'o_oh.h_w': r'O$\mathregular{_{OH}}$-H$\mathregular{_W}$',
        'h_oh.o_w': r'H$\mathregular{_{OH}}$-O$\mathregular{_W}$',
    }
    dict2d_data ={
        'CC': {
            'o_nyl.h_w': 'cc.o_nyl.h_w',
            'o_oh.h_w' : 'cc.o_oh.h_w' ,
            'h_oh.o_w' : 'cc.h_oh.o_w' ,
        },
        'CT': {
            'o_nyl.h_w': 'ct.o_nyl.h_w',
            'o_oh.h_w' : 'ct.o_oh.h_w' ,
            'h_oh.o_w' : 'ct.h_oh.o_w' ,
        },
        'TT': {
            'o_nyl.h_w': 'tt.o_nyl.h_w',
            'o_oh.h_w' : 'tt.o_oh.h_w' ,
            'h_oh.o_w' : 'tt.h_oh.o_w' ,
        },
    }
    dict_ylim = {
        'h_oh.o_w': (0,3),
        'o_oh.h_w': (0,2),
        'o_nyl.h_w': (0,2),
    }
    df = pd.read_csv(dir_dpmd+'carbonicrdf.csv', index_col='r(ang)')
    for ax, key in zip(axs, dict_title):
        ax.set_ylabel('g(r)')
        ax.text(
            x=0.9,
            y=0.9,
            s = dict_title[key],
            horizontalalignment = 'right',
            verticalalignment = 'top',
            transform=ax.transAxes
        )
        ax.set_ylim(dict_ylim[key])
        for label, dict_data in dict2d_data.items():
            ax.plot( df.index, df[dict_data[key]], label=label, lw=1)

    axs[0].tick_params(labelbottom=False)
    axs[1].tick_params(labelbottom=False)
    axs[1].legend(
        frameon = False,
        #handlelength = 1,
        loc = 'center left'
    )

    axs[-1].set_xlabel('r (Å)')
    axs[0].set_xlim(1,6)

def fig_label(
    fig,
    axs,
):

    x = -20/72
    y = 0/72
    dict_pos = {
        '(a)': (x, y),
        '(b)': (x, y),
        '(c)': (x, y),
    }

    for ax, label in zip(axs, dict_pos.keys()):
        (x, y) = dict_pos[label]
        # label physical distance to the left and up:
        trans = mtransforms.ScaledTranslation(x, y, fig.dpi_scale_trans)
        ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
                fontsize='medium', va='top')


def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, 9*cm) )

    gs = fig.add_gridspec(3, 1, left=0.1, right=0.99, bottom=0.1, top=0.99, hspace=0.1)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1], sharex=ax0)
    ax2 = fig.add_subplot(gs[2], sharex=ax0)

    fig_a([ax0, ax1, ax2])

    #fig_label(
    #    fig,
    #    axs = [ax0,ax1,ax2,ax3,ax6]
    #)

    plot.save(
        fig,
        file_save = 'fig_s2',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

