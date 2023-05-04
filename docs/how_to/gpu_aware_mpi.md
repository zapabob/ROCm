# GPU-Enabled MPI

The Message Passing Interface ([MPI](https://www.mpi-forum.org)) is a standard
API for distributed and parallel application development that can scale to
multi-node clusters. To facilitate the porting of applications to clusters with
GPUs, ROCm enables various technologies. These technologies allow users to
directly use GPU pointers in MPI calls and enable ROCm-aware MPI libraries to
deliver optimal performance for both intra-node and inter-node GPU-to-GPU
communication.

The AMD kernel driver exposes Remote Direct Memory Access (RDMA) through the
*PeerDirect* interfaces to allow Host Channel Adapters (HCA, a type of
Network Interface Card or NIC) to directly read and write to the GPU device
memory with RDMA capabilities. These interfaces are currently registered as a
*peer_memory_client* with Mellanox’s OpenFabrics Enterprise Distribution (OFED)
`ib_core` kernel module to allow high-speed DMA transfers between GPU and HCA.
These interfaces are used to optimize inter-node MPI message communication.

This chapter exemplifies how to set up Open MPI with the ROCm platform. The Open
MPI project is an open source implementation of the Message Passing Interface
(MPI) that is developed and maintained by a consortium of academic, research,
and industry partners.

Several MPI implementations can be made ROCm-aware by compiling them with
[Unified Communication Framework](http://www.openucx.org/) (UCX) support. One
notable exception is MVAPICH2: It directly supports AMD GPUs without using UCX,
and you can download it [here](http://mvapich.cse.ohio-state.edu/downloads/).
Use the latest version of the MVAPICH2-GDR package.

The Unified Communication Framework, is an open source cross-platform framework
whose goal is to provide a common set of communication interfaces that targets a
broad set of network programming models and interfaces. UCX is ROCm-aware, and
ROCm technologies are used directly to implement various network operation
primitives. For more details on the UCX design, refer to it's
[documentation](http://www.openucx.org/documentation).

## Building UCX

The following section describes how to set up UCX so it can be used to compile
Open MPI. The following environment variables are set, such that all software
components will be installed in the same base directory (we assume to install
them in your home directory; for other locations adjust the below environment
variables accordingly, and make sure you have write permission for that
location):

```shell
export INSTALL_DIR=$HOME/ompi_for_gpu
export BUILD_DIR=/tmp/ompi_for_gpu_build
mkdir -p $BUILD_DIR
```

```note
The following sequences of build commands assume either the ROCmCC or the AOMP
compiler is active in the environment, which will execute the commands.
```

## Install UCX

The next step is to set up UCX by compiling its source code and install it:

```shell
export UCX_DIR=$INSTALL_DIR/ucx
cd $BUILD_DIR
git clone https://github.com/openucx/ucx.git -b v1.13.0
cd ucx
./autogen.sh
mkdir build
cd build
../contrib/configure-release -prefix=$UCX_DIR \
    --with-rocm=/opt/rocm \
    --without-cuda -enable-optimizations -disable-logging \
    --disable-debug -disable-assertions \
    --disable-params-check -without-java
make -j $(nproc)
make -j $(nproc) install
```

## Install Open MPI

These are the steps to build Open MPI:

```shell
export OMPI_DIR=$INSTALL_DIR/ompi
cd $BUILD_DIR
git clone --recursive https://github.com/open-mpi/ompi.git \
    -b v5.0.x
cd ompi
./autogen.pl
mkdir build
cd build
../configure --prefix=$OMPI_DIR --with-ucx=$UCX_DIR \
    --enable-mca-no-build=btl-uct --enable-mpi1-compatibility \
    CC=clang CXX=clang++ FC=flang
make -j $(nproc)
make -j $(nproc) install
```

## ROCm-enabled OSU

he OSU Micro Benchmarks v5.9 (OMB) can be used to evaluate the performance of
various primitives with an AMD GPU device and ROCm support. This functionality
is exposed when configured with `--enable-rocm` option. We can use the following
steps to compile OMB:

```shell
export OSU_DIR=$INSTALL_DIR/osu
cd $BUILD_DIR
wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-5.9.tar.gz
tar xfz osu-micro-benchmarks-5.9.tar.gz
cd osu-micro-benchmarks-5.9
./configure --prefix=$INSTALL_DIR/osu --enable-rocm \
    --with-rocm=/opt/rocm \
    CC=$OMPI_DIR/bin/mpicc CXX=$OMPI_DIR/bin/mpicxx \
    LDFLAGS="-L$OMPI_DIR/lib/ -lmpi -L/opt/rocm/lib/ \
    $(hipconfig -C) -lamdhip64" CXXFLAGS="-std=c++11"
make -j $(nproc)
```

## Intra-node Run

The following command runs the OSU bandwidth benchmark between the first two GPU
devices (i.e., GPU 0 and GPU 1, same OAM) by default inside the same node. It
measures the unidirectional bandwidth from the first device to the other.

```shell
$OMPI_DIR/bin/mpirun -np 2 --mca btl '^openib' \
   -x UCX_TLS=sm,self,rocm_copy,rocm_ipc \
   --mca pml ucx mpi/pt2pt/osu_bw -d rocm D D
```

To select different devices, for example 2 and 3, use the following command:

```shell
export HIP_VISIBLE_DEVICES=2,3
export HSA_ENABLE_SDMA=0
```

The following output shows the effective transfer bandwidth measured for
inter-die data transfer between GPU device 2 and 3 (same OAM). For messages
larger than 67MB, an effective utilization of about 150GB/sec is achieved, which
corresponds to 75% of the peak transfer bandwidth of 200GB/sec for that
connection:

:::{figure} /data/how_to/gpu_enabled_mpi_1.png
:name: mpi-bandwidth
:alt: OSU execution showing transfer bandwidth increasing alongside payload inc.
Inter-GPU bandwidth with various payload sizes.
:::
