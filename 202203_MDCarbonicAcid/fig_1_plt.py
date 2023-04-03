import matplotlib.pyplot as plt
import matplotlib as mpl
from tf_dpmd_kit import plot
from tf_dpmd_kit import train
import os

plot.set_rcparam()
cm = 1/2.54
homedir = os.environ['homedir']
mpl.rcParams['figure.dpi'] = 300

def fig_a(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        str_file = str_dir+'dptest.e.out',
        int_natoms = 384,
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
    )

def fig_b(
    ax
):

    str_dir = homedir+'/research_d/202203_MDCarbonicAcid/server/03.train/03.iter17_initmodel/03.rmse_val.npt/'
    train.dptest_parity_plt(
        ax,
        str_file = str_dir+'dptest.f.out',
        float_lw = 0.75,
        list_ticks = [-5, 0, 5],
    )

def fig_c(
    axs
):

    str_dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/rdf/'
    str_dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt/330K/TT/rdf/'
    plot.plt_subplots(
        axs,
        dict_title = {
            'tt_h_oh.o_w': r'H$_{OH}$-O$_W$',
            'tt_o_oh.h_w': r'O$_{OH}$-H$_W$',
            'tt_o_c.h_w': r'$^=$O-H$_W$',
        },
        dict2d_data ={
            'DPMD': {
                'tt_h_oh.o_w': str_dir_dpmd+'rdf.tt_h_oh.o_w.ave.csv',
                'tt_o_oh.h_w': str_dir_dpmd+'rdf.tt_o_oh.h_w.ave.csv',
                'tt_o_c.h_w': str_dir_dpmd+'rdf.tt_o_c.h_w.ave.csv',
            },
            'AIMD': {
                'tt_h_oh.o_w': str_dir_aimd+'rdf.h_0_1.o_w.ave.csv',
                'tt_o_oh.h_w': str_dir_aimd+'rdf.o_0_2.h_w.ave.csv',
                'tt_o_c.h_w': str_dir_aimd+'rdf.o_1.h_w.ave.csv',
            },
        },
        str_xlabel = 'r (Å)',
        str_ylabel = 'g(r)',
        tup_xlim = (1,6),
        dict_ylim = {
            'tt_h_oh.o_w': (0,3),
            'tt_o_oh.h_w': (0,2),
            'tt_o_c.h_w': (0,2),
        },
        dict_legend = {
            'tt_o_oh.h_w': True
        },
        float_lw = 1,
    )

def fig_d(
    ax
):

    str_dir_aimd = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/rdf/'
    str_dir_dpmd = '/home/faye/research_d/202203_MDCarbonicAcid/server/04.md_nvt/330K/TT/rdf/'
    plot.plt_subplots(
        ax,
        dict_title = {
            'o_w.o_w': r'O$_W$-O$_W$'
        },
        dict2d_data ={
            'DPMD': {
                'o_w.o_w': str_dir_dpmd+'rdf.o_w.o_w.ave.csv',
            },
            'AIMD': {
                'o_w.o_w': str_dir_aimd+'rdf.o_w.o_w.ave.csv',
            },
        },
        str_xlabel = 'r (Å)',
        str_ylabel = 'g(r)',
        tup_xlim = (1,6),
        dict_ylim = {
            'o_w.o_w': (0,4),
        },
        dict_legend = {},
        float_lw = 1,
    )

def fig_e(
    ax,
):
    ax.axis('off')
    str_dir = '/home/faye/research_d/202203_MDCarbonicAcid/server/01.init/H2CO3_TT_H2O_126/plm/'
    image = plt.imread(str_dir+'33732.png')
    ax.imshow(image)

    plot.add_text(
        ax,
        dict_text = {
            (700,250)  :r'O$_W$'    ,      
            (1000,400) :r'H$_W$'    ,      
            (600,600)  :r'$^=$O'    ,      
            (1300,765) :r'H$_{OH}$' ,   
            (1200,1050):r'O$_{OH}$' ,   
        },
        ha = 'center',
        va = 'center',
    )

def fig_label(
    dict_ax,
):
    dict_pos = {
        '(a)': (-0.15, 0.9),
        '(b)': (-0.2, 0.9),
        '(c)': (-0.2, 0.9),
        '(d)': (-0.2, 0.9),
        '(e)': (-0.1, 0.9),
    }
    for label, ax in dict_ax.items():
        pos = dict_pos[label]
        ax.text(
            x = pos[0],
            y = pos[1],
            s = label,
            transform = ax.transAxes,
        )

def run():

    fig = plt.figure( figsize = (8.6*cm, 10*cm))

    subfigs0 = fig.subfigures(2, 1, height_ratios=[35, 65])
    (ax0, ax1) = subfigs0[0].subplots(1, 2)
    subfigs1 = subfigs0[1].subfigures(1, 2)

    axs1 = subfigs1[0].subplots(3, 1, sharex='all')
    subfigs2 = subfigs1[1].subfigures(2, 1, height_ratios=[0.7, 1])

    ax2 = subfigs2[0].subplots()
    ax3 = subfigs2[1].subplots()
    
    fig_a(ax0)
    fig_b(ax1)
    fig_c(axs1)
    fig_d(ax2)
    fig_e(ax3)

    fig_label(
        dict_ax = {
            '(a)': ax0,
            '(b)': ax1,
            '(c)': axs1[0],
            '(d)': ax2,
            '(e)': ax3,
        }
    )

    plot.save(
        fig,
        file_save = 'fig_1',
        list_type = ['pdf', 'svg']
    )

run()

plt.show()

