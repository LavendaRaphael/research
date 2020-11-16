#!/bin/sh
set -eo pipefail
source ~/tianff/environment.sh

cd ~/tianff/201903/tianff/xas-codes
rm -f *.mod *.o *.x
mpiifort -c pxas_module.f90
mpiifort pxas.f90 pxas_module.o -o xas.x
mpiifort diag_lambda.f90 -o diag_lambda.x -Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a  $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group
mpiifort tmsft.f90 -o tmsft.x
mpiifort tmsftbroad.f90 -o tmsftbroad.x
mpiifort tmsftbroadave.f90 -o tmsftbroadave.x
