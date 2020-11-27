#!/bin/bash
if [ $local_env ]; then
if $local_env;then
    return
fi
fi
local_env=false
set -eo pipefail
source ~/tianff/codes/common/environment.sh
echo "------------------------------------------------[~/tianff/codes/202011_XasWater32Qe/local_env.sh]"
xascodes_dir=~/tianff/201903_XasIce8Qe/asist/zrsun/xas-ice8/xas-codes/
echo "xascodes_dir=${xascodes_dir}"

xascodes_bin=~/tianff/software/QuatumEspresso/xas-codes/bin/
echo "xascodes_bin=${xascodes_bin}"

qe_cohsex_water_bin=~/tianff/software/QuatumEspresso/qe_cohsex_water/bin/
echo "qe_cohsex_water_bin=$qe_cohsex_water_bin"

Templates_dir=~/tianff/202011_XasWater32Qe/server/Templates/
echo "Templates_dir=$Templates_dir"

O_num=32
echo "O_num=$O_num"

natoms=$[O_num*3]
echo "natoms=$natoms"

vbands=$[O_num*4]
echo "vbands=$vbands"

cbands=$[O_num*4]
echo "cbands=$cbands"

nbands=$[$vbands+$cbands]
echo "nbands=$nbands"

pseudo_dir=~/tianff/201903_XasIce8Qe/asist/zrsun/pseudo/
echo "pseudo_dir=$pseudo_dir"

celldm1=18.6655
echo "celldm1=$celldm1"

volume=`echo "${celldm1}^3"|bc`
echo "volume=$volume"

glines=32850
echo "glines=$glines"

Oxygen1swf_dir=~/tianff/201903_XasIce8Qe/asist/zrsun/xas-ToTangfujie/Oxygen-1s-wf/
echo "Oxygen1swf_dir=${Oxygen1swf_dir}"

script_dir=~/tianff/codes/202011_XasWater32Qe/
echo "script_dir=${script_dir}"
#=======================================================
#pbe_dir=~/tianff/202011_XasWater32Qe/server/pbe/
pbe_dir=~/tianff/202011_XasWater32Qe/server/test_pbe/
echo "pbe_dir=$pbe_dir"

#cohsex_dir=~/tianff/202011_XasWater32Qe/server/cohsex/
cohsex_dir=~/tianff/202011_XasWater32Qe/server/test_cohsex/
echo "cohsex_dir=$cohsex_dir"

work_dir=$cohsex_dir
#work_dir=$pbe_dir
echo "work_dir=$work_dir"

#subfile=pbe_sub.sh
subfile=gw_sub.sh
#subfile=xas_sub.sh
#subfile=test_scf_sub.sh
#subfile=test_cp-scf_sub.sh
#subfile=test_nscf_sub.sh
#subfile=test_cp-nscf_sub.sh
#subfile=test_cp-nscf-wf_sub.sh
echo "subfile=$subfile"

loopfile="1"
#loopfile=`seq 1 $O_num`
#loopfile="8 14 31"
#loopfile="1 2 3 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32"
echo "loopfile=$loopfile"
echo ============================================================================

local_env=true