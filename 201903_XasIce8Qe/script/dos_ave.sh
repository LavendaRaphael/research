#!/bin/bash
set -eo pipefail

workhome=/home/tianff/201903/tianff

rm -f water_tt.dos
for N in {1..64}
 
do
	cat Oxygen_${N}/water.dos >> water_tt.dos
done

${workhome}/mycodes/dos_ave.x
