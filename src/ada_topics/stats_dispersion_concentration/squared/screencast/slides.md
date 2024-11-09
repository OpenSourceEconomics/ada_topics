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

### Variance and standard deviation

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

# Variance and standard deviation

- The variance of a sample is the average squared deviation from the sample mean

  $$
  s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
  $$

  where $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$ is the sample mean

<br/>

- The standard deviation isame
  $$
  s = \sqrt{s^2}
  $$

<br/>
<br/>

---

# Degrees of freedom

<div class="grid grid-cols-2 gap-30">
<div>

|      |                                     A |                                     B |
| :--- | ------------------------------------: | ------------------------------------: |
|      |                                     2 |                                     1 |
|      |                                     4 |                                     3 |
|      |                                     6 |                                     8 |
| Mean | <span style="color:#CD7F32;">?</span> | <span style="color:#CD7F32;">?</span> |

<br/>
<br/>
<br/>

</div>
<div>

|      |                                     A |                                     B |
| :--- | ------------------------------------: | ------------------------------------: |
|      |                                     2 |                                     1 |
|      |                                     4 |                                     3 |
|      | <span style="color:#CD7F32;">?</span> | <span style="color:#CD7F32;">?</span> |
| Mean |                                     4 |                                     4 |

<br/>
<br/>
<br/>

</div>
</div>

---

# Sum of squared devs., Var., and Std. Dev.

<div class="flex">
<div>

|         A | (A - 4)² |         B | (B - 4)² |
| --------: | -------: | --------: | -------: |
|         2 |        4 |         1 |        9 |
|         4 |        0 |         3 |        1 |
|         6 |        4 |         8 |       16 |
|       SSD |        8 |       SSD |       26 |
|  Variance |        4 |  Variance |       13 |
| Std. Dev. |        2 | Std. Dev. |      3.6 |

</div>
</div>

---


# Some properties of the variance

- Linear transformations: if $y_i = a + b \cdot x_i$, then

  $$
  s_y^2 = b^2 s_x^2
  $$

- Can be calculated as the difference between the average sum of squares and the squared mean:

  $$
  s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
  = \frac{n}{n - 1} \left( \frac{1}{n} \sum_{i=1}^{n} x_i^2 - \bar{x}^2 \right)
  $$

---
