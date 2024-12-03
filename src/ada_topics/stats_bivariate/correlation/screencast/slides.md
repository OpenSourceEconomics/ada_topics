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

### Correlations

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# (Co)variance & Correlation

Variance:

$$
\begin{aligned}
s^2_x & = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \overline{x})^2
\end{aligned}
$$

Covariance:

$$
\begin{aligned}
s_{x, y} & = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \overline{x}) \cdot (y_i - \overline{y})
\end{aligned}
$$

Correlation (Pearson's $\rho$):

$$
\begin{aligned}
\rho_{x, y} & = \frac{s_{x, y}}{s_{x} \cdot s_{y}}
\end{aligned}
$$

---

<center>
<img src="/fig_30.svg" width=650>
</center>

---

<center>
<img src="/fig_dot_30.svg" width=650>
</center>

---

<center>
<img src="/fig_demeaned.svg" width=650>
</center>

---

<center>
<img src="/fig_standardised.svg" width=650>
</center>

---

<center>
<img src="/fig_30.svg" width=650>
</center>

---

<center>
<img src="/fig_90.svg" width=650>
</center>

---

<center>
<img src="/fig_0.svg" width=650>
</center>

---

<center>
<img src="/fig_-70.svg" width=650>
</center>

---

<center>
<img src="/fig_-99.svg" width=650>
</center>

---

# Correlation: Properties

1. $-1 \leq \rho_{x, y} \leq 1$

1. Both $x$ and $y$ need to vary

1. $-1$ or $1$ means perfect linear relationship, i.e., all points on a straight line
   <br/>
   *(2. guarantees that slope is nonzero and finite)*
