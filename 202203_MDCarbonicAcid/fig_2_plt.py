import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import analysis
import os

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
def fig_label(
    list_ax,
):
    dict_pos = {
        '(a)': (-0.12, 0.9),
        '(b)': (-0.12, 0.9),
    }
    for ax, label in zip(list_ax, dict_pos):
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
        )

def run():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize = (8.6*cm, (3+3)*cm))

    fig_a(ax0)
    fig_b(ax1)

    fig_label([ax0,ax1])

    plot.save(
        fig,
        file_save = 'fig_2',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

