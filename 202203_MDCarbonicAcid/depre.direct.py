import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os
import numpy as np
import matplotlib.transforms as mtransforms
import pandas as pd

homedir = os.environ['homedir']

def addimg(ax, list_img, y):
    
    w, h = ax.bbox.width, ax.bbox.height
    dx = 0.2
    dy = 1200/1600*w/h*dx

    sep = 0.2
    nlen = len(list_img)
    dict_img = {}
    for idx, img in enumerate(list_img):
        dict_img[img] = (sep*idx-dx/2+1/2-(nlen-1)/2*sep, y-dy/2, dx, dy)

    plot.inset_img(
        ax,
        dict_img = dict_img,
        spinels = ':',
        spinecolor = 'tab:grey',
        spinelw = 1
    )

def fig_a(
    ax
):

    dirx = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/CC/snap/'
    diry = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_npt/330K/TT/snap/'
    ax.axis('off')
    addimg(
        ax,
        list_img = [
            dirx+'2.035757.png',
            dirx+'2.035762.png',
            dirx+'2.035768.png',
            dirx+'2.035783.png',
        ],
        y = 0.9
    )
    addimg(
        ax,
        list_img = [
            dirx+'10.388854.png',
            dirx+'10.388898.png',
            dirx+'10.388917.png',
        ],
        y = 0.7
    )
    addimg(
        ax,
        list_img = [
            dirx+'11.331220.png',
            dirx+'11.331223.png',
            dirx+'11.331267.png',
            dirx+'11.331276.png',
        ],
        y = 0.5
    )
    addimg(
        ax,
        list_img = [
            diry+'4.094088.png',
            diry+'4.094147.png',
            diry+'4.094196.png',
            diry+'4.094225.png',
            diry+'4.094245.png',
        ],
        y = 0.3
    )
    addimg(
        ax,
        list_img = [
            diry+'7.413039.png',
            diry+'7.413042.png',
            diry+'7.413048.png',
            diry+'7.413141.png',
        ],
        y = 0.1
    )

def fig_label(
    fig,
    axs,
):

    x = -20/72
    y = 0/72
    dict_pos = {
        '(a)': (x, y),
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

    fig = plt.figure( figsize = (8.6*cm, 1.5*5*cm) )

    gs = fig.add_gridspec(1, 1, left=0.01, right=0.99, bottom=0.01, top=0.99)

    ax0 = fig.add_subplot(gs[0])

    fig_a(ax0)

    #fig_label(
    #    fig,
    #    axs = [ax0,ax1,ax2,ax3,ax6]
    #)

    plot.save(
        fig,
        file_save = 'fig_s3',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

