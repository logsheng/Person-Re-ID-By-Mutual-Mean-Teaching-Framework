# Person-Re-ID-By-Mutual-Mean-Teaching-Framework

请都写成个类方便调用
有些参数请参考论文
保持文件层级一样
如有更改请更改在这readme！
以下仅代表个人想法

建议先做datasets部分

论文3.2.1在源域上对网络有监督训练(stage1也是要训练两个网络的）：
1. 网络ibn_resnet将样本进行特征表示
2. 分类器（聚类算法?)clustering根据特征表示输出M个类别的概率，这就是硬伪标签吧.
3. 根据标签计算损失

论文3.2.2
1. （用stage1的两个网络来初始化stage2的）训练两个初始化不同的网络
2. 分别喂随机增强的图像
3. 还是会用聚类算法clustering.py生成硬伪标签
4. 但是多了在线软伪标签，由网络捕捉到的数据分布和预测得出
在线软伪标签由来自对方网络的平均模型，而不是当前的对方网络（导致网络收敛至相似以及误差被放大）




data  
├── dukemtmc  
├── market1501

code  
├── pre_training (stage1)  
&emsp;&emsp; └── resnet.py 文中有两个backbone:resnet和ibn_resnet，他们在stage2都要被初始化  
&emsp;&emsp; └── ibn_resnet.py  
&emsp;&emsp; └── clustering.py  
&emsp;&emsp; └── train.py  
    
├── training_with_mmt (stage2) 这我还没想好怎么分  
&emsp;&emsp; └── mmt.py  
&emsp;&emsp; └── train.py  
    
├── datasets  
&emsp;&emsp; └── dukemtmc.py 怎么下载要不要写...应该要写到能够直接返回data和target，大概率继承Dataset实现里面的方法，预处理可以写成个方法如果有的话  
&emsp;&emsp; └── market.py  
    
├── utils  
&emsp;&emsp; └── loss.py  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; def cross_entropy()  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; def triplet()  
&emsp;&emsp; └── metrics.py  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; def mean_average_precision()  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; def cmc()  
