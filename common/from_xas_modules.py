#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.21
#===============================================<<

def def_xas_sft( str_datfile, float_sft, str_prefix ):
    dict_logfile = { 'dict_args': locals() }
    import csv
    import json

    print("#--------------------[xas_sft]\n")
    str_logfile = str_prefix + '_log.json'
    str_outfile = str_prefix + '_out.csv'

    with open( str_outfile, 'w' ) obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',')
        with open( str_datfile, 'r' ) as obj_datfile:
            obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ) )
            for list_line in obj_datreader:
                list_line[0] += float_sft
                obj_outwriter.writerow(list_line)

    with open(str_logfile,'w') as obj_logfile:
        json.dump( obj=dict_logfile, fp=obj_logfile, indent=4 )
    print("#--------------------<<\n")
    return

def def_xas_scale( str_datfile, float_scaling, str_prefix ):
    dict_logfile = { 'dict_args': locals() }
    import csv
    import json

    print("#--------------------[xas_scale]\n")
    str_logfile = str_prefix + '_log.json'
    str_outfile = str_prefix + '_out.csv'

    with open( str_outfile, 'w' ) obj_outfile:
        obj_outwriter = csv.writer( obj_outfile, delimiter=',')
        with open( str_datfile, 'r' ) as obj_datfile:
            obj_datreader = csv.reader( filter( lambda row: row[0]!='#', obj_datfile ) )
            for list_line in obj_datreader:
                for int_i in range(1, len(list_line)):
                    list_line[int_i] *= float_scaling
                obj_outwriter.writerow(list_line)
            
    with open(str_logfile,'w') as obj_logfile:
        json.dump( obj=dict_logfile, fp=obj_logfile, indent=4 )
    print("#--------------------<<\n")
    return

#------------------------------[]
# http://kbyanc.blogspot.com/2007/07/python-aggregating-function-arguments.html
#------------------------------[]
def arguments():
    """Returns tuple containing dictionary of calling function's
       named arguments and a list of calling function's unnamed
       positional arguments.
    """
    from inspect import getargvalues, stack
    posname, kwname, args = getargvalues(stack()[1][0])[-3:]
    posargs = args.pop(posname, [])
    args.update(args.pop(kwname, []))
    return args, posargs

def def_xas_findarea( str_file, tuple_xrange, str_prefix ):
    dict_logfile = { 'dict_args': locals() }
    from numpy import trapz
    import csv
    import json

    print("#--------------------[xas_findarea]\n")
    str_logfile = str_prefix + '_log.json'
    str_outfile = str_prefix + '_out.json'
        
    list_xas_e=[]
    list_xas_i=[]

    with open( str_file, 'r' ) as obj_csvfile:
        obj_csvreader = csv.reader( filter( lambda row: row[0]!='#', obj_csvfile ) )
        for list_line in obj_csvreader:
            float_x = float(list_line[0])
            if ( float_x > tuple_xrange[0] and float_x < tuple_xrange[1] ):
                list_xas_e.append( float(list_line[0]) )
                list_xas_i.append( float(list_line[1]) )

    float_area = trapz( y=list_xas_i, x=list_xas_e )
    dict_logfile['float_area'] = float_area

    dict_area = {'float_area': float_area}
    with open( str_outfile, 'w' ) as obj_outfile:
        json.dump(dict_area, obj_outfile, indent=4)

    with open(str_logfile,'w') as obj_logfile:
        json.dump( obj=dict_logfile, fp=obj_logfile, indent=4 )
    print("#--------------------<<\n")
    return

def def_xas_findpeaks(str_file, float_relheight, float_relprominence, str_prefix):
#------------------------------[]
#------------------------------[]
    from scipy.signal import find_peaks
    import csv

    print("#--------------------[xas_findpeaks]\n")
    str_logfile = str_prefix + '_log.json'
    str_outfile = str_prefix + '_out.csv'
    obj_logfile = open(str_logfile,'w')

    obj_logfile.write(f'str_prefix = {str_prefix}\n')
    obj_logfile.write(f'float_relheight = {float_relheight}\n')

    list_xas_e=[]
    list_xas_i=[]

    with open( str_file, 'r' ) as obj_csvfile:
        obj_csvreader = csv.reader( filter( lambda row: row[0]!='#', obj_csvfile ) )
        for list_line in obj_csvreader:
            list_xas_e.append( list_line[0] )
            list_xas_i.append( float(list_line[1]) )
    int_lenxas=len(list_xas_e)
    obj_logfile.write(f'int_lenxas = {int_lenxas}\n')

    float_i_max = max(list_xas_i)
    height = float_relheight * float_i_max

    prominence = float_relprominence * float_i_max

    list_peaks_indices, dict_properties = find_peaks( list_xas_i, height = height, prominence=prominence )
    
    with open( str_outfile, 'w', newline='' ) as obj_csvfile:
        obj_csvwriter = csv.writer( obj_csvfile)
        #obj_csvwriter.writerow( ['# Energy (eV)', 'Intensity/Max','prominences/Max'] )
        int_count = 0
        for i in list_peaks_indices:
            obj_csvwriter.writerow( [list_xas_e[i], list_xas_i[i]/float_i_max, dict_properties['prominences'][int_count]/float_i_max] )
            int_count += 1

    obj_logfile.close()
    print("#--------------------<<\n")
    return


def def_xas_mix(list_files, str_prefix):
#------------------------------[]
# str_prefix = 'xas_mix'
# list_files = []
# list_files.append( ('filea', 0, 1, 0.3) )
# list_files.append( ('fileb', 0, 2, 0.7) )
#------------------------------[]
    import csv

    print("#--------------------[xas_mix]\n")
    str_logfile = str_prefix + '_log.json'
    str_outfile = str_prefix + '_out.csv'
    obj_logfile = open(str_logfile,'w')
    
    list_xas_e=[]
    list_xas_i=[]
    
    tup_filex = list_files[0]
    obj_logfile.write(f'tup_filex {tup_filex}\n')

    with open( tup_filex[0], 'r' ) as obj_csvfile:
        obj_csvreader = csv.reader( filter( lambda row: row[0]!='#', obj_csvfile ) )
        for list_line in obj_csvreader:
            if (not list_line[tup_filex[2]]): continue
            list_xas_e.append( list_line[tup_filex[1]] )
            list_xas_i.append( float(list_line[tup_filex[2]]) * tup_filex[3] )

    int_lenxas=len(list_xas_e)
    obj_logfile.write(f'int_lenxas {int_lenxas}\n')
    
    for tup_filex in list_files[1:]:
        obj_logfile.write(f'tup_filex {tup_filex}\n')
        int_line = 0
        with open( tup_filex[0], 'r' ) as obj_csvfile:
            obj_csvreader = csv.reader( filter( lambda row: row[0]!='#', obj_csvfile ) )
            int_line = 0
            for list_line in obj_csvreader:
                if (not list_line[tup_filex[2]]): continue
                list_xas_i[int_line] += ( float(list_line[tup_filex[2]]) * tup_filex[3] )
                int_line += 1

        if ((int_line - int_lenxas) != 0):
            print (f'{int_line}')
            print ('Error: len(tup_filex) != int_lenxas')
            obj_logfile.write('Error: len(tup_filex) != int_lenxas')
            sys.exit()
    
    with open( str_outfile, 'w', newline='' ) as obj_csvfile:
        obj_csvwriter = csv.writer( obj_csvfile, delimiter=' ')
        #obj_csvwriter.writerow( ['# Energy (eV)', 'Intensity'] )
        for i in range(int_lenxas):
            obj_csvwriter.writerow( [list_xas_e[i], list_xas_i[i]] )

    obj_logfile.close()
    print("#--------------------<<\n")
    return
