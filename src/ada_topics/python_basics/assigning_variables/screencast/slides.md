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

### Assigning variables

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- Assigning variables
- Using Python like a calculator
- Comparing variables

---

### Assigning variables

<div class="flex gap-12">
<div>

```python
[1] a = 3
    a
[1] 3

[2] a = 3.1415
    a
[2] 3.1415

[2] a = "Hello world"
    a
[2] "Hello world"

```


</div>
<div>

<br>
<br>
<br>

- Variables are assigned with a single `=` sign
- You can re-assign variables with different values

</div>
</div>


---

# Python as a calculator

<div class="flex gap-8">
<div>

```python
[1] a = 3
    b = 3.1415
    b / a
[1] 1.0471666666666668

[2] (a + b) * 3
[2] 18.424500000000002

[3] a**b
[3] 31.54106995953402

```

</div>
<div>

<br>
<br>
<br>

- Arithmetic works as you would expect
- Brackets work as expected
- `**` is exponentiation (not `^`)

</div>
</div>


---

# Comparisons

<div class="flex gap-8">
<div>

```python
[1] a = 3
    b = 3
    a == b
[1] True

[2] a < b
[2] False

[3] a >= b
[3] True

[2] a != b
[2] False
```

</div>
<div>

<br>
<br>

- Comparison operators are `==`, `<`, `>`, `<=`, `>=`, `!=`
- Remember:
  - `=` is used for assignment
  - Classic error is trying to use it for comparison
- You cannot compare any two variables
  - e.g. "two" < 3 will return an error
  - More on this in the lecture on scalar types

</div>
</div>
