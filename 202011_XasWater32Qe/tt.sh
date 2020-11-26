#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $work_dir
rm -f tmsftbroad_tt.dat
rm -f tml1_O.dat
rm -f eig_O.dat
for N in $loopfile
do
    cat Oxygen_${N}/tmsftbroad.dat >> tmsftbroad_tt.dat
    echo "$N `head -n 1 Oxygen_${N}/tm.dat`" >> tml1_O.dat
    echo "$N `tail -n 14 Oxygen_${N}/temp/water.eig|head -n 1`" >> eig_O.dat
done
