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
    r  = np.array([ dx/2,      0])
    t  = np.array([    0,   dy/2])
    r1 = np.array([dx1/2,      0])
    t1 = np.array([    0,  dy1/2])
    # shift
    sx = np.array([dx/5,   0])
    sy = np.array([   0,dy/5])

    # pos
    yx = 0.03
    p_tt = np.array([0.3, 0.17+yx])
    p_ct = np.array([0.3,  0.5+yx])
    p_cc = np.array([0.3, 0.83+yx])
    p_xx = np.array([0.9,  0.5+yx])
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
        spinecolor = {
            dir_cc + '0.360003.png': c_xx,
        },
        img_rot90 = True,
    )
    [axin0, axin1, axin2] = plot.inset_img(
        ax,
        dict_img = {
            dir_cc +'3.000000.png': (p_cc[0]-0.5*dx, p_cc[1]-0.5*dy, dx, dy),
            dir_cc +'3.067520.png': (p_ct[0]-0.5*dx, p_ct[1]-0.5*dy, dx, dy),
            dir_cc +'3.170878.png': (p_tt[0]-0.5*dx, p_tt[1]-0.5*dy, dx, dy),
        },
        spinecolor = {
            dir_cc +'3.000000.png': c_cc,
            dir_cc +'3.067520.png': c_ct,
            dir_cc +'3.170878.png': c_tt,
        }
    )

    arrowstyle = 'simple, head_length=4, head_width=4, tail_width=0.2'
    arrowkw = {
        'shrinkA': 0
    }
    # CC
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-t-sx, p_ct+t-sx],
            [p_cc+r+sy, p_xx+t1],
        ],
        arrowstyle = arrowstyle,
        color = c_cc,
        **arrowkw
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-r, p_tt-r],
        ],
        arrowstyle = arrowstyle,
        connectionstyle = 'arc3, rad=0.5',
        color = c_cc,
        **arrowkw
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
        axin0,
        dict_text = {
            (0.97, 0.95): 'CC',
        },
        transform = axin0.transAxes,
        va = 'top',
        ha = 'right',
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
        arrowstyle = arrowstyle,
        color = c_ct,
        **arrowkw
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_ct-r+[0,0.1], p_ct-r-[0,0.1]],
        ],
        arrowstyle = arrowstyle,
        connectionstyle = 'arc3, rad=0.4',
        color = c_ct,
        **arrowkw
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
        axin1,
        dict_text = {
            (0.97, 0.95): 'CT',
        },
        transform = axin1.transAxes,
        va = 'top',
        ha = 'right',
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
        arrowstyle = arrowstyle,
        color = c_tt,
        **arrowkw
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
        axin2,
        dict_text = {
            (0.97, 0.95): 'TT',
        },
        transform = axin2.transAxes,
        va = 'top',
        ha = 'right',
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
        arrowstyle = arrowstyle,
        color = c_xx,
        **arrowkw
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
    # ax
    ax.axis('off')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    # rect
    x_v = 0.405
    ax.vlines(x_v, 0.01, 0.99, colors='black', linestyles=':', linewidth=1.5)
    y_a = 0.07
    x_s = 0.01
    plot.add_arrow(
        ax,
        list_arrow = [
            [(x_v-x_s, y_a), (0.01, y_a)],
            [(x_v+x_s, y_a), (0.99, y_a)],
        ],
        arrowstyle = '->, head_length=4, head_width=2',
        **arrowkw
    )
    plot.add_text(
        ax,
        dict_text = {
            ( 0.2 , 0.02): 'Direct Conformational Changes',
            ( 0.65, 0.02): 'Indirect Conformational Changes',
        },
        va = 'bottom',
        ha = 'center',
        fontweight = 'bold',
    )
def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, 7*cm) )

    gs = fig.add_gridspec(1, 1, left=0.01, right=0.99, bottom=0.01, top=0.99)

    ax0 = fig.add_subplot(gs[0])

    fig_a(ax0)

    plot.save(
        fig,
        file_save = 'rate',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

