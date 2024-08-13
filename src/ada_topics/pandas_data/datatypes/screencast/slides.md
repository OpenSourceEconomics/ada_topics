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
title: Applied Data Analytics
defaults:
  layout: center
---

### Applied Data Analytics

<br>

# Data management with pandas

### Data types

<br>

Hans-Martin von Gaudecker

---

# Overview

- Why different data types?
- Converting to useful dtypes
- Overview of numeric dtypes
- Categoricals vs strings
- Working with categoricals

---

# PIAAC example data

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>gender</th>
      <th>hours_per_week</th>
      <th>programming_at_work</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Netherlands</td>
      <td>Female</td>
      <td>32.0</td>
      <td>Less than once a week but at least once a month</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Netherlands</td>
      <td>Female</td>
      <td>36.0</td>
      <td>Less than once a month</td>
    </tr>
    <tr>
      <th>2</th>
      <td>United States</td>
      <td>Male</td>
      <td>40.0</td>
      <td>Every day</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Germany</td>
      <td>Male</td>
      <td>53.0</td>
      <td>Less than once a month</td>
    </tr>
    <tr>
      <th>4</th>
      <td>United States</td>
      <td>Female</td>
      <td>45.0</td>
      <td>At least once a week but not every day</td>
    </tr>
  </tbody>
</table>

---

# The need for different data types

<div class="grid grid-cols-2 gap-12">
<div>

```python
[1] df.dtypes

[1] country                string[python]
    gender                 string[python]
    hours_per_week                float32
    programming_at_work    string[python]
    dtype: object
```

</div>
<div>

<br/>
<br/>

- Each column has a dtype
- dtypes are not always set optimally after loading data

</div>
</div>

---

# Benefits of good type representation

- Access to operations that are only relevant for some types
- Statistical packages work best with correct dtypes
- Better formatting results tables
- Easier visualisation

---

# Converting to useful dtypes

<div class="flex">
<div>

```python
[1] better_dtypes = {
        "country": pd.CategoricalDtype(),
        "gender": pd.CategoricalDtype(),
        "hours_per_week": pd.UInt64Dtype(),
        "programming_at_work": pd.CategoricalDtype(),
    }
    df = df.astype(better_dtypes)
    df.dtypes

[1] country                category
    gender                 category
    hours_per_week           UInt64
    programming_at_work    category
    dtype: object
```

</div>
<div>

<br/>
<br/>

- Depending on how you load your data, the dtypes are not set optimally
- If so, you can create a dictionary that maps columns to the dtypes you want

</div>
</div>

---

# Overview of numeric dtypes

| Type                | Properties               |
| ------------------- | ------------------------ |
| `pd.BooleanDtype()` | `True`, `False`, `pd.NA` |
| `pd.Int*Dtype()`    | Integers                 |
| `pd.UInt*Dtype()`   | 0 and positive integers  |
| `pd.Float*Dtype()`  | Floating point numbers   |

---

# Categorical vs. String

- `pd.CategoricalDtype()` is for data that takes values in a fixed and relatively
  small set of categories
  - Internally stored as small integers
  - Simple relabeling / resorting of categories

- `pd.StringDtype()` is for actual text data
  - String functions similar to methods of Python strings

---

# Working with categoricals

<div class="flex gap-12">
<div>

```python
[1] cat_type = pd.CategoricalDtype(
        categories=[
          "low", "middle", "high"
        ],
        ordered=True,
    )
    pd.Series(
        ["low", "high", "high"],
        dtype=cat_type,
    )
[1] 0     low
    1    high
    2    high
    dtype: category
    Categories (3, string):
       [low < middle < high]
```

</div>
<div>

<br/>

- Categories are defined independent of data
  - Protection against invalid categories
  - Good for visualization!
- Note: In PIAAC example we got data-dependent categories
- `sr.cat` accessor provides access to methods
- See [this tutorial](https://pandas.pydata.org/docs/user_guide/categorical.html)
  for more methods

</div>
</div>
