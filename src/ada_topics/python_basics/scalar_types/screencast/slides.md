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
# themeConfig:
#   paginationPagesDisabled: true
---

## Applied Data Analytics

<br>

# Python basics

### Scalar data types

Hans-Martin von Gaudecker and Aapo Stenhammar

---

## Contents

- What are types
- How to inspect a variable type
- Representing numbers: ints and floats
- Representing True and False: booleans

---

### What is a variable type

- Different types of variables are used to store different kinds of data
- The main scalar types are:
  + int
  + float
  + boolean
- The type of a variable tells us what kind of information is stored in the variable
  + e.g. an int variable contains a whole number

---

### How to inspect and change variables types

<div class="flex gap-6">
<div>
<br>
<br>

```python
[1] type(3)
[1] 'int'

[2] a = 3
    type(a)
[2] 'int'
```
</div>
<div>

- When you assign variables, the types are inferred, not declared upfront
- Types can be inspected with `type()`
- The type of a variable can be changed using the functions:
  - int()
  - float()
  - bool()
- A variable type cannot be always changed
  - e.g. "hello" cannot be converted into int

</div>
</div>

---

### Representing numbers: ints and floats

<div class="flex gap-6">
<div>

```python
[1] b = 3.1415
    type(b)
[1] 'float'

[2] c = 0.1 + 0.2
    c
[2] 0.30000000000000004

[3] a = 2
    b = 3.1415
    c = a + b
    type(c)
[3] 'float'
```
</div>
<div>

  <br>
  <br>

- In addition to the integers, floats represent real numbers
- They are imperfect representations
- When performing operations among ints and floats,
  ints are automatically converted into floats

</div>
</div>

---

# Representing True and False: Booleans

<div class="flex gap-8">
<div>

```python
[1] a = True
    b = False
    type(a)
[1] 'bool'

[2] a = 3
    b = 3
    a < b
[2] False

[3] int(True)
[3] 1

[4] bool(6)
[4] True
```

</div>
<div>
<br>
<br>

- Booleans can be `True` or `False` (case sensitive)
- The result of a comparison is a Boolean
- `True` or `False` are interpreted as 1 and 0
- All int and floats different from 0 are converted to `True`

</div>
</div>
