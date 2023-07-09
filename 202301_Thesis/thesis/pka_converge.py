import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd


dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/05.metad/'

dict_color = plot.dict_color_temperature(
    colormap = (280, 320),
    dict_temperature = {
        '280 K': 280,
        '290 K': 290,
        '300 K': 300,
        '310 K': 310,
        '320 K': 320,
    }
)
def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def fig_a(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '280 K': rdfcsv(dir_data+'280K/CC/reweight/dist_vp_o_1_2_fes_deltag.csv'),
            '290 K': rdfcsv(dir_data+'290K/CC/reweight/dist_vp_o_1_2_fes_deltag.csv'),
            '300 K': rdfcsv(dir_data+'300K/CC/reweight/dist_vp_o_1_2_fes_deltag.csv'),
            '310 K': rdfcsv(dir_data+'310K/CC/reweight/dist_vp_o_1_2_fes_deltag.csv'),
            '320 K': rdfcsv(dir_data+'320K/CC/reweight/dist_vp_o_1_2_fes_deltag.csv'),
        },
        dict_color = dict_color,
        float_lw = 1,
    )
    ax.set_ylim(None,25)
    ax.legend(frameon=False)
    ax.set_ylabel(r'$\Delta$G (kJ/mol)')
    ax.tick_params(labelbottom=False)

def fig_b(ax):

    plot.plt_compare(
        ax,
        dict_data = {
            '280 K': rdfcsv(dir_data+'280K/CC/reweight/dist_vp_o_1_2_fes_pka.csv'),
            '290 K': rdfcsv(dir_data+'290K/CC/reweight/dist_vp_o_1_2_fes_pka.csv'),
            '300 K': rdfcsv(dir_data+'300K/CC/reweight/dist_vp_o_1_2_fes_pka.csv'),
            '310 K': rdfcsv(dir_data+'310K/CC/reweight/dist_vp_o_1_2_fes_pka.csv'),
            '320 K': rdfcsv(dir_data+'320K/CC/reweight/dist_vp_o_1_2_fes_pka.csv'),
        },
        dict_color = dict_color,
        float_lw = 1,
    )
    ax.set_ylabel('pKa')
    ax.set_xlabel('Time (ns)')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (10*cm, 10*cm))

    gs = fig.add_gridspec(2, 1, left=0.1, right=0.99, bottom=0.1, top=0.99, hspace=0.1)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1], sharex=ax0)
    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'pka_temperature',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

