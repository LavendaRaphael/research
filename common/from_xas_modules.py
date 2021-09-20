#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.18
#===============================================<<

def def_xas_findpeaks(str_file, float_relheight, float_relprominence, str_prefix):
#------------------------------[]
#------------------------------[]
    from scipy.signal import find_peaks
    import csv

    print("#--------------------[xas_findpeaks]\n")

    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.csv'

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
        obj_csvwriter.writerow( ['# Energy (eV)', 'Intensity/Max','prominences/Max'] )
        int_count = 0
        for i in list_peaks_indices:
            obj_csvwriter.writerow( [list_xas_e[i], list_xas_i[i]/float_i_max, dict_properties['prominences'][int_count]/float_i_max] )
            int_count += 1

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

    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.csv'

    obj_logfile = open(str_logfile,'w')
    
    list_xas_e=[]
    list_xas_i=[]
    
    tup_filex = list_files[0]
    obj_logfile.write(f'tup_filex {tup_filex}\n')

    with open( tup_filex[0], 'r' ) as obj_csvfile:
        obj_csvreader = csv.reader( filter( lambda row: row[0]!='#', obj_csvfile ) )
        for list_line in obj_csvreader:
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
                list_xas_i[int_line] += ( float(list_line[tup_filex[2]]) * tup_filex[3] )
                int_line += 1

        if ((int_line - int_lenxas) != 0):
            print (f'{int_line}')
            print ('Error: len(tup_filex) != int_lenxas')
            obj_logfile.write('Error: len(tup_filex) != int_lenxas')
            sys.exit()
    
    with open( str_outfile, 'w', newline='' ) as obj_csvfile:
        obj_csvwriter = csv.writer( obj_csvfile)
        obj_csvwriter.writerow( ['# Energy (eV)', 'Intensity'] )
        for i in range(int_lenxas):
            obj_csvwriter.writerow( [list_xas_e[i], list_xas_i[i]] )

    #obj_outfile = open(str_outfile, 'w')
    #obj_outfile.write(f'#   Energy  Intensity\n')
    #int_count = 0
    #for int_count in range(int_lenxas):
    #    obj_outfile.write(f'{list_xas_e[int_count]} {list_xas_i[int_count]}\n')
    #    int_count += 1
    #obj_outfile.close()

    obj_logfile.close()

    print("#--------------------<<\n")
    return
