import os
import matplotlib.pyplot as plt
from tf_dpmd_kit import analysis
from tf_dpmd_kit import plot
import matplotlib as mpl
import numpy as np
import json
import pandas as pd
import matplotlib.transforms as mtransforms

def fig_b(
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

    list_state = ['CC', 'CT', 'TT', 'HCO3']
    dict_color = {
        'CC': 'tab:blue',
        'CT': 'tab:orange',
        'TT': 'tab:green',
        'HCO3': 'tab:purple',
    }
    dict_label = {
        'HCO3': r'HCO$_3^-$',
    }

    analysis.carbonic_survival_plt(
        ax = ax,
        df = df,
        list_state = list_state,
        dict_color = dict_color,
        dict_label = dict_label,
    )

def fig_a(ax):
    ax.axis('off')

    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'
    fl = {}
    df = pd.read_csv(str_dir+'carbonic_statistic.csv', index_col='state')['frequency(ns-1)']
    fl['cc'] = df['CC']
    fl['ct'] = df['CT']
    fl['tt'] = df['TT']
    fl['xx'] = df['HCO3']

    df = pd.read_csv(str_dir+'carbonic_flow.csv', index_col=['from','to'])['frequency(ns-1)']
    fl['cc_ct'] = df[('CC', 'CT')]
    fl['cc_xx'] = df[('CC', 'HCO3')]
    fl['cc_tt'] = df[('CC', 'TT')]
    fl['ct_cc'] = df[('CT', 'CC')]
    fl['ct_ct'] = df[('CT', 'CT')]
    fl['ct_xx'] = df[('CT', 'HCO3')]
    fl['ct_tt'] = df[('CT', 'TT')]
    fl['xx_cc'] = df[('HCO3', 'CC')]
    fl['xx_ct'] = df[('HCO3', 'CT')]
    fl['xx_tt'] = df[('HCO3', 'TT')]
    fl['tt_ct'] = df[('TT', 'CT')]
    fl['tt_xx'] = df[('TT', 'HCO3')]

    with open(str_dir+'volume.json') as fp:
        volume = json.load(fp)['volume(ang3)']
    Avogadro = 6.02214076e23
    molar = 1e27/Avogadro/volume
    ns2s = 1e9
    print(molar,'mol/L')
    f = {}
    for key, value in fl.items():
        value *= molar*ns2s/1e8
        #f[key] = f'{value:.3f}'
        f[key] = f'{value:.2f}'

    plot.add_text(
        ax,
        dict_text = {
            #(0.9, 0.95): r'Frequency (ns$^{-1}$)',
            (0.9, 0.95): r'Rate ($\times 10^{8}$ mol L$^{-1}$s$^{-1}$)',
        },
        va = 'top',
        ha = 'right',
    )

    # horizon fig
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.27
    dy = 5/8*w/h*dx
    # vertical fig
    dx1 = dy*h/w
    dy1 = dx*w/h

    # right, top
    r = np.array([ dx/2,    0])
    t = np.array([    0,   dy/2])
    r1 = np.array([ dx1/2,    0])
    t1 = np.array([    0,   dy1/2])
    # shift
    sx = np.array([dx/5,   0])
    sy = np.array([   0,dy/5])

    # pos
    p_tt = np.array([1.1*dx, dy/2])
    p_ct = np.array([1.1*dx, 0.5])
    p_cc = np.array([1.1*dx, 1-dy/2])
    p_xx = np.array([1-dx1/2, 0.5])
    # middle
    p_tt_ct = (p_tt+p_ct)/2
    p_ct_cc = (p_ct+p_cc)/2
    p_xx_cc = (p_xx-r1+t1+p_cc+r)/2
    p_xx_ct = (p_xx-r1+p_ct+r)/2
    p_xx_tt = (p_xx-r1-t1+p_tt+r)/2

    # img
    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    dir_tt  = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/TT/plm/'
    [axin3] = plot.inset_img(
        ax,
        dict_img = {
            dir_cp +   '60147.png': (p_xx[0]-0.5*dx1, p_xx[1]-dy1/2, dx1, dy1),
        },
        dict_spinecolor = {
            dir_cp +   '60147.png': 'tab:purple',
        },
        bool_rot90 = True,
    )
    [axin0, axin1, axin2] = plot.inset_img(
        ax,
        dict_img = {
            dir_tt +'1.100001.png': (p_cc[0]-0.5*dx, p_cc[1]-0.5*dy, dx, dy),
            dir_cp +   '60281.png': (p_ct[0]-0.5*dx, p_ct[1]-0.5*dy, dx, dy),
            dir_tt +'0.003922.png': (p_tt[0]-0.5*dx, p_tt[1]-0.5*dy, dx, dy),
        },
        dict_spinecolor = {
            dir_tt +'1.100001.png': 'tab:blue',
            dir_cp +   '60281.png': 'tab:orange', 
            dir_tt +'0.003922.png': 'tab:green',
        }
    )

    headstyle = 'head_length=4, head_width=4'
    # CC
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-t-sx, p_ct+t-sx],
            [p_cc+r+sy, p_xx+t1],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        color = 'tab:blue',
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-r, p_tt-r],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        connectionstyle = 'arc3, rad=0.5',
        color = 'tab:blue',
    )
    plot.add_text(
        axin0,
        dict_text = {
            (0.02, 0.95): f['cc'],
        },
        transform = axin0.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc='tab:blue', lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_ct_cc-sx+0.3*sy): f['cc_ct'],
            tuple(p_xx_cc+sy): f['cc_xx'],
            tuple(p_ct_cc-1.7*r): f['cc_tt'],
            #tuple(p_cc-1.6*r+sy): f['cc_cen']
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:blue', fc='white')
    )

    # CT
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_ct+t+sx, p_cc-t+sx],
            [p_ct-t-sx, p_tt+t-sx],
            [p_ct+r+sy, p_xx-r1+sy],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        color = 'tab:orange',
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_ct-r+[0,0.1], p_ct-r-[0,0.1]],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        connectionstyle = 'arc3, rad=0.4',
        color = 'tab:orange',
    )
    plot.add_text(
        axin1,
        dict_text = {
            (0.02, 0.95): f['ct'],
        },
        transform = axin1.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc='tab:orange', lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_tt_ct-sx+0.3*sy): f['ct_tt'],
            tuple(p_ct_cc+sx-0.3*sy): f['ct_cc'],
            tuple(p_xx_ct+sy): f['ct_xx'],
            tuple(p_ct-r-sx): f['ct_ct'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:orange', fc='white')
    )

    # TT
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_tt+t+sx, p_ct-t+sx],
            [p_tt+r+sy, p_xx-r1-sy*3],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        color = 'tab:green',
    )
    plot.add_text(
        axin2,
        dict_text = {
            (0.02, 0.95): f['tt'],
        },
        transform = axin2.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc='tab:green', lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_tt_ct+sx-0.3*sy): f['tt_ct'],
            tuple(p_xx_tt+sy): f['tt_xx'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:green', fc='white')
    )

    # HCO3
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_xx-r1+sy*3, p_cc+r-sy],
            [p_xx-r1-sy,   p_ct+r-sy],
            [p_xx-t1, p_tt+r-sy],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        color = 'tab:purple',
    )
    plot.add_text(
        axin3,
        dict_text = {
            (0.95, 0.5): f['xx'],
        },
        transform = axin3.transAxes,
        va = 'center',
        ha = 'right',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc='tab:purple', lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_xx_ct-sy): f['xx_ct'],
            tuple(p_xx_cc-sy): f['xx_cc'],
            tuple(p_xx_tt-sy): f['xx_tt'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:purple', fc='white')
    )

def fig_label(
    fig,
    axs,
):

    x = -25/72
    y = 0/72
    dict_pos = {
        '(a)': (x, y),
        '(b)': (x, y),
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

    fig = plt.figure( figsize = (8.6*cm, (4+6)*cm) )

    gs = fig.add_gridspec(2, 1, height_ratios=[6, 4], left=0.15, right=0.99, bottom=0.1, top=0.99, hspace=0.05)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])

    fig_a(ax0)
    fig_b(ax1)

    fig_label(
        fig,
        axs = [ax0,ax1]
    )

    plot.save(
        fig,
        file_save = 'fig_3',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

