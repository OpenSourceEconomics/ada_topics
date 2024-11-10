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

### Dispersion based on absolute deviations

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

<center>
<img src="/only_small.svg" width=600>
</center>

---

<center>
<img src="/bare.svg" width=600>
</center>

---

<center>
<img src="/min_max_small_only.svg" width=600>
</center>

---

<center>
<img src="/min_max.svg" width=600>
</center>

---

<center>
<img src="/deciles.svg" width=600>
</center>

---

<center>
<img src="/quartiles.svg" width=600>
</center>

---

# Ranges

- **Range**: difference between the maximum and minimum values

- **Interdecile range**: difference between the 90th and 10th percentiles

- **Interquartile range**: difference between the 75th and 25th percentiles

- For ratio scales with strictly positive values, ratios between quantiles can be useful
  statistics, too


---

# Describe a DataFrame

```python
df.describe().round(2)
```

<br/>

| Dispersion   |   count |   mean |   std |   min |   25% |   50% |   75% |   max |
|-------------:|--------:|-------:|------:|------:|------:|------:|------:|------:|
| Small        |  100000 |   0    |   1   | -4.27 | -0.67 |    -0 |  0.67 |  4.43 |
| Large        |  100000 |  -0.01 |   1.5 | -7.07 | -1.01 |    -0 |  1    |  6.39 |

---

# Mean absolute deviation

$$
s_\text{MAD} = \frac{1}{n} \sum_{i=1}^{n} |x_i - x_\text{MED}|
$$

---

# Mean absolute deviation

|   A | \|A - 4\| |   B | \|B - 3\| |
| --: | --------: | --: | --------: |
|   2 |         2 |   1 |         2 |
|   4 |         0 |   3 |         0 |
|   6 |         2 |   8 |         5 |
| MAD |      1.33 | MAD |      2.33 |
