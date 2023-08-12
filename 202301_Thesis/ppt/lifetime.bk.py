import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
from tf_dpmd_kit import analysis
import os
import pandas as pd
import numpy as np
import matplotlib.colors as colors
import matplotlib.transforms as mtransforms

def fig_a(
    ax
):

    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'
    df = analysis.carbonic_survival(
        list_file = [
            str_dir+'../CC/carbonic/carbonic_lifedata.csv',
            str_dir+'../CT/carbonic/carbonic_lifedata.csv',
            str_dir+'../TT/carbonic/carbonic_lifedata.csv',
        ]
    )

    list_state = ['CC', 'CT', 'TT','H2CO3', 'HCO3']
    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'H2CO3': 'tab:red',
        'HCO3': 'tab:purple',
    }
    dict_label = {
        'H2CO3': r'H$_2$CO$_3$',
        'HCO3': r'HCO$_3^-$',
    }

    analysis.carbonic_survival_plt(
        ax = ax,
        df = df,
        list_state = list_state,
        dict_color = dict_color,
        dict_label = dict_label,
    )
    ax.vlines(1.5, 0.01, 0.99, ls=':', lw=1, color='grey')
    plot.add_text(
        ax,
        dict_text = {
            (1.5, 0.4): 't = 1.5 ps'
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', fc='white', lw=1, ls=':', ec='grey')
    )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (9*cm, 4.5*cm) )

    gs = fig.add_gridspec(1, 1, left=0.13, right=0.99, bottom=0.2, top=0.97)
    ax = fig.add_subplot(gs[0])

    fig_a(ax)

    plot.save(
        fig,
        file_save = 'lifetime',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

