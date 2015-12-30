# 求解多元回归方程的权重系数
> y = w0 + w1 * x1 + w2 * x2 + w3 * x3 

- 使用 python 以及 numpy 库，没有其它扩展库 
- 使用了两种方法
	- 显式解析解的矩阵方法
	- 随机梯度下降算法

- 仓库结构如下，其中：
	- `data.csv` 为数据
	- `main.py `中包含了用两种方法求解的方法，分别写成两个方程`linRegress(x,y)`（矩阵方法）和‘`sgd(x,y, alpha = 0.001,iteration=200)`（随即梯度下降算法）。
	- `matrix.py`则是构造系数行列式，用Cramer法为方程求解的过程。
```                                                                    
├── data.csv                               
├── main.py      
├── matrix.py                                                        
└── README.md       
```
