# Magma Installation for ROCm

## MAGMA for ROCm

Matrix Algebra on GPU and Multicore Architectures, abbreviated as MAGMA, is a
collection of next-generation dense linear algebra libraries that is designed
for heterogeneous architectures, such as multiple GPUs and multi- or many-core
CPUs.

MAGMA provides implementations for CUDA, HIP, Intel Xeon Phi, and OpenCL™. For
more information, refer to
[https://icl.utk.edu/magma/index.html](https://icl.utk.edu/magma/index.html).

### Using MAGMA for PyTorch

Tensor is fundamental to Deep Learning techniques because it provides extensive
representational functionalities and math operations. This data structure is
represented as a multidimensional matrix. MAGMA accelerates tensor operations
with a variety of solutions including driver routines, computational routines,
BLAS routines, auxiliary routines, and utility routines.

### Build MAGMA from Source

To build MAGMA from the source, follow these steps:

1. In the event you want to compile only for your uarch, use:

   ```bash
   export PYTORCH_ROCM_ARCH=<uarch>
   ```

   `<uarch>` is the architecture reported by the rocminfo command.

2. Use the following:

   ```bash
   export PYTORCH_ROCM_ARCH=<uarch>

   # "install" hipMAGMA into /opt/rocm/magma by copying after build
   git clone https://bitbucket.org/icl/magma.git
   pushd magma
   # Fixes memory leaks of magma found while executing linalg UTs
   git checkout 5959b8783e45f1809812ed96ae762f38ee701972
   cp make.inc-examples/make.inc.hip-gcc-mkl make.inc
   echo 'LIBDIR += -L$(MKLROOT)/lib' >> make.inc
   echo 'LIB += -Wl,--enable-new-dtags -Wl,--rpath,/opt/rocm/lib -Wl,--rpath,$(MKLROOT)/lib -Wl,--rpath,/opt/rocm/magma/lib' >> make.inc
   echo 'DEVCCFLAGS += --gpu-max-threads-per-block=256' >> make.inc
   export PATH="${PATH}:/opt/rocm/bin"
   if [[ -n "$PYTORCH_ROCM_ARCH" ]]; then
     amdgpu_targets=`echo $PYTORCH_ROCM_ARCH | sed 's/;/ /g'`
   else
     amdgpu_targets=`rocm_agent_enumerator | grep -v gfx000 | sort -u | xargs`
   fi
   for arch in $amdgpu_targets; do
     echo "DEVCCFLAGS += --amdgpu-target=$arch" >> make.inc
   done
   # hipcc with openmp flag may cause isnan() on __device__ not to be found; depending on context, compiler may attempt to match with host definition
   sed -i 's/^FOPENMP/#FOPENMP/g' make.inc
   make -f make.gen.hipMAGMA -j $(nproc)
   LANG=C.UTF-8 make lib/libmagma.so -j $(nproc) MKLROOT=/opt/conda
   make testing/testing_dgemm -j $(nproc) MKLROOT=/opt/conda
   popd
   mv magma /opt/rocm
   ```

## References

C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens and Z. Wojna, "Rethinking the Inception Architecture for Computer Vision," CoRR, p. abs/1512.00567, 2015

PyTorch, \[Online\]. Available: [https://pytorch.org/vision/stable/index.html](https://pytorch.org/vision/stable/index.html)

PyTorch, \[Online\]. Available: [https://pytorch.org/hub/pytorch_vision_inception_v3/](https://pytorch.org/hub/pytorch_vision_inception_v3/)

Stanford, \[Online\]. Available: [http://cs231n.stanford.edu/](http://cs231n.stanford.edu/)

Wikipedia, \[Online\]. Available: [https://en.wikipedia.org/wiki/Cross_entropy](https://en.wikipedia.org/wiki/Cross_entropy)

AMD, "ROCm issues," \[Online\]. Available: [https://github.com/RadeonOpenCompute/ROCm/issues](https://github.com/RadeonOpenCompute/ROCm/issues)

PyTorch, \[Online image\]. [https://pytorch.org/assets/brand-guidelines/PyTorch-Brand-Guidelines.pdf](https://pytorch.org/assets/brand-guidelines/PyTorch-Brand-Guidelines.pdf)

TensorFlow, \[Online image\]. [https://www.tensorflow.org/extras/tensorflow_brand_guidelines.pdf](https://www.tensorflow.org/extras/tensorflow_brand_guidelines.pdf)

MAGMA, \[Online image\]. [https://bitbucket.org/icl/magma/src/master/docs/](https://bitbucket.org/icl/magma/src/master/docs/)

Advanced Micro Devices, Inc., \[Online\]. Available: [https://rocmsoftwareplatform.github.io/AMDMIGraphX/doc/html/](https://rocmsoftwareplatform.github.io/AMDMIGraphX/doc/html/)

Advanced Micro Devices, Inc., \[Online\]. Available: [https://github.com/ROCmSoftwarePlatform/AMDMIGraphX/wiki](https://github.com/ROCmSoftwarePlatform/AMDMIGraphX/wiki)

Docker, \[Online\]. [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)

Torchvision, \[Online\]. Available [https://pytorch.org/vision/master/index.html?highlight=torchvision#module-torchvision](https://pytorch.org/vision/master/index.html?highlight=torchvision#module-torchvision)