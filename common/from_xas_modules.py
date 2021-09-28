#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.21
#===============================================<<
import csv
import json
import ase
import scipy.signal
import numpy

def def_vasp_finalenergy(str_prefix):
    dict_args = locals()

    print("#--------------------[vasp_finalenergy]\n")
    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.json'
    obj_logfile = open(str_logfile,'w')
    json.dump( obj=dict_args, fp=obj_logfile, indent=4 )

    float_finalenergy = ase.io.read( filename='OUTCAR' )

    dict_output = {'float_finalenergy': float_finalenergy}
    with open( str_outfile, 'w' ) as obj_outfile:
        json.dump( obj=dict_output, fp=obj_outfile, indent=4 )

    obj_logfile.close()
    print("#--------------------<<\n")
    return

def def_vasp_outcar2xas():
    dict_args = locals()

    print("#--------------------[vasp_outcar2xas]\n")
    print(json.dumps( obj=dict_args, indent=4 ))

    list_xdata = []
    list_ydatas = []

    with open( 'OUTCAR', 'r' ) as obj_datfile:
        for str_line in obj_datfile:
            if (str_line.strip() == 'frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects) density-density'):
                break
        obj_datreader = csv.reader( obj_datfile, delimiter= ' ', skipinitialspace=True )
        list_line = next(obj_datreader)
        str_xheader = list_line[0]
        list_yheaders = list_line[1:]
        str_line = next(obj_datfile)
        int_count = 0
        list_line = next( obj_datreader )
        list_temp = []
        for str_temp in list_line:
            list_temp.append( float(str_temp) )
        array_xdata = numpy.array( [list_temp[0]] )
        for list_line in obj_datreader:
            if ( len(list_line)==0 ):
                break
            list_temp = []
            for str_temp in list_line:
                list_temp.append( float(str_temp) )

            int_count += 1
        print( f'int_count: {int_count}\n' )

    obj_logfile.close()
    print("#--------------------<<\n")
    return

def def_xas_sft( list_xdata, float_sft):
    dict_args = locals() 

    print("#--------------------[xas_sft]\n")
    print(json.dumps( obj=dict_args, indent=4 ))

    list_xdata_sft = []
    for float_x in list_xdata:
        list_xdata_sft.append( float_x + float_sft)

    print("#--------------------<<\n")
    return list_xdata_sft

def def_xas_writedata( list_xdata, list_ydatas, str_xheader, list_yheaders, str_outfile):
    dict_args = locals()
    from numpy import trapz
    import csv
    import json

    print("#--------------------[xas_findarea]\n")
    print(json.dumps( obj=dict_args, indent=4 ))

    with open( str_outfile, 'w', newline='' ) as obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',' )
        obj_outwriter.writerow( [str_xheader] + list_yheaders )
        for int_i in range(len( list_xdata )):
            obj_outwriter.writerow( [ list_xdata[int_i] ] + list_ydatas[int_i] )

    print("#--------------------<<\n")
    return

def arguments():
#------------------------------[]
# http://kbyanc.blogspot.com/2007/07/python-aggregating-function-arguments.html
#------------------------------[]
    """Returns tuple containing dictionary of calling function's
       named arguments and a list of calling function's unnamed
       positional arguments.
    """
    from inspect import getargvalues, stack
    posname, kwname, args = getargvalues(stack()[1][0])[-3:]
    posargs = args.pop(posname, [])
    args.update(args.pop(kwname, []))
    return args, posargs

def def_xas_findarea( array_xdata, array_ydatas, tuple_xrange):
    dict_args = locals()
    del dict_args['array_xdata']
    del dict_args['array_ydatas']

    print("#--------------------[xas_findarea]\n")
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

    print("#--------------------<<\n")
    return float_area

def def_xas_findpeaks( array_xdata, array_ydatas, float_relheight, float_relprominence ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()
    del dict_args['array_xdata']
    del dict_args['array_ydatas']

    print("#--------------------[xas_findpeaks]\n")
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

    print("#--------------------<<\n")
    return list_peaks

def def_xas_mix(list_datas):
#------------------------------[]
#------------------------------[]
    dict_args = locals()
    for list_temp in dict_args['list_datas']:
        del list_temp[0:2]

    print("#--------------------[xas_mix]\n")
    print(json.dumps( obj=dict_args,  indent=4 ))
    
    array_ydatas_mix = []

    array_datai = array_datas[0]
    array_xdata = array_datai[0]
    array_ydatas = array_datai[1]
    list_ycolumns = list_datai[2]
    float_scaling = list_datai[3]
    #for list_line in list_ydatas:
    #    list_temp = []
    #    for int_i in list_ycolumns:
    #        list_temp.append( list_line[int_i] * float_scaling)
    #    list_ydatas_mix.append( list_temp )
    

    int_lendata = len(list_ydatas)
    print(f'int_lendata: {int_lendata}\n')
    
    for list_datai in list_datas[1:]:
        list_ydatas = list_datai[1]
        list_ycolumns = list_datai[2]
        float_scaling = list_datai[3]
        int_line = 0
        for list_line in list_ydatas:
            list_temp = []
            for int_i in list_ycolumns:
                list_temp.append( list_line[int_i] *  float_scaling )
            for i in range(len(list_ycolumns)):
                list_ydatas_mix[int_line][i] += list_temp[i]
            int_line += 1

        if ((int_line - int_lendata) != 0):
            print (f'{int_line}')
            print ('Error: len(tup_filex) != int_lendata')
            sys.exit()

    #if (len(list_ycolumn)==1):
    #    list_temp = []
    #    for i in list_ydatas:
    #        list_temp += i
    #    list_ydatas = list_temp

    list_xdata_mix = list_xdata

    print("#--------------------<<\n")
    return list_xdata_mix, list_ydatas_mix

def def_xas_extract( str_datfile, int_xcolumn, list_ycolumns ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()

    print("#--------------------[xas_mix]\n")
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
    print(f'delimiter: {delimiter}')

    with open( str_datfile, 'r', newline='' ) as obj_datfile:
        obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ), delimiter=delimiter, skipinitialspace=True )
        list_line = next(obj_datreader)
        str_xheader = list_line[int_xcolumn]
        list_yheaders = [ list_line[i] for i in list_ycolumns ]
        print( f'str_xheader: {str_xheader}' )
        print( f'list_yheaders: {list_yheaders}' )
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
    print(f'int_lendata: {int_lendata}\n')
    
    print("#--------------------<<\n")
    return str_xheader, list_yheaders, array_xdata, array_ydatas

