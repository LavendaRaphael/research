import os
import matplotlib.pyplot as plt
from tf_dpmd_kit import analysis
from tf_dpmd_kit import plot
import matplotlib as mpl
import numpy as np
import json
import pandas as pd
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

def fig_a(ax):
    ax.axis('off')

    # read data
    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'
    fl = {}
    df = pd.read_csv(str_dir+'carbonic_statistic.csv', index_col='state')['rate(M/s)']
    fl['cc'] = df['CC']
    fl['ct'] = df['CT']
    fl['tt'] = df['TT']
    fl['xx'] = df['HCO3']

    df = pd.read_csv(str_dir+'carbonic_flow.csv', index_col=['from','to'])['rate(M/s)']
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

    rate = {}
    for key, value in fl.items():
        value /= 1e8
        rate[key] = f'{value:.2f}'

    plot.add_text(
        ax,
        dict_text = {
            (0.8, 0.95): r'Rate ($\times 10^{8}$ M/s)',
        },
        va = 'top',
        ha = 'right',
    )

    # horizon fig
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.2
    dy = 1200/1600*w/h*dx
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
    p_tt = np.array([0.3, 0.13])
    p_ct = np.array([0.3, 0.5])
    p_cc = np.array([0.3, 0.87])
    p_xx = np.array([0.8, 0.5])
    # middle
    p_tt_ct = (p_tt+p_ct)/2
    p_ct_cc = (p_ct+p_cc)/2
    p_xx_cc = (p_xx-r1+t1+p_cc+r)/2
    p_xx_ct = (p_xx-r1+p_ct+r)/2
    p_xx_tt = (p_xx-r1-t1+p_tt+r)/2

    # color
    alpha = 0.7
    c = mcolors.to_rgb('tab:blue')
    c_cc = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:orange')
    c_ct = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:green')
    c_tt = (c[0], c[1], c[2], alpha)
    c = mcolors.to_rgb('tab:purple')
    c_xx = (c[0], c[1], c[2], alpha)

    # img
    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    dir_tt  = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/TT/plm/'
    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    [axin3] = plot.inset_img(
        ax,
        dict_img = {
            dir_cc + '0.360003.png': (p_xx[0]-0.5*dx1, p_xx[1]-dy1/2, dx1, dy1),
        },
        dict_spinecolor = {
            dir_cc + '0.360003.png': c_xx,
        },
        bool_rot90 = True,
    )
    [axin0, axin1, axin2] = plot.inset_img(
        ax,
        dict_img = {
            dir_cc +'3.000000.png': (p_cc[0]-0.5*dx, p_cc[1]-0.5*dy, dx, dy),
            dir_cc +'3.067520.png': (p_ct[0]-0.5*dx, p_ct[1]-0.5*dy, dx, dy),
            dir_cc +'3.170878.png': (p_tt[0]-0.5*dx, p_tt[1]-0.5*dy, dx, dy),
        },
        dict_spinecolor = {
            dir_cc +'3.000000.png': c_cc,
            dir_cc +'3.067520.png': c_ct, 
            dir_cc +'3.170878.png': c_tt,
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
        color = c_cc,
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-r, p_tt-r],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        connectionstyle = 'arc3, rad=0.5',
        color = c_cc,
    )
    plot.add_text(
        axin0,
        dict_text = {
            (0.03, 0.95): rate['cc'],
        },
        transform = axin0.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc=c_cc, lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_ct_cc-sx+0.3*sy): rate['cc_ct'],
            tuple(p_xx_cc+sy): rate['cc_xx'],
            tuple(p_ct_cc-1.7*r): rate['cc_tt'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec=c_cc, fc='white')
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
        color = c_ct,
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_ct-r+[0,0.1], p_ct-r-[0,0.1]],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        connectionstyle = 'arc3, rad=0.4',
        color = c_ct,
    )
    plot.add_text(
        axin1,
        dict_text = {
            (0.03, 0.95): rate['ct'],
        },
        transform = axin1.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc=c_ct, lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_tt_ct-sx+0.3*sy): rate['ct_tt'],
            tuple(p_ct_cc+sx-0.3*sy): rate['ct_cc'],
            tuple(p_xx_ct+sy): rate['ct_xx'],
            tuple(p_ct-r-sx): rate['ct_ct'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec=c_ct, fc='white')
    )

    # TT
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_tt+t+sx, p_ct-t+sx],
            [p_tt+r+sy, p_xx-r1-sy*3],
        ],
        arrowstyle = f'simple, {headstyle}, tail_width=0.2',
        color = c_tt,
    )
    plot.add_text(
        axin2,
        dict_text = {
            (0.03, 0.95): rate['tt'],
        },
        transform = axin2.transAxes,
        va = 'top',
        ha = 'left',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc=c_tt, lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_tt_ct+sx-0.3*sy): rate['tt_ct'],
            tuple(p_xx_tt+sy): rate['tt_xx'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec=c_tt, fc='white')
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
        color = c_xx,
    )
    plot.add_text(
        axin3,
        dict_text = {
            (0.95, 0.97): rate['xx'],
        },
        transform = axin3.transAxes,
        va = 'top',
        ha = 'right',
        color = 'white',
        fontweight = 'bold',
        bbox = dict(boxstyle='round', fc=c_xx, lw=0)
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_xx_ct-sy): rate['xx_ct'],
            tuple(p_xx_cc-sy): rate['xx_cc'],
            tuple(p_xx_tt-sy): rate['xx_tt'],
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec=c_xx, fc='white')
    )
    # box
    rect = mpatches.Rectangle( (0.06,0.01), 0.324, 0.98, linewidth=1, facecolor = 'None', edgecolor='grey', ls=':')
    ax.add_patch(rect)
    rect = mpatches.Rectangle( (0.384,0.01), 0.45, 0.98, linewidth=1, facecolor = 'None', edgecolor='grey', ls=':')
    ax.add_patch(rect)
    plot.add_text(
        ax,
        dict_text = {
            (0.15, 0.05): 'Direct',
            (0.8, 0.05): 'Indirect',
        },
        va = 'bottom',
        ha = 'right',
    )

def fig_b(ax):

    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    # 
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.18
    dy = 1200/1600*w/h*dx
    y0 = 0.75
    y1 = 0.25
    ax.axis('off')
    plot.inset_img(
        ax,
        dict_img = {
            dir_cc+'1.362850.png': (0.2-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362857.png': (0.4-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362864.png': (0.6-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362871.png': (0.8-dx/2, y0-dy/2, dx, dy),
            dir_cc+'0.355834.png': (0.1-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.355840.png': (0.3-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.360003.png': (0.5-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.363351.png': (0.7-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.363355.png': (0.9-dx/2, y1-dy/2, dx, dy),
        },
        bool_axis = False
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [(0.2 +dx/2-0.01, y0), (0.4 -dx/2+0.01, y0)],
            [(0.4 +dx/2-0.01, y0), (0.6 -dx/2+0.01, y0)],
            [(0.6 +dx/2-0.01, y0), (0.8 -dx/2+0.01, y0)],
            [(0.1 +dx/2-0.01, y1), (0.3 -dx/2+0.01, y1)],
            [(0.3 +dx/2-0.01, y1), (0.5 -dx/2+0.01, y1)],
            [(0.5 +dx/2-0.01, y1), (0.7 -dx/2+0.01, y1)],
            [(0.71+dx/2-0.01, y1), (0.91-dx/2+0.01, y1)],
        ],
        arrowstyle = 'fancy, head_length=6, head_width=6, tail_width=0.01',
        lw = 0,
        color = 'tab:blue'
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.5, 0.95): 'Direct: Dihedral Rotation',
            (0.2, 0.6): '0 ps',
            (0.4, 0.6): '0.07 ps',
            (0.6, 0.6): '0.14 ps',
            (0.8, 0.6): '0.21 ps',
            (0.5, 0.45): 'Indirect: Proton Transfer',
            (0.1, 0.1): '0 ps',
            (0.3, 0.1): '0.06 ps',
            (0.5, 0.1): '41.69 ps',
            (0.7, 0.1): '75.17 ps',
            (0.9, 0.1): '75.21 ps',
        },
        va = 'top',
        ha = 'center',
    )

def fig_label(
    fig,
    axs,
):

    x = 0/72
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

    fig = plt.figure( figsize = (8.6*cm, (5.5+4)*cm) )

    gs = fig.add_gridspec(2, 1, height_ratios=[5.5,4], left=0.01, right=0.99, bottom=0.01, top=0.99, hspace=0.05)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])

    fig_a(ax0)
    fig_b(ax1)

    fig_label(fig, [ax0, ax1])

    plot.save(
        fig,
        file_save = 'fig_4',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

