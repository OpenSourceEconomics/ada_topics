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

### Selection problems: Introduction

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Bob refuses to report his income

<div class="grid grid-cols-3 gap-4">
<div>
</div>
<div>

| Name    | Income |
| ------- | ------ |
| Alice   | 3000   |
| Bob     |        |
| Charlie | 5000   |

<br/>

</div>
<div>
</div>
</div>

Q: What is mean / median income in this dataset?

<br/>
<br/>

---

# Three strategies for answers

1. We don't know _<span style="color:#CD7F32;">(propagate missing values)</span>_

1. 4000 _<span style="color:#CD7F32;">(just ignore)</span>_

1. Come up with a number for Bob based on external information _<span style="color:#CD7F32;">(impute)</span>_

---

# Selection: Why is data missing?

**<span style="color:#CD7F32;">Causal question!</span>**

<br/>

Goal:

- Raise awareness, provide a framework to think about it

- Constructive solutions: Later courses

---

# Selection: Why is data missing?

1. A: randomly

   - No problem

   - All three answer strategies lead to the same result

1. A: other reasons

   - Need to think hard about the selection process

   - Causal models and selection

---

# Examples

- Learning from successful founders (case studies, any retrospective study)

- Polling people who spend lots of time answering polls

- Comparing health outcomes of hospitalised and non-hospitalised to learn about the
  effect of hospitalisation

---

# Consequences

- Biased means, medians, variances, etc.

- Biased relationships between variables (correlations, CMF / OLS coefficients)

- Biased causal effects
