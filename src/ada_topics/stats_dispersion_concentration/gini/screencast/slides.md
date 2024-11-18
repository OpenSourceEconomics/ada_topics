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

### The Gini coefficient

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Example

<div class="grid grid-cols-3 gap-10">
<div>

### Ordered data

|   A |   B |   C |
|----:|----:|----:|
|   1 |   2 |   4 |
|   5 |   2 |   4 |
|   6 |   8 |   4 |

<br/>
<br/>
<br/>

</div>
<div>

### Cum. sum

|   A |   B |   C |
|----:|----:|----:|
|   1 |   2 |   4 |
|   6 |   4 |   8 |
|  12 |  12 |  12 |

<br/>
<br/>
<br/>

</div>
<div>

### Cum. dist.

|    A |    B |    C |
|-----:|-----:|-----:|
| 0.08 | 0.17 | 0.33 |
| 0.5  | 0.33 | 0.67 |
| 1    | 1    | 1    |

<br/>
<br/>
<br/>

</div>
</div>


---

<center>
<img src="/data_points_all-lines_all.svg" width=650>
</center>

<br/>
<br/>

---

<center>
<img src="/data_points_only_a-line_all_segments.svg" width=650>
</center>

<br/>
<br/>

---

<center>
<img src="/data_points_all-shade_a.svg" width=650>
</center>

<br/>
<br/>

---


# Calculation: Formula

$$
\begin{aligned}
p_i & = \frac{x_i}{\sum_{i=1}^{k} x_i}\\[2em]
G & = \frac{2 \cdot \sum_{i=1}^{n} i \cdot p_i - (n + 1)}{n}
\end{aligned}
$$



---

# Calculation: Example

<div class="grid grid-cols-3 gap-10">
<div>

### Ordered data

|   A |   B |   C |
|----:|----:|----:|
|   1 |   2 |   4 |
|   5 |   2 |   4 |
|   6 |   8 |   4 |

<br/>
<br/>
<br/>

</div>
<div>

### Normal. data

|    A |    B |    C |
|-----:|-----:|-----:|
| 0.08 | 0.17 | 0.33 |
| 0.42 | 0.17 | 0.33 |
| 0.5  | 0.67 | 0.33 |

<br/>
<br/>
<br/>

</div>
<div>

### Gini

|    A |    B |   C |
|-----:|-----:|----:|
| 0.28 | 0.33 |   0 |

<br/>
<br/>
<br/>

</div>
</div>

---

<center>
<img src="/data_points_all-lines_all.svg" width=650>
</center>

<br/>
<br/>
