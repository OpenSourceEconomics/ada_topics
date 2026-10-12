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

### Graphs & Causality

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Graphs & Causality

- Graphs encode sense of direction

- Data description alone **never** does

---

# Inferring causality

- The introductory graphical criterion used here assumes a DAG.

  _Feedback requires a separately specified dynamic or simultaneous model._

  <br/>

- For the simple unadjusted comparisons here, rule out confounding paths:

```mermaid {theme: 'neutral', scale: 1.5, htmlLabels: false}
flowchart LR
    X ~~~ U ~~~ Y
    U(U) --> Y
    U --> X
    X(X) --> Y(Y)
```

<br/>
<br/>

---


# Inferring causality

- The introductory graphical criterion used here assumes a DAG.

  _A cycle prevents applying this criterion as drawn; it does not by itself prove
  that a causal effect cannot be identified._

  <br/>

- Adjustment may remove confounding if an appropriate set of confounders is observed
  and the statistical model is correctly specified.

  _For example, in a suitable multiple regression:_

  $$Y_i = \beta_0 + \beta_1 X_{1, i} + \beta_2 X_{2_i} + \ldots + \beta_k X_{k_i} + U_i$$

  _but the world is too complex for that._

<br/>
<br/>
<br/>
