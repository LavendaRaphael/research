import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

homedir = os.environ['homedir']
def fig_a(
    ax,
):

    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'HCO3': 'tab:purple',
    }

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature.csv'
    list_header = ['CC', 'CT', 'TT', 'HCO3']

    dfgb = pd.read_csv(file_data, index_col=['state']).groupby(level='state')
    ser_temperature = dfgb.get_group(list_header[0])['temperature(K)']
    ser_0 = pd.Series([0]*len(ser_temperature))
    for header in list_header:
        ser_1 = dfgb.get_group(header)['prop'].reset_index(drop=True)
        if header in dict_color:
            color = dict_color[header]
        ser_1 = ser_0 + ser_1
        ax.fill_between(ser_temperature, ser_0, ser_1, lw=1, color=color, alpha=0.5)
        ser_0 = ser_1

    plot.add_text(
        ax,
        dict_text = {
            (330, 0.65): 'CC',
            (330, 0.87): 'CT',
            (340, 0.87): 'TT',
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
        list_arrow = [
            [(342, 0.87), (348, 0.92)]
        ],
        arrowstyle = 'simple, head_length=2, head_width=2, tail_width=0.1',
        color = 'white'
    )

    ax.set_xlim(290, 350)
    ax.set_ylim(0.5, 1)
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Proportion'),

def fig_b(ax):

    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'HCO3': 'tab:purple',
    }
    dict_marker = {
        'CC': 'o',
        'CT': 'v',
        'TT': '^',
        'HCO3': '>',
    }

    list_header = ['CC', 'CT', 'TT', 'HCO3']

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature.csv'
    dfgb = pd.read_csv(file_data, index_col=['state']).groupby(level='state')
    ser_temperature = dfgb.get_group(list_header[0])['temperature(K)']
    for header in list_header:
        color = dict_color[header]
        marker = dict_marker[header]
        df = dfgb.get_group(header)
        ax.errorbar(ser_temperature, df['lifetime(ps)'], yerr = [df['lower'], df['upper']], ls=':', marker=marker, markersize=2, lw=1, color=color, capsize=2)

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Lifetime (ps)')

    plot.add_text(
        ax,
        dict_text = {
            (355, 1000): 'CC',
            (355,  100): 'CT',
            (355,   50): r'HCO$_3^-$',
            (355,   15): 'TT',
        }
    )
    ax.set_yscale('log')
    ax.set_xlim(None, 375)


def fig_c(ax):

    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'HCO3': 'tab:purple',
    }
    dict_marker = {
        'CC': 'o',
        'CT': 'v',
        'TT': '^',
        'HCO3': '>',
    }

    list_header = ['CC', 'CT', 'TT', 'HCO3']

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature.csv'
    dfgb = pd.read_csv(file_data, index_col=['state']).groupby(level='state')
    ser_temperature = dfgb.get_group(list_header[0])['temperature(K)']
    for header in list_header:
        color = dict_color[header]
        marker = dict_marker[header]
        df = dfgb.get_group(header)
        ax.errorbar(ser_temperature, df['freqprop'], yerr = df['freqprop_sem'], ls=':', marker=marker, markersize=2, lw=1, color=color, capsize=2)

    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('Frequency proportion')

    plot.add_text(
        ax,
        dict_text = {
            (355, 0.2): 'CC',
            (355, 0.3): 'CT',
            (355, 0.4): r'HCO$_3^-$',
            (355, 0.08): 'TT',
        }
    )
    ax.set_xlim(None, 375)

def fig_c_(ax):

    dict_label = {
        'HCO3': r'HCO$_3^-$',
    }
    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'HCO3': 'tab:purple',
    }
    dict_marker = {
        'CC': 'o',
        'CT': 'v',
        'TT': '^',
        'HCO3': '>',
    }

    list_header = ['CC', 'CT', 'TT','HCO3']

    dir_data = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/carbonic/'
    file_data = dir_data+ 'carbonic_statistic.temperature.csv'

    dfgb = pd.read_csv(file_data, index_col=['state']).groupby(level='state')
    ser_temperature = dfgb.get_group(list_header[0])['temperature(K)']
    for header in list_header:
        color = dict_color[header]
        marker = dict_marker[header]
        df = dfgb.get_group(header)
        label = header
        if header in dict_label:
            label = dict_label[header]
        ax.errorbar(ser_temperature, df['frequency(ns-1)'], yerr = df['frequency(ns-1)_sem'], ls=':', marker=marker, markersize=2, lw=1, color=color, capsize=2, label=label)


    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel(r'Frequency (ns$^{-1}$)')

    ax.legend(frameon=False)

def fig_label(
    list_ax,
):

    dict_pos = {
        '(a)': (-0.1, 0.9),
        '(b)': (-0.3, 0.9),
        '(c)': (-0.3, 0.9),
    }
    for ax, label in zip(list_ax, dict_pos):
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
        )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300

    fig = plt.figure( figsize = (8.6*cm, 8*cm))
    (subfig0, subfig1) = fig.subfigures(2, 1)

    ax0 = subfig0.subplots( )
    (ax1, ax2) = subfig1.subplots(1, 2)

    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    fig_label([ax0,ax1,ax2])

    plot.save(
        fig,
        file_save = 'fig_5',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()


