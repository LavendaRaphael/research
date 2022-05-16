#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir
for i in $loopfile
do
    echo $i
    rm -rf atom_${i}/$sub_dir
    cp -r template/$sub_dir atom_${i}/

done
