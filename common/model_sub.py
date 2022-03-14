#/bin/env python
import group_module

str_jobname = 'test'
class_mpi = group_module.class_mpi
class_mpi.int_ppn = 1
class_mpi.str_jobqueue =  'test'

str_excute = group_module.def_str_mpiomp
str_excute += '${software}bin/intelmpi_test.x'

group_module.def_serversub(
    str_jobname = str_jobname,
    str_excute = str_excute,
    class_mpi = class_mpi
    )
