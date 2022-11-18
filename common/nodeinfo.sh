cat $PBS_NODEFILE|sort -u|xargs echo 'NODE:'
lscpu|grep "Model name"
echo "PBS_JOBID=$PBS_JOBID"
