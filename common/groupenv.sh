#!/bin/bash
# 2021.08.30
if [ ! -z ${groupenv+x} ]; then
if [ "$groupenv" == 'pass' ] ;then
    return
fi
fi

export homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/common/environment.sh

echo "#=========================================================================[groupenv.sh]"

#---------------------------------------------[dir]
export vasp_pot=${homedir}software/potpaw_PBE.54/

export goto_pto_exp=${homedir}group/202103_XasPtO/exp/
export goto_pto_work_110=${homedir}group/202103_XasPtO/server/Pt.110_O_vac/
export goto_pto_code=${homedir}codes/group/202103_XasPtO/
export goto_pto_ms=${homedir}group/202103_XasPtO/structures/Untitled_Files/Documents/
export goto_pto_comput_110=${homedir}comput/group/202103_XasPtO/server/Pt.110_O_vac/

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

