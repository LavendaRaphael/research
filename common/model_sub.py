#/bin/env python
import group_module

str_jobname = 'test'
dict_input = {} 
dict_input[ 'int_ncore' ] = 1
dict_input[ 'int_nodes' ] = 1
dict_input[ 'str_jobqueue' ] = 'test'
str_excute = 'mpirun ${software_bin}intelmpi_test.x'


group_module.def_serversub(
    str_jobname = str_jobname,
    dict_input = dict_input,
    str_excute = str_excute,
    )
    
    
