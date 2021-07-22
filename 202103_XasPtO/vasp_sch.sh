#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh
set -euo pipefail

cd $work_dir

if [ 1 = 1 ];then
    echo "#-------------------------------------------------[plot_core_imdiel.sh]"
    for N in $loopfile
    do
        echo $N
        cd atom_${N}/
        ${software_bin}plot_core_imdiel.sh
        cd ..
    done
fi

if [ 1 = 1 ];then
    echo "#-------------------------------------------------[sft]"
    cat > xas_sft.in <<eof
datafile       "xas.x.dat"
datafile1      "fort13"
datafile2      "fort777"
eof
    for N in $loopfile
    do
        echo $N
        cd atom_${N}/
        grep energy ../atom_1/OUTCAR | tail -1 | awk '{print $7}' | tee fort13
        grep energy OUTCAR | tail -1 | awk '{print $7}' | tee fort777
        ${software_bin}xas_sft.x ../xas_sft.in
        cd ..
    done
    rm xas_sft.in
fi

if [ 1 = 1 ];then
    echo "#-------------------------------------------------[tt]"
    rm -f xas_tt.dat
    for N in $loopfile
    do
        echo $N
        cat atom_${N}/xas_sft.dat >> xas_tt.dat
    done
fi

