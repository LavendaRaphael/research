import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import pandas as pd

def fig_a(
    axs
):

    dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/DPMD/330K/CC/carbonicrdf/'
    dict_title = {
        'o_nyl.h_w': r'$^=$O-H$\mathregular{_W}$',
        'h_oh.o_w': r'H$\mathregular{_{OH}}$-O$\mathregular{_W}$',
    }
    dict2d_data ={
        'CC': {
            'o_nyl.h_w': 'cc.o_nyl.h_w',
            'h_oh.o_w' : 'cc.h_oh.o_w' ,
        },
        'CT': {
            'o_nyl.h_w': 'ct.o_nyl.h_w',
            'h_oh.o_w' : 'ct.h_oh.o_w' ,
        },
        'TT': {
            'o_nyl.h_w': 'tt.o_nyl.h_w',
            'h_oh.o_w' : 'tt.h_oh.o_w' ,
        },
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
        for label, dict_data in dict2d_data.items():
            ax.plot( df.index, df[dict_data[key]], label=label, lw=1)

    axs[0].tick_params(labelbottom=False)
    axs[0].legend(
        frameon = False,
        #handlelength = 1,
        loc = (0.2, 0.5)
    )

    axs[-1].set_xlabel('r (Å)')
    axs[0].set_xlim(1,6)
    axs[0].set_ylim(0,3)

def fig_b(
    ax
):

    ax.axis('off')
    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    axins = plot.inset_img(
        ax,
        dict_img = {
            dir_cp +'33732.png'   : (0., 0.66, 1, 0.31),
            dir_cp +'64961.png'   : (0., 0.33, 1, 0.31),
            dir_cc +'3.171816.png': (0., 0.00, 1, 0.31),
        },
        spinecolor = {
            dir_cp +'33732.png'   : 'tab:blue',
            dir_cp +'64961.png'   : 'tab:orange',
            dir_cc +'3.171816.png': 'tab:green'
        }
    )
    for axin, s in zip(axins, ['CC','CT','TT']):
        axin.text(
            0.05, 0.95,
            s,
            ha = 'left', va='top',
            transform=axin.transAxes
        )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = ((6+2)*cm, 5*cm) )

    gs = fig.add_gridspec(2, 2, width_ratios=[6,2], left=0.1, right=0.99, bottom=0.17, top=0.97, hspace=0.1)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0], sharex=ax0, sharey=ax0)
    fig_a([ax0, ax1])

    ax2 = fig.add_subplot(gs[:, 1])
    fig_b(ax2)

    plot.save(
        fig,
        file_save = 'fig_s3',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

