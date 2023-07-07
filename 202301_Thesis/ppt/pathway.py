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

    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    # 
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.18
    dy = 1200/1600*w/h*dx
    y0 = 0.5
    ax.axis('off')
    plot.inset_img(
        ax,
        dict_img = {
            dir_cc+'1.362850.png': (0.2-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362857.png': (0.4-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362864.png': (0.6-dx/2, y0-dy/2, dx, dy),
            dir_cc+'1.362871.png': (0.8-dx/2, y0-dy/2, dx, dy),
        },
        axin_axis = False
    )
    plot.add_arrow(
        ax,
        list_arrow = [
            [(0.2 +dx/2-0.01, y0), (0.4 -dx/2+0.01, y0)],
            [(0.4 +dx/2-0.01, y0), (0.6 -dx/2+0.01, y0)],
            [(0.6 +dx/2-0.01, y0), (0.8 -dx/2+0.01, y0)],
        ],
        arrowstyle = 'fancy, head_length=6, head_width=6, tail_width=0.01',
        lw = 0,
        color = 'tab:blue'
    )
    plot.add_text(
        ax,
        dict_text = {
            (0.5, 0.9): 'Direct: CT$\Rightarrow$CC',
            (0.2, 0.2): '0 ps',
            (0.4, 0.2): '0.07 ps',
            (0.6, 0.2): '0.14 ps',
            (0.8, 0.2): '0.21 ps',
        },
        va = 'top',
        ha = 'center',
    )

def fig_b(ax):

    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    # 
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.18
    dy = 1200/1600*w/h*dx
    y1 = 0.5
    ax.axis('off')
    plot.inset_img(
        ax,
        dict_img = {
            dir_cc+'0.355834.png': (0.1-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.355840.png': (0.3-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.360003.png': (0.5-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.363351.png': (0.7-dx/2, y1-dy/2, dx, dy),
            dir_cc+'0.363355.png': (0.9-dx/2, y1-dy/2, dx, dy),
        },
        axin_axis = False
    )
    plot.add_arrow(
        ax,
        list_arrow = [
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
            (0.5, 0.9): 'Indirect: CT$\Rightarrow$HCO$_3^-$$\Rightarrow$CC',
            (0.1, 0.2): '0 ps',
            (0.3, 0.2): '0.06 ps',
            (0.5, 0.2): '41.69 ps',
            (0.7, 0.2): '75.17 ps',
            (0.9, 0.2): '75.21 ps',
        },
        va = 'top',
        ha = 'center',
    )
def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.constrained_layout.use'] = False

    fig = plt.figure( figsize = (8.6*cm, (2+2)*cm) )

    gs = fig.add_gridspec(2, 1, height_ratios=[2,2], left=0.01, right=0.99, bottom=0.01, top=0.99, hspace=0.0)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])

    fig_a(ax0)
    fig_b(ax1)

    plot.save(
        fig,
        file_save = 'pathway',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

