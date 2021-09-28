#!/bin/env python
import math
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

def def_weight (alpha,beta):
    alpha = math.radians (alpha)
    beta = math.radians (beta)
    result = []
    result.append (0.5 * (math.cos(beta)**2 + math.sin(alpha)**2 * math.sin(beta)**2))
    result.append (result[0])
    result.append (math.cos(alpha)**2 * math.sin(beta)**2)
    return result

list_dirs=[]
list_dirs.append('Pt.110.x12y2z4.5_O22_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O1_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O6_vac15/')

for str_dir in list_dirs:
    str_dir = str_110+str_dir+'vasp_sch/'
    os.chdir(str_dir)

    #----------------------------------[Pt.111]
    #str_datfile = 'xas.dat'
    #float_onset = 530.1
    
    #----------------------------------[Pt.110]
    str_datfile = 'xas_ave.dat'
    float_onset = 529.6
    
    #--------------------------------------------------[extract]
    int_xcolumn = 0
    list_ycolumns = [1,2,3]
    _, _, array_xdata_origin, array_ydatas_origin = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list_ycolumns=list_ycolumns )
    
    #--------------------------------------------------[sft]
    list_datas = [ arrayt_xdata_origin, array_ydatas_origin, [2], 1.0) ]
    array_xdata_mix, array_ydatas_mix = def_xas_mix( array_datas=array_datas )
    
    array_xdata = array_xdata_mix
    array_ydatas = array_ydatas_mix
    float_relheight = 0.4
    float_relprominence = 0.02
    list_peaks = def_xas_findpeaks( array_xdata=array_xdata, array_ydatas=array_ydatas, float_relheight=float_relheight, float_relprominence=float_relprominence )
    
    array_xdata = array_xdata_mix
    float_sft = float_onset - list_peaks[0]
    array_xdata_sft = def_xas_sft( array_xdata=array_xdata, float_sft=float_sft)
    
    #--------------------------------------------------[mix]
    beta = 90
    
    list_alpha=[20,41]
    
    for alpha in list_alpha:
        str_outfile = 'xas_a'+str(alpha)+'_b'+str(beta)+'.csv'
        array_xdata = array_xdata_sft
        array_ydatas = array_ydatas_origin
        list_weight = def_weight (alpha,beta)
        list_datas = []
        list_datas.append( (array_xdata, array_ydatas, [0], list_weight[0]) )
        list_datas.append( (array_xdata, array_ydatas, [1], list_weight[1]) )
        list_datas.append( (array_xdata, array_ydatas, [2], list_weight[2]) )
        array_xdata_mix, array_ydatas_mix = def_xas_mix( list_datas=list_datas)
        
        #--------------------------------------------------[norm]
        array_xdata = array_xdata_mix
        array_ydatas = array_ydatas_mix
        tuple_xrange = (527.0, 540.0)
        float_area = def_xas_findarea( array_xdata=array_xdata, array_ydatas=array_ydatas, tuple_xrange=tuple_xrange)
        
        float_normarea = 20.0
        float_scaling = float_normarea/float_area
        list_datas=[]
        list_datas.append( [array_xdata, array_ydatas, [0], float_scaling] )
        array_xdata_mix, array_ydatas_mix = def_xas_mix( list_datas )
        
        #--------------------------------------------------[write]
        array_xdata = array_xdata_mix
        array_ydatas = array_ydatas_mix
        str_xheader = 'E(eV)'
        list_yheaders = ['Intensity']
        def_xas_writedata( array_xdata=array_xdata, array_ydatas=array_ydatas, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)
