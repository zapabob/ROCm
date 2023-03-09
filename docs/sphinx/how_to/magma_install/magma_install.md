# Magma Installation for ROCm

Pull content from
<https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.4.1/page/Frameworks_Installation.html>

The following sections cover the different framework installations for ROCm and
Deep Learning applications. Figure 5 provides the sequential flow for the use of
each framework. Refer to the ROCm Compatible Frameworks Release Notes for each
framework's most current release notes at
[/bundle/ROCm-Compatible-Frameworks-Release-Notes/page/Framework_Release_Notes.html](/bundle/ROCm-Compatible-Frameworks-Release-Notes/page/Framework_Release_Notes.html).

| ![Figure 5](figures/image.005.png)|
|:--:|
| <b>Figure 5. ROCm Compatible Frameworks Flowchart</b>|

## PyTorch
PyTorch is an open source Machine Learning Python library, primarily differentiated by Tensor computing with GPU acceleration and a type-based automatic differentiation. Other advanced features include:
- Support for distributed training
- Native ONNX support
- C++ frontend
- The ability to deploy at scale using TorchServe
- A production-ready deployment mechanism through TorchScript
### Installing PyTorch
To install ROCm on bare metal, refer to the section [ROCm Installation](https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.4-/page/Prerequisites.html#d2999e60). The recommended option to get a PyTorch environment is through Docker. However, installing the PyTorch wheels package on bare metal is also supported.
#### Option 1 (Recommended): Use Docker Image with PyTorch Pre-installed
Using Docker gives you portability and access to a prebuilt Docker container that has been rigorously tested within AMD. This might also save on the compilation time and should perform as it did when tested without facing potential installation issues.
Follow these steps:
1. Pull the latest public PyTorch Docker image.

```
docker pull rocm/pytorch:latest
```

Optionally, you may download a specific and supported configuration with different user-space ROCm versions, PyTorch versions, and supported operating systems. To download the PyTorch Docker image, refer to [https://hub.docker.com/r/rocm/pytorch](https://hub.docker.com/r/rocm/pytorch).

2. Start a Docker container using the downloaded image.

```
docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latest
```

:::{note}
This will automatically download the image if it does not exist on the host. You can also pass the -v argument to mount any data directories from the host onto the container.
:::

#### Option 2: Install PyTorch Using Wheels Package
PyTorch supports the ROCm platform by providing tested wheels packages. To access this feature, refer to [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/) and choose the "ROCm" compute platform. Figure 6 is a matrix from pytroch.org that illustrates the installation compatibility between ROCm and the PyTorch build.


| ![Figure 6](figures/image.006.png)|
|:--:|
| <b>Figure 6.  Installation Matrix from Pytorch.org</b>|


To install PyTorch using the wheels package, follow these installation steps:

1. Choose one of the following options:

a. Obtain a base Docker image with the correct user-space ROCm version installed from [https://hub.docker.com/repository/docker/rocm/dev-ubuntu-20.04](https://hub.docker.com/repository/docker/rocm/dev-ubuntu-20.04).

 or

b.  Download a base OS Docker image and install ROCm following the installation directions in the section [Installation](https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.4-/page/Prerequisites.html#d2999e60). ROCm 5.2 is installed in this example, as supported by the installation matrix from pytorch.org.

or

 c.  Install on bare metal. Skip to Step 3.

```
docker run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/dev-ubuntu-20.04:latest
```
3. Install any dependencies needed for installing the wheels package.

```
sudo apt update
sudo apt install libjpeg-dev python3-dev
pip3 install wheel setuptools
```

4. Install torch, torchvision, and torchaudio as specified by the installation matrix.

:::{note}
ROCm 5.2 PyTorch wheel in the command below is shown for reference.
:::


```
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/rocm5.2/
```

#### Option 3: Install PyTorch Using PyTorch ROCm Base Docker Image
A prebuilt base Docker image is used to build PyTorch in this option. The base Docker has all dependencies installed, including:
- ROCm
- Torchvision
- Conda packages
- Compiler toolchain
Additionally, a particular environment flag (BUILD_ENVIRONMENT) is set, and the build scripts utilize that to determine the build environment configuration.

Follow these steps:

1. Obtain the Docker image.
```
docker pull rocm/pytorch:latest-base
```
The above will download the base container, which does not contain PyTorch.

2. Start a Docker container using the image.
```
docker run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --shm-size 8G rocm/pytorch:latest-base
```
You can also pass the -v argument to mount any data directories from the host onto the container.

3. Clone the PyTorch repository.
```
cd ~
git clone https://github.com/pytorch/pytorch.git
cd pytorch
git submodule update --init –recursive
```

4. Build PyTorch for ROCm.
:::{note}
By default in the rocm/pytorch:latest-base, PyTorch builds for these architectures simultaneously:
- gfx900
- gfx906
- gfx908
- gfx90a
- gfx1030
:::

5. To determine your AMD uarch, run:
```
rocminfo | grep gfx
```

6. In the event you want to compile only for your uarch, use:
```
export PYTORCH_ROCM_ARCH=<uarch>
```
\<uarch\> is the architecture reported by the rocminfo command. is the architecture reported by the rocminfo command.

7.  Build PyTorch using the following command:
```
./.jenkins/pytorch/build.sh
```
This will first convert PyTorch sources for HIP compatibility and build the PyTorch framework.

8. Alternatively, build PyTorch by issuing the following commands:
```
python3 tools/amd_build/build_amd.py
USE_ROCM=1 MAX_JOBS=4 python3 setup.py install ––user
```
#### Option 4: Install Using PyTorch Upstream Docker File
Instead of using a prebuilt base Docker image, you can build a custom base Docker image using scripts from the PyTorch repository. This will utilize a standard Docker image from operating system maintainers and install all the dependencies required to build PyTorch, including
- ROCm
- Torchvision
- Conda packages
- Compiler toolchain

Follow these steps:

1. Clone the PyTorch repository on the host.
```
cd ~
git clone https://github.com/pytorch/pytorch.git
cd pytorch
git submodule update --init –recursive
```

2. Build the PyTorch Docker image.
```
cd.circleci/docker
./build.sh pytorch-linux-bionic-rocm<version>-py3.7 
# eg. ./build.sh pytorch-linux-bionic-rocm3.10-py3.7
```
This should be complete with a message "Successfully build &lt;image_id&gt;."

3. Start a Docker container using the image:
```
docker run -it --cap-add=SYS_PTRACE --security-opt 
seccomp=unconfined --device=/dev/kfd --device=/dev/dri --group-add 
video --ipc=host --shm-size 8G <image_id>
```
You can also pass -v argument to mount any data directories from the host onto the container.

4. Clone the PyTorch repository.
```
cd ~
git clone https://github.com/pytorch/pytorch.git
cd pytorch
git submodule update --init --recursive
```

5. Build PyTorch for ROCm.

:::{note}
By default in the rocm/pytorch:latest-base, PyTorch builds for these architectures simultaneously:
- gfx900
- gfx906
- gfx908
- gfx90a
- gfx1030
:::

6. To determine your AMD uarch, run:
```
rocminfo | grep gfx
```

7. If you want to compile only for your uarch:
```
export PYTORCH_ROCM_ARCH=<uarch>
```
\<uarch\> is the architecture reported by the rocminfo command.

8. Build PyTorch using:
```
./.jenkins/pytorch/build.sh
```
This will first convert PyTorch sources to be HIP compatible and then build the PyTorch framework.

Alternatively, build PyTorch by issuing the following commands:
```
python3 tools/amd\_build/build\_amd.py
USE\_ROCM=1 MAX\_JOBS=4 python3 setup.py install --user
```

### Test the PyTorch Installation
You can use PyTorch unit tests to validate a PyTorch installation. If using a prebuilt PyTorch Docker image from AMD ROCm DockerHub or installing an official wheels package, these tests are already run on those configurations. Alternatively, you can manually run the unit tests to validate the PyTorch installation fully.

Follow these steps:

1. Test if PyTorch is installed and accessible by importing the torch package in Python.
:::{note}
Do not run in the PyTorch git folder.
:::
```
python3 -c 'import torch' 2> /dev/null && echo 'Success' || echo 'Failure'
```

2. Test if the GPU is accessible from PyTorch. In the PyTorch framework, torch.cuda is a generic mechanism to access the GPU; it will access an AMD GPU only if available.
```
python3 -c 'import torch; print(torch.cuda.is_available())'
```

3. Run the unit tests to validate the PyTorch installation fully. Run the following command from the PyTorch home directory:
```
BUILD_ENVIRONMENT=${BUILD_ENVIRONMENT:-rocm} ./.jenkins/pytorch/test.sh
```
This ensures that even for wheel installs in a non-controlled environment, the required environment variable will be set to skip certain unit tests for ROCm.
:::{note}
Make sure the PyTorch source code is corresponding to the PyTorch wheel or installation in the Docker image. Incompatible PyTorch source code might give errors when running the unit tests.
:::
This will first install some dependencies, such as a supported torchvision version for PyTorch. Torchvision is used in some PyTorch tests for loading models. Next, this will run all the unit tests.
:::{note}
Some tests may be skipped, as appropriate, based on your system configuration. All features of PyTorch are not supported on ROCm, and the tests that evaluate these features are skipped. In addition, depending on the host memory, or the number of available GPUs, other tests may be skipped. No test should fail if the compilation and installation are correct.
:::

4. Run individual unit tests with the following command:
```
PYTORCH\_TEST\_WITH\_ROCM=1 python3 test/test\_nn.py --verbose
```
test_nn.py can be replaced with any other test set.

### Run a Basic PyTorch Example
The PyTorch examples repository provides basic examples that exercise the functionality of the framework. MNIST (Modified National Institute of Standards and Technology) database is a collection of handwritten digits that may be used to train a Convolutional Neural Network for handwriting recognition. Alternatively, ImageNet is a database of images used to train a network for visual object recognition.

Follow these steps:

1. Clone the PyTorch examples repository.
```
git clone https://github.com/pytorch/examples.git
```

2. Run the MNIST example.
```
cd examples/mnist
```

3. Follow the instructions in the README file in this folder. In this case:
```
pip3 install -r requirements.txt
python3 main.py
```

4. Run the ImageNet example.
```
cd examples/imagenet
```

5. Follow the instructions in the README file in this folder. In this case:
```
pip3 install -r requirements.txt
python3 main.py
```

## MAGMA for ROCm
Matrix Algebra on GPU and Multicore Architectures, abbreviated as MAGMA, is a collection of next-generation dense linear algebra libraries that is designed for heterogeneous architectures, such as multiple GPUs and multi- or many-core CPUs.

MAGMA provides implementations for CUDA, HIP, Intel Xeon Phi, and OpenCL™. For more information, refer to [https://icl.utk.edu/magma/index.html](https://icl.utk.edu/magma/index.html).

### Using MAGMA for PyTorch
Tensor is fundamental to Deep Learning techniques because it provides extensive representational functionalities and math operations. This data structure is represented as a multidimensional matrix. MAGMA accelerates tensor operations with a variety of solutions including driver routines, computational routines, BLAS routines, auxiliary routines, and utility routines.

### Build MAGMA from Source
To build MAGMA from the source, follow these steps:

1. In the event you want to compile only for your uarch, use:
```
export PYTORCH_ROCM_ARCH=<uarch>
```
\<uarch\> is the architecture reported by the rocminfo command.

2. Use the following:
```
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
## TensorFlow
TensorFlow is an open source library for solving Machine Learning, Deep Learning, and Artificial Intelligence problems. It can be used to solve many problems across different sectors and industries but primarily focuses on training and inference in neural networks. It is one of the most popular and in-demand frameworks and is very active in open source contribution and development.

### Installing TensorFlow
The following sections contain options for installing TensorFlow.

#### Option 1: Install TensorFlow Using Docker Image
To install ROCm on bare metal, follow the section [ROCm Installation](https://docs.amd.com/bundle/ROCm-Deep-Learning-Guide-v5.4-/page/Prerequisites.html#d2999e60). The recommended option to get a TensorFlow environment is through Docker.

Using Docker provides portability and access to a prebuilt Docker container that has been rigorously tested within AMD. This might also save compilation time and should perform as tested without facing potential installation issues.
Follow these steps:

1. Pull the latest public TensorFlow Docker image.
```
docker pull rocm/tensorflow:latest
```

2. Once you have pulled the image, run it by using the command below:
```
docker run -it --network=host --device=/dev/kfd --device=/dev/dri 
--ipc=host --shm-size 16G --group-add video --cap-add=SYS\_PTRACE 
--security-opt seccomp=unconfined rocm/tensorflow:latest
```

#### Option 2: Install TensorFlow Using Wheels Package
To install TensorFlow using the wheels package, follow these steps:

1. Check the Python version.
```
python3 –version
```
| If:      | Then: |
| ----------- | ----------- |
| The Python version is less than 3.7      | Upgrade Python.       |
| The Python version is more than 3.7   | Skip this step and go to Step 3.        |
:::{note}
The supported Python versions are:
- 3.7
- 3.8
- 3.9
- 3.10
:::
```
sudo apt-get install python3.7 # or python3.8 or python 3.9 or python 3.10
```

2. Set up multiple Python versions using update-alternatives.
```
update-alternatives --query python3
sudo update-alternatives --install
/usr/bin/python3 python3 /usr/bin/python[version] [priority]
```
:::{note}
Follow the instruction in Step 2 for incompatible Python versions.
:::
```
sudo update-alternatives --config python3
```

3. Follow the screen prompts, and select the Python version installed in Step 2.

4. Install or upgrade PIP.
```
sudo apt install python3-pip
```
To install PIP, use the following:
```
/usr/bin/python[version]  -m pip install --upgrade pip
```
Upgrade PIP for Python version installed in step 2:
```
sudo pip3 install --upgrade pip
```

5. Install TensorFlow for the Python version as indicated in Step 2.
```
/usr/bin/python[version] -m pip install --user tensorflow-rocm==[wheel-version] –upgrade
```
For a valid wheel version for a ROCm release, refer to the instruction below:
 ```
sudo apt install rocm-libs rccl
 ```

6. Update protobuf to 3.19 or lower.
```
/usr/bin/python3.7  -m pip install protobuf=3.19.0
sudo pip3 install tensorflow
```

7. Set the environment variable PYTHONPATH.
```
export PYTHONPATH="./.local/lib/python[version]/site-packages:$PYTHONPATH"  #Use same python version as in step 2
```

8. Install libraries.
```
sudo apt install rocm-libs rccl
```

9. Test installation.
```
python3 -c 'import tensorflow' 2> /dev/null && echo 'Success' || echo 'Failure'
```
:::{note}
For details on tensorflow-rocm wheels and ROCm version compatibility, see: [https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/develop-upstream/rocm_docs/tensorflow-rocm-release.md)
:::

### Test the TensorFlow Installation
To test the installation of TensorFlow, run the container image as specified in the previous section Installing TensorFlow. Ensure you have access to the Python shell in the Docker container.
```
python3 -c 'import tensorflow' 2> /dev/null && echo ‘Success’ || echo ‘Failure’
```

### Run a Basic TensorFlow Example
The TensorFlow examples repository provides basic examples that exercise the framework's functionality. The MNIST database is a collection of handwritten digits that may be used to train a Convolutional Neural Network for handwriting recognition.

Follow these steps:
1. Clone the TensorFlow example repository.
```
cd ~
git clone https://github.com/tensorflow/models.git
```

2. Install the dependencies of the code, and run the code.
```
#pip3 install requirement.txt
#python mnist\_tf.py
```
