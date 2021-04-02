#!/bin/bash
homedir=`find ~ -name 'server.me.sh'|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

cd ${homedir}group/202103_XasPtO/server/Pt/Pt-a1b1c1_e500k0.25/
rm -f e0_a.dat
for i in *
do
    if  [ ! -f $i/OUTCAR ];then
        continue
    fi
    echo -e $i "\t" $(grep '  without' $i/OUTCAR | tail -n 1| awk '{print $7}') >> e0_a.dat 
done

