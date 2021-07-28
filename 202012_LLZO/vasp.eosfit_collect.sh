#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

rm -f E0_a.dat
a0=`awk 'NR-3==0{print $1}' template/POSCAR`
for i in ${loopfile[*]}
do
    echo $i
    cd scal_$i
    E=`awk '/F=/ {print $0}' vasp.log`
    cd ..
    a=`bc <<< "scale=4;$a0*$i"`
    echo $a $E  >>E0_a.dat
done


