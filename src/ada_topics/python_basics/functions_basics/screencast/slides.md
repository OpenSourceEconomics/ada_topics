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
title: Applied Data Analytics
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Applied Data Analytics

<br/>

# Basic Python

### Defining Functions

<br/>

Hans-Martin von Gaudecker

---

# Contents

- Anatomy of functions

- An example

---

# Example: CRRA Utility function

$$
u(c, γ) = \frac{c ^{(1 - γ)}}{1 - γ}
$$

---

# Functions are like math functions

- They take arguments

- They return a value

- Difference

  - Math functions typically operate on numerical values

  - Python functions can operate on almost anything

---

# Anatomy of Python functions

<br/>

<div class="grid grid-cols-2 gap-4">
<div>

<br/>
<br/>

<img src="/function_anatomy.png" class="rounded" width="400"/>

</div>
<div>

- Start with the `def` keyword
- Name is `lowercase_with_underscores`
- There can be one or several parameters (a.k.a. arguments)
- You can assign default values for arguments
- Function body is indented by 4 spaces and can have one or several lines
- Inside the body you can do everything you have seen so far!

</div>
</div>

---

# Example: CRRA Utility function

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
[1] def utility_crra(c, γ=1.5):
...     return c ** (1 - γ) / (1 - γ)

[2] utility_crra(1.0)
-2.0

[3] utility_crra(c=1.0, γ=1.5)
-2.0

[4] utility_crra(c=1.0, γ=0.0)
1.0

```

</div>
<div class="col-span-2">

- Function calls work with positional and keyword arguments

- Pass keyword arguments for any function with more than one argument!

</div>
</div>
