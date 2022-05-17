#!/bin/bash
set -euo pipefail

array_file=$(ls WFN_B*.1.png)

for l_file in ${array_file}
do
    echo $l_file
    convert $l_file -draw "font-size 100 fill dodgerblue stroke navy stroke-width 2 text 800,300 'Real'" temp_1.png
    mv temp_1.png $l_file
done

array_file=$(ls WFN_B*.2.png)
for l_file in ${array_file}
do
    echo $l_file
    convert $l_file -draw "font-size 100 fill dodgerblue stroke navy stroke-width 2 text 800,300 'Imaginary'" temp_2.png
    mv temp_2.png $l_file
done
