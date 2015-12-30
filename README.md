# 求解多元回归方程的权重系数

> y = w0 + w1 * x1 + w2 * x2 + w3 * x3 

- 使用 python 以及 numpy 库，没有其它扩展库 
- 使用了两种方法
	- 显式解析解的矩阵方法
	- [随机梯度下降算法](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)

- 仓库结构如下，其中：
	- `data.csv` 为数据
	- `main.py `中包含了用两种方法求解的过程，分别写成两个方程`linRegress(x,y)`（矩阵方法）和`sgd(x,y, alpha = 0.001,iteration=100)`（随即梯度下降算法）。
		- `linRegress(x,y)`中采用的是[QR分解](https://en.wikipedia.org/wiki/QR_decomposition)的方法
		- 在随机梯度下降算法中，将全部样本用于训练，w参数在每次训练中都 updata 一次。
		- 为了方便比较，采用了 Root mean square error (RMSE) 作为拟合优度的指标
	- `matrix.py`则是通过构造系数行列式，用[Cramer法](https://en.wikipedia.org/wiki/Cramer%27s_rule)为方程求解的过程。
```                                                                    
├── data.csv                               
├── main.py      
├── matrix.py                                                        
└── README.md       
```

## 简单原理
<math>\begin{bmatrix} w_1 \\ w_2 \end{bmatrix} :=
    \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}
    -  \eta  \begin{bmatrix} 2 (w_1 + w_2 x_i - y_i) \\ 2 x_i(w_1 + w_2 x_i - y_i) \end{bmatrix}.</math>

## 计算结果
- 矩阵方法拟合的结果为：
```                                            
w0=2.031, w1=2.974, w2 = -0.541, w3 = 0.971                                                    
RMSE = 4.854 
```
- 随机梯度下降算法在学习速率（learning rate)为0.001，迭代100次之后的结果为：
```
w0=2.061, w1=2.989, w2 = -0.531, w3 = 0.989 
RMSE = 4.865          
```
