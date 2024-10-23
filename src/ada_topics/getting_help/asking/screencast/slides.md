---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Effective Programming Practices for Economists
drawings:
  persist: false
transition: fade
title: Effective Programming Practices for Economists
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Effective Programming Practices for Economists

<br/>

# Getting help

### Asking for help

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# How not to ask for help

- "I wanted to do the exercise but it does not work"
- "Jupyteach does not do anything"
- "My code does not work, here is a screenshot"

---

# What to keep in mind

- We do not remember what task 3 in exercise 5 is
- We like to see that you tried on your own
- We like to see that you tried to reduce the amount we have to read
- We love well formatted, self-contained examples


---

# A better way (for a hypothetical task)

In the task where we should use Python to calculate the output value of a Cobb-Douglas
production function (assignment 1, exercise 2) the following line:

```python
cobb_douglas(labor, capital, alpha)
```

gives me a type error:

```python
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'float'
```

I don't understand the error because I'm just passing in numbers.

---

# A better way (continued)

Here is a minimal example to reproduce the error:

```python
labor = 2.5,
capital = 4.5
alpha = 0.33

def cobb_douglas(labor, capital, alpha):
    return labor**alpha * capital**(1 - alpha)


cobb_douglas(labor, capital, alpha)
```

I attach the entire traceback as `txt` file ...
