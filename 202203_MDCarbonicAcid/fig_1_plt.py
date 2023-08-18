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

    ax.set_xticks([])
    ax.set_yticks([])

    img_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    img_tt = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/img/'
    axins = plot.inset_img(
        ax,
        dict_img = {
            img_cc+'30001.png': (0.0    , 0., 1/3, 1),
            img_cc+'63000.png': (1/2-1/6, 0., 1/3, 1),
            img_tt+ '2980.png': (1-1/3  , 0., 1/3, 1),
        },
        axin_axis = False
    )
    #plot.add_text(
    #    ax,
    #    dict_text = {
    #        (0.17, 0.07): 'cis-cis (CC)',
    #        (0.51, 0.07): 'cis-trans (CT)',
    #        (0.85, 0.07): 'trans-trans (TT)',
    #    },
    #    va = 'center',
    #    ha = 'center',
    #    transform = ax.transAxes,
    #    fontweight = 'bold'
    #)
    plot.add_text(
        axins[0],
        dict_text = {
            (0.5 , 0.05): 'cis-cis (CC)',
            (0.52, 0.89) :r'$\bf{^=}$O',
            (0.87, 0.58) :r'H$\bf{\mathregular{_{OH}}}$',
            (0.80, 0.15) :r'O$\bf{\mathregular{_{OH}}}$',
        },
        ha = 'center',
        va = 'center',
        fontweight='bold',
        transform = axins[0].transAxes,
    )
    plot.add_text(
        axins[1],
        dict_text = {
            (0.5 , 0.05): 'cis-trans (CT)',
        },
        ha = 'center',
        va = 'center',
        fontweight='bold',
        transform = axins[1].transAxes,
    )
    plot.add_text(
        axins[2],
        dict_text = {
            (0.5 , 0.05): 'trans-trans (TT)',
        },
        ha = 'center',
        va = 'center',
        fontweight='bold',
        transform = axins[2].transAxes,
    )

def rdfcsv(file):
    
    data = np.loadtxt(file)
    return data[:,0], data[:,1]
 
def fig_b(
    axs
):

    dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/CPBO/CC/carbonicrdf/'
    dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/DPMD/330K/CC/carbonicrdf/'
    df_dpmd = pd.read_csv(dir_dpmd+'carbonicrdf.csv', index_col='r(ang)')
    df_aimd = pd.read_csv(dir_aimd+'carbonicrdf.csv', index_col='r(ang)')
    dict_title = {
        'o_w.o_w': r'O$\mathregular{_W}$-O$\mathregular{_W}$',
        'o_nyl.h_w': r'$^=$O-H$\mathregular{_W}$',
        'o_oh.h_w': r'O$\mathregular{_{OH}}$-H$\mathregular{_W}$',
        'h_oh.o_w': r'H$\mathregular{_{OH}}$-O$\mathregular{_W}$',
    }
    dict2d_data ={
        'DPMD': {
            'o_w.o_w'  : [df_dpmd.index, df_dpmd['o_w.o_w'     ]],
            'h_oh.o_w' : [df_dpmd.index, df_dpmd['cc.h_oh.o_w' ]],
            'o_oh.h_w' : [df_dpmd.index, df_dpmd['cc.o_oh.h_w' ]],
            'o_nyl.h_w': [df_dpmd.index, df_dpmd['cc.o_nyl.h_w']],
        },
        'AIMD': {
            'h_oh.o_w' : [df_aimd.index, df_aimd['cc.h_oh.o_w' ]],
            'o_oh.h_w' : [df_aimd.index, df_aimd['cc.o_oh.h_w' ]],
            'o_nyl.h_w': [df_aimd.index, df_aimd['cc.o_nyl.h_w']],
            'o_w.o_w'  : [df_aimd.index, df_aimd['o_w.o_w'     ]],
        },
    }
    dict_ylim = {
        'o_w.o_w'  : (0,4),
        'h_oh.o_w' : (0,3),
        'o_oh.h_w' : (0,2),
        'o_nyl.h_w': (0,2),
    }
    
    for ax, key in zip(axs, dict_title):
        ax.text(
            x=0.9,
            y=0.9,
            s = dict_title[key],
            horizontalalignment = 'right',
            verticalalignment = 'top',
            transform=ax.transAxes
        )
        for label, dict_data in dict2d_data.items():
            data = dict_data[key]
            ax.plot( data[0], data[1], label=label, lw=1)

    axs[0].legend(
        frameon = False,
        handlelength = 1,
        loc = 'upper left'
    )
    axs[0].set_xlim(1, 6)
    axs[0].set_ylim(0, 4)
    axs[0].set_ylabel('g(r)')
    axs[1].set_ylabel('g(r)')
    axs[1].set_xlabel('r (Å)')
    axs[3].set_xlabel('r (Å)')
    axs[0].tick_params(labelbottom=False)
    axs[2].tick_params(labelbottom=False)
    axs[2].tick_params(labelleft=False)
    axs[3].tick_params(labelleft=False)

def fig_label(
    fig,
    axs,
):

    x = -20/72
    y = 0/72
    dict_pos = {
        'a': (x, y),
        'b': (x, y),
    }

    for ax, label in zip(axs, dict_pos.keys()):
        (x, y) = dict_pos[label]
        # label physical distance to the left and up:
        trans = mtransforms.ScaledTranslation(x, y, fig.dpi_scale_trans)
        ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
                fontsize='medium', va='top', fontweight='bold')

def main():

    plot.set_rcparam()
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (3.33, 2.56) )

    gs = fig.add_gridspec(2, 1, height_ratios=[2.5, 4], left=0.1, right=0.99, bottom=0.15, top=0.99, hspace=0.1)

    ax0 = fig.add_subplot(gs[0])

    gs1 = gs[1].subgridspec(2, 2, wspace=0.1, hspace=0.1)
    ax1 = fig.add_subplot(gs1[0, 0])
    ax2 = fig.add_subplot(gs1[1, 0], sharex=ax1, sharey=ax1)
    ax3 = fig.add_subplot(gs1[0, 1], sharex=ax1, sharey=ax1)
    ax4 = fig.add_subplot(gs1[1, 1], sharex=ax1, sharey=ax1)

    fig_a(ax0)
    fig_b([ax1, ax2, ax3, ax4])

    fig_label(
        fig,
        axs = [ax0,ax1]
    )

    plot.save(
        fig,
        file_save = 'fig_1',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

