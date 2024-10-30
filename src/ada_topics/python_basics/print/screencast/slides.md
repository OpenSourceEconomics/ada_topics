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

### The print function

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Displaying results to the screen

- So far, used functionality of Jupyter Notebooks:

  Return value of the last statement in a cell is displayed below, unless it is assigned
  to a variable

- Limited to Notebooks and a single output

- `print()` is more versatile

---

# Simple usage of print()

`print()` displays arguments, separated by a space

```python
[1] print("Capacity")
[1] Capacity

[2] print("Capacity:", 2123)
[2] Capacity: 2123

[3] print("Capacity:", 2123, "TEU")
    print("Current load:", 1893, "Containers")
[3] Capacity: 2123 TEU
    Current load: 1893 Containers
```

<br/>
<br/>

---

# Two keyword arguments: sep, end

- `sep` specifies the separator between arguments (default: space)
- `end` specifies the end of the output (default: newline `\n`)

<br/>

```python
[1] print("Alice", "Bob", "Charlie", sep=", ", end=".\n")
[1] Alice, Bob, Charlie.


[2] print("Alice", "Bob", "Charlie", sep="\n")
[2] Alice
    Bob
    Charlie

```

<br/>
<br/>
