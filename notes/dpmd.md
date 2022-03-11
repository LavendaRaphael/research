# DPMD

## Install from src

<https://github.com/deepmodeling/deepmd-kit/blob/master/doc/install/install-from-source.md>

### TensorFlow

<https://www.tensorflow.org/install/gpu>

### GPU Driver

### CUDA

```sh
export PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/bin:$PATH"
export LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/lib64:$LIBRARY_PATH"
export LD_LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/lib64:$LD_LIBRARY_PATH"
```

### cuDNN

```sh
export LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cudnn-linux-x86_64-8.3.2.44_cuda11.5/lib:$LIBRARY_PATH"
export LD_LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cudnn-linux-x86_64-8.3.2.44_cuda11.5/lib:$LD_LIBRARY_PATH"
```

## Install from conda

和原本安装 tensorflow 冲突
