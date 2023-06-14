import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
import os

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

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300

    fig, ax = plt.subplots(1, 1, figsize = (8.6*cm, 7*cm))

    fig_a(ax)

    plot.save(
        fig,
        file_save = 'fig_s5',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()


