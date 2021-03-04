#!/bin/bash
set -euo pipefail

qstat -l|grep tianff|awk '{print "'${HOME}'/"$3"/vasp.log"}'|xargs tail

