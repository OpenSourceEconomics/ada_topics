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

### Lorenz curves

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
<img src="/data_points_only_a-line_none.svg" width=650>
</center>

<br/>
<br/>

---

<center>
<img src="/data_points_only_a-line_first_segment.svg" width=650>
</center>

<br/>
<br/>

---

<center>
<img src="/data_points_only_a-line_first_two_segments.svg" width=650>
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
<img src="/data_points_a_b-lines_a_b.svg" width=650>
</center>

<br/>
<br/>

---

<center>
<img src="/data_points_all-lines_all.svg" width=650>
</center>

<br/>
<br/>

---

# Lorenz curve: Definition

$$
\begin{aligned}
u_k & = \frac{k}{n}\\[2em]
v_k & = \frac{\sum_{i=1}^{k} x_i}{\sum_{i=1}^{n} x_i}
\end{aligned}
$$

<br/>

Lorenz curve connects the origin and all points $(u_k, v_k), k \in (1, \ldots, n)$
