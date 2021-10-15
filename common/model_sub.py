#/bin/env python
import groupmodule

str_jobname = 'test'
int_ncore = 58
str_excute = 'mpirun ${software_bin}intelmpi_test.x'

groupmodule.def_serversub(
                str_jobname = str_jobname,
                int_ncore = int_ncore,
                str_excute = str_excute
                )
    
    
