#!/bin/bash
source ~/tianff/codes/common/environment.sh
set -euo pipefail

if [ ! -z ${local_env+x} ]; then
if $local_env;then
    return
fi
fi
local_env=false
echo "------------------------------------------------[~/tianff/codes/202011_XasWater32Vasp/local_env.sh]"
O_num=128
echo "O_num=$O_num"

natoms=$[O_num*3]
echo "natoms=$natoms"

script_dir=~/tianff/codes/202012_XasWater128Vasp/
echo "script_dir=${script_dir}"
#=======================================================
work_dir=~/tianff/202012_XasWater128Vasp/server/
echo "work_dir=$work_dir"

subfile=job_sub.sh
echo "subfile=$subfile"

#loopfile="1"
loopfile=`seq 1 $O_num`
#loopfile="8 14 31"
echo "loopfile=$loopfile"
echo ============================================================================

local_env=true
