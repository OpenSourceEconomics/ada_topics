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

# Data analysis — Interpretation challenges

### Selection models

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Examples

- Learning from successful founders (case studies, any retrospective study)

- Polling people who spend lots of time answering polls

- Comparing health outcomes of hospitalised and non-hospitalised to learn about the
  effect of hospitalisation

---

# Learning from successful founders?

Typical article about founders:

1. Interview successful founders ($Y$)

2. Narrow down the narrative to 1-2 factors ($X$)

Example based on
[Mollick blog](https://www.oneusefulthing.org/p/when-survivorship-bias-meets-superstitious),
[Lifchits et al. (2023)](https://doi.org/10.1017/S1930297500008494)

---

# Learning from successful founders?

<div class="grid grid-cols-2 gap-20">
<div>

Causal relation between $X$ and $Y$

```mermaid {theme: 'neutral', scale: 1.5, htmlLabels: false}
flowchart LR
    X(X) ~~~ Y(Success)
    U(U) --> Y
```

</div>
<div>

Selection model

```mermaid {theme: 'neutral', scale: 1.5, htmlLabels: false}
flowchart LR
    X(X) --> Z(In story)
    Y(Success) --> Z
```


</div>
</div>

<br/>
<br/>

---

<div class="flex">
<div>

|  $Y$ | $X$ | $Y$ condition | $X$ condition | In story |
| ---: | --: | ------------- | ------------- | -------- |
| 1000 | 500 | True          | True          | True     |
|  900 | 400 | True          | True          | True     |
|  800 | 300 | True          | True          | True     |
|  700 | 200 | True          | False         | False    |
|  600 | 100 | True          | False         | False    |
|  500 | 100 | False         | False         | False    |
|  400 | 200 | False         | False         | False    |
|  300 | 300 | False         | True          | False    |
|  200 | 400 | False         | True          | False    |
|  100 | 500 | False         | True          | False    |

</div>
</div>

---

# Published story

All successful founders have exceptionally high values of $X$ and more is better. Here
is the table to prove it:

<br/>

<div class="flex">
<div>

|  $Y$ | $X$ |
| ---: | --: |
| 1000 | 500 |
|  900 | 400 |
|  800 | 300 |

</div>
</div>

---

# Polling people in access panels

<div class="flex">
<div>

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
flowchart LR
    X0(Opportunity cost<br/>of time) --> X1(Access<br/>Panel)
    X0 --> X2(Frequency,<br/>quality<br/>of past answers)
    X1 --> X3(Plans on voting<br/>in the next election)
    X1 --> X2
    X2 --> X3
    X0 --> X3

    style X3 fill:#FFE5B4
```

</div>
</div>

<br/>
<br/>

---

# Health effects of hospitalisation

<div class="flex">
<div>

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
flowchart LR
    X0(Health status<br/>in t-1) --> X1(Pain<br/>in t)
    X0 --> X2(Accident<br/>in t)
    X0 --> X3(GP diagnosis<br/>in t)
    X1 --> X4(Hospitalised<br/>in t)
    X2 --> X4
    X3 --> X4
    X0 --> X5(Health status<br/>at the end of t)
    X4 --> X5

    style X4 fill:#FFE5B4
```

</div>
</div>

<br/>
<br/>
