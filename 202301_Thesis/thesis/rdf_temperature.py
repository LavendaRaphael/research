import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
import numpy as np
import pandas as pd

dir_data = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/'
dict_color = plot.dict_color_temperature(
    colormap = (280, 320),
    dict_temperature = {
        '280K': 280,
        '290K': 290,
        '300K': 300,
        '310K': 310,
        '320K': 320,
    }
)

def rdfcsv(file):

    data = np.loadtxt(file)
    return data[:,0], data[:,1]

def gen_data(
    str_pair: str
) -> dict:

    return {
        '280K': rdfcsv(dir_data+f'/280K/CC.0/rdf/rdf.{str_pair}.ave.csv'),
        '290K': rdfcsv(dir_data+f'/290K/CC.0/rdf/rdf.{str_pair}.ave.csv'),
        '300K': rdfcsv(dir_data+f'/300K/CC.0/rdf/rdf.{str_pair}.ave.csv'),
        '310K': rdfcsv(dir_data+f'/310K/CC.0/rdf/rdf.{str_pair}.ave.csv'),
        '320K': rdfcsv(dir_data+f'/320K/CC.0/rdf/rdf.{str_pair}.ave.csv'),
        #'330K': rdfcsv(f'../330K/rdf.{str_pair}.ave.csv'),
    }

def fig_a(ax):

    str_pair = 'o_1.h_w'
    plot.plt_compare(
        ax,
        dict_data = gen_data(str_pair),
        dict_color = dict_color,
        float_lw = 0.8,
    )
    ax.set_xlabel('r (Å)')
    ax.set_ylabel('g(r)')
    ax.set_xlim(1,6)
    ax.legend(
        frameon = False,
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.3, 0.9): r'$^=$O-H$_W$'
        },
        transform = ax.transAxes
    )

def fig_b(ax):

    str_pair = 'h_0_1.o_w'
    plot.plt_compare(
        ax,
        dict_data = gen_data(str_pair),
        dict_color = dict_color,
        float_lw = 0.8,
    )
    ax.set_xlabel('r (Å)')
    ax.set_xlim(1,6)
    plot.add_text(
        ax,
        dict_text = {
            (0.3, 0.9): r'H$_{OH}$-O$_W$'
        },
        transform = ax.transAxes
    )
    ax.tick_params(labelleft=False)

def fig_c(ax):

    str_pair = 'o_w.o_w'
    plot.plt_compare(
        ax,
        dict_data = gen_data(str_pair),
        dict_color = dict_color,
        float_lw = 0.8,
    )
    ax.set_xlabel('r (Å)')
    ax.set_xlim(2,6)
    ax.set_ylim(0, 4)
    plot.add_text(
        ax,
        dict_text = {
            (0.3, 0.9): r'O$_W$-O$_W$'
        },
        transform = ax.transAxes
    )
    ax.tick_params(labelleft=False)

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (14*cm, 4*cm))

    gs = fig.add_gridspec(1, 3, left=0.07, right=0.99, bottom=0.2, top=0.97, wspace=0.1)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1], sharey=ax0)
    ax2 = fig.add_subplot(gs[2], sharey=ax0)
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'rdf_temperature',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

