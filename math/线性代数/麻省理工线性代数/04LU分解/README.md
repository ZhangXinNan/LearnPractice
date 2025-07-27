
# Inverse of $AB$, $A^T$

$$
AA^{-1}=I=A^{-1}A
$$

## $AB$
$$
ABB^{-1}A^{-1}=I=B^{-1}A^{-1}AB
$$

$$
(AB)^{-1}=B^{-1}A^{-1}
$$

## $A^T$

$$
(A^{-1})^T A^T = I
$$

$$
(A^T)^{-1}=(A^{-1})^T
$$

# Product of elemination matrices

$$
E_{21}A=U
\\
\begin{bmatrix}
1 & 0 \\
-4 & 1 \\
\end{bmatrix}
\begin{bmatrix}
2 & 1 \\
8 & 7 \\
\end{bmatrix}
=
\begin{bmatrix}
2 & 1 \\
0 & 3 \\
\end{bmatrix}
$$


$$
A=LU
\\
\begin{bmatrix}
2 & 1 \\
8 & 7 \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
4 & 1 \\
\end{bmatrix}
\begin{bmatrix}
2 & 1 \\
0 & 3 \\
\end{bmatrix}
\\
=
\begin{bmatrix}
1 & 0 \\
4 & 1 \\
\end{bmatrix}
\begin{bmatrix}
2 & 0 \\
0 & 3 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0.5 \\
0 & 1 \\
\end{bmatrix}
$$

- L : Lower triangular
- U : Upper triangular

# $A = LU$ (no row exchange)

$$
E_{32}E_{31}E_{21}A=U(no row exchanges)
\\
A=E_{21}^{-1}E_{31}^{-1}E_{32}^{-1}U
$$


$$E_{32}E_{21}=U$$

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -5 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
-2 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0\\
-2 & 1 & 0 \\
10 & -5 & 1\\
\end{bmatrix}
=E
$$




$$
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 5 & 1 \\
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
0 & 0 & 1\\
\end{bmatrix}
=L
$$


$A=LU$
If no row exchanges, multipliers go directly into $L$.

How many operations on $n \times n$ matrix A ?

$n = 100$

运算次数为：$y=\frac{n(n+1)(n-1)}{3}$

- Transposes 转置
- Permutations 置换

$$
P^{-1}=P^{T}
$$