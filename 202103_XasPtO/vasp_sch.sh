#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir

if [ 1 = 1 ];then
    echo "#-------------------------------------------------[plot_core_imdiel.sh]"
    for N in $loopfile
    do
        echo $N
        cd O_${N}/
        ${software_bin}plot_core_imdiel.sh
        cd ..
    done
fi

if [ 0 = 1 ];then
    echo "#-------------------------------------------------[tt]"
    rm -f xas_tt.dat
    for N in $loopfile
    do
        echo $N
        cat O_${N}/CORE_DIELECTRIC_IMAG.dat >> xas_tt.dat
    done
    echo "#-------------------------------------------------[ave]"
    cat > xas_ave.in <<eof
datafile       "xas_tt.dat"
npiece         3000
eof
    ${software_bin}xas_ave.x xas_ave.in
    rm xas_ave.in
    echo "#-------------------------------------------------[alignorm]"
    cat > xas_alignorm.in <<eof
datafile       "xas_ave.dat"
e_align        530                         #eV
area           1.0
e_begin        526.d0                          #eV
e_end          546.d0                          #eV
predge_tolera  0.5
eof
    ${software_bin}xas_alignorm.x xas_alignorm.in
    rm xas_alignorm.in
fi
