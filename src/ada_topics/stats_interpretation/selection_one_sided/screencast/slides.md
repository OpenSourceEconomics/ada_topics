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

### One-sided selection

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Possible goals

- Describe distribution of $Y$ and/or $X$

- Describe relation between $X$ and $Y$ (correlation, CMF $\bar{Y}|X$, ...)

# Problem

- Data on $X$ and/or $Y$ is missing for some reason

# Examples

- Not clear what salary expectation of 15k € annually meant

- Most hip hop musicians are still alive


---

# When is this a problem?

<br/>

```mermaid {theme: 'neutral', scale: 1.25, htmlLabels: false}
flowchart LR
    X(Genre of top<br/>performing artists) ~~~ U(Year of birth) ~~~ Y(Age at death)
    U --> Y
    U --> X
    X ~~~ Y

    style Y fill:#FFE5B4
```

---

# Distribution of birth years

<img src="/fig_birthyears.svg" class="rounded" width="600">

---

# Using observed age at death

- Calculated mean age at death < true mean age at death

  *Many artists are still alive, so it can only go up.*

- Wrong result for relation between genre and age at death

  *Distribution of birth years not the same for all genres.*

---

# One-sided selection: Summary

- Interested in describing (joint) distributions

- Data is missing on $X$ and/or $Y$

- Why is it missing?

  - Purely at random? E.g., because of proper sampling?

    <span style="color:#CD7F32;">Typically fine to ignore.</span>

  - Else: Think hard about the causal selection process

    <span style="color:#CD7F32;">Obvious bias in some direction?</span>
