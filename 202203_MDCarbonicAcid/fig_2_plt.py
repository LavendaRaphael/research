import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import analysis
import os

plot.set_rcparam()
cm = 1/2.54
homedir = os.environ['homedir']
mpl.rcParams['figure.dpi'] = 300

def fig_a(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/carbonic/'
    analysis.carbonic_rolling_plt(
        ax,
        str_file = str_dir+'carbonic_rolling.csv',
        float_xscale = 0.0004837769,
        str_xlabel = 'Time (ps)',
        tup_ylim = (0.5, 4.5),
        list_header = ['HCO3', 'TT', 'CT', 'CC'],
        list_ypos = [1, 2, 3, 4],
        list_yticklabels = ['HCO$_3^-$', 'TT','CT','CC'],
    )
    img_dir = homedir+'/research/202203_MDCarbonicAcid/structure/'
    plot.inset_img(
        ax,
        dict_img = {
            img_dir+'H2CO3_TT.png': (0.1, 0.5, 0.2, 0.4),
            img_dir+'H2CO3_CT.png': (0.3, 0.5, 0.2, 0.4),
            img_dir+'H2CO3_CC.png': (0.5, 0.5, 0.2, 0.4),
        },
        bool_axis = False,
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.9, 0.9 )  : 'AIMD',
            (0.2, 0.45)  : 'TT'  ,
            (0.4, 0.45)  : 'CT'  ,
            (0.6, 0.45)  : 'CC'  ,
        },
        va = 'center',
        ha = 'center',
        transform = ax.transAxes
    )

def fig_b(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/TT/carbonic/'
    analysis.carbonic_rolling_plt(
        ax,
        str_file = str_dir+'carbonic_rolling.csv',
        float_xscale = 0.000005,
        str_xlabel = 'Time (ns)',
        tup_ylim = (0.5, 4.5),
        list_header = ['HCO3', 'TT', 'CT', 'CC'],
        list_ypos = [1, 2, 3, 4],
        list_yticklabels = ['HCO$_3^-$', 'TT','CT','CC'],
    )
    plot.add_text(
        ax,
        dict_text = {(0.9, 0.9): 'DPMD'},
        va = 'center',
        ha = 'center',
        transform = ax.transAxes
    )

def fig_c(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'

    list_state = ['TT', 'CT', 'CC','H2CO3', 'HCO3']
    dict_color = {
        'TT': 'tab:blue',
        'CT': 'tab:orange',
        'CC': 'tab:green',
        'H2CO3': 'tab:red',
        'HCO3': 'tab:purple',
    }
    dict_label = {
        'H2CO3': r'H$_2$CO$_3$',
        'HCO3': r'HCO$_3^-$',
    }

    analysis.carbonic_survival(
        ax = ax,
        file_data = str_dir+'carbonic_lifedata.csv',
        list_state = list_state,
        dict_color = dict_color,
        dict_label = dict_label,
        file_lifetime = None
    )

def fig_label(
    dict_ax,
):
    dict_pos = {
        '(a)': (-0.12, 0.9),
        '(b)': (-0.12, 0.9),
        '(c)': (-0.12, 0.9),
    }
    for label, ax in dict_ax.items():
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
        )

def run():

    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize = (8.6*cm, 10*cm))

    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    fig_label({
        '(a)': ax0,
        '(b)': ax1,
        '(c)': ax2,
    })

    plot.save(
        fig,
        file_save = 'fig_2',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

