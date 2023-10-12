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

### Strings

<br/>


Hans-Martin von Gaudecker

---

# Contents

- Representing text: Strings
- Methods to manipulate strings
- String formatting
- Strings as sequences

---


# Assigning strings

<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] a = "Hello"
    type(a)
str

[1] b = 'embed "double" quotes'
    c = "embed 'single' quotes"

[1] not_an_int = "123"
    type(not_an_int)
str

[1] not_an_int * 2
'123123'
```

</div>
<div>

- Strings can hold arbitrary text data
- Defined with single or double quotes
- Strings containing numbers do not behave like numbers!

</div>
</div>


---

# Everything is an object == Everything has methods

- Any language has `int`, `float`, `bool` and `string`
- C, Fortran, ...:
  - low level types to store data efficiently and do fast calculations
- Python: Everything is an object
  - Objects with convenient methods
  - Trade efficiency for convenience
  - We can still get efficient when needed!

---

# Some string methods


<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] a = "Hello World!"
    a.lower()
'hello world!'

[1] a.replace("!", ".")
"Hello World."

[1] a.startswith("Hello")
True
```

</div>
<div>

- There are many methods for string manipulation
- [Full documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

</div>
</div>


---

# String formatting


<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] a = "Hello"
    b = "3"
[1] f"{a} {b}"
'Hello 3'

[1] c = 3.145
    f"{a} {c}"
'Hello 3.145'

```

</div>
<div>

- "f-strings" allow you to puzzle together different strings
- Variables used in formatting are automatically converted to strings
- Many useful applications:
  - Embed results of calculations in messages
  - Write good error messages
  - Format numbers in tables

</div>
</div>


---

# Strings are a sequence type


<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] a = "Hello World!"
    len(a)
12

[1] a[0]
'H'

[1] a[1]
'e'

[1] a[-1]
'!'
```

</div>
<div>

- Most of the time, you can think of strings as scalar variables
- They are actually sequences of characters
    - Have a length
    - Can be indexed
    - *Can be sliced*
    - *Can be iterated over*
- Indexing starts at 0
- Negative indices start from the end

</div>
</div>
