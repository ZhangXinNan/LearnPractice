
# 1. Matrix Multiplication (4 ways)

## 1.1 定义法（标准算法）
$$
C_{34}=(row3 of A) (column4 of B)
\\
=a_{31} b_{14} + a_{32} b_{24} + \dots
= \sum_i^n a_{3i} b_{i4}
$$

$$
A_{m \times n} B_{n \times p} = C_{m \times p}
$$

## 1.2 用列
C的 $i$ 列等于矩阵A乘以B的$i$列。

columns of C are combinations of columns of A

$column_i of C = A \{column_i of B\}$


## 1.3 用行
C的 $i$ 行等于矩阵A有 $i$ 行乘以矩阵B

rows of C are combinations of rows of B

$row_i of C = \{row_i of A\} B$


## 1.4 列乘以行
$$
AB=sum of (cols of A) (rows of B)
$$

## 1.5 矩阵分块

# 2. Inverse of A/AB/$A^T$
逆矩阵是否存在非常重要。

$$
A^{-1}A=I=AA^{-1}
$$
如果矩阵可逆，称为invertible或者non-singular。

## 2.1 Singular case (No inverse)
I can find a Vector x with $Ax=0$

# 3. Gauss-Jordan / Find $A^{-1}$

solve 2 equations at once

求矩阵的逆
$$
A =
\begin{bmatrix}
1 & 3 \\
2 & 7 \\
\end{bmatrix}
$$

$$
A =
\begin{bmatrix}
1 & 3 & 1 & 0 \\
2 & 7 & 0 & 1 \\
\end{bmatrix}
->
\begin{bmatrix}
1 & 3 & 1 & 0 \\
0 & 1 & -2 & 1 \\
\end{bmatrix}
->
\begin{bmatrix}
1 & 0 & 7 & -3 \\
0 & 1 & -2 & 1 \\
\end{bmatrix}
$$


因此
$$
A^{-1}=
\begin{bmatrix}
7 & -3 \\
-2 & 1 \\
\end{bmatrix}
$$


$$
A^{-1}
\begin{bmatrix}
A | I
\end{bmatrix}
=
\begin{bmatrix}
I | A^{-1}
\end{bmatrix}
$$

