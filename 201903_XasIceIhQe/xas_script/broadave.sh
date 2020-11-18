#!/bin/bash

set -eo pipefail
source ~/tianff/environment.sh

rm -f tmsftbroad_tt.dat tmsftbroadave.dat
for N in {1,}
 
do
	cat Oxygen_${N}/tmsftbroad.dat >> tmsftbroad_tt.dat
done

~/tianff/201903/tianff/xas-codes/tmsftbroadave.x

