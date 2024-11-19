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

### Skewness

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

<center>
<img src="/only_sym.svg" width=600>
</center>

---

<center>
<img src="/sym_right.svg" width=600>
</center>

---

<center>
<img src="/sym_left.svg" width=600>
</center>

---

<center>
<img src="/bare.svg" width=600>
</center>

---

# Describe a DataFrame

```python
df.describe().round(2)
```

<br/>

|      Example |  count | mean | std |   min |   25% |   50% |  75% |  max |
| -----------: | -----: | ---: | --: | ----: | ----: | ----: | ---: | ---: |
|    Symmetric | 100000 |   -0 |   1 | -4.54 | -0.67 |     0 | 0.68 | 4.35 |
| Right-skewed | 100000 |   -0 |   1 | -2.46 | -0.75 | -0.18 | 0.59 | 5.77 |
|  Left-skewed | 100000 |   -0 |   1 | -5.72 | -0.59 |  0.18 | 0.76 | 2.38 |

---

# Describe a DataFrame

<div class="flex">
<div>

```python
df.skew().round(1)
```

<br/>

|      Example | Value |
| -----------: | ----: |
|    Symmetric |   0.0 |
| Right-skewed |   0.9 |
|  Left-skewed |  -0.9 |

</div>
</div>

---

# Skewness

$$
\frac{n}{(n-1)(n-2)} \cdot \frac{\sum_{i=1}^{n} (x_i - \bar{x})^3}{s^3}
$$

- The only important bit is the second fraction

- Pandas actually uses a slightly different df normalisation

---

# Skewness

|        A | (A - 4)³ |        B | (B - 4)³ |
| -------: | -------: | -------: | -------: |
|        2 |       -8 |        1 |      -27 |
|        4 |        0 |        3 |       -1 |
|        6 |        8 |        8 |       64 |
|      SCD |        0 |      SCD |       36 |
| Skewness |        0 | Skewness |     0.84 |
