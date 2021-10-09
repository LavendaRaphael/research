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

def def_xas_findtm( array1d_xdata, array1d_ydata, float_onset, float_xwidth=0.5, int_ ):
    def_startfunc( locals(), ['array1d_xdata', 'array1d_ydata'] )

    list1d_band = []
    float_yheight = numpy.amax( array1d_ydata ) * float_yrevheight
    for int_i in range( shape(array1d_xdata) ):
        float_x = array1d_xdata[ int_i ]
        if ( float_x < float_onset-float_xwidth or float_x > float_onset+float_xwidth): continue
        float_y = array1d_ydata[ int_i ]
        if ( float_y < float_yheight ): continue
        list1d_band.append( [int_i+1, float_x, float_y] )
    print( json.dump( [] ) )

def def_xas
    for int_k in range(1):
        int_k += 1
        str_datfile = 'xas_tm.a20_b90.K'+str(int_k)+'.csv'
        _, _, array1d_xdata, array2d_ydata = from_xas_modules.def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )

def def_xas_atom_abworkflow(  str_jsonfile, list2d_angle, list2d_atom, float_tm_scaling=5.0):
#----------------------------------------------[]
#----------------------------------------------[]
    def_startfunc( locals() )

    dict_jsonfile={}
    with open(str_jsonfile) as obj_jsonfile:
        dict_jsonfile = json.load( fp=obj_jsonfile )
    float_align = dict_jsonfile['float_align']
    float_scaling = dict_jsonfile['float_scaling']

    str_chdir=list2d_atom[0][0]
    os.chdir(str_chdir)
    print(os.getcwd())
    float_finalenergy_1 = def_vasp_finalenergy()
    os.chdir('..')

    str_abname=str_jsonfile[4:-5]
    def_print_paras( locals(), ['str_abname'] )
    for list1d_atom in list2d_atom:
        str_chdir = list1d_atom[0]
        os.chdir(str_chdir)
        print(os.getcwd())
        #----------------------------------------------[extract]
        str_xheader, array1d_xdata_align, array2d_ydata_scaling, list2d_tm_data_alignscaling = def_xas_atom_alignscaling( float_align=float_align, float_scaling=float_scaling, float_finalenergy_1=float_finalenergy_1 )

        array2d_ydata = array2d_ydata_scaling
        list1d_yheader, array2d_ydata_alphabeta = def_xas_alphabeta( list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )

        array1d_xdata = array1d_xdata_align
        array2d_ydata = array2d_ydata_alphabeta
        str_outfile = 'xas.'+str_abname+'.csv'
        def_xas_writedata( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, str_xheader=str_xheader, list1d_yheader=list1d_yheader, str_outfile=str_outfile)

        int_i = 1
        for list1d_tm_data_alignscaling in list2d_tm_data_alignscaling:
            array1d_tm_xdata_align, array2d_tm_ydata_scaling = list1d_tm_data_alignscaling
            array2d_ydata = array2d_tm_ydata_scaling
            list1d_yheader, array2d_tm_ydata_alphabeta = def_xas_alphabeta( list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )

            array1d_xdata = array1d_tm_xdata_align
            array2d_ydata = array2d_tm_ydata_alphabeta * float_tm_scaling
            str_outfile = 'xas_tm.'+str_abname+'.K'+str(int_i)+'.csv'
            int_i += 1
            def_xas_writedata( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, str_xheader=str_xheader, list1d_yheader=list1d_yheader, str_outfile=str_outfile)

        os.chdir('..')

def def_xas_atom_alignscaling(float_align, float_scaling, float_finalenergy_1):
#----------------------------------------------[]
#----------------------------------------------[]
    def_startfunc( locals() )

    #----------------------------------------------[extract]
    str_xheader, _, array1d_xdata, array2d_ydata = def_vasp_outcar2xas()
    #----------------------------------------------[alignscaling]
    float_finalenergy = def_vasp_finalenergy()
    float_sft = float_finalenergy-float_finalenergy_1
    float_sft += float_align
    array1d_xdata_align = array1d_xdata + float_sft
    array2d_ydata_scaling = array2d_ydata * float_scaling
    #----------------------------------------------[tm]
    list2d_tm_data = def_xas_tm_extract()
    list2d_tm_data_alignscaling = []
    for list1d_tm_data in list2d_tm_data:
        array1d_tm_xdata_align = list1d_tm_data[0] + float_sft
        array2d_tm_ydata_scaling = list1d_tm_data[1] * float_scaling
        list2d_tm_data_alignscaling.append( [ array1d_tm_xdata_align, array2d_tm_ydata_scaling] )

    return str_xheader, array1d_xdata_align, array2d_ydata_scaling, list2d_tm_data_alignscaling

def def_xas_tm_extract( str_datfile='MYCARXAS' ):
#------------------------------[]
#------------------------------[]
    def_startfunc( locals() )

    delimiter = ' '
    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ), delimiter=delimiter, skipinitialspace=True )
        int_nband = 0
        for list1d_line in obj_datreader:
            if (list1d_line): break
        for list1d_line in obj_datreader:
            if (not list1d_line): break
            int_nband += 1
    int_nband += 1
    def_print_paras( locals(), ['int_nband'] )
    
    list2d_data = []
    array1d_xdata = numpy.empty( shape=(int_nband) )
    array2d_ydata = numpy.empty( shape=(int_nband, 3) )

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ), delimiter=delimiter, skipinitialspace=True )
        for list1d_line in obj_datreader:
            if (not list1d_line): continue
            int_i = 0
            array1d_xdata[ int_i ] = list1d_line[0]
            array2d_ydata[ int_i ] = numpy.array( list1d_line[1:4] )
            for list1d_line in obj_datreader:
                if (not list1d_line): break
                int_i += 1
                array1d_xdata[ int_i ] = list1d_line[0]
                array2d_ydata[ int_i ] = numpy.array( list1d_line[1:4] )
            int_i += 1
            if (int_i != int_nband):
                raise RuntimeError(f'int_i {int_i} != int_nband {int_nband}')
            list2d_data.append( [array1d_xdata.copy(), array2d_ydata.copy()] )

    int_len2ddata = len(list2d_data)
    def_print_paras( locals(), ['int_len2ddata'] )
 
    def_endfunc()
    return list2d_data

def def_xas_exp_xyfit( list2d_alpha, str_outfile='xas_exp.xyfit.csv' ):
#----------------------------------------------[]
# list2d_alpha = []
# list2d_alpha.append( [20, '20210924.Pt.110.a20.csv'] )
# list2d_alpha.append( [41, '20210924.Pt.110.a41.csv'] )
#----------------------------------------------[]
    def_startfunc( locals() )

    int_lenalpha = len(list2d_alpha)
    array1d_alpha = numpy.empty( shape=(int_lenalpha) )
    list2d_data = []
    for int_i in range(int_lenalpha):
        array1d_alpha[int_i] = list2d_alpha[ int_i ][ 0 ]
        str_datfile = list2d_alpha[ int_i ][ 1 ]
        str_xheader, list1d_yheader, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )
        list2d_data.append( [ array1d_xdata, array2d_ydata] )

    array1d_sinalpha2 = numpy.sin( numpy.radians( array1d_alpha ) ) **2
    def_print_paras( locals(), ['array1d_sinalpha2'] )

    array1d_xdata_interp, list1d_ydata_interp = def_xas_interp( list2d_data )

    int_len1dxdata = len( array1d_xdata_interp )
    def_print_paras( locals(), ['int_len1dxdata'] )

    array1d_ydata_fit = numpy.empty( shape=(int_len1dxdata) )    
    array1d_temp = numpy.empty( shape=(int_lenalpha) )
    for int_i in range( int_len1dxdata ):
        for int_j in range( int_lenalpha ):
            array1d_temp[int_j] = list1d_ydata_interp[int_j][int_i]
        polyfit = numpy.polynomial.Polynomial.fit( array1d_sinalpha2, array1d_temp, 1 )
        array1d_ydata_fit[ int_i ] = numpy.sum( polyfit.convert().coef )

    array2d_ydata = numpy.reshape( array1d_ydata_fit, newshape=( int_len1dxdata,1 ) )
    def_xas_writedata( array1d_xdata=array1d_xdata_interp, array2d_ydata=array2d_ydata, str_xheader='E(eV)', list1d_yheader=['sigma_xyfit'], str_outfile=str_outfile)

class NumpyEncoder(json.JSONEncoder):
#----------------------------------------------[]
# https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
#----------------------------------------------[]
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def def_print_paras( dict_localpara, list_paraname ):
    dict_paraprint = {}
    for str_paraname in list_paraname:
        dict_paraprint[ str_paraname ] = dict_localpara[ str_paraname ]
    print(json.dumps( dict_paraprint, indent=4, cls=NumpyEncoder ))

class class_structures(object):

    @property
    def str_chdir(self):
        return self._str_chdir
    @str_chdir.setter
    def str_chdir(self, str_temp):
        self._str_chdir = str_temp
  
    @property
    def list2d_atom(self):
        return self._list2d_atom

    @list2d_atom.setter
    def list2d_atom(self, list_temp):
        float_sum = 0
        for list_i in list_temp: float_sum += list_i[1]
        for list_i in list_temp: list_i[1] /= float_sum
        for list_i in list_temp: list_i[0] = 'atom_'+str(list_i[0])
        self._list2d_atom = list_temp

def def_xas_ave( list2d_atom, str_outfile = 'xas.ave.csv'):
#----------------------------------------------[]
# list2d_atom = []
# list2d_atom.append([ 1,2.0])
#----------------------------------------------[]
    def_startfunc( locals() )

    str_chdir=list2d_atom[0][0]
    os.chdir(str_chdir)
    print(os.getcwd())
    float_finalenergy_1 = def_vasp_finalenergy()
    os.chdir('..')

    list2d_data = []
    for list1d_atom in list2d_atom:

        str_chdir = list1d_atom[0]
        float_scaling = list1d_atom[1]
        os.chdir(str_chdir)
        print(os.getcwd())

        str_xheader, list1d_yheader, array1d_xdata, array2d_ydata = def_vasp_outcar2xas()

        float_finalenergy = def_vasp_finalenergy()
        float_sft = float_finalenergy-float_finalenergy_1 
        array1d_xdata_sft = def_xas_sft( array1d_xdata=array1d_xdata, float_sft=float_sft)

        array1d_xdata = array1d_xdata_sft
        list_ycolums = list(range(len(array2d_ydata[0])))
        list2d_data.append( [ array1d_xdata, array2d_ydata, list_ycolums, float_scaling ] )

        os.chdir('..')

    array1d_xdata_mix, array2d_ydata_mix = def_xas_mix(list2d_data=list2d_data)
    def_xas_writedata( array1d_xdata=array1d_xdata_mix, array2d_ydata=array2d_ydata_mix, str_xheader=str_xheader, list1d_yheader=list1d_yheader, str_outfile=str_outfile)

def def_xas_abworkflow( list1d_alignangle, list1d_scalingangle, float_onset, list2d_angle, str_outfile, str_datfile='xas.ave.csv'):
#----------------------------------------------[]
# list_alignangle = [ alpha0, beta0 ]
# list_scalingangle = [ alpha1, beta1 ]
# float_onset = 530.6
#----------------------------------------------[]
    def_startfunc( locals() )
    
    #--------------------------------------------------[extract]
    int_xcolumn = 0
    list1d_ycolumn = [1,2,3]
    str_xheader, _, array1d_xdata_origin, array2d_ydata_origin = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list1d_ycolumn=list1d_ycolumn )
    
    #--------------------------------------------------[alignscaling]
 
    str_abname = def_abname( alpha=list1d_scalingangle[0], beta=list1d_scalingangle[1])
    str_jsonfile = 'xas.'+str_abname+'.json'
    array1d_xdata = array1d_xdata_origin
    array2d_ydata = array2d_ydata_origin
    array1d_xdata_align, array2d_ydata_scaling = def_xas_alignscaling( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, list1d_alignangle=list1d_alignangle, list1d_scalingangle=list1d_scalingangle, float_onset=float_onset, str_jsonfile=str_jsonfile )
    
    array2d_ydata = array2d_ydata_scaling
    list1d_yheader, array2d_ydata_alphabeta = def_xas_alphabeta( list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )

    array1d_xdata = array1d_xdata_align
    array2d_ydata = array2d_ydata_alphabeta
    def_xas_writedata( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, str_xheader=str_xheader, list1d_yheader=list1d_yheader, str_outfile=str_outfile)

    def_endfunc()
    return

def def_xas_alignscaling( array1d_xdata, array2d_ydata, list1d_alignangle, list1d_scalingangle, float_onset,str_jsonfile, tuple_xrange = (527.0, 540.0), float_scalingarea = 20.0 ):
#----------------------------------------------[]
# list_alignangle = [ alpha0, beta0 ]
# list_scalingangle = [ alpha1, beta1 ]
# float_onset = 530.6
#----------------------------------------------[]
    def_startfunc( locals(), ['array1d_xdata', 'array2d_ydata'] )
    
    array1d_xdata_origin = array1d_xdata
    array2d_ydata_origin = array2d_ydata
    #--------------------------------------------------[align]
    list2d_angle=[ list1d_alignangle ]
    _, array2d_ydata_alphabeta = def_xas_alphabeta( list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )
    
    array1d_xdata = array1d_xdata_origin
    array2d_ydata = array2d_ydata_alphabeta
    list1d_peakx = def_xas_findpeaks( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata)
    
    array1d_xdata = array1d_xdata_origin
    float_align = float_onset - list1d_peakx[0]
    array1d_xdata_align = array1d_xdata + float_align
    dict_jsonfile = {}
    dict_jsonfile[ 'float_align' ] = float_align
    #--------------------------------------------------[scaling]
    list2d_angle = [ list1d_scalingangle ] 
    array2d_ydata = array2d_ydata_origin
    _, array2d_ydata_alphabeta = def_xas_alphabeta(list2d_angle=list2d_angle, array2d_ydata=array2d_ydata )
    
    array1d_xdata = array1d_xdata_align
    array2d_ydata = array2d_ydata_alphabeta
    print( array2d_ydata )
    float_area = def_xas_findarea( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, tuple_xrange=tuple_xrange)
    float_scaling = float_scalingarea/float_area
    dict_jsonfile[ 'float_scaling' ] = float_scaling

    array2d_ydata_scaling=array2d_ydata_origin*float_scaling
    #--------------------------------------------------[output]
    with open( str_jsonfile, 'w' ) as obj_jsonfile:
        json.dump( obj=dict_jsonfile, fp=obj_jsonfile, indent=4 )

    def_endfunc()
    return array1d_xdata_align, array2d_ydata_scaling

def def_xas_alphabeta( list2d_angle, array2d_ydata ):
    def_startfunc( locals(), ['array2d_ydata'] )

    int_shape2dydata0 = numpy.shape(array2d_ydata)[0]
    def_print_paras( locals(), ['int_shape2dydata0'] )
    array2d_ydata_alphabeta = numpy.empty( shape=(int_shape2dydata0, len(list2d_angle)) )
    list1d_yheader = []
    for int_i in range(len(list2d_angle)):
        alpha, beta = list2d_angle[int_i]
        str_yheader = 'a'+str(alpha)+'_b'+str(beta)
        list1d_yheader.append( str_yheader )
    
        array1d_weight = def_weight (alpha,beta)
        array1d_ydata_dot = numpy.dot(array2d_ydata, array1d_weight)

        array2d_ydata_alphabeta[:,int_i] = array1d_ydata_dot

    return list1d_yheader, array2d_ydata_alphabeta

def def_weight (alpha,beta):
#----------------------------------------------[]
# Suitable for Dichroism.
#-------------------------[in]
# alpha: float, degree angle
# beta:  float, degree angle
#-------------------------[out]
# array1d_weight:  list, shape(3)
#               array1d_weight[1] = array1d_weight[0]
#               sigma = [sigma_x, sigma_y, sigma_z]*array1d_weight
#----------------------------------------------[]
    alpha = math.radians (alpha)
    beta = math.radians (beta)
    array1d_weight = numpy.empty( shape=(3) )
    array1d_weight[0]= (0.5 * (math.cos(beta)**2 + math.sin(alpha)**2 * math.sin(beta)**2))
    array1d_weight[1]= (array1d_weight[0])
    array1d_weight[2]= (math.cos(alpha)**2 * math.sin(beta)**2)
    return array1d_weight

def def_vasp_finalenergy():
    def_startfunc( locals() )

    float_finalenergy = ase.io.read( filename='OUTCAR' ).get_total_energy()
    print( json.dumps({'float_finalenergy': float_finalenergy}, indent=4))

    def_endfunc()
    return float_finalenergy

def def_vasp_outcar2xas():
    def_startfunc( locals() )

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
    str_xheader, list1d_yheader, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list1d_ycolumn=list1d_ycolumn )
    for int_i in range(len(array1d_xdata)):
        array2d_ydata[int_i,:] *= array1d_xdata[int_i]

    os.remove( str_tempfile )

    def_endfunc()
    return str_xheader, list1d_yheader, array1d_xdata, array2d_ydata

def def_xas_sft( array1d_xdata, float_sft):
    def_startfunc( locals(), ['array1d_xdata'] )

    array1d_xdata_sft = array1d_xdata + float_sft

    def_endfunc()
    return array1d_xdata_sft

def def_xas_writedata( array1d_xdata, array2d_ydata, str_xheader, list1d_yheader, str_outfile):
    def_startfunc( locals(), ['array1d_xdata', 'array2d_ydata'] )

    with open( str_outfile, 'w', newline='' ) as obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',' )
        obj_outwriter.writerow( [str_xheader] + list1d_yheader )
        for int_i in range(len( array1d_xdata )):
            obj_outwriter.writerow( [ array1d_xdata[int_i] ] + array2d_ydata[int_i].tolist() )

    def_endfunc()
    return

def def_xas_findarea( array1d_xdata, array2d_ydata, tuple_xrange):
    def_startfunc( locals(), ['array1d_xdata', 'array2d_ydata'] )

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

def def_xas_findpeaks( array1d_xdata, array2d_ydata, float_relheight = 0.4, float_relprominence = 0.02):
#------------------------------[]
#------------------------------[]
    def_startfunc( locals(), ['array1d_xdata', 'array2d_ydata'] )

    array_ydata = numpy.reshape( a=array2d_ydata, newshape=-1 )

    float_y_max = max(array_ydata)
    height = float_relheight * float_y_max

    prominence = float_relprominence * float_y_max

    list1d_peakx_indices, dict_properties = scipy.signal.find_peaks( array_ydata, height = height, prominence=prominence )
    
    list_print = []
    list_print.append( ['Energy (eV)', 'Intensity/Max','prominences/Max'] )
    int_count = 0
    list1d_peakx = []
    for i in list1d_peakx_indices:
        list1d_peakx.append( array1d_xdata[i] )
        list_print.append( [array1d_xdata[i], array_ydata[i]/float_y_max, dict_properties['prominences'][int_count]/float_y_max] )
        int_count += 1
    print( json.dumps( obj=list_print, indent=4 ) )

    def_endfunc()
    return list1d_peakx

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

    int_shape1dxdata = numpy.shape(list2d_data[0][0])[0]
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
    def_startfunc( dict_args )
    

    list2d_xydata = []
    for list1d_data in list2d_data:
        list2d_xydata.append( [ list1d_data[0], list1d_data[1] ] )
    array1d_xdata_interp, list1d_ydata_interp = def_xas_interp( list2d_xydata )

    int_len1dxdata = len( array1d_xdata_interp )
    int_lenycolumn = len( list2d_data[0][2] )
    array2d_ydata_mix = numpy.zeros( shape=(int_len1dxdata, int_lenycolumn) )

    int_len2ddata = len(list2d_data)
    for int_i in range(int_len2ddata):
        list1d_ycolumn = list2d_data[int_i][2]
        array2d_ydata = list1d_ydata_interp[ int_i][:, list1d_ycolumn ]
        float_scaling = list2d_data[int_i][3]
        array2d_ydata_mix += array2d_ydata * float_scaling

    def_endfunc()
    return array1d_xdata_interp, array2d_ydata_mix

def def_xas_extract( str_datfile, int_xcolumn, list1d_ycolumn, log_head=True ):
#------------------------------[]
#------------------------------[]
    def_startfunc( locals() )
    
    list_xdata = []
    list_ydatas = []

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: (row[0]!='#' and not row), obj_datfile ), delimiter= ' ', skipinitialspace=True )
        if log_head:
            list1d_line = next(obj_datreader)
        list1d_line = next(obj_datreader)
        if (',' in list1d_line[0]):
            delimiter=','
        else:
            delimiter=' '
    print(json.dumps({'delimiter': delimiter},indent=4))

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: (row[0]!='#' and not row), obj_datfile ), delimiter=delimiter, skipinitialspace=True )
        if log_head:
            list1d_line = next(obj_datreader)
            str_xheader = list1d_line[int_xcolumn]
            list1d_yheader = [ list1d_line[i] for i in list1d_ycolumn ]
        else:
            str_xheader = ''
            list1d_yheader = [ '' for i in list1d_ycolumn ]
        print(json.dumps({'str_xheader': str_xheader},indent=4))
        print(json.dumps({'list1d_yheader': list1d_yheader}, indent=4))
        for list1d_line in obj_datreader:
            if ( not list1d_line[ int_xcolumn ] ): continue
            list_xdata.append( float(list1d_line[int_xcolumn]) )
            list_temp = []
            for int_i in list1d_ycolumn:
                list_temp.append( float(list1d_line[int_i]) )
            list_ydatas.append( list_temp )
    array1d_xdata = numpy.array( list_xdata )
    array2d_ydata = numpy.array( list_ydatas )

    int_lendata = len(list_xdata)
    print(json.dumps({ 'int_lendata': int_lendata },indent=4))
 
    def_endfunc()
    return str_xheader, list1d_yheader, array1d_xdata, array2d_ydata

def def_abname( alpha, beta ):
    str_abname = 'a'+str(alpha)+'_b'+str(beta)
    return str_abname

def def_startfunc( dict_args={}, list1d_del=[] ):
    this_function_name = inspect.currentframe().f_back.f_code.co_name
    print("#"+'-'*20+"["+this_function_name+"]\n")
    for str_del in list1d_del:
        del dict_args[ str_del ]
    print(json.dumps( obj=dict_args, indent=4 ))

def def_endfunc():
    print("#"+'-'*20+"<<\n")
