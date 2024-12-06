---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: Applied Data Analytics
drawings:
  persist: false
transition: fade
defaults:
  layout: center
---

### Applied Data Analytics

<br/>

# Statistics — Measures for bivariate data

### Ordinary Least Squares (OLS): Derivation

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

<center>
<img src="/fig_line_xb_u_line_xb_u_2.svg" width=650>
</center>

---

# OLS: Setup

Rewrite

$$Y_i = \beta_0 + \beta_1 X_i + U_i$$

as

$$U_i = Y_i - \beta_0 - \beta_1 X_i$$

and pick $\beta_0$, $\beta_1$ as to minimize the sum of squares of the $U_i$

---

# Minimisation problem

$$
\begin{aligned}
(\hat{\beta}_0, \hat{\beta}_1) & = \argmin_{b_0,b_1} \: \sum_{i=1}^{n} U_i^2 \\
&= \argmin_{b_0,b_1} \: \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}
\end{aligned}
$$


---

# Steps for $\hat{\beta}_0$

Differentiate objective function with respect to $b_0$:

$$
\frac{\partial \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}}{\partial b_0} = \sum_{i=1}^{n} 2 \cdot \left(Y_{i}-b_0-b_1 X_{i}\right) \cdot (-1)
$$

$\beta_0$ and $\beta_1$ are the values solving this:

$$
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) \overset{!}{=} 0
$$

Divide by $-2$


---

# Steps for $\hat{\beta}_0$

$$
\begin{aligned}
\sum_{i=1}^{n} Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i} & = 0 \\
\sum_{i=1}^{n} Y_{i} - \sum_{i=1}^{n}\hat{\beta}_0 - \sum_{i=1}^{n} \hat{\beta}_1 X_{i} & = 0 \\
\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 \sum_{i=1}^{n} 1 - \hat{\beta}_1 \sum_{i=1}^{n} X_{i} & = 0 \\
\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 n - \hat{\beta}_1 \sum_{i=1}^{n} X_{i} & = 0 \\
\end{aligned}
$$

---

# Steps for $\hat{\beta}_0$

Divide by $n$ and rearrange:
$$
\begin{aligned}
\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 n - \hat{\beta}_1 \sum_{i=1}^{n} X_{i} & = 0 \\
\frac{1}{n}\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^{n} X_{i} & = 0 \\
\hat{\beta}_0 & = \frac{1}{n}\sum_{i=1}^{n} Y_{i} - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^{n} X_{i}\\[4ex]
\hat{\beta}_0 & = \bar{Y} - \hat{\beta}_1 \bar{X}\\
\end{aligned}
$$

---


# Steps for $\hat{\beta}_1$

Differentiate objective function with respect to $b_1$:

$$
\frac{\partial \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}}{\partial b_1} = \sum_{i=1}^{n} 2 \cdot \left(Y_{i}-b_0-b_1 X_{i}\right) \cdot (-X_i)
$$

$\beta_0$ and $\beta_1$ are the values solving this:

$$
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_i \overset{!}{=} 0
$$

Divide by $-2$, multiply out

---

# Steps for $\hat{\beta}_1$

$$
\begin{aligned}
\sum_{i=1}^{n} X_{i} Y_{i} - \hat{\beta}_0 X_{i} - \hat{\beta}_1 X_{i}^{2} & = 0 \\
\sum_{i=1}^{n} X_{i} Y_{i} - \hat{\beta}_0 \sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \sum_{i=1}^{n} X_{i}^{2} & = 0 \\
\sum_{i=1}^{n} X_{i} Y_{i} - \left(\bar{Y} - \hat{\beta}_1 \bar{X}\right) \sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \sum_{i=1}^{n} X_{i}^{2} & = 0 \\
\sum_{i=1}^{n} X_{i} Y_{i} - \bar{Y}\sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \left( \sum_{i=1}^{n} X_{i}^{2} - \bar{X}\sum_{i=1}^{n} X_{i}\right) & = 0 \\
\end{aligned}
$$

---

# Focus on first two terms

$$
\begin{aligned}
& \sum_{i=1}^{n} X_{i} Y_{i} - \bar{Y}\sum_{i=1}^{n} X_{i}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \sum_{i=1}^{n} \bar{X} Y_{i}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \bar{X} \cdot n \cdot \frac{1}{n}\sum_{i=1}^{n} Y_{i}\\
\end{aligned}
$$


---

$$
\begin{aligned}
& \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \bar{X} \cdot n \cdot \frac{1}{n}\sum_{i=1}^{n} Y_{i}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + n \bar{X} \bar{Y}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \sum_{i=1}^{n} \bar{X} \bar{Y}\\
= & \sum_{i=1}^{n} X_{i} Y_{i} - X_{i}\bar{Y} - \bar{X} Y_{i} + \bar{X} \bar{Y}\\
= & \sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)\cdot\left(Y_{i} - \bar{Y}\right)
\end{aligned}
$$

---

# Back to the equation for $\hat{\beta}_1$

$$
\begin{aligned}
\sum_{i=1}^{n} X_{i} Y_{i} - \bar{Y}\sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \left( \sum_{i=1}^{n} X_{i}^{2} - \bar{X}\sum_{i=1}^{n} X_{i}\right) & = 0 \\
\frac{1}{n-1}\sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)\cdot\left(Y_{i} - \bar{Y}\right) - \hat{\beta}_1 \cdot \frac{1}{n-1}\sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)^2 & = 0 \\
s_{XY} - \hat{\beta}_1 \cdot s_{X}^2 & = 0
\end{aligned}
$$

$$
\hat{\beta}_1 = \frac{s_{XY}}{s_{X}^2}
$$

---

# Implications: $\bar{U} = 0$, $s_{X, U} = 0$

Remember the FOC's:

$$
\begin{aligned}
\frac{1}{n}\sum_{i=1}^{n} Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i} & = \frac{1}{n}\sum_{i=1}^{n} U_i = \frac{1}{n}\bar{U}  = 0 \\[4ex]
\frac{1}{n-1}\sum_{i=1}^{n} \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_{i} & = \frac{1}{n-1}\sum_{i=1}^{n} U_i X_i = s_{X, U} = 0
\end{aligned}
$$

Second equation follows from same argument as above for $\sum^n_{i=1} X_i Y_i - \bar{X}\bar{Y}$ and observing that $\bar{U} = 0$.


---

# OLS estimator

$$
\begin{aligned}
\hat{\beta}_0 & = \bar{Y} - \hat{\beta}_1 \bar{X}\\[2ex]
\hat{\beta}_1 & = \frac{s_{XY}}{s_{X}^2}
\end{aligned}
$$

These are the intercept and slope of the regression line:

- $\hat{\beta}_0$ is the mean value of $Y$ when $X$ is zero

- $\hat{\beta}_1$ is the mean change in $Y$ when $X$ changes by one unit

---

<center>
<img src="/fig_bare.svg" width=650>
</center>
