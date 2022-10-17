import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from matplotlib.lines import Line2D

def run(
    dict_file: dict,
    str_save: str = None
) -> None:

    rc('font',**{'size':15, 'family':'sans-serif','sans-serif':['Arial']})
    
    fig, ax = plt.subplots()

    for str_file, str_marker in zip(dict_file, Line2D.filled_markers):
        str_label = dict_file[str_file]
        np_data = np.loadtxt(str_file)
        ax.errorbar(np_data[:,0], np_data[:,1], yerr=np_data[:,2], linestyle=':', marker=str_marker, label=str_label, capsize=3)

    ax.set_xlabel(r'Temperature (${^\circ}C$)')
    ax.set_ylabel('pKa')
    ax.legend()
    if str_save:
        fig.set_size_inches(6, 5)
        fig.savefig(str_save, bbox_inches='tight', dpi=300)

run(
    dict_file = {
        '2019_PNAS_DanielAminov/Fig_1.csv': '2019 Daniel Aminov',
        '2010_JPCA_WangXiaoguang/Sfig_3.csv': '2010 Xiaoguang Wang'
    },
    str_save = 'exp_pka.pdf'
)

plt.show()
