import from_xas_modules
import os
import matplotlib.pyplot as plt

str_110=os.environ['goto_pto_work_110']
str_chdir = str_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11'
os.chdir( str_chdir )

list1d_xheader, list1d_yheader, array2d_xdata, array2d_ydata = from_xas_modules.def_vasp_outcar2xas()

float_eigcore = -514.703961144

list3d_angle = []
list3d_angle.append( [[0, 90]] )
list3d_angle.append( [[90, 45]] )
plt.xlim(515,525)
for list2d_angle in list3d_angle:
    list1d_yheader, array2d_ydata_alphabeta = from_xas_modules.def_xas_alphabeta( list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )
    list1d_peakx = from_xas_modules.def_xas_findpeaks( array2d_xdata=array2d_xdata, array2d_ydata=array2d_ydata_alphabeta)
    float_e_pcore = list1d_peakx[0] + float_eigcore
    from_xas_modules.def_print_paras( locals(), ['float_e_pcore'])