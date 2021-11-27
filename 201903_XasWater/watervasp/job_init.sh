#!/bin/bash
source ~/tianff/codes/202012_XasWater128Vasp/local_env.sh
set -euo pipefail

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
