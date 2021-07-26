#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

rm -f E0_a.dat
for i in ${loopfile[*]}
do
    echo $i
    cd a_$i
    E=`awk '/F=/ {print $0}' vasp.log`
    cd ..
    echo $i $E  >>E0_a.dat
done


