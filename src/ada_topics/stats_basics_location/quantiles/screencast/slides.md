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

### Quantiles

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

- Median divides the data into two halves

- Terciles divide the data into three equally sized bins

- Quartiles divide the data into four equally sized bins

- Quintiles divide the data into five equally sized bins

- Deciles divide the data into ten equally sized bins

- Percentiles divide the data into one hundred equally sized bins

---

<img src="/dist.svg" class="rounded" width="600">

---

<img src="/dist_median.svg" class="rounded" width="600">

---

<img src="/dist_terciles.svg" class="rounded" width="600">

---

<img src="/dist_quartiles.svg" class="rounded" width="600">

---

<img src="/dist_quintiles.svg" class="rounded" width="600">

---

<img src="/dist_deciles.svg" class="rounded" width="600">

---

<img src="/dist_percentiles.svg" class="rounded" width="600">

---

# Quantile $\in [0, 1]$

The $q$-th quantile of a distribution is the value $x$ such that:

1. A fraction $q$ of the data is less than or equal to $x$.

2. A fraction $1 - q$ is greater than or equal to $x$.

Examples:

- The median is the 0.5 quantile.

- The 57th percentile is the 0.57 quantile.

<br/>
<br/>

---

# Terminology often a bit loose

We often refer to things like "the top quartile", meaning all observations above the
3<sup>rd</sup> quartile / 0.75-quantile.

Another example: "Observations in the 90<sup>th</sup> percentile" would mean
observations such that

$$q_{0.9} \leq x_i < q_{0.91} $$

Hence, reference to bins instead of points.
<br/>
<br/>
<br/>
