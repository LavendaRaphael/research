echo "export: `export|grep CUDA_VISIBLE_DEVICES`"

exec_gpus=`qstat -f ${PBS_JOBID}|grep exec_gpus`
export CUDA_VISIBLE_DEVICES=${exec_gpus##*/}

echo "CUDA_VISIBLE_DEVICES set to: ${CUDA_VISIBLE_DEVICES}"
