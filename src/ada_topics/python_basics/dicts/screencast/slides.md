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

### Dictionaries

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- Creating dictionaries

- What can go in a dict

- Accessing elements in dictionaries

- Advantages of labelled data structures


---

# Dictionaries

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> a = {"a": 1, "b": 2, "c": 3}
>>> type(a)
<class 'dict'>


>>> a["b"]
2

>>> a["c"] = 42
>>> a
{'a': 1, 'b': 2, 'c': 42}

>>>a["d"] = 4
{'a': 1, 'b': 2, 'c': 42, 'd': 4}
```

</div>
<div>

- Map a set of keys to a set of values
- Creation by curly braces and `:` to separate keys and values
- **mutable**: Can add or overwrite entries
- Order is preserved *(since Python 3.6)*


</div>
</div>


---

# What can go in a dict?


<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> nested = {
>>>   1: {"bla": "blubb"},
>>>   "two": {"foo": "bar"},
>>> }
```

</div>
<div>

- Keys need to be hashable, for example

  - strings
  - ints
  - tuples thereof

- Values can be absolutely anything

- If values are dicts we get nested dictionaries

<br/>
<br/>

</div>
</div>

---

# Accessing elements

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> flat = {"bla": "blubb"}
>>> nested = {
>>>   1: flat,
      "two": {"foo": "bar"}
>>> }

>>> flat["bla"]
'blubb'

>>> nested[1]
{'bla': 'blubb'}

>>> nested[1]["bla"]
'blubb'

```

</div>
<div>

- Elements are accessed with square brackets

- Chained access for nested dictionaries



</div>
</div>



---

# When to use dictionaries


- Dictionaries provide label based access

- Lists provide position based access

- Label based access is more readable and less error prone!
