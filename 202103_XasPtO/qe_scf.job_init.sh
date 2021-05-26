#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir
for i in $loopfile
do
    echo $i
    rm -rf atom_${i}
    mkdir atom_${i}
    cp -r template/* atom_${i}/
    cd atom_${i}/

    num1=$(awk '$1 ~ /^ATOMIC_SPECIES/ {print NR}' scf.in)
    atom1=$(awk 'NR-"'$(($num1+1))'"==0 {print $1} ' scf.in)
    atom2=$(awk 'NR-"'$(($num1+2))'"==0 {print $1} ' scf.in)

    num2=$(awk '$1 ~ /^ATOMIC_POSITIONS/ {print NR}' scf.in)
    line1=$(awk 'NR-"'$(($num2+1))'"==0 {print} ' scf.in)
    line2=$(awk 'NR-"'$(($num2+$i))'"==0 {$1=$1""1;print} ' scf.in)
    sed -i "$(($num2+$i))c $line1" scf.in
    sed -i "$(($num2+1))c $line2" scf.in

    cd ..
done
