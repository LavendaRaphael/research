#!/bin/bash
homedir=`find ~ -name 'server.me.sh'|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

rm -f e0_a.dat
for i in *
do
    if  [ ! -f $i/OUTCAR ];then
        continue
    fi
    echo -e $i "\t" $(grep '  without' $i/OUTCAR | tail -n 1| awk '{print $7}') >> e0_a.dat 
done

