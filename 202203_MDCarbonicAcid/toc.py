import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import pandas as pd

def fig_c(ax):

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

    ax.pie(
        [81.32, 12.38, 0.28, 5.82],
        explode = (0.1, 0.1, 0.1, 0.1),
        colors = [c_cc, c_ct, c_tt, c_xx],
        labeldistance=.6,
    )
    plot.add_text(
        ax,
        dict_text = {
            (-0.7, 0.3): 'CC', 
            (0.5, -0.7): 'CT', 
        },
        color = 'white',
        fontweight = 'bold',
    )
    plot.add_text(
        ax,
        dict_text = {
            (1.05, -0.6): 'TT', 
            (0.95, 0.05): 'HCO$_3^-$', 
        },
    )
    ax.set_xlim(None, 1.7)

def fig_b(ax):
    layer_text = {
        (0, 0): 'R',
        (3, 0): 'E'
    }
    layer_sizes = [1, 4, 4, 1]
    colors='tab:green'
    left=.1
    right=.9
    bottom=.1
    top=.9
    rwidth = 0.15
    w, h = ax.bbox.width, ax.bbox.height
    rheight = rwidth/h*w

    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for m in range(layer_size):
            if isinstance(colors, str):
                color = colors
            else:
                color = colors[n]
            circle = mpatches.Ellipse((n*h_spacing + left, layer_top - m*v_spacing), rwidth, rheight,
                                color=color, zorder=4, lw=0.5)
            ax.add_artist(circle)
            # Node annotations
            if (n, m) in layer_text:
                ax.text(
                    x = n*h_spacing + left,
                    y = layer_top - m*v_spacing - 0.005,
                    s = layer_text[(n,m)],
                    color = 'white',
                    weight = 'bold',
                    style = 'italic',
                    zorder=5, 
                    ha='center', va='center')
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k', lw=0.5)
                ax.add_artist(line)
    
    ax.axis('off')

def fig_a(ax):

    # read data
    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/carbonic/'

    # horizon fig
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.45
    dy = 1200/1600*w/h*dx
    # vertical fig
    dx1 = dy*h/w
    dy1 = dx*w/h

    # right, top
    r  = np.array([ dx/2,      0])
    t  = np.array([    0,   dy/2])
    r1 = np.array([dx1/2,      0])
    t1 = np.array([    0,  dy1/2])

    # pos
    p_tt = np.array([0.25, 0.17])
    p_ct = np.array([0.25,  0.5])
    p_cc = np.array([0.25, 0.83])
    p_xx = np.array([0.85,  0.5])

    # img
    dir_cp  = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_CC_H2O_126/plm/'
    dir_tt  = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt_velocity/330K/TT/plm/'
    dir_cc = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    [axin3] = plot.inset_img(
        ax,
        dict_img = {
            dir_cc + '0.360003.png': (p_xx[0]-0.5*dx1, p_xx[1]-dy1/2, dx1, dy1),
        },
        img_rot90 = True,
        axin_axis = False,
    )
    [axin0, axin1, axin2] = plot.inset_img(
        ax,
        dict_img = {
            dir_cc +'3.000000.png': (p_cc[0]-0.5*dx, p_cc[1]-0.5*dy, dx, dy),
            dir_cc +'3.067520.png': (p_ct[0]-0.5*dx, p_ct[1]-0.5*dy, dx, dy),
            dir_cc +'3.170878.png': (p_tt[0]-0.5*dx, p_tt[1]-0.5*dy, dx, dy),
        },
        axin_axis = False,
    )

    plot.add_text(
        axin0,
        dict_text = {
            (0.03, 0.95): 'CC',
        },
        transform = axin0.transAxes,
        va = 'top',
        ha = 'left',
        fontweight = 'bold'
    )
    plot.add_text(
        axin1,
        dict_text = {
            (0.03, 0.95): 'CT',
        },
        transform = axin1.transAxes,
        va = 'top',
        ha = 'left',
        fontweight = 'bold'
    )
    plot.add_text(
        axin2,
        dict_text = {
            (0.03, 0.95): 'TT',
        },
        transform = axin2.transAxes,
        va = 'top',
        ha = 'left',
        fontweight = 'bold'
    )

    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-t , p_ct+t],
            [p_ct-t , p_tt+t],
            [p_xx+t1, p_cc+r],
            [p_xx-r1, p_ct+r],
            [p_xx-t1, p_tt+r],
        ],
        arrowstyle = '<|-|>, head_length=2, head_width=2',
        shrinkA = 0, 
        shrinkB = 0,
        color = 'tab:blue'
    )
    # ax
    ax.axis('off')
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)

def main():

    plot.set_rcparam()
    mpl.rcParams['figure.dpi'] = 400
    mpl.rcParams['figure.constrained_layout.use'] = False
    
    fig = plt.figure( figsize = (2.9, 1.57) )

    gs = fig.add_gridspec(1, 3, width_ratios=[1.2, 0.7, 1], left=0.0, right=1, bottom=0.0, top=1, wspace=0)

    ax0 = fig.add_subplot(gs[0])
    ax1 = fig.add_subplot(gs[1])
    ax2 = fig.add_subplot(gs[2])
    fig_a(ax0)
    fig_b(ax1)
    fig_c(ax2)

    plot.save(
        fig,
        file_save = 'toc',
        list_type = ['pdf', 'svg', 'tif']
    )
    
    plt.show()

main()

