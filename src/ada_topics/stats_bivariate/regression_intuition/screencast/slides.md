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

### Regression methods: Intuition

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Conditional mean function

- Given that I know $X$, what is the mean value of $Y$?

- We saw this for $X$ discrete and measured $Y$ (GDP per capita for different countries)

- Now look $\bar{Y} | X = x$

  - Discrete $X$: `df.groupby("x").mean()["y"]`

---

<center>
<img src="/fig_violin.svg" width=650>
</center>

---

# Conditional mean function

- Given that I know $X$, what is the mean value of $Y$?

- We saw this for $X$ discrete and measured $Y$ (GDP per capita for different countries)

- Now look $\bar{Y} | X = x$

  - Discrete $X$: `df.groupby("x").mean()["y"]`

  - Continuous $X$: Bin the data and calculate the mean for each bin

---

<center>
<img src="/fig_cont_overall_mean.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_means_2.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_means_3.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_means_4.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_means_5.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_means_6.svg" width=650>
</center>

---

# Continuous $X$, alternative

- Assume a functional form for the relationship between $X$ and $Y$

- Linear relationship: $Y_i = \beta_0 + \beta_1 \cdot X_i + U_i$

- $\bar{Y} | X = x$ becomes $\beta_0 + \beta_1 \cdot x$

---

<center>
<img src="/fig_cont_overall_mean.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-35.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-30.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-25.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-20.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-15.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_-10.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_0.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_5.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_10.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_15.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_20.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_25.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_30.svg" width=650>
</center>

---

<center>
<img src="/fig_cont_line_35.svg" width=650>
</center>
