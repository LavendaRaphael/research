import os
import math
import subprocess

def def_serversub( 
         str_jobname,
         int_ncore,
         str_excute
         ):
    str_homedir = os.environ[ 'homedir' ]
    str_mycluster = os.environ[ 'mycluster' ]
    str_jobqueue = os.environ[ 'jobqueue' ]
    int_maxppn = int(os.environ[ 'maxppn' ])

    str_jobname = 'tff.'+str_jobname
    int_nodes = math.ceil( int_ncore/int_maxppn )
    int_ppn = math.ceil( int_ncore/int_nodes )
    str_nodefile = str_jobname+'.nodelist'
    str_subfile = str_jobname + '.sh'

    dict_subconfig = {}
    dict_jobsub = {}
    dict_subconfig[ 'qsub' ] = (
        '#PBS -l nodes='+str(int_nodes)+':ppn='+str(int_ppn)+'\n'+
        '#PBS -l walltime=240:00:00\n'+
        '#PBS -N '+str_jobname+'\n'+
        '#PBS -q '+str_jobqueue+'\n'+
        '#PBS -j oe\n'+
        'cd $PBS_O_WORKDIR\n'+
        'cat $PBS_NODEFILE > '+str_nodefile+'\n'
        )
    dict_jobsub[ 'qsub' ] = 'qsub '+str_subfile

    str_timecount='echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s."'

    str_subhead = (
        'source '+str_homedir+'codes/common/environment.sh\n'+
        'set -euo pipefail\n'+
        'SECONDS=0\n'+
        'sort -u '+str_nodefile+' > '+str_nodefile+'.tmp && mv '+str_nodefile+'.tmp '+str_nodefile+'\n'
        )

    with open( str_subfile, 'w' ) as obj_subfile:
        obj_subfile.write( dict_subconfig[ str_mycluster ] ) 
        obj_subfile.write( str_subhead )
        obj_subfile.write( str_excute )
        obj_subfile.write( '\n' )
        obj_subfile.write( str_timecount )
    subprocess.run( dict_jobsub[ str_mycluster ].split()  )

