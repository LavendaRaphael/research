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
    plot.add_text(
        ax,
        dict_text = {'AIMD': (0.9, 0.9)},
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
        dict_text = {'DPMD': (0.9, 0.9)},
        transform = ax.transAxes
    )

def run():

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize = (8.6*cm, 7*cm))

    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        str_save = 'fig_2',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

