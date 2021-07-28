#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

for i in ${loopfile[*]}
do
    echo $i
    rm -rf scal_$i
    cp -r template scal_$i
    cd scal_$i
    sed -i "2c $i" POSCAR
    sed -i "s/xNUMx/$i/g"  $subfile
    cd ..
done


