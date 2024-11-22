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

### Equivalence scales

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Distribution of economic resources

- Consumption vs. income

- People live in households of different sizes

- Still want to compare everyone

  - Equivalence

  - Scales

---

# Public goods / economies of scale

- Dwelling

- Appliances

- Food

- Vacations

- Mobility

- ...

---

## Equivalence scales

$$\textrm{weight}(\textrm{HH}_i) = f\big(N^\textrm{adults}_i, N^\textrm{kids}_i\big)$$

Properties

- $f(1, 0) = 1$
- $0 < \Delta f / \Delta N < 1$
- $\Delta^2 f / \Delta N \Delta N \leq 0$
- $\Delta f / \Delta N^\textrm{adults} \geq \Delta f / \Delta N^\textrm{kids}$

---

## The "new" OECD scale

<div class="flex">
<div>

|                  Description | Weight |
| ---------------------------: | -----: |
|                  First adult |    1.0 |
| Each further person aged 14+ |    0.5 |
|                   Each child |    0.3 |

</div>
</div>
