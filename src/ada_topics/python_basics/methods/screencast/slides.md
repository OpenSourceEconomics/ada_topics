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

## Applied Data Analytics

<br>

# Python basics

### Methods

Hans-Martin von Gaudecker and Aapo Stenhammar

---

## Contents

- Methods basics
- String methods

---

### Methods basics

What is a method?
- A method is a function that is associated with an object.
- Methods are defined within a class. They can manipulate data of the object and perform operations.

Functions vs Methods
- Function: A block of reusable code that performs a specific task.
- Method: A function that is defined inside a class and is called on an instance of the class.

How to call a method?
'object.method_name()'


---

# Main methods of strings

<div class="flex gap-8">
<div>

```python
[1] a = "hello"
    a.capitalize()
[1] 'Hello'

[2] a.upper()
[2] 'HELLO'

[3] b = "Hello Mr. 007 and Mss. X"
    b.lower()
[3] 'hello mr. 007 and mss. x'
```

</div>
<div>
<br>
<br>

- Strings have a number of methods.
  You can find a list [here](https://www.w3schools.com/python/python_ref_string.asp).
- The most common methods are:
  - str.capitalize() - This makes the first character in the string uppercase
  - str.upper() - This makes all the letters in the string uppercase
  - str.lower() - This makes all the letters in the string lowercase
</div>
</div>
