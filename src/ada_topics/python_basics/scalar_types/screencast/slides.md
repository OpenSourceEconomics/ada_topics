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

# Some Chapter

### Some Subchapter

<br/>


Hans-Martin von Gaudecker

---

# Contents

- Why types and how to inspect a variable type
- Representing numbers: ints and floats
- Representing True and False: booleans
- Representing text: strings
- Operations among different types

---

# What is a variable type

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

- Different types of variables are used to store different kinds of data
- The main scalar types are:
  - int
  - float
  - boolean
  - string
- The type of a variable tells us what kind of information is stored in the variable
  - e.g. an int variable contains a whole number
- When you assign variables, the types are inferred, not declared upfront
- Types can be inspected with `type()`
- The type of a variable can be changed using the functions:
  - int()
  - float()
  - bool()
  - str()
- Variables types can be changed (not always)

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

- Floats represent real numbers
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
```

</div>
<div>

- Booleans can be `True` or `False` (case sensitive)
- The result of a comparison is a Boolean
- `True` or `False` are also interpreted as 1 and 0

</div>
</div>



---

# Representing text: strings

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
```

</div>
<div>

- Booleans can be `True` or `False` (case sensitive)
- The result of a comparison is a Boolean
- `True` or `False` are also interpreted as 1 and 0

</div>
</div>
