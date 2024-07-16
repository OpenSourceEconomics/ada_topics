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

### Applied Data Analytics

<br/>

# Python basices

### Scalar types

<br/>


Hans-Martin von Gaudecker

---

# Contents

- What are types
- How to inspect a variable type
- Representing numbers: ints and floats
- Representing True and False: booleans
- Representing text: strings

---
# What is a variable type

- Different types of variables are used to store different kinds of data
- The main scalar types are:
  - int
  - float
  - boolean
  - string
- The type of a variable tells us what kind of information is stored in the variable
  - e.g. an int variable contains a whole number

---
# How to inspect and change variables types

<div class="flex gap-12">
<div>

```python
[1] type(3)
[1] <class 'int'>

[2] a = 3
    type(a)
[2] <class 'int'>
```


</div>
<div>

- When you assign variables, the types are inferred, not declared upfront
- Types can be inspected with `type()`
- The type of a variable can be changed using the functions:
  - int()
  - float()
  - bool()
  - str()
- A variable type cannot be always changed
  - e.g. "hello" cannot be converted into int

</div>
</div>

---

# Representing numbers: ints and floats

<div class="flex gap-12">
<div>

```python
[1] b = 3.1415
    type(b)
[1] <class 'float'>

[2] c = 0.1 + 0.2
    c
[2] 0.30000000000000004

[3] a = 2
    b = 3.1415
    c = a + b
    type(c)
[3] <class 'float'>
```


</div>
<div>

- In addition to the integers, floats represent real numbers
- They are imperfect representations
- When performing operations among ints and floats,
  ints are automatically converted into floats

</div>
</div>

---

# Representing True and False: booleans

<div class="flex gap-8">
<div>

```python
[1] a = True
    b = False
    type(a)
[1] <class 'bool'>

[2] a = 3
    b = 3
    a < b
[2] False

[3] type(a < b)
[3] <class 'bool'>

[4] c = a == b
    type(c)
[4] <class 'bool'>

[5] int(True)
[5] 1

[6] bool(6)
[6] True
```

</div>
<div>

- Booleans can be `True` or `False` (case sensitive)
- The result of a comparison is a Boolean
- `True` or `False` are interpreted as 1 and 0
- All int and floats different from 0 are converted to True (but you will never do this)

</div>
</div>

---

# Representing text: strings

<div class="flex gap-8">
<div>

```python
[1] a = "Hello world"
    type(a)
[1] <class 'str'>

[2] a = "1.0"
    type(a)
[2] <class 'str'>

[3] a = "Hello"
    b = " "
    c = "world"
    a + b + c
[3] "Hello world"
```

</div>
<div>

- Strings represent texts
- A string can contain any alphanumeric character
- "+" is used to concatenate strings
- "-" is not supported by strings

</div>
</div>
