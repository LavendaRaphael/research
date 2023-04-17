lscpu|grep "Model name"
nvidia-smi
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"

cat $PBS_NODEFILE|sort -u|xargs echo 'NODE:'
echo "PBS_JOBID=$PBS_JOBID"
