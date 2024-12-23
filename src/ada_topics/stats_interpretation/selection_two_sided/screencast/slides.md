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

### Two-sided selection

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Causality as a two-sided selection problem

- Interested in the effect of study choice on entry wages

- $X_i$: Study economics or business administration

- $Y_i$: Entry wage

---

# Outcomes

|         | Choice: Econ | Choice: Bus admin | $Y_i$ │ Econ | $Y_i$ │ Bus admin |
| ------- | -----------: | ----------------: | -----------: | ----------------: |
| Alice   |        False |              True |            . |            53,000 |
| Bob     |         True |             False |       52,000 |                 . |
| Charlie |        False |              True |            . |            45,000 |
| Derek   |        False |              True |            . |            67,000 |

---

# Potential outcomes = Counterfactuals

|         | Choice: Econ | Choice: Bus admin | $Y_i$ │ Econ | $Y_i$ │ Bus admin |
| ------- | -----------: | ----------------: | -----------: | ----------------: |
| Alice   |        False |              True |            ? |            53,000 |
| Bob     |         True |             False |       52,000 |                 ? |
| Charlie |        False |              True |            ? |            45,000 |
| Derek   |        False |              True |            ? |            67,000 |

---

# Comparing means

|                           | Choice: Econ | Choice: Bus admin |
| ------------------------- | -----------: | ----------------: |
| **$\bar{Y}$ │ Econ**      |       52,000 |                 . |
| **$\bar{Y}$ │ Bus admin** |            . |            55,000 |

Why don't we observe the two missing values?

<span style="color:#CD7F32;">Model of selection into type of study!</span>

---

# Selection model

<br/>

```mermaid {theme: 'neutral', scale: 1.25, htmlLabels: false}
flowchart LR
    X(Study choice) ~~~ U0(Idealism) ~~~ Y(Entry wage)
    U0 --> Y
    X --> Y
    X(Study choice) ~~~ U1(Expected salary) ~~~ Y(Entry wage)
    U0 --> X
    U1 --> Y
    U1 --> X

    style Y fill:#FFE5B4
```

---

# Selection model

$$
\begin{align*}
Y_i & = \alpha + \beta \text{Bus admin}_i + U_{i}\\[2ex]
\bar{Y} | \text{Econ} & = \alpha \quad\;\;\; + \bar{U} | \text{Econ} \\[2ex]
\bar{Y} | \text{Bus admin} & = \alpha + \beta +  \bar{U} | \text{Bus admin}
\end{align*}
$$

**<span style="color:#CD7F32;">No contradiction:</span>**

$\bar{Y} | \text{Econ} < \bar{Y} | \text{Bus admin} \qquad$ **and** $\qquad\beta < 0$

---

# Consequences

- We can never observe the causal effect at the individual level

  **<span style="color:#CD7F32;">Always need some reduction operation</span>**

- Comparing means only makes sense if selection is random, i.e.

  $$\bar{U} | \text{Econ} = \bar{U} | \text{Bus admin} = 0$$

- When thinking about causal effects, always define the population of interest

  - All people who study economics? Economics or business administration?

  - All people with Abitur?

  - All people born in 2005?
