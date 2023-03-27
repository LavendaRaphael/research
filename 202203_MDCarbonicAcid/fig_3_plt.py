import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import pandas as pd
import numpy as np
from matplotlib import patheffects

plot.set_rcparam()
cm = 1/2.54
homedir = os.environ['homedir']
mpl.rcParams['figure.dpi'] = 300

def fig_a(
    fig,
    ax,
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'

    df_data = pd.read_csv(str_dir+'carbonic_dihedrals.csv')

    h, xedges, yedges = np.histogram2d(df_data['dihedral0(rad)'], df_data['dihedral1(rad)'], bins=100, density=True)

    energy = plm.prob_to_deltag(h, temperature=330)
    energy -= np.amin(energy)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    cmap_new = plt.get_cmap('coolwarm', 10)
    #cmap_new = 'coolwarm'
    image = ax.imshow(
        energy.T,
        origin = 'lower',
        extent = extent,
        cmap = cmap_new,
        aspect = 'auto',
    )
    fig.colorbar( mappable=image )

    ax.set_aspect(1)
    ax.set_xlabel(r'$\alpha$ (rad)')
    ax.set_ylabel(r'$\beta$ (rad)')

    ax.set_xticks([0, np.pi/2, np.pi])
    ax.set_yticks([0, np.pi/2, np.pi])
    ax.set_xticklabels([0, r'$\pi$/2', r'$\pi$'])
    ax.set_yticklabels([0, r'$\pi$/2', r'$\pi$'])

    plot.add_text(
        ax,
        dict_text = {
            (0, 0)       : 'TT',
            (np.pi, 0)   : 'CT',
            (0, np.pi)   : 'CT',
            (np.pi, np.pi): 'CC',
        },
        va = 'center',
        ha = 'center',
        color = 'white',
        fontweight = 'bold',
        fontsize = 8,
        #path_effects = [patheffects.withStroke(linewidth=1, foreground='black')]
    )

    axin = ax.inset_axes((0.35, 0.38, 0.3, 0.3))
    fig_a_sub(axin)

def fig_a_sub(
    ax,
):

    img_dir = homedir+'/research/202203_MDCarbonicAcid/structure/'
    np_img = plt.imread(img_dir+'H2CO3_TS.png')
    ax.imshow(np_img)
    ax.axis('off')

    o_car = np.array([816, 171])
    c = np.array((798, 624))
    o_0 = np.array((534, 956))
    v_0 = o_car + o_0 - c
    h_0 = np.array([143, 1000])
    o_1 = np.array([968, 900])
    v_1 = o_car + o_1 - c
    h_1 = np.array([1280, 960])
    plot.add_line(
        ax,
        dict_line = {
            '0': [c, o_car],
            '1': [o_car, v_0],
            '2': [v_0, o_0],
            '3': [o_0, c],
            '4': [o_car, v_1],
            '5': [v_1, o_1],
            '6': [o_1, c],
            '7': [o_0, h_0],
            '8': [o_1, h_1],
        },
        linestyle = '--',
        color = 'tab:blue',
        lw = 1,
    )

    arc0_a = (o_0+v_0)/2
    arc0_b = (o_0+h_0)/2
    arc1_a = (o_1+v_1)/2
    arc1_b = (o_1+h_1)/2
    plot.add_arrow(
        ax,
        dict_arrow = {
            '0': [arc0_a, arc0_b]
        },
        arrowstyle = '-',
        connectionstyle = 'arc3, rad=0.5'
    )
    plot.add_arrow(
        ax,
        dict_arrow = {
            '0': [arc1_a, arc1_b]
        },
        arrowstyle = '-',
        connectionstyle = 'arc3, rad=-0.5'
    )

    plot.add_text(
        ax,
        dict_text = {
            (268, 700): r'$\alpha$',
            (1200, 670): r'$\beta$',
        }
    )

def fig_b(
    ax,
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'

    df_data = pd.read_csv(str_dir+'carbonic_dihedrals.csv')
    ser_sum = df_data['dihedral0(rad)'] + df_data['dihedral1(rad)']

    np_hist, bin_edges = np.histogram(ser_sum, bins=100, density=True)
    np_energy = plm.prob_to_deltag(np_hist, temperature=330)
    np_energy -= np.amin(np_energy)
    bin_center = bin_edges[:-1] + (bin_edges[1]-bin_edges[0])/2

    ax.plot(bin_center, np_energy)

    ax.set_xlabel(r'$\alpha+\beta$ (rad)')
    ax.set_ylabel('Free energy (kJ/mol)')
    ax.set_xticks([0, np.pi/2, np.pi, np.pi*1.5, np.pi*2])
    ax.set_xticklabels([0, r'$\pi$/2', r'$\pi$', r'3$\pi$/2', r'2$\pi$'])
    ax.set_ylim(None, None)

    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/plm/'
    dir_cc  = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/CC/plm/'
    plot.inset_img(
        ax,
        dict_img = {
            dir_cc +'1.100001.png': (0.05, 0.5, 0.3, 0.4),
            dir_cp +   '60281.png': (0.33, 0.5, 0.3, 0.4),
            dir_cc +'0.003922.png': (0.6, 0.1, 0.3, 0.3),
            dir_cc +'0.003576.png': (0.6, 0.65, 0.3, 0.3),
        },
        bool_axis = False,
    )
    plot.add_arrow(
        ax,
        dict_arrow = {
            '1': [(np.pi*2, 26), (np.pi*2, 20)],
            '2': [(np.pi*2, 14), (np.pi*1.75, 19)],
            '3': [(np.pi*2, 14), (np.pi*2.25, 19)],
        },
        arrowstyle = 'simple, head_length=2, head_width=2, tail_width=0.2',
        color = 'tab:orange',
        lw = 1,
    )


def run():

    fig = plt.figure( figsize = (8.6*cm, 11*cm))
    (subfig0, subfig1) = fig.subfigures(2, 1, height_ratios=[7, 4])

    ax0 = subfig0.subplots()
    ax1 = subfig1.subplots()

    fig_a(subfig0, ax0)
    fig_b(ax1)

    plot.save(
        fig,
        str_save = 'fig_3',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

