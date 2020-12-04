#!/bin/bash
source ~/tianff/codes/common/environment.sh
set -euo pipefail

xascodes_dir=~/tianff/201903_XasIce8Qe/asist/zrsun/xas-ice8/xas-codes/
cd $software_bin
#ifort -c ${xascodes_dir}pxas_module.f90
#mpiifort ~/tianff/codes/202011_XasWater32Qe/pxas.f90 pxas_module.o -o xas.x
#ifort ${xascodes_dir}diag_lambda.f90 -o diag_lambda.x -Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a  $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group
#ifort ${xascodes_dir}tmsft.f90 -o tmsft.x
#ifort ${xascodes_dir}tmsftbroad.f90 -o tmsftbroad.x
ifort ~/tianff/codes/202011_XasWater32Vasp/xas_ave.f90 -o xas_ave.x
ifort ~/tianff/codes/202011_XasWater32Vasp/xas_alignorm.f90 -o xas_alignorm.x
#ifort ~/tianff/codes/202011_XasWater32Vasp/xas_sft.f90 -o xas_sft.x
