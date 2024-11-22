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

# Statistics — Miscellaneous topics

### Index numbers and inflation

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Proportional numbers

One number divided by another, non-zero number.

1. Structural numbers: Divide total into parts

   Imports by good, students by school type, employees by sector

2. Relationship Numbers: Divide two different, but related numbers

   All flows, arithmetic mean, return on investment

3. Measurement numbers: Divide by the same number at different times

   Price of a good in 2024 relative to 2010, GDP in 2000 relative to 1000

---

# Index numbers

- Aggregate multiple numbers into one, typically a (weighted) sum

- Comparisons only make sense for proportional numbers

- There is an [OECD-EU JRC handbook on constructing such
  numbers](https://doi.org/10.1787/9789264043466-en)

- Most common: Inflation

  - Basket of goods & services × associated prices

  - Different baskets → different inflation rates

    CPI, PPI, core inflation, ...

---
layout: default
---

# Price and quantity data

<div class="flex">
<div>

| Good | Period | Quantity | Price |
| ---: | -----: | -------: | ----: |
|    A |      0 |       83 |     2 |
|      |      t |       73 |     3 |
|    B |      0 |       45 |    20 |
|      |      t |       60 |    19 |
|    C |      0 |     2500 |   0.1 |
|      |      t |     1800 |   0.2 |

</div>
</div>

---
layout: default
---

# Price and quantity data: notation

<div class="flex gap-16">
<div>

| Good | Period |   Quantity |      Price |
| ---: | -----: | ---------: | ---------: |
|    A |      0 | $q_{A, 0}$ | $p_{A, 0}$ |
|      |      t | $q_{A, t}$ | $p_{A, t}$ |
|    B |      0 | $q_{B, 0}$ | $p_{B, 0}$ |
|      |      t | $q_{B, t}$ | $p_{B, t}$ |
|    C |      0 | $q_{C, 0}$ | $p_{C, 0}$ |
|      |      t | $q_{C, t}$ | $p_{C, t}$ |

</div>
<div>

- Periods $s \in (1, 2, \ldots, t)$

- Goods $i \in \{1, 2, \ldots, n\}$

- $t \cdot n \;$ quantities $\;q_{i, s} > 0$

- $t \cdot n \;$ prices $\;p_{i, s} > 0$


</div>
</div>

---

# Composite price index by period

$$
P_s = \sum_{i=1}^n p_{i, s} \cdot q_{i, s}
$$

- For comparing two periods: What to do with $\Delta q$?

- Just dividing $P_t$ by $P_{0}$ would yield growth in (total) expenditures

  $$
  \frac{\sum_{i=1}^n p_{i, t} \cdot q_{i, t}}{\sum_{i=1}^n p_{i, 0} \cdot q_{i, 0}}
  $$

- So would like to hold $q$ constant

---

# Laspeyres index

$$
\begin{aligned}
P^\text{Laspeyres}_{t, 0} & = \sum_{i=1}^n \frac{p_{i, t}}{p_{i, 0}} \cdot g(i, \; p_{1, 0}, p_{2, 0}, \ldots, p_{n, 0}, \; q_{1, 0}, q_{2, 0}, \ldots, q_{n, 0})\\[4ex]
  & = \sum_{i=1}^n \frac{p_{i, t}}{p_{i, 0}} \cdot \frac{p_{i, 0} \cdot q_{i, 0}}{\sum_{j=1}^n p_{j, 0} \cdot q_{j, 0}}\\[4ex]
  & = \frac{\sum_{i=1}^n p_{i, t} \cdot q_{i, 0}}{\sum_{i=1}^n p_{i, 0} \cdot q_{i, 0}}
\end{aligned}
$$


---

# Paasche index

$$
\begin{aligned}
P^\text{Paasche}_{t, 0} & = \sum_{i=1}^n \frac{p_{i, t}}{p_{i, 0}} \cdot g(i, \; p_{1, 0}, p_{2, 0}, \ldots, p_{n, 0}, \; q_{1, t}, q_{2, t}, \ldots, q_{n, t})\\[4ex]
  & = \sum_{i=1}^n \frac{p_{i, t}}{p_{i, 0}} \cdot \frac{p_{i, 0} \cdot q_{i, t}}{\sum_{j=1}^n p_{j, 0} \cdot q_{j, t}}\\[4ex]
  & = \frac{\sum_{i=1}^n p_{i, t} \cdot q_{i, t}}{\sum_{i=1}^n p_{i, 0} \cdot q_{i, t}}
\end{aligned}
$$
