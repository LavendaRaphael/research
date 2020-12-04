#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $work_dir
rm -f tmsftbroad_tt.dat
rm -f tml1_O.dat
rm -f eig_O.dat
rm -f fort.777_tt
for N in $loopfile
do
    echo ${N}
#    cat Oxygen_${N}/tmsftbroad.dat >> tmsftbroad_tt.dat
#    echo "$N `head -n 1 Oxygen_${N}/tm.dat`" >> tml1_O.dat
#    echo "$N `tail -n 14 Oxygen_${N}/temp/water.eig|head -n 1`" >> eig_O.dat
done
cat > xas_alignorm.in <<eof
datafile       "tmsftbroadsum.dat"
e_align        535.10455397636667                         #eV
area           88.3000030518
e_begin        532.d0                          #eV
e_end          546.d0                          #eV
predge_tolera  0.1
eof
#${xascodes_bin}tmsftbroadsum.x
#${xascodes_bin}xas_alignorm.x xas_alignorm.in
#mv tmsftbroadsum.dat.norm tmsftbroadalignorm.dat
rm -f xas_alignorm.in
