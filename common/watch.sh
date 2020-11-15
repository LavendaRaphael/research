#!/bin/bash
set -eo pipefail
source ~/tianff/myscript/environment.sh

for ((N = 1; N <= 120; N++));do
    echo "-----------------------------------------------------"
    tail $1
    sleep 1s
done

