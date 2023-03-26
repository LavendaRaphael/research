import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import plm
import os
import pandas as pd
import numpy as np

plot.set_rcparam()
cm = 1/2.54
homedir = os.environ['homedir']
mpl.rcParams['figure.dpi'] = 300

def angle_sft(x):

    if x < -np.pi/2:
        return x + 2*np.pi
    else:
        return x

def fig_a(
    fig,
    ax,
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/TT/carbonic/'

    list_file = [
        str_dir+'carbonic.product.csv',
        str_dir+'../../CT/carbonic/carbonic.product.csv',
        str_dir+'../../CC/carbonic/carbonic.product.csv',
    ]

    df_new = None
    for str_file in list_file:
        print(str_file)
        df_tmp = pd.read_csv(str_file)
        if df_new is None:
            df_new = df_tmp
        else:
            df_new = pd.concat([df_new, df_tmp], ignore_index=True)
    print(df_new)

    df_new = df_new[df_new['dihedral0(rad)'].notnull()]
    alpha = df_new['dihedral0(rad)'].apply(angle_sft)
    beta = df_new['dihedral1(rad)'].apply(angle_sft)

    h, xedges, yedges = np.histogram2d(alpha, beta, bins=100, density=True)
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

def fig_b(
    ax,
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/TT/carbonic/'

    list_file = [
        str_dir+'carbonic.product.csv',
        str_dir+'../../CT/carbonic/carbonic.product.csv',
        str_dir+'../../CC/carbonic/carbonic.product.csv',
    ]

    df_new = None
    for str_file in list_file:
        print(str_file)
        df_tmp = pd.read_csv(str_file)
        if df_new is None:
            df_new = df_tmp
        else:
            df_new = pd.concat([df_new, df_tmp], ignore_index=True)
    print(df_new)

    df_new = df_new[df_new['dihedral0(rad)'].notnull()]
    ser_alpha = df_new['dihedral0(rad)'].apply(angle_sft)
    ser_beta = df_new['dihedral1(rad)'].apply(angle_sft)
    ser_sum = ser_alpha + ser_beta

    np_hist, bin_edges = np.histogram(ser_sum, bins=100, density=True)
    np_energy = plm.prob_to_deltag(np_hist, temperature=330)
    np_energy -= np.amin(np_energy)
    bin_center = bin_edges[:-1] + (bin_edges[1]-bin_edges[0])/2

    ax.plot(bin_center, np_energy, color='tab:grey')

    ax.set_xlabel(r'$\alpha+\beta$ (rad)')
    ax.set_ylabel('Free energy (kJ/mol)')
    ax.set_xticks([0, np.pi/2, np.pi, np.pi*1.5, np.pi*2])
    ax.set_xticklabels([0, r'$\pi$/2', r'$\pi$', r'3$\pi$/2', r'2$\pi$'])

    ax.set_ylim(None, 30)

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

