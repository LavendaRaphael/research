import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/05.metad/'

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def rdfcsv_error(file):

    data = np.loadtxt(file, ndmin=2)
    return data[:,0], data[:,1], data[:,2]

def fig_a(ax):

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

    plot.plt_compare(
        ax,
        dict_data = {
            '280 K': rdfcsv(dir_data+'280K/TT/reweight/dist_vp_o_1_2_fes.ave.grid'),
            '290 K': rdfcsv(dir_data+'290K/TT/reweight/dist_vp_o_1_2_fes.ave.grid'),
            '300 K': rdfcsv(dir_data+'300K/TT/reweight/dist_vp_o_1_2_fes.ave.grid'),
            '310 K': rdfcsv(dir_data+'310K/TT/reweight/dist_vp_o_1_2_fes.ave.grid'),
            '320 K': rdfcsv(dir_data+'320K/TT/reweight/dist_vp_o_1_2_fes.ave.grid'),
        },
        dict_color = dict_color,
        bool_minzero = True,
        float_lw = 1,
    )
    ax.set_ylim(None, 60)
    ax.legend(frameon=False)
    ax.set_xlabel('R(V$_P$O$_{CA}$) (Å)')
    ax.set_ylabel('Free energy (kJ/mol)')

def fig_b(ax):

    dir_exp = '/home/faye/research/202203_MDCarbonicAcid/literature/ref/'
    plot.plt_error(
        ax,
        dict_data = {
            'Aminov et al. 2019': rdfcsv_error(dir_exp+'/2019_PNAS_DanielAminov/Fig_1_kelvin.csv'),
            'Pines et al. 2016' : rdfcsv_error(dir_exp+'/2016_JPCB_DinePines/pka_kelvin.csv'),
            'Wang et al. 2010'  : rdfcsv_error(dir_exp+'/2010_JPCA_WangXiaoguang/Sfig_3_kelvin.csv'),
            'this work'         : rdfcsv_error(dir_data+'reweight.dist_vp_o_1_2_fes.pka.ave.csv'),
        },
        float_lw = 1,
        dict_ls = {
            'this work': ':'
        }
    )
    ax.legend(frameon=False)
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('pKa')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (10*cm, 10*cm))

    gs = fig.add_gridspec(2, 1, left=0.12, right=0.99, bottom=0.1, top=0.99, hspace=0.3)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'fes_temperature',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

