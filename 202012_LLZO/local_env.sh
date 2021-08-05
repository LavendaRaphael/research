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
# work_dir=${goto_llzo_li}Li.a1b1c1_eosfit.PBE-D3/
# work_dir=${goto_llzo_li}Li.a1b1c1_eosfit.optB88-vdW/
# work_dir=${goto_llzo_au}Au.a1b1c1_eosfit/
 work_dir=${goto_llzo}LLZO/Li7La3Zr2O12.a1b1c1_eosfit/
echo "work_dir=$work_dir"

  subfile=vasp_sub.sh
echo "subfile=$subfile"

 loopfile=(0.91 0.92 0.93 0.95 0.97 0.98 0.99 1.00 1.01 1.03)
# loopfile=$(seq 0.90 0.01 1.10)
# loopfile=$(seq 0.90 0.02 1.10)
echo "loopfile=$loopfile"

echo "#=========================================================================<<<"

local_env=true
