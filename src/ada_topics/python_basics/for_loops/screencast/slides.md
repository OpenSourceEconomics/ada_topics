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

### for loops

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- **D**on't **R**epeat **Y**ourself

- Syntax of for loops

- Looping over lists and tuples

- Looping over dicts


---

# Don't repeat yourself

<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> names = ["Guy", "Ray", "Tim"]
>>> lower_names = [
>>>   names[0].lower(),
>>>   names[1].lower(),
>>>   names[2].lower(),
>>> ]
>>> lower_names
['guy', 'ray', 'tim']
```

</div>
<div>

- This code repetition is problematic

  - If we have a typo, we need to fix it multiple times

  - Cumbersome if list becomes longer

- In many situations we want to do similar things multiple times

  - Cleaning several similar variables

  - Getting several bivariate estimates

  - ...

</div>
</div>

---

# A simple for loop

<div class="grid grid-cols-2 gap-4">
<div>

Example

```python
>>> for i in range(5):
...     print(i ** 2)
0
1
4
9
16
```

General pattern

```python
for running_var in iterable:
    do_something(running_var)
    and_something_else(running_var)
```

</div>
<div>

<br/>

for loops let us do things repeatedly

- First line ends with a `:`

- In each iteration, the running variable is bound to a new value

- Loop body with one or several lines is indented by 4 spaces

<br/>
<br/>
<br/>
<br/>
<br/>

</div>
</div>



---

# Looping over lists and tuples



<div class="grid grid-cols-2 gap-4">
<div>

```python
>>> names = ["Guy", "Ray", "Tim"]
>>> for name in names:
...     print(name.lower())
'guy'
'ray'
'tim'
```

</div>
<div>

- Looping over lists and tuples works in the same way

- Running variable is iteratively bound to the iterable's elements

- Try to choose a good name for the running variable!

</div>
</div>


---

# Looping over dictionaries

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
>>> letter_to_position = {
...     "a": 0,
...     "b": 1,
...     "c": 2,
... }

>>> for let in letter_to_position:
...     print(let)
a
b
c

>>> for let, pos in letter_to_position.items():
...     print(let, pos)
a 0
b 1
c 2
```

</div>
<div class="col-span-2">

<br/>
<br/>
<br/>
<br/>
<br/>

- By default you loop over dictionary keys

<br/>
<br/>


- Use `.items()` for looping over key/value pairs

</div>
</div>
