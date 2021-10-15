#/bin/env python
import os

str_jobname = 'test'
int_ncore = 1
str_excute = 'mpirun ${software_bin}intelmpi_test.x'

import os
import math

def def_serversub():
    str_mycluster = os.environ( 'mycluster' )
    int_maxppn = int(os.environ( 'maxppn' ))
    int_nodes = math.ceil( int_ncore/int_maxppn )
    int_ppn = 
    str_nodefile=jobname+'.nodelist'
    str_subfile = str_jobname + '.sh'
    dict_subhead = {}
    dict_subhead[ 'qsub' ]= '
        #PBS -l nodes=${jobnodes}:ppn=${jobppn}
        #PBS -l walltime=240:00:00
        #PBS -N '+jobname+'
        #PBS -q '+jobqueue+'
        #PBS -j oe
        cd $PBS_O_WORKDIR
        cat $PBS_NODEFILE > ${str_nodefile}
        '

    with open( str_subfile, 'w' ) as obj_subfile:
        
