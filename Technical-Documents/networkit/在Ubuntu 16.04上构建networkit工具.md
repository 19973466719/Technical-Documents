### <center>**在Ubuntu 16.04上构建networkit工具**</center>
***
[TOC]

#### **概述**
***

networkit是一个大规模图分析库，底层使用并行技术构建软件，本文将主要说明如何在Ubuntu 16.04.5 LTS (GNU/Linux 4.15.0-51-generic x86_64)上构建networkit过程。
#### **使用pip安装**
***

* 检查python版本，确定为3.5以上版本

```shell
python --version  #保证机器安装的是python 3.5以上版本，
# 然后在.bashrc中增加该变量ARCHFLAGS="-arch x86_64"，
# 安装python3之后，
# 使用`sudo rm -rf /usr/bin/python` 和 `sudo ln -s /usr/bini/python3 /usr/bin/python`，再次使用`python --version`查看python版本是否为3.5以上
```

* 初始化安装依赖

```shell
pip install pandas seaborn scipy numpy matplotlib tabulate networkx cython sklearn ipython python3-tk setuptools pygments pickleshare cmake sphinx sphinx_bootstrap_theme nbformat --user   #这些依赖环境在安装过程中可能会却很多，随时安装其他的依赖
pip install --upgrade --force-reinstall pandas seaborn scipy numpy matplotlib tabulate networkx cython sklearn ipython python3-tk setuptools pygments pickleshare cmake sphinx sphinx_bootstrap_theme nbformat --user
sudo apt-get install build-essential
wget https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
sudo unzip ninja-linux.zip -d /usr/local/bin/
sudo update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force
/usr/bin/ninja --version   #安装版本为1.8.2
sudo apt-get install libomp-dev   #安装openmp
apt show libomp-dev   # 查看openmp分发版本
```

* 安装networkit工具

```shell
pip install networkit  #完成上述操作之后，使用该命令安装networkit工具即可
```

#### **源码构建networkit**
***

* 安装依赖

```shell
sudo apt-get install libomp-dev   #安装openmp
pip install pandas seaborn scipy numpy matplotlib tabulate networkx cython sklearn ipython python3-tk setuptools pygments pickleshare cmake sphinx sphinx_bootstrap_theme nbformat --user
sudo apt-get install build-essential
wget https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
sudo unzip ninja-linux.zip -d /usr/local/bin/
sudo update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force
/usr/bin/ninja --version   #安装版本为1.8.2
```

* 构建

```shell
git clone https://github.com/networkit/networkit.git   #源码构建只能采用拉取仓库的方式构建，否则在后续会缺少tlx，不能采用git submodule方法拉取下来进行编译
cd networkit
mkdir buildfile
cd buildfile
cmake ..  #此时会报错： Missing TLX library in extlibs/tlx
cd ..  #回到networkit目录
git submodule update --init  #将缺少的子模块拉取到extlibs文件夹中
cd buildfile
cmake ..  #构建完成
make -j 1000
cd ..   #回到networkit目录下
```

* 安装

```shell
python setup.py build_ext --inplace  #或可以采用下面两条命令代替该条命令
# sudo ARCHFLAGS="-arch x86_64" python setup.py build_ext --inplace -j100
# sudo ARCHFLAGS="-arch x86_64" pip install networkit
```


#### **参考文献**
***

1. 在windows上安装Linux扩展部分 [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. networkit工具 [https://networkit.github.io/](https://networkit.github.io/)
3. 安装高版本ninja [https://www.claudiokuenzler.com/blog/756/install-newer-ninja-build-tools-ubuntu-14.04-trusty](https://www.claudiokuenzler.com/blog/756/install-newer-ninja-build-tools-ubuntu-14.04-trusty)
4. Ubuntu 上构建networkit参考 [https://stackoverflow.com/questions/40349110/unable-to-install-networkit-using-sudo-pip3-install-networkit](https://stackoverflow.com/questions/40349110/unable-to-install-networkit-using-sudo-pip3-install-networkit)