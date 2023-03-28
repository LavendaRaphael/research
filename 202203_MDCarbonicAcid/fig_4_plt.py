import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import pandas as pd
import numpy as np
from matplotlib import patheffects
from matplotlib.lines import Line2D

plot.set_rcparam()
cm = 1/2.54
homedir = os.environ['homedir']
mpl.rcParams['figure.dpi'] = 300

def fig_a(
    ax,
):

    dict_color = {
        'TT': 'tab:blue',
        'CT': 'tab:orange',
        'CC': 'tab:green',
        'H2CO3': 'tab:red',
        'HCO3': 'tab:purple',
    }

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature_prop.csv'
    list_header = ['TT', 'CT', 'CC', 'HCO3']

    df_data = pd.read_csv(file_data)
    ser_0 = pd.Series([0]*len(df_data))
    for header in list_header:
        if header in dict_color:
            color = dict_color[header]
        ser_1 = ser_0 + df_data[header]
        ax.fill_between(df_data['temperature(K)'], ser_0, ser_1, lw=1, color=color, alpha=0.5)
        ser_0 = ser_1

    plot.add_text(
        ax,
        dict_text = {
            (330, 0.65): 'TT',
            (330, 0.87): 'CT',
            (340, 0.87): 'CC',
            (330, 0.97): r'HCO$_3^-$',
        },
        va = 'center',
        ha = 'center',
        color = 'white',
        fontweight = 'bold',
        fontsize = 8,
    ),
    plot.add_arrow(
        ax,
        dict_arrow = {
            'x': [(342, 0.87), (348, 0.92)]
        },
        arrowstyle = 'simple, head_length=2, head_width=2, tail_width=0.1',
        color = 'white'
    )

    ax.set_ylim(0.5, 1)
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Proportion'),

def fig_b(ax):

    dict_color = {
        'TT': 'tab:blue',
        'CT': 'tab:orange',
        'CC': 'tab:green',
        'H2CO3': 'tab:red',
        'HCO3': 'tab:purple',
    }

    list_header = ['TT', 'CT', 'CC','H2CO3', 'HCO3']

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature_timemean.csv'
    df_data = pd.read_csv(file_data)
    for header, marker in zip(list_header, Line2D.filled_markers):
        color = dict_color[header]
        ax.errorbar(df_data['temperature(K)'], df_data[header], ls=':', marker=marker, markersize=2, lw=1, color=color)

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Lifetime (ps)')

    plot.add_text(
        ax,
        dict_text = {
            (355, 1000): 'TT',
            (355,  400): r'H$_2$CO$_3$',
            (355,  100): 'CT',
            (355,   30): r'HCO$_3^-$',
            (355,   15): 'CC',
        }
    )
    ax.set_yscale('log')
    ax.set_xlim(None, 380)

def fig_c(ax):

    dict_label = {
        'H2CO3': r'H$_2$CO$_3$',
        'HCO3': r'HCO$_3^-$',
    }
    dict_color = {
        'TT': 'tab:blue',
        'CT': 'tab:orange',
        'CC': 'tab:green',
        'H2CO3': 'tab:red',
        'HCO3': 'tab:purple',
    }

    list_header = ['TT', 'CT', 'CC','H2CO3']

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature_count.csv'
    df_data = pd.read_csv(file_data)
    for header, marker in zip(list_header, Line2D.filled_markers):
        label = header
        if header in dict_label:
            label = dict_label[header]
        color = dict_color[header]
        ax.errorbar(df_data['temperature(K)'], df_data[header], label=label, ls=':', marker=marker, markersize=2, lw=1, color=color) 

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel(r'Count (ns$^{-1}$)')

    ax.legend(frameon=False)

def main():

    fig = plt.figure( figsize = (8.6*cm, 8*cm))
    (subfig0, subfig1) = fig.subfigures(2, 1)

    ax0 = subfig0.subplots()
    (ax1, ax2) = subfig1.subplots(1, 2)

    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'fig_4',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()


