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

### Defining Functions

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar


---

# Example: OECD equivalence scale

$$
\text{weight}_\text{hh} = 1 + 0.5 \cdot (N_\text{adults} + N_\text{youth} - 1) + 0.3 \cdot N_\text{kids}
$$



---

# Anatomy of Python functions


<img src="/function_anatomy.png" class="rounded" width="700"/>


- Start with the `def` keyword

- Name is `lowercase_with_underscores`

- There can be one or several parameters (a.k.a. arguments)

- Function body is indented by 4 spaces, can have one+ lines

- Inside the body you can do everything you have seen so far!

<br/>

---

# Example: OECD equivalence scale

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
[1] def oecd_scale(n_adults, n_youth, n_kids):
        tmp = n_adults + n_youth - 1
        return 1 + 0.5 * tmp + 0.3 * n_kids

[2] oecd_scale(1, 0, 0)
[2] 1.0

[3] oecd_scale(2, 1, 1)
[3] 2.3

[4] oecd_scale(n_adults=2, n_youth=1, n_kids=1)
[4] 2.3

```

</div>
<div class="col-span-2">

- Function calls work with positional and keyword arguments

- Pass keyword arguments for any function with more than one argument!


</div>
</div>
