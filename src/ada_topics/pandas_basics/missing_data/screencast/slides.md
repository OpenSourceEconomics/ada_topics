---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Applied Data Analytics
drawings:
  persist: false
transition: fade
defaults:
  layout: center
marp: true
---

## Applied Data Analytics

<br>

# Pandas

### Missing data

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# ...

| Name    | Income |
| ------- | ------ |
| Alice   | 3000   |
| Bob     |        |
| Charlie | 5000   |

What is mean / median income in this dataset?

---

# Three strategies for answers

1. We don't know *(propagate missing values)*

1. 4000 *(just ignore)*

1. Come up with a number for Bob based on external information *(impute)*
