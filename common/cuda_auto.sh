#!/bin/bash

qstat -f ${PBS_JOBID}|grep exec_gpus

str_print=$(python << EOF

import subprocess
import os
import numpy
import time

str_jobid = os.environ["PBS_JOBID"]
subprocess_tmp = subprocess.run( args=[f"qstat -f {str_jobid}|grep exec_gpus"], shell=True ,stdout=subprocess.PIPE, encoding="utf-8")
list_gpu_exec = subprocess_tmp.stdout.split()[-1].split("+")
list_gpu_exec = [ str_gpu.split("/")[-1] for str_gpu in list_gpu_exec ]
str_gpu_exec = ",".join(list_gpu_exec)

str_cuda_visible_devices = os.environ["CUDA_VISIBLE_DEVICES"]

if (str_cuda_visible_devices == "" or str_gpu_exec == str_cuda_visible_devices):
    str_gpu_export = str_gpu_exec
else:
    str_gpu_export = list_gpu_exec[ int(str_cuda_visible_devices) ]

def get_utilization_free(gpu_id) -> float:
    subprocess_tmp = subprocess.run(
        args=[f"nvidia-smi -q -d UTILIZATION -i {gpu_id}|grep Gpu"], 
        shell=True,
        stdout=subprocess.PIPE, 
        encoding="utf-8"
    )
    return float(subprocess_tmp.stdout.split()[-2])

def get_memory_free(gpu_id) -> float:
    subprocess_tmp = subprocess.run(
        args=[f"nvidia-smi -q -d MEMORY -i {gpu_id}|grep Free|head -n 1"], 
        shell=True,
        stdout=subprocess.PIPE, 
        encoding="utf-8"
    )
    return float(subprocess_tmp.stdout.split()[-2])

for int_time in range(6):
    float_utilization_gpu = get_utilization_free(str_gpu_export)
    float_memory_free = get_memory_free(str_gpu_export)
    print('float_utilization_gpu',float_utilization_gpu)
    print('float_memory_free',float_memory_free)
    if (float_utilization_gpu < 100 and float_memory_free > 5000):
        print(str_gpu_export)
        break
    else:
        open('memory','w+').write(str(int_time))
        time.sleep(600)
        if int_time == 5:
            open('memory','w+').write('timeout')
            print("timeout")

EOF
)

echo "$str_print"

str_gpu_export=$(echo "$str_print"|tail -n 1)
if [ "$str_gpu_export" == "timeout" ] 
then
    exit 1
else
    export CUDA_VISIBLE_DEVICES=$str_gpu_export
fi

echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"
