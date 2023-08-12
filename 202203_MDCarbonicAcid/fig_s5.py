import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import analysis
from tf_dpmd_kit import plm
import os
import numpy as np
import pandas as pd

homedir = os.environ['homedir']

def fig_a(fig, ax):

    data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/'

    df_data = analysis.read_multidata([
        data_dir+'CC/carbonic/carbonic.product.csv',
        data_dir+'CT/carbonic/carbonic.product.csv',
        data_dir+'TT/carbonic/carbonic.product.csv',
    ]).dropna()

    print(df_data)

    h, xedges, yedges = np.histogram2d(df_data['roh0(ang)'], df_data['roh1(ang)'], bins=[300, 300], density=True, range=[[0.8, 6],[0.8, 1.3]])

    energy = plm.prob_to_deltag(h, temperature=330)
    energy -= np.amin(energy)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    image = ax.imshow(
        energy.T,
        origin = 'lower',
        extent = extent,
        cmap = 'coolwarm',
        aspect = 'auto',
    )
    colorbar = fig.colorbar( mappable=image, ax=ax, extend='max')
    colorbar.ax.set_ylabel('Free energy (kcal/mol)')

    ax.set_xlim(0.8, 6)
    ax.set_xlabel(r'R$_0$ (Å) [R$_0$ > R$_1$]')
    ax.set_ylabel(r'R$_1$ (Å)')

def fig_b(ax):

    dict_label = {
        'CC': 'CC',
        'CT': 'CT',
        'TT': 'TT',
        'H2CO3': r'H$_2$CO$_3$',
    }
    data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'
    df = pd.read_csv(data_dir+'carbonic_roh_1d.csv', index_col='roh0(ang)')
    for header in ['CC', 'CT', 'TT', 'H2CO3']:
        ser = df[header]
        ser -= min(ser[(ser.index>3.0) & (ser.index<4.2)])
        ax.plot(df.index, df[header], label=dict_label[header], lw=1)

    ax.set_xlabel(r'R$_0$ (Å)')
    ax.set_ylabel('Free energy (kcal/mol)')
    ax.set_xlim(0.8, 6)
    ax.legend(
        frameon = False,
    )
    ax.hlines(0, xmin=0.8, xmax=4, color='grey', ls=':')

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize = (8.6*cm, (4+4)*cm))

    fig_a(fig, ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'fig_s4',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

