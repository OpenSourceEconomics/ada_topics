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

### Ordinary Least Squares (OLS): Intuition

<br/>

Hans-Martin von Gaudecker

---

# Linear conditional mean function

- Given that I know $X$, what is the mean value of $Y$?

- Linear relationship:

  $$Y_i = \beta_0 + \beta_1 \cdot X_i + U_i$$

- Divides each $Y_i$ into two parts:

  - Systematic part (conditional mean): $\beta_0 + \beta_1 \cdot X_i$

  - Residual / unobserved part: $U_i$

---

<center>
<img src="/fig_bare.svg" width=650>
</center>

---

<center>
<img src="/fig_point.svg" width=650>
</center>

---

<center>
<img src="/fig_line_y.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb_u.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb_u_point_2.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb_u_line_y_2.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb_u_line_xb_2.svg" width=650>
</center>

---

<center>
<img src="/fig_line_xb_u_line_xb_u_2.svg" width=650>
</center>

---

# OLS: Setup

Rewrite

$$Y_i = \beta_0 + \beta_1 \cdot X_i + U_i$$

as

$$U_i = Y_i - \beta_0 - \beta_1 \cdot X_i$$

and pick $\beta_0$, $\beta_1$ as to minimize a total distance of the $U_i$

---

# OLS: Setup

"pick $\beta_0$, $\beta_1$ as to minimize a total distance of the $U_i$":

- Total: Sum

- Criterion: Squared distances

$$
\begin{aligned}
(\hat{\beta}_0, \hat{\beta}_1) & = \argmin_{b_0,b_1} \: \sum_{i=1}^{n} U_i^2 \\
&= \argmin_{b_0,b_1} \: \sum_{i=1}^{n}\left(Y_{i}-b_0-b_1 X_{i}\right)^{2}
\end{aligned}
$$

---

# OLS: Why that setup?

- Among straight lines $a+b\cdot X$, OLS has the smallest in-sample sum of
  squared vertical residuals, by construction.

- Squaring gives larger residuals more weight in this criterion.

- Statistical optimality for a population requires additional assumptions about
  how the data were generated.

- Those assumptions and results are covered in later statistics and econometrics
  courses.

---

# OLS: Hugely important

- Easily extends to multiple $X$, non-linear relationships, etc.

- Basis for huge amount of other statistical methods

- Will only scratch the surface here

- Large part(s) of econometrics course(s) will be spent on this model
