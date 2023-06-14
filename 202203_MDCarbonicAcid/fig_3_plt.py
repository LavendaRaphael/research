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

homedir = os.environ['homedir']

def fig_a(
    fig,
    ax,
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/'

    df_data = analysis.read_multidata([
        str_dir+'CC/carbonic/carbonic.product.csv',
        str_dir+'CT/carbonic/carbonic.product.csv',
        str_dir+'TT/carbonic/carbonic.product.csv',
    ]).dropna()
    df_data = df_data[df_data['roh0(ang)']<1.3]
    df_sym = df_data.rename(columns={'dihedral1(rad)': 'dihedral0(rad)', 'dihedral0(rad)': 'dihedral1(rad)'})
    df_data = pd.concat([df_data, df_sym], ignore_index=True)

    h, xedges, yedges = np.histogram2d(df_data['dihedral0(rad)'], df_data['dihedral1(rad)'], bins=200, density=True)
    energy = plm.prob_to_deltag(h, temperature=330)
    energy -= np.amin(energy)

    print(energy)
    cen_x = (xedges[:-1] + xedges[1:])/2
    cen_y = (yedges[:-1] + yedges[1:])/2
    bool_xc = (cen_x < np.pi/2)
    bool_xt = (cen_x > np.pi/2)
    bool_yc = (cen_y < np.pi/2)
    bool_yt = (cen_y > np.pi/2)
    print('CC', min(energy[bool_xc, bool_yc]))
    print('CT', min(energy[bool_xc, bool_yt]))
    print('TC', min(energy[bool_xt, bool_yc]))
    print('TT', min(energy[bool_xt, bool_yt]))

    image = ax.imshow(
        energy.T,
        origin = 'lower',
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]],
        cmap = 'coolwarm',
        #cmap = 'terrain',
        aspect = 'auto',
        norm =colors.BoundaryNorm(boundaries=np.linspace(0, 7, 8), ncolors=256, extend='max')
    )
    colorbar = fig.colorbar( mappable=image, ax=ax, extend='max')
    colorbar.ax.set_ylabel('Free energy (kcal/mol)')

    ax.set_xlabel(r'$\alpha$ (rad)')
    ax.set_ylabel(r'$\beta$ (rad)')

    ax.set_xlim(-np.pi/2, 1.5*np.pi)
    ax.set_ylim(-np.pi/2, 1.5*np.pi)
    ax.set_xticks([0, np.pi/2, np.pi])
    ax.set_yticks([0, np.pi/2, np.pi])
    ax.set_xticklabels([0, r'$\pi$/2', r'$\pi$'])
    ax.set_yticklabels([0, r'$\pi$/2', r'$\pi$'])

    plot.add_text(
        ax,
        dict_text = {
            (0, 0)       : 'CC',
            (np.pi, 0)   : 'CT',
            (0, np.pi)   : 'CT',
            (np.pi, np.pi): 'TT',
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

    dir_file = homedir+'/research/202203_MDCarbonicAcid/structure/'
    np_img = plt.imread(dir_file+'H2CO3_TS_02.png')
    ax.imshow(np_img)
    ax.axis('off')

    p0 = np.array((303,590))
    p1 = np.array((255,531))
    p2 = np.array((314,683))
    p3 = np.array((323,627))
    plot.add_line(
        ax,
        dict_line = {
            '0': [p0, p1],
            '1': [p2, p3],
        },
        lw = 1,
        color = 'tab:blue',
        linestyle = ':',
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p1, p2]
        ],
        arrowstyle = '-',
        lw = 1,
        color = 'tab:blue',
        connectionstyle = 'arc3, rad=0.3',
        shrinkA = 0,
        shrinkB = 0,
    )

    l = 942
    p0 = (l-p0[0],p0[1])
    p1 = (l-p1[0],p1[1])
    p2 = (l-p2[0],p2[1])
    p3 = (l-p3[0],p3[1])
    plot.add_line(
        ax,
        dict_line = {
            '0': [p0, p1],
            '1': [p2, p3],
        },
        lw = 1,
        linestyle = ':',
        color = 'tab:blue',
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p1, p2]
        ],
        arrowstyle = '-',
        lw = 1,
        color = 'tab:blue',
        connectionstyle = 'arc3, rad=-0.3',
        shrinkA = 0,
        shrinkB = 0,
    )

    p0 = (190, 450)
    p1 = (l-p0[0], p0[1])
    plot.add_text(
        ax,
        dict_text = {
            p0: r'-$\beta$',
            p1: r'$\alpha$'
        },
        va = 'center',
        ha = 'center',
        fontweight = 'bold',
        fontsize = 8,
    )

def fig_b(
    ax
):

    ax.axis('off')
    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    dir_tt  = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/TT/plm/'
    plot.inset_img(
        ax,
        dict_img = {
            dir_tt +'0.003922.png': (0., 0.5, 1, 0.4),
            dir_tt +'0.003576.png': (0., 0.1, 1, 0.4),
        },
        axin_axis = False,
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.5, 0.5): r'$\alpha$ = $\beta$ = $\pi$',
            (0.5, 0.9): r'$\alpha$ = $\beta$ = 0.88$\pi$',
        },
        ha = 'center',
        va = 'top'
    )
 

def fig_c(
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

def fig_label(
    fig,
    axs,
):

    x = -25/72
    y = 0/72
    dict_pos = {
        '(a)': (x, y),
        '(b)': (0/72, y),
        '(c)': (x, y),
    }

    for ax, label in zip(axs, dict_pos.keys()):
        (x, y) = dict_pos[label]
        # label physical distance to the left and up:
        trans = mtransforms.ScaledTranslation(x, y, fig.dpi_scale_trans)
        ax.text(0.0, 1.0, label, transform=ax.transAxes + trans,
                fontsize='medium', va='top')


def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, (5+3.5)*cm) )

    gs = fig.add_gridspec(2, 2, height_ratios=[5, 3.5], width_ratios=[6,2.6], left=0.13, right=0.99, bottom=0.1, top=0.99, hspace=0.25, wspace=0.1)
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[1, :])


    fig_a(fig, ax0)
    fig_b(ax1)
    fig_c(ax2)

    fig_label(
        fig,
        axs = [ax0 ,ax1, ax2]
    )

    plot.save(
        fig,
        file_save = 'fig_3',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

