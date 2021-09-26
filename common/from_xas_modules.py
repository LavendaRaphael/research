#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.21
#===============================================<<
def def_vasp_finalenergy(str_prefix):
    dict_args = locals()
    import json
    from ase.io import read as ase_read

    print("#--------------------[vasp_finalenergy]\n")
    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.json'
    obj_logfile = open(str_logfile,'w')
    json.dump( obj=dict_args, fp=obj_logfile, indent=4 )

    float_finalenergy = ase_read( filename='OUTCAR' )

    dict_output = {'float_finalenergy': float_finalenergy}
    with open( str_outfile, 'w' ) as obj_outfile:
        json.dump( obj=dict_output, fp=obj_outfile, indent=4 )

    obj_logfile.close()
    print("#--------------------<<\n")
    return

def def_vasp_outcar2xas(str_prefix):
    dict_args = locals()
    import csv
    import json

    print("#--------------------[vasp_outcar2xas]\n")
    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.csv'
    obj_logfile = open(str_logfile,'w')
    json.dump( obj=dict_args, fp=obj_logfile, indent=4 )

    with open( 'OUTCAR', 'r' ) as obj_datfile:
        for str_line in obj_datfile:
            if (str_line.strip() == 'frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects) density-density'):
                break
        with open( str_outfile, 'w', newline='' ) as obj_outfile:
            obj_outwriter = csv.writer( obj_outfile, delimiter=',' )
            #obj_datreader = csv.reader( obj_datfile, delimiter=' ' )
            list_headers = next(obj_datfile).split()
            obj_outwriter.writerow( list_headers )
            obj_logfile.write( f'list_headers: {list_headers}\n' )
            list_line = next(obj_datfile)
            int_count = 0
            for str_line in obj_datfile:
                if ( not str_line.strip() ):
                    break
                obj_outwriter.writerow( str_line.split() )
                int_count += 1
            obj_logfile.write( f'int_count: {int_count}\n' )

    obj_logfile.close()
    print("#--------------------<<\n")
    return

def def_xas_sft( list_xdata, float_sft):
    dict_args = locals() 
    import json

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

def def_xas_findarea( list_xdata, list_ydatas, tuple_xrange):
    dict_args = locals()
    from numpy import trapz
    import json

    print("#--------------------[xas_findarea]\n")
    print(json.dumps( obj=dict_args, indent=4 ))

    list_ydata = []
    for list_temp in list_ydatas:
        list_ydata += list_temp
 
    list_x_new=[]
    list_y_new=[]

    for int_i in range(len(list_xdata)):
        float_x = list_xdata[int_i]
        float_y = list_ydata[int_i]
        if ( float_x > tuple_xrange[0] and float_x < tuple_xrange[1] ):
            list_x_new.append( float_x )
            list_y_new.append( float_y )

    float_area = trapz( y=list_y_new, x=list_x_new )
    print(f'float_area: {float_area}\n')

    print("#--------------------<<\n")
    return float_area

def def_xas_findpeaks( list_xdata, list_ydatas, float_relheight, float_relprominence ):
#------------------------------[]
#------------------------------[]
    dict_args = locals()
    from scipy.signal import find_peaks
    import json

    print("#--------------------[xas_findpeaks]\n")
    print( json.dumps( obj=dict_args, indent=4 ))

    list_ydata = []
    for list_temp in list_ydatas:
        list_ydata += list_temp

    float_y_max = max(list_ydata)
    height = float_relheight * float_y_max

    prominence = float_relprominence * float_y_max

    list_peaks_indices, dict_properties = find_peaks( list_ydata, height = height, prominence=prominence )
    
    print( ['Energy (eV)', 'Intensity/Max','prominences/Max'] )
    int_count = 0
    list_peaks = []
    for i in list_peaks_indices:
        list_peaks.append( list_xdata[i] )
        print( [list_xdata[i], list_ydata[i]/float_y_max, dict_properties['prominences'][int_count]/float_y_max] )
        int_count += 1

    print("#--------------------<<\n")
    return list_peaks

def def_xas_mix(list_datas):
#------------------------------[]
# list_datas = []
# list_datas.append( [list_xdata, list_ydatas, [1, 3], 0.3] )
#------------------------------[]
    dict_args = locals()
    import json

    print("#--------------------[xas_mix]\n")
    print(json.dumps( obj=dict_args,  indent=4 ))
    
    list_ydatas_mix = []

    list_datai = list_datas[0]
    list_xdata = list_datai[0]
    list_ydatas = list_datai[1]
    list_ycolumns = list_datai[2]
    float_scaling = list_datai[3]
    #list_yheaders = [ list_line[i] for i in list_ycolumn ]
    #print( f'list_yheaders: {list_yheaders}' )
    for list_line in list_ydatas:
        list_temp = []
        for int_i in list_ycolumns:
            list_temp.append( list_line[int_i] * float_scaling)
        list_ydatas_mix.append( list_temp )

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
    import csv
    import json

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

    int_lendata = len(list_xdata)
    print(f'int_lendata: {int_lendata}\n')
    
    print("#--------------------<<\n")
    return str_xheader, list_yheaders, list_xdata, list_ydatas

