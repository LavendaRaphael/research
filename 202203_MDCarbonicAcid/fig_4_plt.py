import os
import matplotlib.pyplot as plt
from tf_dpmd_kit import analysis
from tf_dpmd_kit import plot
import matplotlib as mpl
import numpy as np

def fig_a(
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

def fig_b(ax):
    ax.axis('off')

    f_cc = 0.46
    f_ct = 0.71
    f_tt = 0.12
    f_xx = 1.05
    f_tt_ct = 0.02
    f_tt_xx = '0.10'
    f_ct_tt = 0.03
    f_ct_ct = 0.01
    f_ct_xx = '0.60'
    f_ct_cc = 0.08
    f_xx_tt = 0.09
    f_xx_ct = 0.59
    f_xx_cc = 0.37
    f_cc_tt = 0.01
    f_cc_ct = 0.09
    f_cc_xx = 0.35
    f_cc_cen = 0.02
    f_cen_cc = 0.02

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
    p_tt = np.array([1.2*dx, dy/2])
    p_ct = np.array([1.2*dx, 0.5])
    p_cc = np.array([1.2*dx, 1-dy/2])
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
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-r+sy, p_cc-2.2*r+sy],
        ],
        arrowstyle = f'-',
        color = 'tab:blue',
        shrinkA=5, shrinkB=5,
        linestyle = ':'
    ),
    plot.add_arrow(
        ax,
        list_arrow = [
            [p_cc-r+sy, p_cc-2.2*r+sy],
        ],
        arrowstyle = f'<|-|>, head_length=4, head_width=2',
        color = 'tab:blue',
        linewidth = 0,
    )
    plot.add_text(
        axin0,
        dict_text = {
            (0.02, 0.95): f_cc,
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
            tuple(p_ct_cc-sx+0.3*sy): f_cc_ct,
            tuple(p_xx_cc+sy): f_cc_xx,
            tuple(p_ct_cc-1.7*r): f_cc_tt,
            tuple(p_cc-1.6*r+sy): f_cc_cen
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:blue', fc='white')
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_cc-1.6*r+2*sy): 'Censored',
        },
        va = 'center',
        ha = 'center',
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
            (0.02, 0.95): f_ct,
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
            tuple(p_tt_ct-sx+0.3*sy): f_ct_tt,
            tuple(p_ct_cc+sx-0.3*sy): f_ct_cc,
            tuple(p_xx_ct+sy): f_ct_xx,
            tuple(p_ct-r-sx): f_ct_ct,
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:orange', fc='white')
    )
    plot.add_text(
        ax,
        dict_text = {
            tuple(p_ct-r-sx+sy): 'TS',
        },
        va = 'center',
        ha = 'center',
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
            (0.02, 0.95): f_tt,
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
            tuple(p_tt_ct+sx-0.3*sy): f_tt_ct,
            tuple(p_xx_tt+sy): f_tt_xx,
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
            (0.95, 0.5): f_xx,
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
            tuple(p_xx_ct-sy): f_xx_ct,
            tuple(p_xx_cc-sy): f_xx_cc,
            tuple(p_xx_tt-sy): f_xx_tt,
        },
        va = 'center',
        ha = 'center',
        bbox = dict(boxstyle='round', ec='tab:purple', fc='white')
    )

    plot.add_text(
        ax,
        dict_text = {
            (0.9, 0.95): r'Frequency (ns$^{-1}$)',
        },
        va = 'top',
        ha = 'right',
    )

def fig_label(
    list_ax,
):

    dict_pos = {
        '(a)': (-0.1, 0.9),
        '(b)': (0, 1),
    }
    for ax, label in zip(list_ax, dict_pos):
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
        )

def main():

    plot.set_rcparam()
    cm = 1/2.54
    mpl.rcParams['figure.dpi'] = 300
    homedir = os.environ['homedir']

    fig = plt.figure(figsize=(8.6*cm, (4+6)*cm))
    (sfig0, sfig1) = fig.subfigures(2, 1, height_ratios=[4,6])
    ax0 = sfig0.subplots()
    ax1 = sfig1.subplots()

    fig_a(ax0)
    fig_b(ax1)

    fig_label([ax0, ax1])

    plot.save(
        fig,
        file_save = 'fig_4',
        list_type = ['pdf', 'svg']
    )

    plt.show()

main()

