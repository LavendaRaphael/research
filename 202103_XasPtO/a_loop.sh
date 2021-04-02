#!/bin/bash
homedir=`find ~ -name 'server.me.sh'|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

cd ${homedir}group/202103_XasPtO/server/Pt/Pt-a1b1c1_e500k0.25/

i_pred=$(awk 'NR-2==0  {print $1}' template/POSCAR|tr -d '\r')
for (( i = -20; i <= 20; i++))
do
    a=$(bc <<< "${i_pred}+${i}*0.001")
    echo $a
    rm -rf $a
    mkdir $a
    cd $a
    cp ../template/* ./
    sed -i "2c $a" POSCAR
    sed -i "s/xNAMEx/$a/g" model_sub.sh
    ./model_sub.sh
    rm model_sub.sh
    cd ..
done


