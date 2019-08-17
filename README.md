## **使用到的第三方开发Library**

* Boost https://www.boost.org/   （C++语言增强库）
* Dlib http://dlib.net/   安装Dlib之前首先应该编译Boost，机器学习库
* TensorFlow  https://www.tensorflow.org/
* igraph http://igraph.org/ （图API）
* libpqxx https://github.com/jtv/libpqxx   （C语言连接PostgreSQL数据库）
* json-c https://github.com/json-c/json-c     将数据封装为JSON格式（C语言）
* Google Protocol Buffer https://github.com/protocolbuffers/protobuf/releases   结构化数据序列化工具
* word2vec https://arxiv.org/pdf/1310.4546.pdf  https://code.google.com/archive/p/word2vec/  https://rare-technologies.com/word2vec-tutorial/#app  https://juejin.im/post/59f13363f265da431875f746 (中文维基百科语料)
* networkx https://networkx.github.io/ (图API)

## **使用的技术**

* RDMA Remote Direct Memory Access  远程内存直接访问
    * IB-verbs
* Graph Theory and Graph Database
    * Properties Graph Databases
    * RDF Graph Databases
* storage techniques
    * NVMe SSD
    * NFS
    * DNFS
* Linux System Programming
    * system call
    * glibc
    * C Compile
    * GNU Makefile https://seisman.github.io/how-to-write-makefile/overview.html
    * automake
* 库的编译与安装
    * pkg-config 使用 https://people.freedesktop.org/~dbn/pkg-config-guide.html ，尤其要学会写.pc文件，并添加到环境变量中
    * 编译动态与静态链接库，通过写.pc文件，使得pkg-config可用 
    ```shell
    gcc -fPIC -shared -o libxxx.so.1.0.0 xxx.c 将共享库编译为标准格式libxxx.so.1.0.0   
    ln -s libxxx.so.1.0.0 libxxx.so    建立符号链接，将其指向最新版本的共享库
    ```
* RPC （Romote Procedure Calls） 远程过程调用
    * 安装`sudo apt-get install rpcbind`，用其提供portmap服务
    * RPC programming
    * Google Protocol Buffer： https://www.ibm.com/developerworks/cn/linux/l-cn-gpb/index.html
* 并行程序设计（Parallel Programming）
    * pthread多核、共享内存并行程序设计
    * CUDA数据并行程序设计
    * MPI分布式内存并行程序设计
    * openMP共享内存并行程序设计
* Machine Learning 机器学习
    * 监督学习
    * 非监督学习
* FPGA 现场可编程门阵列
    * Zynq UltraScale+ MPSoC ZCU102 （20000RMB）
    * Zynq UltraScale+ MPSoC ZCU104 （8000RMB）
    * verilog
    * C语言交叉编译技术
* Text Mining  文本挖掘
* Deep Learing 深度学习
* 知识图谱
    * 信息/知识抽取
        * 命名实体识别
        * 关系抽取
    * 知识存储
    * 知识表示
    * 知识学习与挖掘
