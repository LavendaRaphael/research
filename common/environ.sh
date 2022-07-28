#!/bin/bash
# 2021.08.30
if [ ! -z ${research_environ+x} ]; then
if [ "$research_environ" == 'pass' ] ;then
    return
fi
fi

echo ">>>>----[research/common/envrion.sh]---->>>>"

#---------------------------------------------[jobsub]
if [ "$mycluster" = "qsub" ]; then
    alias jobsub="qsub"
    alias jobkill="qdel"
elif [ "$mycluster" = "sbatch" ]; then
    alias jobsub="sbatch <"
    alias jobkill="scancel"
elif [ "$mycluster" = "bsub" ]; then
    alias jobsub="bsub <"
    alias jobkill="bkill"
elif [ "$mycluster" = "none" ]; then
    true
else
    echo "ERROR: 'mycluster' not set!"
    exit
fi

echo "<<<<--------<<<<"
research_environ='pass'

