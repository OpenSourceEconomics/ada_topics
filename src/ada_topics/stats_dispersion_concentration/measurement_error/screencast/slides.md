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

# Statistics — Dispersion & concentration

### Measurement error and summary statistics

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Goals

- Remember measurement issues are pervasive

- Show when mean-zero measurement errors preserve the mean, while other
  summaries, including medians and variances, can change

- Show that systematic measurement errors impact all statistics

- Realise that we need to understand where the data comes from

---

# Model

- True value: $x^*_i$

- Actual measurement: $x_i \equiv x_i^* + \varepsilon_i$

- Assume the realised errors sum to zero: $\bar{\varepsilon} \equiv \frac{1}{n}\sum^n_{i=1}\varepsilon_i = 0$

- $\frac{1}{n-1}\sum^n_{i=1}(\varepsilon_i - \bar{\varepsilon})^2 > 0$

---

# Mean

$$
\begin{aligned}
  \bar{x} &= \frac{1}{n}\sum^n_{i=1}x_i\\
          &= \frac{1}{n}\sum^n_{i=1}(x_i^* + \varepsilon_i)\\
          &= \frac{1}{n}\sum^n_{i=1}x_i^* + \frac{1}{n}\sum^n_{i=1} \varepsilon_i\\
          &= \frac{1}{n}\sum^n_{i=1}x_i^*\\
          &= \bar{x^*}
\end{aligned}
$$

---

# Variance

$$
\begin{aligned}
  s^2_x &= \frac{1}{n-1}\sum^n_{i=1}(x_i - \bar{x})^2 \\
        &= \frac{1}{n-1}\sum^n_{i=1}(x_i^* + \varepsilon_i  - \bar{x^*})^2\\
        &= s_{x^*}^2 + s_{\varepsilon}^2 + \frac{2}{n-1}\sum^n_{i=1}(x_i^*-\bar{x^*})\varepsilon_i\\
\end{aligned}
$$

With a zero cross-product term, the variance rises by $s_{\varepsilon}^2$.
Independence makes that term zero in expectation, not in every realised sample.
The cross-product term can be negative and make the realised variance fall.




---

# Systematic Measurement Error

- Example: Censoring

- Real-world: German Employment Agency (BA) data

  - Reports of earnings are precise until a threshold
  - Only know that they are at least this threshold value beyond that

---

# Model

$$
x_i = \begin{cases}
x_i^* & \text{if} \;\; x_i^* \leq 90,600\,€ \\
90,600\,€ & \text{otherwise}
\end{cases}
$$

If I was to use this data directly:

- $\bar{x} \leq \bar{x^*}$, strictly if at least one value is clipped

- $s_x \leq s_{x^*}$

- Order-statistic quantiles at or below the cutoff are unchanged. For pandas'
  interpolated sample quantiles, a sufficient condition for no change is that all
  contributing order statistics are at or below the cutoff; the interpolated
  quantile alone being below it is not enough.
