nvidia-smi
qstat -f ${PBS_JOBID}|grep exec_gpus
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"

str_gpu_export=$(python << EOF

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
        args=[f"nvidia-smi -q -d UTILIZATION -i {gpu_id}|grep Avg|head -n 1"], 
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

float_utilization_gpu = get_utilization_free(str_gpu_export)
np_memory_free = get_memory_free(str_gpu_export)
for int_time in range(6):
    if (float_utilization_gpu < 10 and np_memory_free > 5000):
        break
    else:
        subprocess_tmp = subprocess.run( args=["nvidia-smi -q|grep Attached"], shell=True ,stdout=subprocess.PIPE, encoding="utf-8")
        int_gpu_all = int(subprocess_tmp.stdout.split()[-1])

        np_memory_free = numpy.zeros(shape=int_gpu_all)
        np_utilization_gpu = numpy.zeros(shape=int_gpu_all)
        for int_gpu in range(int_gpu_all):
            np_memory_free[int_gpu] = get_memory_free(int_gpu)
            np_utilization_gpu[int_gpu] = get_utilization_free(int_gpu)

        int_utilization_gpu_argmin = numpy.argmin(np_utilization_gpu)
        int_memory_free_argmax = numpy.argmax(np_memory_free)
        int_select = int_utilization_gpu_argmin
        if np_memory_free[int_select] > 5000:
            str_gpu_export = int_select
            break
        else:
            open('memory','w+').write(str(int_time))
            time.sleep(600)
            if int_time == 5:
                open('memory','w+').write('timeout')
                str_gpu_export = "timeout"
print(str_gpu_export)

EOF
)

echo str_gpu_export=$str_gpu_export
if [ "$str_gpu_export" == "timeout" ] 
then
    exit 1
else
    export CUDA_VISIBLE_DEVICES=$str_gpu_export
fi

