#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

echo "#-------------------------------------------------[plot_core_imdiel.sh]"
for N in ${loopfile[*]}
do
    echo $N
    cd atom_${N}/
    ${software_bin}plot_core_imdiel.sh
    grep energy ../atom_1/OUTCAR | tail -1 | awk '{print $7}' | tee fort13
    grep energy OUTCAR | tail -1 | awk '{print $7}' | tee fort777
    cd ..
done

cat > xas_ave.in <<eof
datafile       "xas_tt.dat"
npiece         3000
eof

for xyz in ${tensorxyz[*]}
do
    echo "#-------------------------------------------------[sft]"
    cat > xas_sft.in <<eof
datafile       "xas.$xyz.dat"
datafile1      "fort13"
datafile2      "fort777"
eof
    for N in ${loopfile[*]}
    do
        echo $N
        cd atom_${N}/
        ${software_bin}xas_sft.x ../xas_sft.in
        cd ..
    done
    rm xas_sft.in

    echo "#-------------------------------------------------[tt]"
    rm -f xas_tt.dat
    for N in ${loopfile[*]}
    do
        echo $N
        cat atom_${N}/xas_sft.dat >> xas_tt.dat
    done
    
    echo "#-------------------------------------------------[ave]"
    ${software_bin}xas_ave.x xas_ave.in
    mv xas_ave.dat xas_ave.$xyz.dat
done

rm xas_tt.dat xas_ave.log xas_ave.in
