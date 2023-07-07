import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os
from tf_dpmd_kit import analysis
from tf_dpmd_kit import plm
import numpy as np
import pandas as pd

homedir = os.environ['homedir']

def run0(ax):

    o0 = (540, 840)
    h0 = (401, 697)
    o1 = (1018, 829)
    h1 = (1217, 729)

    ax.plot( [o0[0], h0[0]], [o0[1], h0[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)
    ax.plot( [o1[0], h1[0]], [o1[1], h1[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)

    plot.add_text(
        ax,
        dict_text = {
            (325, 884): r'R$_1$',
            (1000, 630): r'R$_0$ = 1.09 Å',
            (680, 320): r'$^=$O',
            (624, 618): r'C',
            (511, 1000): r'O$_1$',
            (999, 1000): r'O$_0$',
            (1310, 791): r'Ex$_0$',
            (185, 672): r'Ex$_1$',
        }
    )

def run1(ax):

    o0 = (354, 845)
    h0 = (195, 704)
    o1 = (810, 815)
    h1 = (1099, 707)

    ax.plot( [o0[0], h0[0]], [o0[1], h0[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)
    ax.plot( [o1[0], h1[0]], [o1[1], h1[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)

    plot.add_text(
        ax,
        dict_text = {
            (125, 840): r'R$_1$',
            (780, 610): r'R$_0$ = 1.42 Å'
        }
    )

def run2(ax):

    o0 = (341, 837)
    h0 = (196, 705)
    o1 = (798, 837)
    h1 = (1318, 733)

    ax.plot( [o0[0], h0[0]], [o0[1], h0[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)
    ax.plot( [o1[0], h1[0]], [o1[1], h1[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)

    plot.add_text(
        ax,
        dict_text = {
            (116, 846): r'R$_1$',
            (780, 630): r'R$_0$ = 2.44 Å',
            (1190, 966): 'Zundel'
        }
    )

def run3(ax):

    o0 = (335, 834)
    h0 = (157, 713)
    o1 = (798, 843)
    h1 = (1356, 465)

    ax.plot( [o0[0], h0[0]], [o0[1], h0[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)
    ax.plot( [o1[0], h1[0]], [o1[1], h1[1]], ls=':', marker='o', color='tab:cyan', lw=1, markersize=1)

    plot.add_text(
        ax,
        dict_text = {
            (748, 524): r'R$_0$ = 3.34 Å',
            (101, 870): r'R$_1$'
        }
    )

def fig_a(
    ax
):

    img_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    # 
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.45
    dy = 1200/1600*w/h*dx
    ax.axis('off')

    ax0, ax1, ax2, ax3 = plot.inset_img(
        ax,
        dict_img = {
            img_dir+'0.174174.png': (1/4-dx/2, 3/4-dy/2, dx, dy),
            img_dir+'0.174177.png': (3/4-dx/2, 3/4-dy/2, dx, dy),
            img_dir+'0.174180.png': (3/4-dx/2, 1/4-dy/2, dx, dy),
            img_dir+'0.174181.png': (1/4-dx/2, 1/4-dy/2, dx, dy),
        },
        axin_axis = False,
    )
    run0(ax0)
    run1(ax1)
    run2(ax2)
    run3(ax3)

    plot.add_arrow(
        ax,
        list_arrow = [
            [(1/2-0.01, 3/4), (1/2+0.01, 3/4)],
            [(3/4, 1/2+0.01), (3/4, 1/2-0.01)],
            [(1/2+0.01, 1/4), (1/2-0.01, 1/4)],
        ],
        arrowstyle = 'fancy, head_length=6, head_width=6, tail_width=0.01',
        lw = 0,
        color = 'tab:blue'
    )

def fig_b(fig, ax):

    data_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/'

    df_data = analysis.read_multidata([
        data_dir+'CC/carbonic/carbonic.product.csv',
        #data_dir+'CT/carbonic/carbonic.product.csv',
        #data_dir+'TT/carbonic/carbonic.product.csv',
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
    #ax.set_xlabel(r'R$_0$ (Å) [R$_0$ > R$_1$]')
    ax.set_ylabel(r'R$_1$ (Å)')
    ax.tick_params(labelbottom=False)

def fig_c(ax):

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

    ax.set_xlabel(r'R$_0$ (Å) [R$_0$ > R$_1$]')
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
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure(figsize = ((8+8)*cm, 8*cm))
    gs = fig.add_gridspec(2, 2, width_ratios=[7,6], left=0., right=0.99, bottom=0.12, top=0.99, wspace=0.2, hspace=0.1)

    ax0 = fig.add_subplot(gs[:, 0])
    fig_a(ax0)

    ax1 = fig.add_subplot(gs[0, 1])
    fig_b(fig, ax1)
    
    gs1 = gs[1, 1].subgridspec(1, 2, width_ratios=[8,2], wspace=0)
    ax2 = fig.add_subplot(gs1[0], sharex=ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'fes_r0',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

