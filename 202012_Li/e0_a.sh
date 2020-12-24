#!/bin/bash
source ~/tianff/codes/common/environment.sh
set -euo pipefail

rm -f e0_a.dat
i=4.300
i_end=4.340
while [ "${i_end}" != "${i}" ]; do
i=$(echo "${i}+0.001"|bc)
cat >POSCAR <<!
Li4
$i
        1.0         0.0000000000         0.0000000000
        0.0000000000         1.0         0.0000000000
        0.0000000000         0.0000000000         1.0
   Li
    4
Direct
     0.000000000         0.000000000         0.000000000
     0.000000000         0.500000000         0.500000000
     0.500000000         0.000000000         0.500000000
     0.500000000         0.500000000         0.000000000

!
echo "a= $i"
${software_bin}vasp_std
E=`awk '/F=/ {print $0}' OSZICAR`
echo $i $E  >>e0_a.dat
done


