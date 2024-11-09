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

### Skewness

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

<center>
<img src="/only_sym.svg" width=600>
</center>

---

<center>
<img src="/sym_right.svg" width=600>
</center>

---

<center>
<img src="/sym_left.svg" width=600>
</center>

---

<center>
<img src="/bare.svg" width=600>
</center>

---

# Skewness

$$
\frac{n}{(n-1)(n-2)} \cdot \frac{\sum_{i=1}^{n} (x_i - \bar{x})^3}{s^3}
$$

- The only important bit is the second fraction

- Pandas actually uses a slightly different df normalisation

---

| A        |   (A - 4)³ | B        |   (B - 4)³ |
| --------: | -------: | --------: | -------: |
| 2        |         -8 | 1        |     -27    |
| 4        |          0 | 3        |      -1    |
| 6        |          8 | 8        |      64    |
| SCD      |          0 | SCD      |      36    |
| Skewness |          0 | Skewness |       0.84 |
