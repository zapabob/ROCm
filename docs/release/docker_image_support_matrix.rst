******************************************************************
Docker image support matrix
******************************************************************

ROCm 5.7 supports the following `Pytorch <https://hub.docker.com/r/rocm/pytorch>`_ and
`TensorFlow <https://hub.docker.com/r/rocm/tensorflow>`_ Docker images:.


.. tab-set::

    .. tab-item:: PyTorch

        .. tab-set::

            .. tab-item:: Ubuntu

                * ``rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_staging``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `Torch 2.1.0 <https://github.com/ROCmSoftwarePlatform/pytorch/tree/rocm5.7_internal_testing>`_
                    * `Apex 0.1 <https://github.com/ROCmSoftwarePlatform/apex/tree/v0.1>`_
                    * `Torchvision 0.16.0 <https://github.com/pytorch/vision/tree/release/0.16>`_
                    * `Tensorboard 2.14.0 <https://github.com/tensorflow/tensorboard/tree/2.14>`_
                    * `MAGMA <https://bitbucket.org/icl/magma/src/master/>`_
                    * `UCX 1.10.0 <https://github.com/openucx/ucx/tree/v1.10.0>`_
                    * `OMPI 4.0.3 <https://github.com/open-mpi/ompi/tree/v4.0.3>`_
                    * `OFED 5.4.3 <https://content.mellanox.com/ofed/MLNX_OFED-5.3-1.0.5.0/MLNX_OFED_LINUX-5.3-1.0.5.0-ubuntu20.04-x86_64.tgz>`_


                * ``Ubuntu rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_1.12.1``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `Torch 1.12.1 <https://github.com/ROCmSoftwarePlatform/pytorch/tree/release/1.12>`_
                    * `Apex 0.1 <https://github.com/ROCmSoftwarePlatform/apex/tree/v0.1>`_
                    * `Torchvision 0.13.1 <https://github.com/pytorch/vision/tree/v0.13.1>`_
                    * `Tensorboard 2.14.0 <https://github.com/tensorflow/tensorboard/tree/2.14>`_
                    * `MAGMA <https://bitbucket.org/icl/magma/src/master/>`_
                    * `UCX 1.10.0 <https://github.com/openucx/ucx/tree/v1.10.0>`_
                    * `OMPI 4.0.3 <https://github.com/open-mpi/ompi/tree/v4.0.3>`_
                    * `OFED 5.4.3 <https://content.mellanox.com/ofed/MLNX_OFED-5.3-1.0.5.0/MLNX_OFED_LINUX-5.3-1.0.5.0-ubuntu20.04-x86_64.tgz>`_

                * ``Ubuntu rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_1.13.1``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `Torch 1.12.1 <https://github.com/ROCmSoftwarePlatform/pytorch/tree/release/1.13>`_
                    * `Apex 0.1 <https://github.com/ROCmSoftwarePlatform/apex/tree/v0.1>`_
                    * `Torchvision 0.14.0 <https://github.com/pytorch/vision/tree/v0.14.0>`_
                    * `Tensorboard 2.12.0 <https://github.com/tensorflow/tensorboard/tree/2.12.0>`_
                    * `MAGMA <https://bitbucket.org/icl/magma/src/master/>`_
                    * `UCX 1.10.0 <https://github.com/openucx/ucx/tree/v1.10.0>`_
                    * `OMPI 4.0.3 <https://github.com/open-mpi/ompi/tree/v4.0.3>`_
                    * `OFED 5.4.3 <https://content.mellanox.com/ofed/MLNX_OFED-5.3-1.0.5.0/MLNX_OFED_LINUX-5.3-1.0.5.0-ubuntu20.04-x86_64.tgz>`_

                * ``Ubuntu rocm/pytorch:rocm5.7_ubuntu20.04_py3.9_pytorch_2.0.1``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `Torch 2.0.1 <https://github.com/ROCmSoftwarePlatform/pytorch/tree/release/2.0>`_
                    * `Apex 0.1 <https://github.com/ROCmSoftwarePlatform/apex/tree/v0.1>`_
                    * `Torchvision 0.15.2 <https://github.com/pytorch/vision/tree/release/0.15>`_
                    * `Tensorboard 2.14.0 <https://github.com/tensorflow/tensorboard/tree/2.14>`_
                    * `MAGMA <https://bitbucket.org/icl/magma/src/master/>`_
                    * `UCX 1.10.0 <https://github.com/openucx/ucx/tree/v1.10.0>`_
                    * `OMPI 4.0.3 <https://github.com/open-mpi/ompi/tree/v4.0.3>`_
                    * `OFED 5.4.3 <https://content.mellanox.com/ofed/MLNX_OFED-5.3-1.0.5.0/MLNX_OFED_LINUX-5.3-1.0.5.0-ubuntu20.04-x86_64.tgz>`_

            .. tab-item:: CentOS 7

                ``rocm/pytorch:rocm5.7_centos7_py3.9_pytorch_staging``

                * `ROCm 5.7 <https://repo.radeon.com/rocm/yum/5.7/>`_
                * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                * `Torch 2.1.0 <https://github.com/ROCmSoftwarePlatform/pytorch/tree/rocm5.7_internal_testing>`_
                * `Apex 0.1 <https://github.com/ROCmSoftwarePlatform/apex/tree/v0.1>`_
                * `Torchvision 0.16.0 <https://github.com/pytorch/vision/tree/release/0.16>`_
                * `MAGMA <https://bitbucket.org/icl/magma/src/master/>`_

    .. tab-item:: TensorFlow

        .. tab-set::

            .. tab-item:: Ubuntu

                * ``rocm5.7_ubuntu20.04_py3_tensorflow_r2.12-rocm-enhanced_release``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `tensorflow-rocm 2.12.1 <https://pypi.org/project/tensorflow-rocm/2.12.1.570/>`_
                    * `Tensorboard 2.12.3 <https://github.com/tensorflow/tensorboard/tree/2.12>`_

                * ``rocm5.7_ubuntu20.04_py3_tensorflow_r2.13-rocm-enhanced_release``

                    * `ROCm 5.7 <https://repo.radeon.com/rocm/apt/5.7/>`_
                    * `Python 3.9 <https://www.python.org/downloads/release/python-3918/>`_
                    * `tensorflow-rocm 2.13.0 <https://pypi.org/project/tensorflow-rocm/2.13.0.570/>`_
                    * `Tensorboard 2.13.0 <https://github.com/tensorflow/tensorboard/tree/2.13>`_
