import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms

homedir = os.environ['homedir']

def fig_a(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        str_file = str_dir+'dptest.e.out',
        int_natoms = 384,
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
    )

def fig_b(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        str_file = str_dir+'dptest.f.out',
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
    )

def fig_c(
    ax
):

    str_dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/rdf/'
    str_dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt/330K/CC/rdf/'
    dict2d_data ={
        'DPMD': {
            'o_w.o_w': str_dir_dpmd+'rdf.o_w.o_w.ave.csv',
        },
        'AIMD': {
            'o_w.o_w': str_dir_aimd+'rdf.o_w.o_w.ave.csv',
        },
    }
    ax.set_ylabel('g(r)')
    ax.text(
        x=0.1,
        y=0.9,
        s = r'O$\mathregular{_W}$-O$\mathregular{_W}$',
        horizontalalignment = 'left',
        verticalalignment = 'top',
        transform=ax.transAxes
    )
    ax.set_ylim((0,4))
    for str_label, dict_data in dict2d_data.items():
        str_file = dict_data['o_w.o_w']
        np_data = np.loadtxt(str_file)
        ax.plot( np_data[:,0], np_data[:,1], label=str_label, lw=1)

    ax.legend(
        frameon = False,
        handlelength = 1
    )
    ax.set_xlabel('r (Å)')
    ax.set_xlim(1,6)

def fig_d(
    axs
):

    str_dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/rdf/'
    str_dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt/330K/CC/rdf/'
    dict_title = {
        'cc_o_c.h_w': r'$^=$O-H$\mathregular{_W}$',
        'cc_o_oh.h_w': r'O$\mathregular{_{OH}}$-H$\mathregular{_W}$',
        'cc_h_oh.o_w': r'H$\mathregular{_{OH}}$-O$\mathregular{_W}$',
    }
    dict2d_data ={
        'DPMD': {
            'cc_h_oh.o_w': str_dir_dpmd+'rdf.cc_h_oh.o_w.ave.csv',
            'cc_o_oh.h_w': str_dir_dpmd+'rdf.cc_o_oh.h_w.ave.csv',
            'cc_o_c.h_w': str_dir_dpmd+'rdf.cc_o_c.h_w.ave.csv',
        },
        'AIMD': {
            'cc_h_oh.o_w': str_dir_aimd+'rdf.cc_h_oh.o_w.ave.csv',
            'cc_o_oh.h_w': str_dir_aimd+'rdf.cc_o_oh.h_w.ave.csv',
            'cc_o_c.h_w': str_dir_aimd+'rdf.cc_o_c.h_w.ave.csv',
        },
    }
    dict_ylim = {
        'cc_h_oh.o_w': (0,3),
        'cc_o_oh.h_w': (0,2),
        'cc_o_c.h_w': (0,2),
    }
    
    for ax, str_key in zip(axs, dict_title):
        ax.set_ylabel('g(r)')
        ax.text(
            x=0.9,
            y=0.9,
            s = dict_title[str_key],
            horizontalalignment = 'right',
            verticalalignment = 'top',
            transform=ax.transAxes
        )
        ax.set_ylim(dict_ylim[str_key])
        for str_label, dict_data in dict2d_data.items():
            str_file = dict_data[str_key]
            np_data = np.loadtxt(str_file)
            ax.plot( np_data[:,0], np_data[:,1], label=str_label, lw=1)
    axs[0].tick_params(labelbottom=False)
    axs[1].tick_params(labelbottom=False)
    #axs[1].legend(
    #    frameon = False,
    #    handlelength = 1
    #)

    axs[-1].set_xlabel('r (Å)')
    axs[0].set_xlim(1,6)

def fig_e(
    ax,
):
    ax.axis('off')
    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    image = plt.imread(str_dir+'33733.png')
    ax.set_ylim(1200,-300)
    ax.imshow(image, origin='upper')

    plot.add_text(
        ax,
        dict_text = {
            #(700,250)  :r'O$_W$'    ,      
            #(1000,400) :r'H$_W$'    ,      
            (572,365)  :r'$\bf{^=}$O',
            (1244,532) :r'H$\bf{\mathregular{_{OH}}}$',
            (1061,992) :r'O$\bf{\mathregular{_{OH}}}$',
        },
        ha = 'center',
        va = 'center',
        fontweight='bold'
    )

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
        '(d)': (x, y),
        '(e)': (x, -12/72),
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

    fig = plt.figure( figsize = (8.6*cm, 10*cm) )

    gs = fig.add_gridspec(2, 1, height_ratios=[4, 7.4], left=0.1, right=0.99, bottom=0.1, top=0.99, hspace=0.3)

    gs0 = gs[0].subgridspec(1, 2, wspace=0.3)
    ax0 = fig.add_subplot(gs0[0])
    ax1 = fig.add_subplot(gs0[1])

    gs1 = gs[1].subgridspec(3, 2, wspace=0.3)
    ax2 = fig.add_subplot(gs1[0, 0])
    ax3 = fig.add_subplot(gs1[0, 1])
    ax4 = fig.add_subplot(gs1[1, 1], sharex=ax2)
    ax5 = fig.add_subplot(gs1[2, 1], sharex=ax2)
    ax6 = fig.add_subplot(gs1[1:, 0])

    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)
    fig_d([ax3, ax4, ax5])
    fig_e(ax6)

    fig_label(
        fig,
        axs = [ax0,ax1,ax2,ax3,ax6]
    )

    plot.save(
        fig,
        file_save = 'fig_1',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

