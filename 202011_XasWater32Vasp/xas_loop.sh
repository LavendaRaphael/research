#!/bin/bash
source ~/tianff/codes/202011_XasWater32Vasp/local_env.sh
set -euo pipefail

cd $work_dir

echo "=============================================[plot_core_imdiel.sh]"
if [ 0 = 1 ];then
for N in $loopfile
do
    echo $N
    cd O_${N}/
    ~/tianff/codes/202011_XasWater32Vasp/plot_core_imdiel.sh
    cd ..
done
fi
echo "=============================================[sft]"
cat > xas_sft.in <<eof
datafile       "CORE_DIELECTRIC_IMAG.dat"
datafile1      "fort13"
datafile2      "fort777"
eof
sft_dir=~/tianff/202011_XasWater32Qe/server/pbe/
for N in $loopfile
do
    echo $N
    cd O_${N}/
    cp ${sft_dir}/Oxygen_${N}/fort.13 ./fort13
    cp ${sft_dir}/Oxygen_${N}/fort.777 ./fort777
    ${software_bin}xas_sft.x ../xas_sft.in
    rm fort13 fort777
    cd ..
done
rm xas_sft.in
echo "=============================================[tt]"
rm -f xas_tt.dat
for N in $loopfile
do
    echo $N
#    cat O_${N}/CORE_DIELECTRIC_IMAG.dat >> ../xas_tt.dat
    cat O_${N}/xas_sft.dat >> xas_tt.dat
done
echo "=============================================[ave]"
cat > xas_ave.in <<eof
datafile       "xas_tt.dat"
npiece         3000
eof
${software_bin}xas_ave.x xas_ave.in
rm xas_ave.in
echo "=============================================[alignorm]"
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
