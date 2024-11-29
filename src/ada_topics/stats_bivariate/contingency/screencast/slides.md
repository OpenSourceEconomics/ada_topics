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

<div class="flex gap-12">
<div>

Raw data

|    | x   |   y |
|---:|:----|----:|
|  0 | c   |   7 |
|  1 | a   |   3 |
|  2 | b   |   3 |
|  3 | a   |   4 |
|  4 | b   |   7 |
|  5 | b   |   3 |

</div>
<div>

Frequency distributions

| x   |   count |
|:----|--------:|
| a   |       2 |
| b   |       3 |
| c   |       1 |

<br>
<br>

|   y |   count |
|----:|--------:|
|   3 |       3 |
|   4 |       1 |
|   7 |       2 |

</div>
</div>

---

# Usefulness of strategies

- Small number of outcomes on each axis: Contingency tables

- Large number of outcomes, small number of observations: Scatter plots

- Large number of outcomes, large number of observations: `.describe` + correlations
