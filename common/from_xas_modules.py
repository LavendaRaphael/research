#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.29
#===============================================<<
import csv
import json
import ase.io
import scipy.signal
import numpy
import copy
import sys
import inspect
import math
import os

class class_structures(object):

    @property
    def str_chdir(self):
        return self._str_chdir
    @str_chdir.setter
    def str_chdir(self, str_temp):
        self._str_chdir = str_temp
  
    @property
    def list_atoms(self):
        return self._list_atoms

    @list_atoms.setter
    def list_atoms(self, list_temp):
        float_sum = 0
        for list_i in list_temp: float_sum += list_i[1]
        for list_i in list_temp: list_i[1] /= float_sum
        for list_i in list_temp: list_i[0] = 'atom_'+str(list_i[0])
        self._list_atoms = list_temp

def def_xas_ave( list_atoms, str_outfile = 'xas.ave.csv' ):
#----------------------------------------------[]
# list_atoms = []
# list_atoms.append([ 1,2.0])
#----------------------------------------------[]
    dict_args = locals()
    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))
    
    float_sum = 0
    for list_i in list_atoms: float_sum += list_i[1]
    for list_i in list_atoms: list_i[1] /= float_sum

    str_chdir=list_atoms[0][0]
    os.chdir(str_chdir)
    print(os.getcwd())
    
    float_finalenergy_1 = def_vasp_finalenergy()
    os.chdir('..')

    list_datas = []
    for list_atom in list_atoms:

        str_chdir = list_atom[0]
        float_scaling = list_atom[1]
        os.chdir(str_chdir)
        print(os.getcwd())

        str_xheader, list_yheaders, array_xdata, array_ydatas = def_vasp_outcar2xas()

        float_finalenergy = def_vasp_finalenergy()
        float_sft = float_finalenergy-float_finalenergy_1 
        array_xdata_sft = def_xas_sft( array_xdata=array_xdata, float_sft=float_sft)

        array_xdata = array_xdata_sft
        list_ycolums = list(range(len(array_ydatas[0])))
        list_datas.append( [ array_xdata, array_ydatas, list_ycolums, float_scaling ] )

        os.chdir('..')

    array_xdata_mix, array_ydatas_mix = def_xas_mix(list_datas=list_datas)
    def_xas_writedata( array_xdata=array_xdata_mix, array_ydatas=array_ydatas_mix, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)

def def_weight (alpha,beta):
#----------------------------------------------[]
# Suitable for Dichroism.
#-------------------------[in]
# alpha: float, degree angle
# beta:  float, degree angle
#-------------------------[out]
# list_weight:  list, shape(3)
#               list_weight[1] = list_weight[0]
#               sigma = [sigma_x, sigma_y, sigma_z]*list_weight
#----------------------------------------------[]
    alpha = math.radians (alpha)
    beta = math.radians (beta)
    list_weight = []
    list_weight.append (0.5 * (math.cos(beta)**2 + math.sin(alpha)**2 * math.sin(beta)**2))
    list_weight.append (list_weight[0])
    list_weight.append (math.cos(alpha)**2 * math.sin(beta)**2)
    return list_weight

def def_xas_alignorm( list_alignangle, list_normangle, list_resultangles, str_datfile, float_onset, str_outfile, tuple_xrange = (527.0, 540.0), float_normarea = 20.0 ):
#----------------------------------------------[]
# list_alignangle = [ alpha0, beta0 ]
# list_normangle = [ alpha1, beta1 ]
# list_resultangles = []
# list_resultangles.append( [ alpha2, beta2 ] )
# list_resultangles.append( [ alpha3, beta3 ] )
# float_onset = 530.6
#----------------------------------------------[]
    dict_args = locals()
    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    #--------------------------------------------------[extract]
    int_xcolumn = 0
    list_ycolumns = [1,2,3]
    _, _, array_xdata_origin, array_ydatas_origin = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list_ycolumns=list_ycolumns )
    
    #--------------------------------------------------[align]
    alpha = list_alignangle[0]
    beta = list_alignangle[1]
    array_xdata = array_xdata_origin
    array_ydatas = array_ydatas_origin
    list_weight = def_weight (alpha,beta)
    list_datas = []
    list_datas.append( [array_xdata, array_ydatas, [0], list_weight[0]] )
    list_datas.append( [array_xdata, array_ydatas, [1], list_weight[1]] )
    list_datas.append( [array_xdata, array_ydatas, [2], list_weight[2]] )
    array_xdata_mix, array_ydatas_mix = def_xas_mix( list_datas=list_datas )
    
    array_xdata = array_xdata_mix
    array_ydatas = array_ydatas_mix
    float_relheight = 0.4
    float_relprominence = 0.02
    list_peaks = def_xas_findpeaks( array_xdata=array_xdata, array_ydatas=array_ydatas, float_relheight=float_relheight, float_relprominence=float_relprominence )
    
    array_xdata = array_xdata_mix
    float_sft = float_onset - list_peaks[0]
    array_xdata_align = def_xas_sft( array_xdata=array_xdata, float_sft=float_sft)
    #--------------------------------------------------[norm]
    alpha = list_normangle[0]
    beta = list_normangle[1]
    array_xdata = array_xdata_align
    array_ydatas = array_ydatas_origin
    list_weight = def_weight (alpha,beta)
    list_datas = []
    list_datas.append( [array_xdata, array_ydatas, [0], list_weight[0]] )
    list_datas.append( [array_xdata, array_ydatas, [1], list_weight[1]] )
    list_datas.append( [array_xdata, array_ydatas, [2], list_weight[2]] )
    _, array_ydatas_mix = def_xas_mix( list_datas=list_datas)
    
    array_xdata = array_xdata_align
    array_ydatas = array_ydatas_mix
    float_area = def_xas_findarea( array_xdata=array_xdata, array_ydatas=array_ydatas, tuple_xrange=tuple_xrange)
    
    array_ydatas = array_ydatas_origin
    float_scaling = float_normarea/float_area
    list_datas=[]
    list_datas.append( [array_xdata, array_ydatas, [0,1,2], float_scaling] )
    _, array_ydatas_mix = def_xas_mix( list_datas )

    array_ydatas_save = array_ydatas_mix 
    #--------------------------------------------------[mix]
 
    str_xheader = 'E(eV)'
    list_yheaders = []
    array_ydatas_final = numpy.empty( shape=(len(array_xdata), len(list_resultangles)) )
  
    for int_i in range(len(list_resultangles)):
        alpha, beta = list_resultangles[int_i]
        str_yheader = 'a'+str(alpha)+'_b'+str(beta)
        list_yheaders.append( str_yheader )
   
        array_xdata = array_xdata_align
        array_ydatas = array_ydatas_save
    
        list_weight = def_weight (alpha,beta)
        list_datas = []
        list_datas.append( [array_xdata, array_ydatas, [0], list_weight[0]] )
        list_datas.append( [array_xdata, array_ydatas, [1], list_weight[1]] )
        list_datas.append( [array_xdata, array_ydatas, [2], list_weight[2]] )
        _, array_ydatas_mix = def_xas_mix( list_datas=list_datas )
        array_ydatas_final[:,int_i] = array_ydatas_mix[:,0]
    
    array_xdata = array_xdata_align
    array_ydatas = array_ydatas_final
    def_xas_writedata( array_xdata=array_xdata, array_ydatas=array_ydatas, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)

    def_endfunc()
    return

def def_startfunc():
    this_function_name = inspect.currentframe().f_back.f_code.co_name
    print("#"+'-'*20+"["+this_function_name+"]\n")

def def_endfunc():
    print("#"+'-'*20+"<<\n")

def def_vasp_finalenergy():
    dict_args = locals()

    def_startfunc()

    float_finalenergy = ase.io.read( filename='OUTCAR' ).get_total_energy()
    print( json.dumps({'float_finalenergy': float_finalenergy}, indent=4))

    def_endfunc()
    return float_finalenergy

def def_vasp_outcar2xas():
    def_startfunc()

    str_tempfile = 'outcar2xas.tmp'
    with open( 'OUTCAR', 'r' ) as obj_datfile:
        for str_line in obj_datfile:
            if (str_line.strip() == 'frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects) density-density'):
                break
        with open( str_tempfile, mode='w' ) as obj_tmp: 
            str_line = next(obj_datfile)
            obj_tmp.write( str_line )
            str_line = next(obj_datfile)
            for str_line in obj_datfile:
                if (not str_line.strip()): break
                obj_tmp.write( str_line )
    str_datfile = str_tempfile
    int_xcolumn = 0
    list_ycolumns = [1,2,3]
    str_xheader, list_yheaders, array_xdata, array_ydatas = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list_ycolumns=list_ycolumns )
    for int_i in range(len(array_xdata)):
        array_ydatas[int_i,:] *= array_xdata[int_i]

    os.remove( str_tempfile )

    def_endfunc()
    return str_xheader, list_yheaders, array_xdata, array_ydatas

def def_xas_sft( array_xdata, float_sft):
    dict_args = locals()
    del dict_args['array_xdata'] 

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    array_xdata_sft = array_xdata + float_sft

    def_endfunc()
    return array_xdata_sft

def def_xas_writedata( array_xdata, array_ydatas, str_xheader, list_yheaders, str_outfile):
    dict_args = locals()
    del dict_args['array_xdata']
    del dict_args['array_ydatas']

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    with open( str_outfile, 'w', newline='' ) as obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',' )
        obj_outwriter.writerow( [str_xheader] + list_yheaders )
        for int_i in range(len( array_xdata )):
            obj_outwriter.writerow( [ array_xdata[int_i] ] + array_ydatas[int_i].tolist() )

    def_endfunc()
    return

def def_xas_findarea( array_xdata, array_ydatas, tuple_xrange):
    dict_args = locals()
    del dict_args['array_xdata']
    del dict_args['array_ydatas']

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    array_ydata = numpy.reshape( a=array_ydatas, newshape=-1 )
 
    array_x_new=[]
    array_y_new=[]

    for int_i in range(len(array_xdata)):
        float_x = array_xdata[int_i]
        float_y = array_ydata[int_i]
        if ( float_x > tuple_xrange[0] and float_x < tuple_xrange[1] ):
            array_x_new.append( float_x )
            array_y_new.append( float_y )

    float_area = numpy.trapz( y=array_y_new, x=array_x_new )
    print(json.dumps( obj={'float_area':float_area}, indent=4))

    def_endfunc()
    return float_area

def def_xas_findpeaks( array_xdata, array_ydatas, float_relheight, float_relprominence ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()
    del dict_args['array_xdata']
    del dict_args['array_ydatas']

    def_startfunc()
    print( json.dumps( obj=dict_args, indent=4 ))

    array_ydata = numpy.reshape( a=array_ydatas, newshape=-1 )

    float_y_max = max(array_ydata)
    height = float_relheight * float_y_max

    prominence = float_relprominence * float_y_max

    list_peaks_indices, dict_properties = scipy.signal.find_peaks( array_ydata, height = height, prominence=prominence )
    
    list_print = []
    list_print.append( ['Energy (eV)', 'Intensity/Max','prominences/Max'] )
    int_count = 0
    list_peaks = []
    for i in list_peaks_indices:
        list_peaks.append( array_xdata[i] )
        list_print.append( [array_xdata[i], array_ydata[i]/float_y_max, dict_properties['prominences'][int_count]/float_y_max] )
        int_count += 1
    print( json.dumps( obj=list_print, indent=4 ) )

    def_endfunc()
    return list_peaks

def def_xas_mix(list_datas):
#------------------------------[]
# list_datas = []
# list_datas.append( [ array_xdata, array_ydatas, [0,2], 0.7 ] )
#------------------------------[]
    dict_args = copy.deepcopy(locals())
    for list_temp in dict_args['list_datas']:
        del list_temp[0:2]

    def_startfunc()
    print(json.dumps( obj=dict_args,  indent=4 ))
    
    float_xl = float('-inf')
    float_xr = float('+inf')
    for list_data in list_datas:
        array_xdata = list_data[0]
        float_xl = max( float_xl, numpy.amin( array_xdata ))
        float_xr = min( float_xr, numpy.amax( array_xdata )) 
    
    dict_json = {}
    dict_json[ 'float_xl' ] = float_xl
    dict_json[ 'float_xr' ] = float_xr
    print( json.dumps( dict_json, indent=4 ) )
    
    int_lendata = len(array_xdata)
    int_lenycolumns = len(list_datas[0][2])
    dict_json = {}
    dict_json[ 'int_lendata' ] = int_lendata
    dict_json[ 'int_lenycolumns' ] = int_lenycolumns
    print( json.dumps( dict_json, indent=4 ) )
    
    array_xdata_mix = numpy.linspace( start=float_xl, stop=float_xr, num=int_lendata )

    array_ydatas_mix = numpy.zeros( shape=(int_lendata, int_lenycolumns) )
    for list_datai in list_datas:
        array_xdata = list_datai[0]
        array_ydatas = list_datai[1]
        list_ycolumns = list_datai[2]
        float_scaling = list_datai[3]
        array_ydatas = array_ydatas[ :, list_ycolumns ]
        for int_i in range(int_lenycolumns):
            array_ydatas[:,int_i] = numpy.interp( x=array_xdata_mix, xp=array_xdata, fp=array_ydatas[:,int_i] )

        array_ydatas_mix += array_ydatas * float_scaling

    def_endfunc()
    return array_xdata_mix, array_ydatas_mix

def def_xas_extract( str_datfile, int_xcolumn, list_ycolumns ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()

    def_startfunc()
    print(json.dumps( obj=dict_args,  indent=4 ))
    
    list_xdata = []
    list_ydatas = []

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ), delimiter= ' ', skipinitialspace=True )
        list_line = next(obj_datreader)
        list_line = next(obj_datreader)
        if (',' in list_line[0]):
            delimiter=','
        else:
            delimiter=' '
    print(json.dumps({'delimiter': delimiter},indent=4))

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ), delimiter=delimiter, skipinitialspace=True )
        list_line = next(obj_datreader)
        str_xheader = list_line[int_xcolumn]
        list_yheaders = [ list_line[i] for i in list_ycolumns ]
        print(json.dumps({'str_xheader': str_xheader},indent=4))
        print(json.dumps({'list_yheaders': list_yheaders}, indent=4))
        for list_line in obj_datreader:
            if ( not list_line[ int_xcolumn ] ): continue
            list_xdata.append( float(list_line[int_xcolumn]) )
            list_temp = []
            for int_i in list_ycolumns:
                list_temp.append( float(list_line[int_i]) )
            list_ydatas.append( list_temp )
    array_xdata = numpy.array( list_xdata )
    array_ydatas = numpy.array( list_ydatas )

    int_lendata = len(list_xdata)
    print(json.dumps({ 'int_lendata': int_lendata },indent=4))
 
    def_endfunc()
    return str_xheader, list_yheaders, array_xdata, array_ydatas

