#!/bin/bash
set -euo pipefail

awk 'BEGIN{print "#","Timestep","Temperature","FreeEnergy"}/F=/{print $1,$3,$7}' vasp.log > step.dat
