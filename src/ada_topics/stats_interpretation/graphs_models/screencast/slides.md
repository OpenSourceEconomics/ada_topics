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
  layout: default
---

### Applied Data Analytics

<br/>

# Data analysis — Interpretation challenges

### Using graphs for modelling

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Forest fires and ice cream sales

<br/>
<br/>

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
graph LR
    A(forest<br/>fires) ~~~ B(temperature) ~~~ C(ice cream<br/>sales)
    A ~~~ D(rain) ~~~ C
```

---

# Marshmallows and education

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
graph LR
    X["&nbsp;"]
    style X fill:none,stroke:none;
    A(grab marshmallow<br/>immediately) ~~~ X ~~~ C(educational<br/>attainment)
    A ~~~ B(patience at age 15) ~~~ C
    A ~~~ D(parental background) ~~~ C
```

---

# Supply and demand

<br/>
<br/>

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
graph LR
    A(price) ~~~ B(consumer demand) ~~~ C(quantity)
    A(price) ~~~ D(production costs) ~~~ C(quantity)
```

<br/>

---

# Income and health

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
graph LR
    A(income) ~~~ B(doctor visits) ~~~ C(health)
    A ~~~ D(food) ~~~ C
    A ~~~ E(earnings capacity) ~~~ C
    A ~~~ F(cogn. / personality) ~~~ C
```

---

# Military service and earnings

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
graph LR
    A(military service) ~~~ B(in combat) ~~~ C(trauma) ~~~ D(earnings)
    A ~~~ E(ambition) ~~~ D
    A ~~~ F(leadership skills) ~~~ D
```

---

# Steps to structure models

1. Start from a large model with many variables.

2. Only then remove paths based on arguments about how the world works (theory!)

Missing paths are restrictions!
