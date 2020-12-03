#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Vasp/local_env.sh

cd $work_dir
rm -f xas_tt.dat
for N in $loopfile
do
	echo $N
	cd O_${N}/
	${script_dir}plot_core_imdiel.sh
    cat CORE_DIELECTRIC_IMAG.dat >> ../xas_tt.dat
	cd ../
done

cat > xas_ave.in <<eof
datafile       "xas_tt.dat"
npiece         3000
eof
${software_bin}xas_ave.x xas_ave.in
rm xas_ave.in
cat > xas_alignorm.in <<eof
datafile       "xas_ave.dat"
e_align        535.10455397636667                         #eV
area           88.3000030518
e_begin        532.d0                          #eV
e_end          546.d0                          #eV
predge_tolera  0.1
eof
${software_bin}xas_alignorm.x xas_alignorm.in
rm xas_alignorm.in
