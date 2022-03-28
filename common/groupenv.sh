#!/bin/bash
# 2021.08.30
if [ ! -z ${groupenv+x} ]; then
if [ "$groupenv" == 'pass' ] ;then
    return
fi
fi

export homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/

echo "#=========================================================================[groupenv.sh]"

#---------------------------------------------[export]
export vasp_pot=${software}src/potpaw_PBE.54/
export ESPRESSO_PSEUDO=${software}src/qe_pseudo/
#export PATH=${homedir}software/vtstscripts-967:$PATH

#source $software/bin/kim-api-activate

#export PLUMED_KERNEL="${software}/lib/libplumedKernel.so"
#export PLUMED_VIMPATH="${software}/src/plumed2.7/vim"
#export PYTHONPATH="${software}/lib/plumed/python:$PYTHONPATH"

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
    echo "none"
else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi

echo "#=========================================================================<<<"
groupenv='pass'

