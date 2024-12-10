# Ordinary Least Squares (OLS): Derivation

## Learning objectives

After working through this topic, you should be able to:

- derive the bivariate OLS estimator
- explain why the OLS estimator implies $\bar{U} = 0$ and $s_{X, U} = 0$
- interpret what the parameter values of the OLS estimator mean

The derivation is [reproduced below the videos](derivation-of-the-ols-estimator) for
your convenience.

## Materials

Video with English subtitles:

<iframe
  src="https://electure.uni-bonn.de/paella7/ui/watch.html?id=f4644bef-2315-4ea7-bc8b-e76fcb0b0a18"
  width="640"
  height="360"
  frameborder="0"
  allowfullscreen
></iframe>

Download the [slides](stats_bivariate-ols_derivation.pdf).

Video with German subtitles:

*(turn subtitles on in the bottom right corner of the video)*

<iframe
  src="https://electure.uni-bonn.de/paella7/ui/watch.html?id=d4762f13-fd80-416c-b4b3-d399eb09bb7c"
  width="640"
  height="360"
  frameborder="0"
  allowfullscreen
></iframe>

(derivation-of-the-ols-estimator)=

## Derivation of the OLS estimator

### Setup

Rewrite

$$Y_i = \beta_0 + \beta_1 X_i + U_i$$

as

$$U_i = Y_i - \beta_0 - \beta_1 X_i$$

and pick $\beta_0$, $\beta_1$ as to minimize the sum of squares of the $U_i$

______________________________________________________________________

### Minimisation problem

$$
\begin{align}
(\hat{\beta}_0, \hat{\beta}_1) & = \text{arg}\min_{b_0,b_1} \: \sum_{i=1}^{n} U_i^2 \\
&= \text{arg}\min_{b_0,b_1} \: \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}
\end{align}
$$

______________________________________________________________________

### First order conditions

Differentiate the objective function with respect to $b_0$ and $b_1$:

$$
\begin{align}
\frac{\partial \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}}{\partial b_0} & = \sum_{i=1}^{n} 2 \cdot \left(Y_{i}-b_0-b_1 X_{i}\right) \cdot (-1)\\
\frac{\partial \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}}{\partial b_1} & = \sum_{i=1}^{n} 2 \cdot \left(Y_{i}-b_0-b_1 X_{i}\right) \cdot (-X_i)
\end{align}
$$

The OLS estimator $(\hat{\beta}_0, \hat{\beta}_1)$ is the pair of values solving the
system of equation that results when setting the derivatives to zero:

$$
\begin{align}
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) & \overset{!}{=} 0 \\
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_i &\overset{!}{=} 0
\end{align}
$$

### Steps for $\hat{\beta}_0$

Start from first order condition for $\hat{\beta}_0$

$$
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) = 0
$$

divide by $-2$

$$
\sum_{i=1}^{n} Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i} = 0
$$

use $\sum_i (a_i + b_i) = \sum_i a_i + \sum_i b_i$

$$\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_i &\overset{!}{=} 0

\sum_{i=1}^{n} Y_{i} - \sum_{i=1}^{n}\hat{\beta}_0 - \sum_{i=1}^{n} \hat{\beta}_1 X_{i} = 0
$$

use $a (b + c) = ab + ac$

$$
\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 \sum_{i=1}^{n} 1 - \hat{\beta}_1 \sum_{i=1}^{n} X_{i} = 0
$$

definition of product

$$
\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 n - \hat{\beta}_1 \sum_{i=1}^{n} X_{i} = 0
$$

divide by $n$

$$
\frac{1}{n}\sum_{i=1}^{n} Y_{i} - \hat{\beta}_0 - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^{n} X_{i} = 0
$$

add $\hat{\beta}_0$ on both sides

$$
\hat{\beta}_0 = \frac{1}{n}\sum_{i=1}^{n} Y_{i} - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^{n} X_{i}
$$

definition of $\bar{Y}, \bar{X}$

$$
\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}
$$

This gives us the formula for $\hat{\beta}_0$. This is only useful in conjuction with
the formula for $\hat{\beta}_1$, though.

### Steps for $\hat{\beta}_1$

Start from first order condition for $\hat{\beta}_1$

$$
\sum_{i=1}^{n} -2 \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_i = 0
$$

divide by $-2$

$$
\sum_{i=1}^{n} \cdot \left(Y_{i}-\hat{\beta}_0-\hat{\beta}_1 X_{i}\right) X_i = 0
$$

multiply out

$$
\sum_{i=1}^{n} X_{i} Y_{i} - \hat{\beta}_0 X_{i} - \hat{\beta}_1 X_{i}^{2} = 0
$$

use $\sum_i (a_i + b_i) = \sum_i a_i + \sum_i b_i$

$$
\sum_{i=1}^{n} X_{i} Y_{i} - \hat{\beta}_0 \sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \sum_{i=1}^{n} X_{i}^{2} = 0
$$

plug in the formula derived above $\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}$

$$
\sum_{i=1}^{n} X_{i} Y_{i} - \left(\bar{Y} - \hat{\beta}_1 \bar{X}\right) \sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \sum_{i=1}^{n} X_{i}^{2} = 0
$$

multiply out and use use $ab + ac = a (b + c)$

$$
\sum_{i=1}^{n} X_{i} Y_{i} - \bar{Y}\sum_{i=1}^{n} X_{i} - \hat{\beta}_1 \left( \sum_{i=1}^{n} X_{i}^{2} - \bar{X}\sum_{i=1}^{n} X_{i}\right) = 0
$$

Use [property derived below](sums-of-products-and-products-of-sums) (twice)

$$
\sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)\cdot\left(Y_{i} - \bar{Y}\right) - \hat{\beta}_1 \cdot \sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)^2 = 0
$$

Divide by $n - 1$, add term starting with $\hat{\beta}_1$ to both sides

$$
\hat{\beta}_1 \cdot \frac{1}{n-1}\sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)^2 = \frac{1}{n-1}\sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)\cdot\left(Y_{i} - \bar{Y}\right)
$$

Divide by $n - 1$, add term starting with $\hat{\beta}_1$ to both sides

$$
\hat{\beta}_1 \cdot s_{X}^2 = s_{XY}
$$

Divide by $s_{X}^2$

$$
\hat{\beta}_1 = \frac{s_{XY}}{s_{X}^2}
$$

(sums-of-products-and-products-of-sums)=

### Sums of products and products of sums / means

$$
\sum_{i=1}^{n} X_{i} Y_{i} - \bar{Y}\sum_{i=1}^{n} X_{i}
$$

use $a (b + c) = ab + ac$

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y}
$$

add and subtract $\sum_{i=1}^{n} \bar{X} Y_{i}$

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \sum_{i=1}^{n} \bar{X} Y_{i}
$$

use $1 = n / n$

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \bar{X} \cdot n \cdot \frac{1}{n}\sum_{i=1}^{n} Y_{i}
$$

definition of $\bar{Y}$

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + n \bar{X} \bar{Y}
$$

definition of product

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - \sum_{i=1}^{n} X_{i}\bar{Y} - \sum_{i=1}^{n} \bar{X} Y_{i} + \sum_{i=1}^{n} \bar{X} \bar{Y}
$$

use $\sum_i a_i + \sum_i b_i = \sum_i a_i + b_i$

$$
= \sum_{i=1}^{n} X_{i} Y_{i} - X_{i}\bar{Y} - \bar{X} Y_{i} + \bar{X} \bar{Y}
$$

binomial formula

$$
= \sum_{i=1}^{n} \left(X_{i} - \bar{X}\right)\cdot\left(Y_{i} - \bar{Y}\right)
$$
