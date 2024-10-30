---
theme: academic
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

## Applied Data Analytics

<br>

# Python basics

### Scalar data types

Hans-Martin von Gaudecker and Aapo Stenhammar

---

## Contents

- What are types?

- How to inspect a variable type

- Representing numbers: ints and floats

- Representing True and False: Booleans

<br/>
<br/>
<br/>
<br/>

---

### What is a variable type?

- The type indicates the type of information stored in a variable

  - int: An Integer

  - float: A real number (approximation)

  - Boolean: True or False

- Types are inferred upon assignment

<br/>
<br/>
<br/>
<br/>

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

[3] b = float(a)
    b
[3] 3.0

[4] type(b)
[4] 'float'
```
</div>
<div>

- Types can be inspected with `type()`

- The type of a variable can be changed using the functions:

  - int()
  - float()
  - bool()

- A variable type cannot be always changed

  - e.g. `"hello"` cannot be converted into int

<br/>
<br/>
<br/>
<br/>

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


- Floats represent real numbers

- They are imperfect representations

- When performing operations involving ints and floats, ints are automatically converted
  into floats
<br/>
<br/>
<br/>
<br/>

</div>
</div>

---

### Representing True and False: Booleans

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

<br/>
<br/>
<br/>
<br/>

</div>
</div>
