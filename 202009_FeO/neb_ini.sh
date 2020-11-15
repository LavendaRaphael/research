#!/bin/bash
set -eo pipefail

image=(01 02 03 04 05 06 07 08 09)
list=(02 04 06 08 10 12 14 16 18)
for j in ${!list[@]}; do
if [ ! -d ${image[j]} ]; then
    mkdir ${image[j]}
fi
cp posfile/degree${list[j]}_POSCAR ${image[j]}/POSCAR
done
