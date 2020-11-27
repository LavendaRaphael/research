#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Vasp/local_env.sh
cd $work_dir
for i in $loopfile
do
    echo $i
	rm -rf O_${i}
	mkdir O_${i}
	cp template/* O_${i}/
	cd O_${i}/
    awk "NR==${i}{print}" snap.pos >> POSCAR
    awk "NR!=${i}{print}" snap.pos >> POSCAR
    rm snap.pos
    cd ..
done
