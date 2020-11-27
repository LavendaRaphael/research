#!/bin/bash
if [ $local_env ]; then
if $local_env;then
    return
fi
fi
local_env=false
set -eo pipefail
source ~/tianff/codes/common/environment.sh
echo "------------------------------------------------[~/tianff/codes/202011_XasWater32Vasp/local_env.sh]"
O_num=32
echo "O_num=$O_num"

natoms=$[O_num*3]
echo "natoms=$natoms"

script_dir=~/tianff/codes/202011_XasWater32Vasp/
echo "script_dir=${script_dir}"
#=======================================================
work_dir=~/tianff/202011_XasWater32Vasp/server/
echo "work_dir=$work_dir"

subfile=job_sub.sh
echo "subfile=$subfile"

#loopfile="1"
loopfile=`seq 1 $O_num`
#loopfile="8 14 31"
#loopfile="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32"
echo "loopfile=$loopfile"
echo ============================================================================

local_env=true
