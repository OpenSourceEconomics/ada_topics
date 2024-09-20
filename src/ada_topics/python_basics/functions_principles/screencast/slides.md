---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Econometrics (BSc)
drawings:
  persist: false
transition: fade
title: Econometrics (BSc)
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Econometrics (BSc)

<br/>

# Basic Python

### Principles for Good Functions

<br/>


Hans-Martin von Gaudecker

---

# Contents

- Why functions are important!

- Guidelines for self-contained functions

  - Pass all variables you want to use inside

  - Do not modify mutable arguments

---

# Why functions are important

- Help to re-use code and avoid duplication

- Help to structure code and reduce cognitive load

- Make individual code snippets testable

---

# Pass all variables you want to use inside

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
# bad example
[1] global_msg = "Hello {}!"

[1] def greet_with_global(name):
...     print(global_msg.format(name))

[1] greet_with_global("Guido")
Hello Guido!
```

</div>
<div class="col-span-2">

- Inside a function you have access to variables in the enclosing scope

- This is dangerous because the behaviour of the function now depends on global
  variables

- Do not use this in your code!


</div>
</div>


---

# Pass all variables you want to use inside

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
# solution 1: define inside function
[1] def greet(name):
...     msg = "Hello {}!
...     print(msg.format(name))
[1] greet("Guido")
Hello Guido!

# solution 2: pass as argument
[1] def greet_explicit(name, msg):
...     print(msg.format(name))

[1] greet_explicit("Guido", "Hello {}!")
Hello Guido!
```


</div>
<div class="col-span-2">

- Inside a function you have access to variables in the enclosing scope

- This is dangerous because the behaviour of the function now depends on global
  variables

- Do not use this in your code!

</div>
</div>


---

# Do not modify mutable arguments

<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] def append_4(some_list):
...     some_list.append(4)
...     return some_list

[2] a = [1, 2, 3]

[3] b = append_4(a)

[4] b
[1, 2, 3, 4]

[5] a
[1, 2, 3, 4]
```

</div>
<div>

- Arguments are passed without making a copy

- Make sure that functions do not modify mutable arguments!

  - Make copies

  - Avoid changing objects in the first place

</div>
</div>


---

# Do not modify mutable arguments

<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] def append_4(some_list)
...     out = some_list.copy()
...     out.append(4)
...     return out

[2] a = [1, 2, 3]

[3] b = append_4(a)

[4] b
[1, 2, 3, 4]

[5] a
[1, 2, 3]

```

</div>
<div>


- Arguments are passed without making a copy

- Make sure that functions do not modify mutable arguments!

  - Make copies

  - Avoid changing objects in the first place

</div>
</div>
