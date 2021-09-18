#!/bin/env python
#===============================================[README]
# @FeifeiTian
# 2021.09.18
#===============================================<<

def def_xas_mix(list_files, str_prefix):
#------------------------------[]
# str_outfile = 'xas_mix'
# list_files = []
# list_files.append( ('filea', 1, 0.3) )
# list_files.append( ('fileb', 2, 0.7) )
#------------------------------[]
    str_logfile = str_prefix + '.log'
    str_outfile = str_prefix + '.dat'

    obj_logfile = open(str_logfile,'w')
    obj_logfile.write("#--------------------[xas_mix]\n")
    
    list_xas_e=[]
    list_xas_i=[]
    
    tup_filex = list_files[0]
    obj_logfile.write(f'tup_filex {tup_filex}\n')
    for str_line in open(tup_filex[0]):
        if ((not str_line.strip()) or str_line.strip().startswith("#")):
            continue
        # print (str_line, end='')
        list_xas_e.append (str_line.split()[0])
        list_xas_i.append (float(str_line.split()[tup_filex[1]]) * tup_filex[2] )
    int_lenxas=len(list_xas_e)
    obj_logfile.write(f'int_lenxas {int_lenxas}\n')
    
    for tup_filex in list_files[1:]:
        obj_logfile.write(f'tup_filex {tup_filex}\n')
        int_line = 0
        for str_line in open(tup_filex[0]):
            if ((not str_line.strip()) or str_line.strip().startswith("#")):
                continue
            list_xas_i[int_line] += (float(str_line.split()[tup_filex[1]]) * tup_filex[2] )
            int_line += 1
        if ((int_line - int_lenxas) != 0):
            print (f'{int_line}')
            print ('Error: len(tup_filex) != int_lenxas')
            obj_logfile.write('Error: len(tup_filex) != int_lenxas')
            sys.exit()
    
    obj_outfile = open(str_outfile, 'w')
    obj_outfile.write(f'#   Energy  Intensity\n')
    int_count = 0
    for int_count in range(int_lenxas):
        obj_outfile.write(f'{list_xas_e[int_count]} {list_xas_i[int_count]}\n')
        int_count += 1
    obj_outfile.close()

    obj_logfile.write("#--------------------<<\n")
    obj_logfile.close()

    return
