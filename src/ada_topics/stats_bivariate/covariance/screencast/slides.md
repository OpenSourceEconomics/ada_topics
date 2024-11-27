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

### Covariances

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# (Co)variance

Variance:

$$
\begin{aligned}
s^2_x & = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \overline{x})^2 \\
& = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \overline{x}) \cdot (x_i - \overline{x})
\end{aligned}
$$

Covariance:

$$
\begin{aligned}
s^2_{x, y} & = \frac{1}{n - 2} \sum_{i=1}^{n} (x_i - \overline{x}) \cdot (y_i - \overline{y})
\end{aligned}
$$
