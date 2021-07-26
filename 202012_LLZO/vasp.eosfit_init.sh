#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

for i in ${loopfile[*]}
do
    echo $i
    rm -rf a_$i
    cp -r template a_$i
    cd a_$i
    sed -i "2c $i" POSCAR
    sed -i "3c 1.0     0.0     0.0" POSCAR
    sed -i "4c 0.0     1.0     0.0" POSCAR
    sed -i "5c 0.0     0.0     1.0" POSCAR
    sed -i "s/xNUMx/$i/g"  $subfile
    cd ..
done


