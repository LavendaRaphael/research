#!/bin/bash
set -euo pipefail

min=$(awk 'NR==1{min=$2;next}{min=min-$2<0?min:$2}END{print min}' $1)
awk '{$2=$2-"'$min'"}1' $1 > ${1}.ysft

