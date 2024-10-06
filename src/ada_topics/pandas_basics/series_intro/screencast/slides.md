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

# Pandas

### Introduction to Series

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# What is a Series?

- A vector (one-dimensional array) of data with associated labels

- All elements have the same data type


<div class="grid grid-cols-2 gap-4">
<div>

Example

| Ship                  | Capacity |
| --------------------- | -------- |
| Laura Mærsk           | 1,926    |
| CMA CGM San Francisco | 6,956    |

</div>
<div>
</div>
</div>

<br/>
<br/>
<br/>

---

# How to create pd.Series

<div class="grid grid-cols-9 gap-4">
<div class="col-span-4">

```python
[1] pd.Series([2_100, 6_956])
[1] 0    2100
    1    6956
    dtype: int64




[2] pd.Series(
        [2_100, 6_956],
        name="capacity"
    )
[2] 0    2100
    1    6956
    Name: capacity, dtype: int64
```

</div>
<div class="col-span-5">

- Call `pd.Series()` with values in square brackets, separated by commas.

  Result: Unnamed Series with default index (consecutive integers starting at 0).

<br/>

- Set the `name` parameter to communicate the contents of the Series.

<br/>
<br/>
<br/>
<br/>
</div>
</div>

<br/>
<br/>

---

# How to create pd.Series (cont'd)

<div class="grid grid-cols-11 gap-4">
<div class="col-span-7">

```python
[3] pd.Series(
        [2_100, 6_956],
        index=["Laura Mærsk", "CMA CGM San Francisco"],
        name="capacity"
    )
[3] Laura Mærsk              2100
    CMA CGM San Francisco    6956
    Name: capacity, dtype: int64



[4] capacity = pd.Series(
        [2_100, 6_956],
        index=["Laura Mærsk", "CMA CGM San Francisco"]
    )
```

</div>
<div class="col-span-4">


- Set a meaningful `index` with values in square brackets, separated by
  commas.

  The number of elements must be the same as in the data.

- To continue working with the Series, assign it to a variable

</div>
</div>
