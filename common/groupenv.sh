#!/bin/bash
# 2021.08.30
if [ ! -z ${groupenv+x} ]; then
if [ "$groupenv" == 'pass' ] ;then
    return
fi
fi

homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

echo "#=========================================================================[groupenv.sh]"

#---------------------------------------------[dir]
vasp_pot=${homedir}software/potpaw_PBE.54/
echo "vasp_pot=${vasp_pot}"

#---------------------------------------------[path]
export PATH=${homedir}software/vtstscripts-967:$PATH

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

