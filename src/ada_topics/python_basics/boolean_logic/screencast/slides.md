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

# Boolean logic

- George Boole (1815-1864)
- Basis of all things programming: Will define
- Define conditions (true or false) and combine them

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

[4] a != b
[4] False
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


---


# Truth Table

| `a`   | `b`   | not `a` | `a` and `b` | `a` or `b` |
| ----- | ----- | ------- | ----------- | ---------- |
| True  | True  | False   | True        | True       |
| True  | False | False   | False       | True       |
| False | True  | True    | False       | True       |
| False | False | True    | False       | False      |
