#!/bin/env python 
#===============================================[README]
# @FeifeiTian
# 2021.09.17
#------------------------------[xas_mix_in.py]
# class cla_paras:
#   list_files=[]
#   list_files.append( ('filea', 1, 0.3) )
#   list_files.append( ('fileb', 2, 0.7) )
#===============================================<<

obj_logfile = open('xas_mix.log','w')

import sys
obj_logfile.write("#--------------------[python version]\n")
obj_logfile.write(sys.version)
obj_logfile.write("\n#--------------------<<\n")

sys.path.append(r'./')
from xas_mix_in import cla_paras

list_files = cla_paras.list_files

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

obj_outfile = open('xas_mix.dat','w')
obj_outfile.write(f'#   Energy  Intensity\n')
int_count = 0
for int_count in range(int_lenxas):
    obj_outfile.write(f'{list_xas_e[int_count]} {list_xas_i[int_count]}\n')
    int_count += 1

obj_outfile.close()

# for i in range(len(file_list)):
#     data_list[i] = open(file_list[i][0],"r")
#     data_list_read=data_list[i].readlines()
#     for j in range(len(data_list_read)):
#         line = data_list_read[i].split()
#         if (line and (line[0][0] not in "#"))
#             data[j] += (float(line[file_list[i][1]])*file_list[2])
#     data_list[i].close()
#     del data_list_read
# data_avarage = sum(data)/len(data) 
# infile.close()

obj_logfile.close()
