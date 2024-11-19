---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: Applied Data Analytics
drawings:
  persist: false
transition: fade
defaults:
  layout: center
marp: true
---

## Applied Data Analytics

<br>

# Statistics — Basics & location

### Measures of Central Tendency: More properties

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Reduction operations

- Technically, mean/median/mode are reduction operations

- Take a sequence of numbers and reduce it to a single number

- You will encounter that term a lot in programming-related contexts

- In a sense, all of statistics is about reduction operations

---

# Mean, median, and aggregates

- Remember median depends on middle value(s) of the data only, mean on all

- Highest-earning person has a disproportionate impact on total income — not reflected
  in median at all

- Having data on mean income and population size allows me to calculate aggregate income

- Median income and population size don't allow me to do that

- Flipside of sensitivity to outliers

---

# Transformations

- We are often interested in relative effects

- E.g., a 5€ increase in hourly pay makes a large difference if the base is 15€ / hour.

- If the base is 150€ / hour, the same 5€ increase is less important

- Take logarithms for that

---

### Median is invariant to order-preserving transform's

$$
\begin{aligned}
\text{med}(1, 10, 100) & = 10\\
\text{med}(\log(1), \log(10), \log(100)) & = \log(10)
\end{aligned}
$$

In general:

$$
f(\text{med}(\text{data})) = \text{med}(f(\text{data}))
$$

so long as $f$ does not change the order of the data

<br/>
<br/>

---

### Mean is invariant to positive affine transformations

$$
\begin{aligned}
\text{mean}(1, 10, 100) & = \frac{1 + 10 + 100}{3} = 37\\[3ex]
\text{mean}(\log(1), \log(10), \log(100)) & = \frac{0 + 1 + 2}{3} = 1
\end{aligned}
$$

In general:

$$
f(\text{mean}(\text{data})) = \text{mean}(f(\text{data}))
$$

if and only if $f(x) = a + b \cdot x$ with $b > 0$ (positive affine transformation)

<br/>
<br/>

---

<img src="/income_nbins_100.svg" class="rounded" width="600">

---

<img src="/log_income_nbins_100.svg" class="rounded" width="600">

---

<img src="/income_nbins_100_vlines.svg" class="rounded" width="600">

---

<img src="/log_income_nbins_100_vlines.svg" class="rounded" width="600">

---

# Numerical values

| Measure             | $g(x_1, ..., x_N)$ | $10 ^ {g(\log_{10}{x_1}, ..., \log_{10}{x_N})}$ |
| ------------------- | ------------------ | ----------------------------------------------- |
| $g = \text{median}$ | 18300              | 18300                                           |
| $g = \text{mean}$   | 20600              | 17900                                           |

<br/>
<br/>


---

<img src="/symmetric.svg" class="rounded" width="600">

---

<img src="/right-skewed.svg" class="rounded" width="600">
