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

### Strategies for summarising bivariate data

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Histograms

<div class="flex gap-30">
<div>

Raw data

|     | x   | y   |
| --: | :-- | :-- |
|   0 | c   | R   |
|   1 | a   | S   |
|   2 | b   | S   |
|   3 | a   | T   |
|   4 | b   | R   |
|   5 | b   | S   |

</div>
<div>

(Marginal) Frequencies

<div class="grid grid-cols-2 gap-15">
<div>
<br/>
<br/>

| x   | count |
| :-- | ----: |
| a   |     2 |
| b   |     3 |
| c   |     1 |

</div>
<div>
<br/>
<br/>

| y   | count |
| :-- | ----: |
| R   |     2 |
| S   |     3 |
| T   |     1 |

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
| :-- | --: | --: | --: |
| a   |   0 |   1 |   1 |
| b   |   1 |   2 |   0 |
| c   |   1 |   0 |   0 |

</div>
</div>

---

# Scatter plot, discrete

<center>
<img src="/fig_discrete.svg" width=500>
</center>

---

# Heatmap, small

<center>
<img src="/fig_heatmap_small.svg" width=500>
</center>

---

# Survey on SRH & life satisfaction

|     | poor | fair | good | very good | excellent |
| --: | ---: | ---: | ---: | --------: | --------: |
|   0 |  179 |  407 |  879 |      1013 |      1411 |
|   1 |  853 | 1351 | 1031 |      2028 |      1498 |
|   2 | 1319 | 1636 | 2291 |      2803 |      2017 |
|   3 | 1355 | 1610 | 2817 |      3358 |      2436 |
|   4 | 2370 | 2872 | 2761 |      3930 |      2751 |
|   5 | 2213 | 3172 | 3148 |      3513 |      3454 |
|   6 | 2955 | 3619 | 3786 |      4711 |      4331 |
|   7 | 3930 | 4482 | 4424 |      4683 |      4913 |
|   8 | 4201 | 4474 | 5074 |      5646 |      5499 |
|   9 | 3606 | 4115 | 4488 |      5075 |      4649 |
|  10 | 2979 | 3314 | 3682 |      4850 |      4297 |

---

# Heatmap, large

<center>
<img src="/fig_heatmap_large.svg" width=500>
</center>

---

# Heatmap including contingency table

<center>
<img src="/fig_heatmap_large_w_labels.svg" width=500>
</center>

---

# Continuous data

<div class="flex gap-30">
<div>

Raw data

|     |         x |          y |
| --: | --------: | ---------: |
|   0 | -0.231075 |   0.103152 |
|   1 |  0.999491 | -0.0753982 |
|   2 |   0.41889 |   0.115341 |
| ... |       ... |        ... |
|  97 |   1.36987 |   -1.22625 |
|  98 | -0.413597 |   0.507763 |
|  99 |  -1.45686 |  -0.151736 |

</div>
</div>

---

# Scatter plot, continuous, n=100

<center>
<img src="/fig_continuous_100.svg" width=500>
</center>

---

# Scatter plot, continuous, n=10,000

<center>
<img src="/fig_continuous_10000.svg" width=500>
</center>

---

# Scatter plot, discrete + continuous

<center>
<img src="/fig_dc.svg" width=500>
</center>

---

# Scatter plot, discrete + continuous

<center>
<img src="/fig_box.svg" width=500>
</center>

---

# Scatter plot, discrete + continuous

<center>
<img src="/fig_violin.svg" width=500>
</center>

---

# Which strategy to use?

- `X` discrete

  - `Y` discrete: Contingency table, heatmaps

  - `Y` continuous: Box plots, violin plots

- `X` continuous

  - `Y` continuous: Scatter plots, correlations

- Always look at marginal distributions, too!
