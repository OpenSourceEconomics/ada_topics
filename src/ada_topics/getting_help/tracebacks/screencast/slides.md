---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: Effective Programming Practices for Economists
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

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

- We sometimes told you that you cannot do certain things:
  - Example: Can only use hashable objects as dictionary keys
- Now we will discuss what happens if you do it anyways
  - Exception: What class of error?
  - Traceback: Detailed report that helps you to localize the error
- Pro tip: Read the traceback!


---

# Example Traceback

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> d = {"a" : 1}
>>> d[[1, 2, 3]] = "b"
>>> d["c"] = 3
```
<br/>

<img src="/simple_traceback.png" class="rounded" width="400"/>

</div>
<div>

- The code on the left has a problem
- Traceback tells us everything we need:
  1. What type of Exception occurred: `TypeError`
  2. Where did it occur: In line 2 of `some_file.py`
  3. What happened exactly *(used an unhashable type where we must not)*
- Tracebacks can get very long! Read from bottom to top.
- Always look for these three things!

</div>
</div>

---

# Common sources of errors

- `ValueError`: Called a function with something invalid
- `KeyError`: Typo in a variable name or a dictionary key
- `TypeError`: Called a function with something that has the wrong type
- `ImportError`: Typo in an import
