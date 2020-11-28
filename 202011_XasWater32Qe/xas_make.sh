#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $xascodes_bin
ifort -c ${xascodes_dir}pxas_module.f90
mpiifort ${script_dir}pxas.f90 pxas_module.o -o xas.x
ifort ${xascodes_dir}diag_lambda.f90 -o diag_lambda.x -Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a  $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group
ifort ${xascodes_dir}tmsft.f90 -o tmsft.x
ifort ${xascodes_dir}tmsftbroad.f90 -o tmsftbroad.x
ifort ${script_dir}tmsftbroadave.f90 -o tmsftbroadave.x
