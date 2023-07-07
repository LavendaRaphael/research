import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import pandas as pd
import matplotlib.ticker as mticker

homedir = os.environ['homedir']

def fig_a(
    axs
):

    dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/CPBO/CC/carbonicrdf/'
    dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/DPMD/330K/CC/carbonicrdf/'
    df_dpmd = pd.read_csv(dir_dpmd+'carbonicrdf.csv', index_col='r(ang)')
    df_aimd = pd.read_csv(dir_aimd+'carbonicrdf.csv', index_col='r(ang)')
    dict_title = {
        'o_w.o_w': 'O$\mathregular{_W}$-O$\mathregular{_W}$',
        'h_oh.o_w': r'H$\mathregular{_{OH}}$-O$\mathregular{_W}$',
        'o_nyl.h_w': r'$^=$O-H$\mathregular{_W}$',
        'o_oh.h_w': r'O$\mathregular{_{OH}}$-H$\mathregular{_W}$',
    }
    dict2d_data ={
        'DPMD': {
            'o_w.o_w': [df_dpmd.index, df_dpmd['o_w.o_w']],
            'h_oh.o_w' : [df_dpmd.index, df_dpmd['cc.h_oh.o_w' ]],
            'o_oh.h_w' : [df_dpmd.index, df_dpmd['cc.o_oh.h_w' ]],
            'o_nyl.h_w': [df_dpmd.index, df_dpmd['cc.o_nyl.h_w']],
        },
        'BOMD': {
            'o_w.o_w': [df_aimd.index, df_aimd['o_w.o_w']],
            'h_oh.o_w' : [df_aimd.index, df_aimd['cc.h_oh.o_w' ]],
            'o_oh.h_w' : [df_aimd.index, df_aimd['cc.o_oh.h_w' ]],
            'o_nyl.h_w': [df_aimd.index, df_aimd['cc.o_nyl.h_w']],
        },
    }
    dict_ylim = {
        'o_w.o_w': (0,4),
        'h_oh.o_w': (0,3),
        'o_oh.h_w': (0,2),
        'o_nyl.h_w': (0,2),
    }
    
    for ax, key in zip(axs, dict_title):
        ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
        ax.text(
            x=0.9,
            y=0.9,
            s = dict_title[key],
            horizontalalignment = 'right',
            verticalalignment = 'top',
            transform=ax.transAxes
        )
        ax.set_xlim(1,6)
        ax.set_ylim(dict_ylim[key])
        for label, dict_data in dict2d_data.items():
            data = dict_data[key]
            ax.plot( data[0], data[1], label=label, lw=1)
    axs[0].legend(
        frameon = False,
        handlelength = 0.5,
        loc = 'upper left'
    )
    axs[0].tick_params(labelbottom=False)
    axs[2].tick_params(labelbottom=False)
    axs[0].set_ylabel('g(r)')
    axs[1].set_ylabel('g(r)')
    axs[1].set_xlabel('r (Å)')
    axs[3].set_xlabel('r (Å)')

def fig_c(
    ax,
):
    ax.axis('off')
    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    image = plt.imread(str_dir+'33733.png')
    ax.imshow(image, origin='upper')

    plot.add_text(
        ax,
        dict_text = {
            (572,365)  :r'$\bf{^=}$O',
            (1244,532) :r'H$\bf{\mathregular{_{OH}}}$',
            (1061,992) :r'O$\bf{\mathregular{_{OH}}}$',
        },
        ha = 'center',
        va = 'center',
        fontweight='bold'
    )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8*cm, 5*cm) )
    gs = fig.add_gridspec(2, 2, left=0.1, right=0.99, bottom=0.17, top=0.97, hspace=0.1, wspace=0.2)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0], sharex=ax0)
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, 1], sharex=ax2)
    fig_a([ax0, ax1, ax2, ax3])
    plot.save(
        fig,
        file_save = 'rdf_aimd_dpmd.0',
        list_type = ['pdf', 'svg']
    )

    fig = plt.figure( figsize = (4*cm, 3*cm) )
    gs = fig.add_gridspec(1, 1, left=0.0, right=1, bottom=0., top=1)
    ax4 = fig.add_subplot(gs[0])
    fig_c(ax4)
    plot.save(
        fig,
        file_save = 'rdf_aimd_dpmd.1',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

