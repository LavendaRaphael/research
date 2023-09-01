import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import analysis
import os
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

homedir = os.environ['homedir']

def fig_a(
    ax
):

    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/07.md_water62/CPBO/CC/carbonic/'
    analysis.carbonic_rolling_plt(
        ax,
        file_data = str_dir+'carbonic_state.csv',
        float_xscale = 0.0004837769*5,
        int_window = 10,
        list_header = ['HCO3', 'CC', 'CT', 'TT'],
        list_ypos = [1, 2, 3, 4],
        dict_color = {
            'CC': 'tab:blue',
            'CT': 'tab:orange',
            'TT': 'tab:green',
            'H2CO3': 'tab:red',
            'HCO3': 'tab:purple',
        }
    )
    ax.set_xlabel('Time (ps)')
    ax.set_ylim(0.5, 4.8)
    ax.set_yticklabels(['HCO$_3^-$', 'CC','CT','TT'])
    img_dir = homedir+'/research/202203_MDCarbonicAcid/structure/'
    axins = plot.inset_img(
        ax,
        dict_img = {
            img_dir+'H2CO3_CC.png': (0.1, 0.5, 0.2, 0.4),
            img_dir+'H2CO3_CT.png': (0.3, 0.5, 0.2, 0.4),
            img_dir+'H2CO3_TT.png': (0.5, 0.5, 0.2, 0.4),
        },
        axin_axis = False
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.9, 0.9 )  : 'AIMD',
            (0.2, 0.45)  : 'CC'  ,
            (0.4, 0.45)  : 'CT'  ,
            (0.6, 0.45)  : 'TT'  ,
        },
        va = 'center',
        ha = 'center',
        transform = ax.transAxes
    )

def fig_b(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/carbonic/'
    analysis.carbonic_rolling_plt(
        ax,
        file_data = str_dir+'carbonic_state.csv',
        float_xscale = 0.00001,
        int_window = 100,
        list_header = ['HCO3', 'CC', 'CT', 'TT'],
        list_ypos = [1, 2, 3, 4],
        dict_color = {
            'CC': 'tab:blue',
            'CT': 'tab:orange',
            'TT': 'tab:green',
            'H2CO3': 'tab:red',
            'HCO3': 'tab:purple',
        }
    )
    ax.set_xlabel('Time (ns)')
    ax.set_ylim(0.5, 4.8)
    ax.set_yticklabels(['HCO$_3^-$', 'CC','CT','TT'])
    plot.add_text(
        ax,
        dict_text = {(0.9, 0.9): 'DPMD'},
        va = 'center',
        ha = 'center',
        transform = ax.transAxes
    )

def fig_c(ax):

    # color
    alpha = 0.7
    c = mcolors.to_rgb('tab:blue')
    c_cc = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:orange')
    c_ct = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:green')
    c_tt = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:purple')
    c_xx = (c[0], c[1], c[2], alpha)

    ax.pie(
        [81.32, 12.38, 0.28, 5.82],
        explode = (0.1, 0.1, 0.1, 0.1),
        colors = [c_cc, c_ct, c_tt, c_xx],
        labeldistance=.6,
    )
    plot.add_text(
        ax,
        dict_text = {
            (-0.7, 0.3): 'CC',
            (0.5, -0.7): 'CT',
        },
        color = 'white',
        fontweight = 'bold',
    )
    plot.add_text(
        ax,
        dict_text = {
            (1.05, -0.6): 'TT',
            (0.95, 0.05): 'HCO$_3^-$',
        },
    )
    ax.set_xlim(None, 1.7)

def fig_label(
    list_ax,
):
    dict_pos = {
        'a': (-0.12, 0.9),
        'b': (-0.12, 0.9),
    }
    for ax, label in zip(list_ax, dict_pos):
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
            fontweight='bold'
        )

def run():

    plot.set_rcparam()
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (3.33, 2.36) )

    gs = fig.add_gridspec(2, 2, width_ratios=[1.5, 1], left=0.12, right=0.99, bottom=0.15, top=0.99, wspace=0.1, hspace=0.4)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[1, 0])
    fig_a(ax0)
    fig_b(ax1)

    ax2 = fig.add_subplot(gs[:, 1])
    fig_c(ax2)

    fig_label([ax0,ax1])

    plot.save(
        fig,
        file_save = 'fig_2.new',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

