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
title: Applied Data Analytics
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Applied Data Analytics

<br/>

# Getting help / Python basics

### Python tracebacks

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- What are Exceptions and Tracebacks?

- The Anatomy of a Python Traceback

- Reading tracebacks


---

# Motivation

- We pretty much told you what you need to do so far

  - Example: `pd.Series([1, 2, 3], index=["a", "b", "c"])`

- Now we will discuss what happens if you do not follow instructions precisely

  - Exception: What class of error?

  - Traceback: Detailed report that helps you to localize the error

- Pro tip: Read the traceback!

<br/>
<br/>
<br/>


---

# Example Traceback

<div class="grid grid-cols-2 gap-4">
<div>

```python
pd.Series(
  [1, 2, 3],
  labels=["a", "b", "c"]
)
```
<br/>

<img src="/simple_traceback.png" class="rounded" width="400"/>

</div>
<div>

- The code on the left has a problem
- Traceback tells us everything we need:
  1. What type of Exception occurred: `TypeError`
  2. Where did it occur: In line 1 of our cell.
  3. What happened exactly *(tried to use a non-existent keyword argument)*
- Tracebacks can get very long! Read from bottom to top.
- Always look for these <br/>
  three things!

<br/>
<br/>
<br/>

</div>
</div>

---

# Common sources of errors

- `ValueError`: Called a function with something invalid

- `KeyError`: Typo in an index label or a dictionary key

- `TypeError`: Called a function with something that has the wrong type

- `ImportError`: Typo in an import
