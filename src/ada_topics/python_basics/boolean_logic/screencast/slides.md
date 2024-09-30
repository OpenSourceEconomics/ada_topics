---
theme: academic
coverDate: ""
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

### Applied Data Analytics

<br/>

# Python Basics

### Boolean Logic

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

### Boolean logic

- George Boole (1815-1864)

- Basis of all things programming

- Define conditions (True or False) and combine them

<br>
<br>
<br>
<br>

---

### Comparisons

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

[4] a != b
[4] False
```

</div>
<div>

- Comparison operators are `==`, `<`, `>`, `<=`, `>=`, `!=`

- Remember:

  - `=` is used for assignment

  - Classic error is trying to use it for comparison

- You cannot compare any two variables

  - e.g. `"two" < 3` will return an error

<br>
<br>
<br>
<br>
<br>

</div>
</div>

---

### Truth Table

|       |       | not a | a and b | a or b |
| ----- | ----- | ----- | ------- | ------ |
| **a** | **b** |       |         |        |
| ✅    | ✅    | ❌    | ✅      | ✅     |
| ✅    | ❌    | ❌    | ❌      | ✅     |
| ❌    | ✅    | ✅    | ❌      | ✅     |
| ❌    | ❌    | ✅    | ❌      | ❌     |

<br>
<br>
<br>
<br>
