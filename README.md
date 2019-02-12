# PPCL

Base PCL python library for deep learning, which DINK needs.

Already supported PointCloud_PointXYZI, PointCloud_PointXYZRGB, PointCloud_PointXYZRGBA ApproximateVoxelGrid.

![PCL](pcl_logo.png)

# QUICK SRART

## 1 Install Depandency

```bash
$ sudo apt-get update 

$ sudo apt-get install git build-essential linux-libc-dev 

$ sudo apt-get install cmake cmake-gui 

$ sudo apt-get install libusb-1.0-0-dev libusb-dev libudev-dev 

$ sudo apt-get install mpi-default-dev openmpi-bin openmpi-common 

$ sudo apt-get install libflann1.8 libflann-dev 

$ sudo apt-get install libeigen3-dev 

$ sudo apt-get install libboost-all-dev 

$ sudo apt-get install libvtk5.10-qt4 libvtk5.10 libvtk5-dev 

$ sudo apt-get install libqhull* libgtest-dev 

$ sudo apt-get install freeglut3-dev pkg-config 

$ sudo apt-get install libxmu-dev libxi-dev 

$ sudo apt-get install mono-complete 

$ sudo apt-get install qt-sdk openjdk-8-jdk openjdk-8-jre 

$ (sudo apt-get install libproj-dev)
```


## 2 Install libpcl-dev


```bash
$ sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl

$ sudo apt-get update

$ sudo apt-get install libpcl-dev
```


## 3 Install PCL

```bash
$ wget   https://github.com/PointCloudLibrary/pcl/archive/pcl-1.9.1.tar.gz

$ tar -xzvf pcl-1.9.1.tar.gz

$ cd pcl-pcl-1.9.1

$ mkdir build && cd build

$ cmake -DCMAKE_BUILD_TYPE=Release ..

$ make -j2

$ sudo make -j2 install
```

## 4 Install PPCL

```bash
$ git clone https://github.com/FPAI/PPCL

$ cd python-pcl

$ sudo python setup.py build_ext -i
$ (sudo python3 setup.py build_ext -i)

$ sudo python setup.py install
$ (sudo python3 setup.py install)
```

## 5 Validation

```bash
$ python

$ import pcl

```

## 6 Test


examples/tests/test_filters.py

run unittest     TestApproximateVoxelGrid Class



***

[![第一太平洋AI](fpai.png)](http://fp-ai.com)

第一太平洋AI，TF源码贡献者顶尖人工智能团队，底层技术驱动上层应用，垂直领域规模化落地。

First Pacific AI, the top AI team of TF source contributors, the bottom technology drives the upper application, and the vertical field is landed on a large scale. Technological fanaticism!!!Solve problem fundamentally!!!


官网|Official website： http://fp-ai.com

联系电话|Contact number： 400-153-0988

商务邮箱|Business email： info@fp-ai.com
