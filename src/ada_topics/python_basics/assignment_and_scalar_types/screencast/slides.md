---
theme: academic
coverDate: ""
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

### Assigning variables and built-in scalar types

<br/>


Hans-Martin von Gaudecker

---

# Contents

- Representing numbers: ints and floats
- Using Python like a calculator
- Comparing variables
- Representing True and False: Booleans

---

# Integers

<div class="flex gap-12">
<div>

```python
[1] a = 3
    a
[1] 3

[2] type(a)
[2] <class 'int'>

[3] type(3)
[3] <class 'int'>

[4] a = 5
    a
[4] 5
```


</div>
<div>

- Variables are assigned with a single `=` sign
- Types are inferred, not declared upfront
- Types can be inspected with `type()`
- You can re-assign variables with different values

</div>
</div>


---

# Floats

<div class="flex gap-12">
<div>

```python
[1] b = 3.1415
    b
[1] 3.1415

[2] type(b)
[2] <class 'float'>

[3] c = 0.1 + 0.2
    c
[3] 0.30000000000000004
```


</div>
<div>

- Floats represent real numbers
- They are imperfect representations

</div>
</div>


---

# Python as a calculator

<div class="flex gap-8">
<div>

```python
[1] a = 3
    b = 3.1415
    b / a
[1] 1.0471666666666668

[2] (a + b) * 3
[2] 18.424500000000002

[3] a**b
[3] 31.54106995953402

```

</div>
<div>

- Arithmetic works as you would expect
- Brackets work as expected
- Mixing ints and floats converts everything to floats
- `**` is exponentiation (not `^`)

</div>
</div>


---

# Comparisons

<div class="flex gap-8">
<div>

```python
[1] a = 3
    b = 3
    a == b
[1] True

[2] a < b
[2] False

[3] a >= b
[3] True
```

</div>
<div>

- Comparison operators are `==`, `<`, `>`, `<=`, `>=`
- Remember:
  - `=` is used for assignment
  - Classic error is trying to use it for comparison
- The result of a comparison is a Boolean

</div>
</div>


---

# Booleans

<div class="flex gap-8">
<div>

```python
[1] a = True
    b = False
    type(a)
[1] <class 'bool'>

[2] a and b
[2] False

[3] a or b
[3] True

[4] not b
[4] True
```

</div>
<div>

- Booleans can be `True` or `False` (case sensitive)
- `and`, `or` and `not` can be used to express complex conditions
- Important: `or` is the inclusive or!

</div>
</div>
