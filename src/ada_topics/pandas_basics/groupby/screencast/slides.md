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
marp: true
---

## Applied Data Analytics

<br>

# Pandas basics

### Grouping DataFrames by rows

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Grouped data is required all the time

- size of groups
- aggregate group differences in other variables
- stratified sampling of individuals

---

# Example: PIAAC data

| country     | age_group  | use_computer_at_work | programs_monthly |
| :---------- | :--------- | -------------------: | ---------------: |
| Germany     | Aged 30-34 |                0.776 |            0.079 |
|             | Aged 55-59 |                0.679 |            0.035 |
| Netherlands | Aged 30-34 |                0.872 |            0.096 |
|             | Aged 55-59 |                0.802 |            0.028 |

<br/>

- Index: `country`, `age_group`
- Float columns: `use_computer_at_work`, `programs_monthly`
- _(Already grouped)_ — Goal: Broaden groups, calculate statistics

---

# Calculating grouped values: Two steps

1. Generate a grouped object

2. Perform an operation on that

<br/>

Resulting object will be a DataFrame (_almost always of smaller size_).

---

# Calculating means by country

```python
[1] df.groupby("country")
[1] <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f6da889ba50>

[2] df.groupby("country").mean()
```

<br/>

| age_group  | use_computer_at_work | programs_monthly |
| :--------- | -------------------: | ---------------: |
| Aged 30-34 |                0.824 |            0.088 |
| Aged 55-59 |                 0.74 |            0.031 |

---

# Calculating standard dev's by age group

```python
[1] df.groupby("age_group")

[1] <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f6da88b5d90>

[2] df.groupby("age_group").std()
```

| age_group  | use_computer_at_work | programs_monthly |
| :--------- | -------------------: | ---------------: |
| Aged 30-34 |                0.067 |            0.012 |
| Aged 55-59 |                0.087 |            0.005 |

---

# Important methods on _groupby_-objects

| Method            | Description                        | Applies to               |
| ----------------- | ---------------------------------- | ------------------------ |
| mean              | Averages                           | floats, (ints)           |
| std               | Standard deviation                 | floats, (ints)           |
| median / quantile | Quantiles                          | floats, ints             |
| min / max         | Minimum / Maximum                  | anything that is ordered |
| count             | Number of non-missing observations | any                      |
| value_counts      | Number of observations per value   | categorical, (ints)      |
| apply             | Pass your own function             | depends                  |

**Semantics may change depending on whether you pass one or more columns!**
