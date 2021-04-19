#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir
for i in $loopfile
do
    echo $i
    rm -rf O_${i}
    mkdir O_${i}
    cp template/* O_${i}/
    cd O_${i}/

    num1=$(awk 'NR-7==0 {print $1}' POSCAR)
    if [ "$num1" != "1" ];then
        awk 'NR-6==0{$1=$1" "$1}1' POSCAR > tmp && mv tmp POSCAR
        awk 'NR-7==0{$1=1" "$1-1}1' POSCAR > tmp && mv tmp POSCAR
    fi
    num2=$(awk 'NR-8>=0 && NR-9<=0 && $1 ~ /^D/ {print NR}' POSCAR)
    line1=$(awk 'NR-"'$(($num2+1))'"==0 {print} ' POSCAR)
    line2=$(awk 'NR-"'$(($num2+$i))'"==0 {print} ' POSCAR)
    sed -i "$(($num2+1))c $line2" POSCAR
    sed -i "$(($num2+$i))c $line1" POSCAR

    cd ..
done
