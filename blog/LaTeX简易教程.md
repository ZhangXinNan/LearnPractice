	排版数学公式是TeX系统设计的初衷，它在LaTeX中占有特殊地位，也是LaTeX最为人所称道的功能之一。基于对MathType排版效果的不满意，以及对公式进行检索的需求，我们使用LaTeX输入数学公式。

## 1 数学模式概说
	数学公式有两种，行内（inline)公式和行间(displayed)公式。
	行内公式使用<latex inline>...</latex>表示；行间公式用<latex> ... </latex>表示。
	
## 2 常用字体
类别 			| 字体命令	| 简写 	| 输出效果
------			|--------			|------	|-----
默认字体 	| \mathit 		| \it		| $ABC$
罗马 			| \mathrm 	| \rm 	| $\rm{ABC}$
粗体			| \mathbf		| \bf		| $\bf{ABC}$

## 3 常用希腊字母列表
小写字母  | 字体命令
-------  | -----
$\alpha$ | \alpha
$\beta$ | \beta
$\gamma$ | \gamma
$\theta$ | \theta
$\varphi$ | \varphi
$\mu$ | \mu
$\lambda$ | \lambda
$\omega$ | \omega
$\pi$ | \pi
$\Sigma$ | \Sigma
$\Phi$ | \Phi
$\varepsilon$ | \varepsilon
$\phi$ | \phi
$\eta$ | \eta
$\xi$ | \xi
$\rho$ | \rho
$\sigma$ | \sigma
$\tau$ | \tau
$\delta$ | \delta
$\Delta$ | \Delta
$\Pi$ | \Pi
$\varPhi$ | \varPhi 

## 4 常见公式实现方案
### 4.1 集合
公式 | 代码
---- | -------
$x \in {\bf R},￼y \notin {\bf R}$ | x \in {\bf R},￼y \notin {\bf R}
$\left \{x\left |x\gt \dfrac {1}{2}\right.\right\}$ | \left \{x\left \|x\gt \dfrac {1}{2}\right.\right\}
$\complement_UA$ | \complement_UA
$\varnothing$ | \varnothing
$(−1,+\infty)$ | (−1,+\infty)
$(A\cup B)\cap C$ | (A\cup B)\cap C
$A \subset B \subseteq C$ | A \subset B \subseteq C
$A \not\subset B \subsetneq C$ | A \not\subset B \subsetneq C
$A \supset B \supseteq C$ | A \supset B \supseteq C

### 4.2 简易逻辑
公式 | 代码
---- | ----
$\neg p:x^2\lt 1$ | \neg p:x^2\lt 1
$\forall x$ | \forall x
$\exists y$ | \exists y
$p\lor q \Rightarrow p \land q$ | p\lor q \Rightarrow p \land q
$(p \to q)\land (p \gets q)$ | (p \to q)\land (p \gets q)
$\Leftrightarrow$ | \Leftrightarrow
$\Leftarrow$ | \Leftarrow

### 4.3 函数
公式 | 代码
---- | ----
${\rm e}^x$ | {\rm e}^x
$x^a$ | x^a
$\sqrt x, \sqrt [3] x$ | \sqrt x, \sqrt [3] x
$\lg x$ | \lg x
${\log_a}x$ | {\log_a}x
$\Delta=b^2-4ac$ | \Delta=b^2-4ac
$\begin{cases} x=2y+z\\y=2z+x\\z=2x+y\end{cases}$ | `\begin{cases} x=2y+z\\y=2z+x\\z=2x+y\end{cases}`
$f(x)=\begin{cases} x,x\gt 0\\0,x=0\\−x,x\lt 0\\\end{cases}$ | `f(x)=\begin{cases} x,x\gt 0\\0,x=0\\−x,x\lt 0\\\end{cases}`


### 4.4 三角函数
公式 | 代码
---- | ----
$\sin x, \cos x, \tan x$ | \sin x, \cos x, \tan x
$\sec x, \csc x, \cot x$ | \sec x, \csc x, \cot x

### 4.5 数列
公式 | 代码
---- | ----
$a_{n+2} = a_{n+1}-a_n$ | a_{n+2} = a_{n+1}-a_n
$a_n=\begin{cases} 2, &n=1\\n^2, &n\geq 2\end{cases}$ | `a_n=\begin{cases} 2, &n=1\\n^2, &n\geq 2\end{cases}`


### 4.6 向量
公式 | 代码
---- | ----
$\overrightarrow{AB}$ | \overrightarrow{AB}
$\vec a$ | \vec a
$\vec a \parallel \vec b$ | \vec a \parallel \vec b
$\vec a\perp \vec b$ | \vec a\perp \vec b
$\vec a\cdot \vec b$ | \vec a\cdot \vec b
$\langle \vec a, \vec c \rangle$ | \langle \vec a, \vec c \rangle


### 4.7 微积分
公式 | 代码
---- | ----
$\lim\limits_{\Delta x \to 0}{\Delta^2 x}$ | \lim\limits_{\Delta x \to 0}{\Delta^2 x}
$\int_a^b{x{\rm d}x}=\left.\frac12 x^2\right |_a^b$ | \int_a^b{x{\rm d}x}=\left.\frac12 x^2\right |_a^b

### 4.8 概率
公式 | 代码
---- | ----
${\rm A}_4^2=4!/2!$ | {\rm A}_4^2=4!/2!
$X \sim N(\mu,\sigma^2)$ | X \sim N(\mu,\sigma^2)

### 4.9 统计
公式 | 代码
---- | ----
$\bar x$ | \bar x
$\hat y=\hat ax + \hat b$ | \hat y=\hat a x + \hat b
$\sum\limits_{i=1}^{n}{x_i}$ | \sum\limits_{i=1}^{n}{x_i}

### 4.10 几何
公式 | 代码
---- | ----
$45\circ$ | 45\circ
$\stackrel \frown{AB}$ | \stackrel \frown{AB}
$\odot O$ | \odot O
$a\parallel b$ | a\parallel b
$a\perp b$ | a\perp b
$\triangle ABC \backsim \triangle DEF$ | \triangle ABC \backsim \triangle DEF
$\triangle ABC \cong \triangle DEF$ | \triangle ABC \cong \triangle DEF


### 4.11 矩阵
公式 | 代码
---- | ----
$\begin{matrix}a&b \\ c&d \end{matrix}$ | `\begin{matrix}a&b \\ c&d \end{matrix}`
$\begin{pmatrix}a&b \\ c&d \end{pmatrix}$ | `\begin{pmatrix}a&b \\ c&d \end{pmatrix}`
$\begin{Bmatrix}a&b \\ c&d \end{Bmatrix}$ | `\begin{Bmatrix}a&b \\ c&d \end{Bmatrix}`
$\begin{vmatrix}a&b \\ c&d \end{vmatrix}$ | `\begin{vmatrix}a&b \\ c&d \end{vmatrix}`

### 4.12 其它特殊符号
公式 | 代码
---- | ----
$\bigoplus$ | \bigoplus
$\bigotimes$ | \bigotimes
$\bigodot$ | \bigodot
$\equiv$ | \equiv
$\ast或*$ | \ast或*
$\pm$ | \pm
$\mp$ | \mp
$\times$ | \times
$\div￼ $ | \div￼ 
$\geqslant$ | \geqslant
$\leqslant$ | \leqslant
$\cdots￼ $ | \cdots￼ 
$\%$ | \%
$\to或\rightarrow$ | \to或\rightarrow
$\gets或\leftarrow$ | \gets或\leftarrow
$\Rightarrow$ | \Rightarrow
$\Leftarrow$ | \Leftarrow
$\leftrightarrow$ | \leftrightarrow
$\Leftrightarrow$ | \Leftrightarrow
$\nearrow$ | \nearrow
$\searrow$ | \searrow
$\swarrow$ | \swarrow
$\nwarrow$ | \nwarrow

### 4.13 其它排版
公式 | 代码
----|----
$\begin{split}(x−1)(x−3)&=x^2−4x+3 \\ &=x^2−4x+4−1 \\ &=(x−2)^2−1\end{split}$ | `\begin{split}(x−1)(x−3)&=x^2−4x+3 \\ &=x^2−4x+4−1 \\ &=(x−2)^2−1\end{split}`