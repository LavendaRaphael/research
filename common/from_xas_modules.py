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

    list2d_data = []
    for list_atom in list_atoms:

        str_chdir = list_atom[0]
        float_scaling = list_atom[1]
        os.chdir(str_chdir)
        print(os.getcwd())

        str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_vasp_outcar2xas()

        float_finalenergy = def_vasp_finalenergy()
        float_sft = float_finalenergy-float_finalenergy_1 
        array1d_xdata_sft = def_xas_sft( array1d_xdata=array1d_xdata, float_sft=float_sft)

        array1d_xdata = array1d_xdata_sft
        list_ycolums = list(range(len(array2d_ydata[0])))
        list2d_data.append( [ array1d_xdata, array2d_ydata, list_ycolums, float_scaling ] )

        os.chdir('..')

    array1d_xdata_mix, array2d_ydata_mix = def_xas_mix(list2d_data=list2d_data)
    def_xas_writedata( array1d_xdata=array1d_xdata_mix, array2d_ydata=array2d_ydata_mix, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)

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
    list1d_ycolumn = [1,2,3]
    _, _, array1d_xdata_origin, array2d_ydata_origin = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list1d_ycolumn=list1d_ycolumn )
    
    #--------------------------------------------------[align]
    alpha = list_alignangle[0]
    beta = list_alignangle[1]
    array1d_xdata = array1d_xdata_origin
    array2d_ydata = array2d_ydata_origin
    list_weight = def_weight (alpha,beta)
    list2d_data = []
    list2d_data.append( [array1d_xdata, array2d_ydata, [0], list_weight[0]] )
    list2d_data.append( [array1d_xdata, array2d_ydata, [1], list_weight[1]] )
    list2d_data.append( [array1d_xdata, array2d_ydata, [2], list_weight[2]] )
    array1d_xdata_mix, array2d_ydata_mix = def_xas_mix( list2d_data=list2d_data )
    
    array1d_xdata = array1d_xdata_mix
    array2d_ydata = array2d_ydata_mix
    float_relheight = 0.4
    float_relprominence = 0.02
    list_peaks = def_xas_findpeaks( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, float_relheight=float_relheight, float_relprominence=float_relprominence )
    
    array1d_xdata = array1d_xdata_mix
    float_sft = float_onset - list_peaks[0]
    array1d_xdata_align = def_xas_sft( array1d_xdata=array1d_xdata, float_sft=float_sft)
    #--------------------------------------------------[norm]
    alpha = list_normangle[0]
    beta = list_normangle[1]
    array1d_xdata = array1d_xdata_align
    array2d_ydata = array2d_ydata_origin
    list_weight = def_weight (alpha,beta)
    list2d_data = []
    list2d_data.append( [array1d_xdata, array2d_ydata, [0], list_weight[0]] )
    list2d_data.append( [array1d_xdata, array2d_ydata, [1], list_weight[1]] )
    list2d_data.append( [array1d_xdata, array2d_ydata, [2], list_weight[2]] )
    _, array2d_ydata_mix = def_xas_mix( list2d_data=list2d_data)
    
    array1d_xdata = array1d_xdata_align
    array2d_ydata = array2d_ydata_mix
    float_area = def_xas_findarea( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, tuple_xrange=tuple_xrange)
    
    array2d_ydata = array2d_ydata_origin
    float_scaling = float_normarea/float_area
    list2d_data=[]
    list2d_data.append( [array1d_xdata, array2d_ydata, [0,1,2], float_scaling] )
    _, array2d_ydata_mix = def_xas_mix( list2d_data )

    array2d_ydata_save = array2d_ydata_mix 
    #--------------------------------------------------[mix]
 
    str_xheader = 'E(eV)'
    list_yheaders = []
    array2d_ydata_final = numpy.empty( shape=(len(array1d_xdata), len(list_resultangles)) )
  
    for int_i in range(len(list_resultangles)):
        alpha, beta = list_resultangles[int_i]
        str_yheader = 'a'+str(alpha)+'_b'+str(beta)
        list_yheaders.append( str_yheader )
   
        array1d_xdata = array1d_xdata_align
        array2d_ydata = array2d_ydata_save
    
        list_weight = def_weight (alpha,beta)
        list2d_data = []
        list2d_data.append( [array1d_xdata, array2d_ydata, [0], list_weight[0]] )
        list2d_data.append( [array1d_xdata, array2d_ydata, [1], list_weight[1]] )
        list2d_data.append( [array1d_xdata, array2d_ydata, [2], list_weight[2]] )
        _, array2d_ydata_mix = def_xas_mix( list2d_data=list2d_data )
        array2d_ydata_final[:,int_i] = array2d_ydata_mix[:,0]
    
    array1d_xdata = array1d_xdata_align
    array2d_ydata = array2d_ydata_final
    def_xas_writedata( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)

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
    list1d_ycolumn = [1,2,3]
    str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list1d_ycolumn=list1d_ycolumn )
    for int_i in range(len(array1d_xdata)):
        array2d_ydata[int_i,:] *= array1d_xdata[int_i]

    os.remove( str_tempfile )

    def_endfunc()
    return str_xheader, list_yheaders, array1d_xdata, array2d_ydata

def def_xas_sft( array1d_xdata, float_sft):
    dict_args = locals()
    del dict_args['array1d_xdata'] 

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    array1d_xdata_sft = array1d_xdata + float_sft

    def_endfunc()
    return array1d_xdata_sft

def def_xas_writedata( array1d_xdata, array2d_ydata, str_xheader, list_yheaders, str_outfile):
    dict_args = locals()
    del dict_args['array1d_xdata']
    del dict_args['array2d_ydata']

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    with open( str_outfile, 'w', newline='' ) as obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',' )
        obj_outwriter.writerow( [str_xheader] + list_yheaders )
        for int_i in range(len( array1d_xdata )):
            obj_outwriter.writerow( [ array1d_xdata[int_i] ] + array2d_ydata[int_i].tolist() )

    def_endfunc()
    return

def def_xas_findarea( array1d_xdata, array2d_ydata, tuple_xrange):
    dict_args = locals()
    del dict_args['array1d_xdata']
    del dict_args['array2d_ydata']

    def_startfunc()
    print(json.dumps( obj=dict_args, indent=4 ))

    array_ydata = numpy.reshape( a=array2d_ydata, newshape=-1 )
 
    array_x_new=[]
    array_y_new=[]

    for int_i in range(len(array1d_xdata)):
        float_x = array1d_xdata[int_i]
        float_y = array_ydata[int_i]
        if ( float_x > tuple_xrange[0] and float_x < tuple_xrange[1] ):
            array_x_new.append( float_x )
            array_y_new.append( float_y )

    float_area = numpy.trapz( y=array_y_new, x=array_x_new )
    print(json.dumps( obj={'float_area':float_area}, indent=4))

    def_endfunc()
    return float_area

def def_xas_findpeaks( array1d_xdata, array2d_ydata, float_relheight, float_relprominence ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()
    del dict_args['array1d_xdata']
    del dict_args['array2d_ydata']

    def_startfunc()
    print( json.dumps( obj=dict_args, indent=4 ))

    array_ydata = numpy.reshape( a=array2d_ydata, newshape=-1 )

    float_y_max = max(array_ydata)
    height = float_relheight * float_y_max

    prominence = float_relprominence * float_y_max

    list_peaks_indices, dict_properties = scipy.signal.find_peaks( array_ydata, height = height, prominence=prominence )
    
    list_print = []
    list_print.append( ['Energy (eV)', 'Intensity/Max','prominences/Max'] )
    int_count = 0
    list_peaks = []
    for i in list_peaks_indices:
        list_peaks.append( array1d_xdata[i] )
        list_print.append( [array1d_xdata[i], array_ydata[i]/float_y_max, dict_properties['prominences'][int_count]/float_y_max] )
        int_count += 1
    print( json.dumps( obj=list_print, indent=4 ) )

    def_endfunc()
    return list_peaks

def def_xas_interp(list2d_data):
#------------------------------[]
# list2d_data = []
# list_data.append( [ array1d_xdata, array2d_ydata ] )
#------------------------------[]
    def_startfunc()

    float_xl = float('-inf')
    float_xr = float('+inf')
    for list1d_data in list2d_data:
        array1d_xdata = list1d_data[0]
        float_xl = max( float_xl, numpy.amin( array1d_xdata ))
        float_xr = min( float_xr, numpy.amax( array1d_xdata ))

    dict_json = {}
    dict_json[ 'float_xl' ] = float_xl
    dict_json[ 'float_xr' ] = float_xr
    print( json.dumps( dict_json, indent=4 ) )

    int_shape1dxdata = numpy.shape(array1d_xdata)[0]
    dict_json = {}
    dict_json[ 'int_shape1dxdata' ] = int_shape1dxdata
    print( json.dumps( dict_json, indent=4 ) )

    array1d_xdata_interp = numpy.linspace( start=float_xl, stop=float_xr, num=int_shape1dxdata )

    list1d_ydata_interp = []
    for list1d_data in list2d_data:
        array1d_xdata = list1d_data[0]
        array2d_ydata = list1d_data[1]
        int_shape2dydata_1 = numpy.shape( array2d_ydata )[1]
        array2d_temp = numpy.empty( shape=(int_shape1dxdata, int_shape2dydata_1) )
        for int_i in range(int_shape2dydata_1):
            array2d_temp[:,int_i] = numpy.interp( x=array1d_xdata_interp, xp=array1d_xdata, fp=array2d_ydata[:,int_i] )

        list1d_ydata_interp.append( array2d_temp )

    def_endfunc()
    return array1d_xdata_interp, list1d_ydata_interp

def def_xas_mix(list2d_data):
#------------------------------[]
# list2d_data = []
# list2d_data.append( [ array1d_xdata, array2d_ydata, [0,2], 0.7 ] )
#------------------------------[]
    dict_args = copy.deepcopy(locals())
    for list_temp in dict_args['list2d_data']:
        del list_temp[0:2]

    def_startfunc()
    print(json.dumps( obj=dict_args,  indent=4 ))
    
    int_len2ddata = len(list2d_data)
    list2d_xydata = []
    for list1d_data in list2d_data:
        list2d_xydata.append( [ list1d_data[0], list1d_data[1] ] )

    array1d_xdata_interp, list1d_ydata_interp = def_xas_interp( list2d_xydata )

    int_len1dxdata = len( list2d_data[0][0] )
    int_lenycolumn = len( list2d_data[0][2] )
    array2d_ydata_mix = numpy.zeros( shape=(int_len1dxdata, int_lenycolumn) )
    for int_i in range(int_len2ddata):
        list1d_ycolumn = list2d_data[int_i][2]
        array2d_ydata = list1d_ydata_interp[ int_i][:, list1d_ycolumn ]
        float_scaling = list2d_data[int_i][3]
        array2d_ydata_mix += array2d_ydata * float_scaling

    def_endfunc()
    return array1d_xdata_interp, array2d_ydata_mix

def def_xas_extract( str_datfile, int_xcolumn, list1d_ycolumn ):
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
        list_yheaders = [ list_line[i] for i in list1d_ycolumn ]
        print(json.dumps({'str_xheader': str_xheader},indent=4))
        print(json.dumps({'list_yheaders': list_yheaders}, indent=4))
        for list_line in obj_datreader:
            if ( not list_line[ int_xcolumn ] ): continue
            list_xdata.append( float(list_line[int_xcolumn]) )
            list_temp = []
            for int_i in list1d_ycolumn:
                list_temp.append( float(list_line[int_i]) )
            list_ydatas.append( list_temp )
    array1d_xdata = numpy.array( list_xdata )
    array2d_ydata = numpy.array( list_ydatas )

    int_lendata = len(list_xdata)
    print(json.dumps({ 'int_lendata': int_lendata },indent=4))
 
    def_endfunc()
    return str_xheader, list_yheaders, array1d_xdata, array2d_ydata

