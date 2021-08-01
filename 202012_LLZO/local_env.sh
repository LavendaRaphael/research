#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

if [ ! -z ${local_env+x} ]; then
if $local_env;then
    return
fi
fi
local_env=false
echo "---------------------------------------------------------------------------[local_env.sh]"
# work_dir=${goto_llzo_li}Li.a1b1c1_eosfit/
# work_dir=${goto_llzo_au}Au.a1b1c1_eosfit/
  work_dir=${goto_llzo_llzo}Li7La3Zr2O12.a1b1c1_eosfit/

echo "work_dir=$work_dir"

  subfile=vasp_sub.sh
echo "subfile=$subfile"

# loopfile=(0.94 0.95 0.96)
# loopfile=$(seq 0.90 0.01 1.10)
# loopfile=$(seq 0.90 0.02 1.10)
 loopfile=$(seq 0.91 0.02 1.09)
echo "loopfile=$loopfile"

echo "#=========================================================================<<<"

local_env=true
