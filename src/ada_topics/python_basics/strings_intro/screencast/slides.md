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

### Strings: A very basic introduction

Hans-Martin von Gaudecker and Aapo Stenhammar

---

## Contents

- What are strings and how to define them
- Main operations with strings
- Main methods of strings

---

### What are strings and how to define them

<div class="flex gap-6">
<div>
<br>
<br>

```python
[1] a = 'hello world'
    a
[1] 'hello world'

[2] b = "1.0"
    b
[2] '1.0'

[3] type(b)
[3] str
```
</div>
<div>

- Strings are used to represent text
- A string can store any alphanumeric character
- You can define a string variable by using "" or ''
- You can set the type of a variable as *string* using the str() function.
  However, this is not very common

</div>
</div>

---

### Main operations with strings

<div class="flex gap-6">
<div>

```python
[1] a = "Hello"
    b = " "
    c = "world"
    a + b + c
[1] "Hello world"

[2] d = "hello"
    a == d
[2] False
```
</div>
<div>
<br>
<br>

- You can concatenate strings using the "+" operator
- You can compare strings with the "==" and "!=" operators

</div>
</div>

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
  You can find a list (here)[https://www.w3schools.com/python/python_ref_string.asp].
- The most common methods are:
  - str.capitalize() - This makes the first character in the string uppercase
  - str.upper() - This makes all the letters in the string uppercase
  - str.lower() - This makes all the letters in the string lowercase
</div>
</div>
