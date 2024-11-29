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

### Contingency tables

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Histograms

<div class="flex gap-30">
<div>

Raw data

|    | x   | y   |
|---:|:----|:----|
|  0 | c   | R   |
|  1 | a   | S   |
|  2 | b   | S   |
|  3 | a   | T   |
|  4 | b   | R   |
|  5 | b   | S   |

</div>
<div>

(Marginal) Frequencies

<div class="grid grid-cols-2 gap-15">
<div>
<br/>
<br/>

| x   |   count |
|:----|--------:|
| a   |       2 |
| b   |       3 |
| c   |       1 |

</div>
<div>
<br/>
<br/>

| y   |   count |
|:----|--------:|
| R   |       2 |
| S   |       3 |
| T   |       1 |

</div>
</div>
</div>
</div>

---

# Joint frequencies

<div class="flex">
<div>

```python
pd.crosstab(df["x"], df["y"])
```

<br/>
<br/>

| x   |   R |   S |   T |
|:----|----:|----:|----:|
| a   |   0 |   1 |   1 |
| b   |   1 |   2 |   0 |
| c   |   1 |   0 |   0 |

</div>
</div>

---

# Scatterplot, discrete

<center>
<img src="/fig_discrete.svg" width=500>
</center>

---

# Scatterplot, continuous, n=100

<center>
<img src="/fig_continuous_100.svg" width=500>
</center>

---

# Scatterplot, continuous, n=10,000

<center>
<img src="/fig_continuous_10000.svg" width=500>
</center>

---

# Usefulness of strategies

- Small number of outcomes on each axis: Contingency tables

- Large number of outcomes, small number of observations: Scatter plots

- Large number of outcomes, large number of observations: `.describe` + correlations
