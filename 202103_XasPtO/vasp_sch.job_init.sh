#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir
for i in $loopfile
do
    echo $i
    if [ ! -d "atom_${i}" ]; then
        mkdir atom_${i}
    fi

#   ls tempalte/
#   $ INCAR POTCAR vasp_sub.sh
    cp template/* atom_${i}/
    cd atom_${i}/

#6     O   O   X   
#7     1   3   3
    num1=$(awk 'NR-7==0 {print $1}' POSCAR)
    if [ "$num1" != "1" ];then
        awk 'NR-6==0{$1=$1" "$1}1' POSCAR > tmp && mv tmp POSCAR
        awk 'NR-7==0{$1=1" "$1-1}1' POSCAR > tmp && mv tmp POSCAR
    fi

#8      Select
#9      Direct
    num2=$(awk 'NR-8>=0 && NR-9<=0 && $1 ~ /^D/ {print NR}' POSCAR)
    line1=$(awk 'NR-"'$(($num2+1))'"==0 {print} ' POSCAR)
    line2=$(awk 'NR-"'$(($num2+$i))'"==0 {print} ' POSCAR)
    sed -i "$(($num2+1))c $line2" POSCAR
    sed -i "$(($num2+$i))c $line1" POSCAR

    cd ..
done
