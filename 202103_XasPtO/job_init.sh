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
    awk 'NR-"'${i}'"==0{print}' snap.pos >> POSCAR
    awk 'NR-"'${i}'"!=0{print}' snap.pos >> POSCAR
    rm snap.pos
    cd ..
done
