#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

cd template

# POSCAR
num1=$(awk 'NR-7==0 {print $1}' POSCAR)
num2=$(awk 'NR-8>=0 && NR-9<=0 && $1 ~ /^D/ {print NR}' POSCAR)
cp POSCAR POSCAR.bk
if [ "$num1" != "1" ];then
    awk 'NR-6==0{$1=$1" "$1}1' POSCAR > tmp && mv tmp POSCAR
    awk 'NR-7==0{$1=1" "$1-1}1' POSCAR > tmp && mv tmp POSCAR
fi

# INCAR
nelect=$(awk '/NELECT/{printf "%6.0f",$3}' ../../posopt/OUTCAR)
echo "NELECT = "$nelect
sed -i "/NBANDS/c\  NBANDS = $nelect" INCAR

# POTCAR
source ${software_bin}vasp_pot.sh

cd ..

for i in ${loopfile[@]}
do
    echo $i
    if [ ! -d "atom_${i}" ]; then
        mkdir atom_${i}
    fi

    cp template/* atom_${i}/

    cd atom_${i}/

    rm POSCAR.bk

    #6     O   O   X   
    #7     1   3   3
    if [ "$num1" != "1" ];then
        awk 'NR-6==0{$1=$1" "$1}1' POSCAR > tmp && mv tmp POSCAR
        awk 'NR-7==0{$1=1" "$1-1}1' POSCAR > tmp && mv tmp POSCAR
    fi

    #8      Select
    #9      Direct
    line1=$(awk 'NR-"'$(($num2+1))'"==0 {print} ' POSCAR)
    line2=$(awk 'NR-"'$(($num2+$i))'"==0 {print} ' POSCAR)
    sed -i "$(($num2+1))c $line2" POSCAR
    sed -i "$(($num2+$i))c $line1" POSCAR

    sed -i "s/xNUMx/$i/g"  $subfile

    cd ..
done

cd template
rm POTCAR
mv POSCAR.bk POSCAR
