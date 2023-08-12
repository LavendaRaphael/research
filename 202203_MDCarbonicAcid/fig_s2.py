import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import analysis
import os

homedir = os.environ['homedir']

def run(
    ax,
    data_dir,
    text,
    float_xscale,
):

    analysis.carbonic_rolling_plt(
        ax,
        file_data = data_dir+'carbonic_state.csv',
        float_xscale = float_xscale,
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
        dict_text = {(0.5, 0.9): text},
        va = 'center',
        ha = 'center',
        transform = ax.transAxes
    )

def fig_a(
    ax,
):

    run(
        ax,
        data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/07.md_water62/DPMD/330K/CC/carbonic/',
        text = 'H$_2$CO$_3$ + 62 H$_2$O NVT (330 K)',
        float_xscale = 0.000005,
    )

def fig_b(
    ax,
):

    run(
        ax,
        data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CT/carbonic/',
        text = 'H$_2$CO$_3$ + 126 H$_2$O NpT (330 K, 1 bar)',
        float_xscale = 0.00001,
    )

def fig_c(
    ax,
):

    run(
        ax,
        data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/TT/carbonic/',
        text = 'H$_2$CO$_3$ + 126 H$_2$O NpT (330 K, 1 bar)',
        float_xscale = 0.00001,
    )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300

    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize = (8.6*cm, (3+3+3)*cm))

    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'fig_s2',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

