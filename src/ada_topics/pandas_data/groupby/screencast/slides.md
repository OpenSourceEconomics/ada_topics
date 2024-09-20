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
---

### Econometrics (BSc)

<br>

# Data management with pandas

### Splitting DataFrames into groups

<br>

Hans-Martin von Gaudecker

---

# Grouped data is required all the time

- size of groups
- aggregate group differences in other variables
- stratified sampling of individuals

---

# Example

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>use_computer_at_work</th>
      <th>programs_monthly</th>
    </tr>
    <tr>
      <th>country</th>
      <th>age_group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Germany</th>
      <th>Aged 30-34</th>
      <td>0.776498</td>
      <td>0.07943</td>
    </tr>
    <tr>
      <th>Aged 55-59</th>
      <td>0.678756</td>
      <td>0.034765</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Netherlands</th>
      <th>Aged 30-34</th>
      <td>0.871728</td>
      <td>0.096154</td>
    </tr>
    <tr>
      <th>Aged 55-59</th>
      <td>0.801822</td>
      <td>0.028219</td>
    </tr>
  </tbody>
</table>

<br/>

- Index: `country`, `age_group`
- Float columns: `use_computer_at_work`, `programs_monthly`
- _(Already grouped)_ — Goal: Broaden groups, calculate statistics

---

# Calculating grouped values: Two steps

1. Generate a grouped object
2. Perform an operation on that

Resulting object will be a DataFrame (_almost always of smaller size_).

---

# Calculating means by country

```python
[1] df.groupby("country")

[1] <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f6da889ba50>

[2] df.groupby("country").mean()
```

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>use_computer_at_work</th>
      <th>programs_monthly</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Germany</th>
      <td>0.727627</td>
      <td>0.057097</td>
    </tr>
    <tr>
      <th>Netherlands</th>
      <td>0.836775</td>
      <td>0.062186</td>
    </tr>
  </tbody>
</table>

---

# Calculating standard dev's by age group

```python
[1] df.groupby("age_group")

[1] <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f6da88b5d90>

[2] df.groupby("age_group").std()
```

<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>use_computer_at_work</th>
      <th>programs_monthly</th>
    </tr>
    <tr>
      <th>age_group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Aged 30-34</th>
      <td>0.067338</td>
      <td>0.011826</td>
    </tr>
    <tr>
      <th>Aged 55-59</th>
      <td>0.087021</td>
      <td>0.004629</td>
    </tr>
  </tbody>
</table>

---

# Important methods on _groupby_-objects

| Method            | Description                        | Applies to               |
| ----------------- | ---------------------------------- | ------------------------ |
| mean              | Averages                           | floats, (ints)           |
| std               | Standard deviation                 | floats, (ints)           |
| median / quantile | Quantiles                          | floats, (ints)           |
| min / max         | Minimum / Maximum                  | anything that is ordered |
| count             | Number of non-missing observations | any                      |
| value_counts      | Number of observations per value   | categorical, (ints)      |
| apply             | Pass your own function             | depends                  |

**Semantics may change depending on whether you pass one or more columns!**
