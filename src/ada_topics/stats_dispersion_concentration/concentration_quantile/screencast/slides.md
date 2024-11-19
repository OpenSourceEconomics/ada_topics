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

### Quantile-based concentration measures

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Concentration measures

- Dispersion

  - Q: How far apart are values, typically?

  - A only depends on distances between values

- Concentration

  - Q: How is the total amount distributed over values?

  - A depends on distances and total amount

---

# Example

|      |    A |    B |
| :--- | ---: | ---: |
| 0    | 0.17 | 0.04 |
| 1    | 0.17 | 0.33 |
| 2    | 0.67 | 0.62 |
| mean | 0.33 | 0.33 |
| var  | 0.08 | 0.08 |

---

# [Example](https://www.bpb.de/kurz-knapp/zahlen-und-fakten/soziale-situation-in-deutschland/61896/steuer-und-abgabenlast-von-durchschnittsverdienern/)

Nach Angaben des BMF zahlten im Jahr 2022 die – gemessen an der Höhe der Einkünfte –
oberen 10 Prozent der Einkommensteuerpflichtigen 55,8 Prozent des gesamten Lohn- und
Einkommensteueraufkommens. Bei den untersten 50 Prozent der Einkommensteuerpflichtigen
lag der entsprechende Anteil bei lediglich 6,1 Prozent

Beim obersten Prozent lag der Anteil am Einkommensteueraufkommen bei 22,8 Prozent, bei
den untersten 20 Prozent waren es 0,3 Prozent.

---

# [Example](https://www.bpb.de/kurz-knapp/zahlen-und-fakten/soziale-situation-in-deutschland/61896/steuer-und-abgabenlast-von-durchschnittsverdienern/)

According to the Federal Ministry of Finance (BMF), in 2022, the top 10 percent of
income taxpayers contributed 55.8 percent of the total wage and income tax revenue,
measured by the amount of income. In contrast, the bottom 50 percent of income taxpayers
accounted for only 6.1 percent of this revenue.

The top 1 percent contributed 22.8 percent of the income tax revenue, while the bottom
20 percent contributed just 0.3 percent.

---

# Histogram

<center>
<img src="/initial.svg" width=650>
</center>

<br/>
<br/>

---

# Histogram with sums of values

<center>
<img src="/sum.svg" width=650>
</center>

<br/>
<br/>

---

# Histogram with fractions of values

<center>
<img src="/frac.svg" width=650>
</center>

<br/>
<br/>

---

# Palma ratio

$$
\text{Palma ratio} = \frac{\text{top 10\% of income}}{\text{bottom 40\% of income}}
$$

---

# All concentration measures are relative

<div class="flex">
<div>

|     | Country A | Country B |
| :-- | --------: | --------: |
| 0   |         1 |         2 |
| 1   |         2 |         5 |
| 2   |         3 |        10 |

</div>
</div>
