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
defaults:
  layout: center
---

### Applied Data Analytics

<br/>

# Basic Python

### Lists and tuples

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- Unlabelled, ordered containers

  - Lists

  - Tuples

- Selecting elements


---

# Lists

<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

```python
>>> a = [1, 2, 3]
>>> type(a)
<class 'list'>

>>> a.append(4)
>>> a
[1, 2, 3, 4]

>>> a[0] = "bla"
>>> a
['bla', 2, 3, 4]

>>> len(a)
4
```

</div>
<div class="col-span-3">

- Created with square brackets

- Definition: Mutable sequence of objects

  - **mutable**: Can change it after creation

  - **sequence**: An ordered collection

  - **of objects**: Items can consist of anything

- Lists are used a lot!

- `len` works for all collections

<br/>

</div>
</div>

---

# Tuples

<div class="grid grid-cols-5 gap-4">
<div class="col-span-2">

```python
>>> a = (1, 2, 3)
>>> type(a)
<class 'tuple'>

>>> b = (1)
>>> type(b)
<class 'int'>

>>> c = (1,)
>>> type(c)
<class 'tuple'>

>>> d = 2,
>>> type(d)
<class 'tuple'>
```

</div>
<div class="col-span-3">

- Created with round brackets

- Definition: Immutable sequence of objects

  - **immutable**: Cannot change after creation

- Single element tuples need a comma

- But sometimes you don't need the brackets!

- Less flexible than lists, less common

- Somewhat unfair

<br/>
</div>
</div>

---

# Selecting elements

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[1]
2

>>> a[1: 2]
[2]

>>> a[:2]
[1, 2]

>>> a[2:]
[3, 4, 5]

>>> a[-1]
[5]
```

</div>
<div>

- Selecting elements is the same for lists, tuples, and other sequences

- Indexing starts at 0

- Upper index of slices is not included

- lower and upper index can be left implicit

- negative indices start from the end

</div>
</div>
