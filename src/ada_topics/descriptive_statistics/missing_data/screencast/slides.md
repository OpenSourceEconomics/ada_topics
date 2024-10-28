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

# Descriptive Statistics


### Missing data

<br>

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

1. We don't know *<span style="color:#CD7F32;">(propagate missing values)</span>*

1. 4000 *<span style="color:#CD7F32;">(just ignore)</span>*

1. Come up with a number for Bob based on external information *<span style="color:#CD7F32;">(impute)</span>*


---

# Reasons for why data might be missing

- Refusal to answer

- Does not apply: Ask only those who are employed about labour income

- Question routing

- Privacy concerns (e.g., small cells)
