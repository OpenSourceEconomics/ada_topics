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

- The median marks the halfway point of a distribution.

- Terciles, quartiles and quintiles use cut points at thirds, quarters and fifths.

- Deciles and percentiles use cut points at tenths and hundredths.

These cut points give equally probable bins for continuous distributions. In finite
samples, ties and indivisible observations can prevent exactly equal bin counts.

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

For $0<q<1$, an order-statistic or population $q$-quantile is a value $x$ such that:

1. At least a fraction $q$ of the distribution is less than or equal to $x$.

2. At least a fraction $1-q$ is greater than or equal to $x$.

Ties can make either inequality strict. For finite samples we use the minimum and
maximum as the endpoint quantiles at $q=0$ and $q=1$.

Pandas uses a different sample convention by default: linear interpolation between
ordered observations. Its cutoffs need not satisfy these empirical fractions exactly.

Examples:

- The median is the 0.5 quantile.

- The 57th percentile is the 0.57 quantile.

<br/>
<br/>

---

# Terminology often a bit loose

We often refer to things like "the top quartile", meaning all observations above the
3<sup>rd</sup> quartile / 0.75-quantile.

To avoid ambiguous phrases such as "in the 90<sup>th</sup> percentile", specify
the bin explicitly. For example, a 90%–91% quantile bin contains observations such that

$$q_{0.9} \leq x_i < q_{0.91} $$

This refers to a bin instead of a point; with ties it may be empty or have more than
1% of observations.
<br/>
<br/>
<br/>
