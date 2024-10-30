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
title: Applied Data Analytics
defaults:
  layout: center
---

### Applied Data Analytics

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

In the task where we are asked to create a series from scratch
(assignment 2, exercise 2.3), the following line

```python
pd.Series([1, 2, 3], labels=["a", "b", "c"])
```

gives me a type error:

```python
TypeError: Series.__init__() got an unexpected keyword argument 'labels'
```

I don't understand the error because all I am passing in are the values and their
associated labels. I have looked at the documentation of `pd.Series` and searched the
web, to no avail. Can you help me?

---

# A better way (continued)

Here is a minimal example to reproduce the error:

```python
import pandas as pd

pd.Series([1, 2, 3], labels=["a", "b", "c"])
```

I attach the entire traceback as a `.txt` file ...
