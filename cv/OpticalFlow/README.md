[光流Optical Flow介绍与OpenCV实现](https://blog.csdn.net/zouxy09/article/details/8683859)

[OpenCv Optical Flow](https://docs.opencv.org/3.3.1/d7/d8b/tutorial_py_lucas_kanade.html)

[维基百科 光流法](https://zh.wikipedia.org/wiki/%E5%85%89%E6%B5%81%E6%B3%95)


# Optical Flow
Optical flow 有两个假设：
1. 在相邻连续两帧中一个目标的像素强度不会变化。
2. 周围像素有类似运行。

假设在第一帧中像素 $I(x,y,t)$，$dt$时间后，在下一帧中它运动了 $(dx, dy)$。因为像素相同，强度没有变化。

$$ I(x,y,t) = I(x+dx, y+dy, t+dt) $$

根据Taylor 级数得到：

$$ I(x+dx, y+dy, t+dt) = I(x,y,t) + \frac{\partial I}{\partial x}\Delta x +  \frac{\partial I}{\partial y}\Delta y + \frac{\partial I}{\partial t}\Delta t$$

因此：

$$ \frac{\partial I}{\partial x}\Delta x +  \frac{\partial I}{\partial y}\Delta y + \frac{\partial I}{\partial t}\Delta t = 0$$

或者

$$ \frac{\partial I}{\partial x} \frac{\Delta x}{\Delta t} +  \frac{\partial I}{\partial y}\frac{\Delta y}{\Delta t} + \frac{\partial I}{\partial t}\frac{\Delta t}{\Delta t} = 0$$

用速度来代替后：

$$ \frac{\partial I}{\partial x} V_x +  \frac{\partial I}{\partial y} V_y + \frac{\partial I}{\partial t} = 0$$

# Lucas-Kanade method


此方法取点周围 3x3 的patch 。9个点有相同的运动。
推导过程 ：

$$ I(x,y,t) = I(x+dx, y+dy, t+dt) $$


$$ f_x u + f_y v + f_t = 0 $$


$$ f_x = \frac{\partial f}{\partial x} $$
$$ f_y = \frac{\partial f}{\partial y} $$
$$ u = \frac{dx}{dt} $$
$$ v = \frac{dy}{dt} $$

$$ \begin{bmatrix}
u\\ 
v
\end{bmatrix} 
=
\begin{bmatrix}
\Sigma_i f_{x_i} ^ 2 & \Sigma_i f_{x_i} f_{y_i} \\ 
\Sigma_i f_{x_i} f_{y_i} & \Sigma_i f_{x_i} ^ 2
\end{bmatrix}^{-1}

\begin{bmatrix}
-\Sigma_i f_{x_i} f_{t_i}\\ 
-\Sigma_i f_{y_i} f_{t_i}
\end{bmatrix}
$$ 



当有大的运动时会失败。所以我们使用金字塔，大的运动也可以变成小运动。