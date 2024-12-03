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

# Pandas basics

### Merging Series / DataFrames

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Same units, different sources

- Country data on life expectancy and GDP per capita

- Annual data on life expectancy and countries' distance from the equator

- Individuals' occupational classifications and labels thereof

→ Combine data from different sources into various colums of a single DataFrame

---

# Merging on the index

<div class="grid grid-cols-2 gap-60">
<div>

| country | year | lifeExp |
| :------ | ---: | ------: |
| Cuba    | 2002 |  77.158 |
| Cuba    | 2007 |  78.273 |
| Spain   | 2002 |   79.78 |
| Spain   | 2007 |  80.941 |

  <br/>
</div>
<div>

| country | year | gdpPercap |
| :------ | ---: | --------: |
| Cuba    | 2002 |   6340.65 |
| Cuba    | 2007 |    8948.1 |
| Spain   | 2002 |   24835.5 |
| Spain   | 2007 |   28821.1 |

  <br/>
</div>
</div>

<div class="grid grid-cols-7 gap-0">
<div>
</div>
<div>
</div>
<div>
  <br/>

| country | year | lifeExp | gdpPercap |
| :------ | ---: | ------: | --------: |
| Cuba    | 2002 |  77.158 |   6340.65 |
| Cuba    | 2007 |  78.273 |    8948.1 |
| Spain   | 2002 |   79.78 |   24835.5 |
| Spain   | 2007 |  80.941 |   28821.1 |

  <br/>
  <br/>
</div>
</div>

---

# Syntax

- `life_exp` holds a Series or DataFrame with data on life expectancy

- `gdp_pc` holds a Series or DataFrame with data on GDP per capita

- Both have the same index, `country` and `year`

<br/>
<div class="flex">
<div>

```python
df = pd.merge(left=life_exp, right=gdp_pc, left_index=True, right_index=True)
```

</div>
</div>

---

# Merging Series / DataFrames on columns

<div class="grid grid-cols-2 gap-60">
<div>

|    | country   |   year |   lifeExp |
|:---|:----------|-------:|----------:|
| A  | Cuba      |   2002 |    77.158 |
| B  | Cuba      |   2007 |    78.273 |
| C  | Spain     |   2002 |    79.78  |
| D  | Spain     |   2007 |    80.941 |

  <br/>
</div>
<div>

|    | country   |   year |   gdpPercap |
|---:|:----------|-------:|------------:|
|  5 | Cuba      |   2002 |     6340.65 |
|  9 | Cuba      |   2007 |     8948.1  |
|  3 | Spain     |   2002 |    24835.5  |
|  1 | Spain     |   2007 |    28821.1  |

  <br/>
</div>
</div>

<div class="grid grid-cols-7 gap-0">
<div>
</div>
<div>
</div>
<div>
  <br/>

|    | country   |   year |   lifeExp |   gdpPercap |
|---:|:----------|-------:|----------:|------------:|
|  0 | Cuba      |   2002 |    77.158 |     6340.65 |
|  1 | Cuba      |   2007 |    78.273 |     8948.1  |
|  2 | Spain     |   2002 |    79.78  |    24835.5  |
|  3 | Spain     |   2007 |    80.941 |    28821.1  |


  <br/>
  <br/>
</div>
</div>

---

# Syntax

- `life_exp` holds a DataFrame with `country`, `year`, `lifeExp`

- `gdp_pc` holds a DataFrame with `country`, `year`, `gdpPercap`

- Both indices do not matter and will be discarded

<br/>

<div class="grid grid-cols-2 gap-0">
<div class="flex">
<div>

```python
df = pd.merge(
    left=life_exp,
    right=gdp_pc,
    left_on=["country", "year"],
    right_on=["country", "year"],
)
```

</div>
</div>
<div class="flex">
<div>

```python
df = pd.merge(
    left=life_exp,
    right=gdp_pc,
    on=["country", "year"],
)
```

</div>
</div>
</div>


---

# What if not all data are present?

<div class="grid grid-cols-2 gap-60">
<div>

| country   |   year |   lifeExp |
|:----------|-------:|----------:|
| Cuba      |   2002 |    77.158 |
| Cuba      |   2007 |    78.273 |
| Spain     |   2002 |    79.78  |

  <br/>
</div>
<div>

| country   |   year |   gdpPercap |
|:----------|-------:|------------:|
| Cuba      |   2007 |      8948.1 |
| Spain     |   2002 |     24835.5 |
| Spain     |   2007 |     28821.1 |

  <br/>
</div>
</div>

<div class="grid grid-cols-3 gap-5">
<div>

<br/>

```python

df = pd.merge(
    left=life_exp,
    right=gdp_pc,
    on=["country", "year"],
    how="outer",
)
```

</div>
<div>
  <br/>

| country   |   year |   lifeExp |   gdpPercap |
|:----------|-------:|----------:|------------:|
| Cuba      |   2002 |    77.158 |             |
| Cuba      |   2007 |    78.273 |      8948.1 |
| Spain     |   2002 |    79.78  |     24835.5 |
| Spain     |   2007 |           |     28821.1 |

  <br/>
  <br/>
</div>
</div>


---

# The how keyword to merging

- `how="inner"`: only rows with matching keys in both DataFrames

- `how="left"`: all rows from the left DataFrame

- `how="right"`: all rows from the right DataFrame

- `how="outer"`: all rows from both DataFrames


---

# Many-to-one merges

<div class="grid grid-cols-2 gap-60">
<div>

| country   |   year |   lifeExp |
|:----------|-------:|----------:|
| Cuba      |   2002 |    77.158 |
| Cuba      |   2007 |    78.273 |
| Spain     |   2002 |    79.78  |
| Spain     |   2007 |    80.941 |

  <br/>
</div>
<div>

| country   | capital   |
|:----------|:----------|
| Cuba      | Havana    |
| Spain     | Madrid    |

  <br/>
</div>
</div>

<div class="grid grid-cols-3 gap-5">
<div>

<br/>

```python
df = pd.merge(
    left=life_exp,
    right=cap,
    left_index=True,
    right_index=True,
)
```

</div>
<div>
  <br/>

| country   |   year |   lifeExp | capital   |
|:----------|-------:|----------:|:----------|
| Cuba      |   2002 |    77.158 | Havana    |
| Cuba      |   2007 |    78.273 | Havana    |
| Spain     |   2002 |    79.78  | Madrid    |
| Spain     |   2007 |    80.941 | Madrid    |


  <br/>
  <br/>
</div>
</div>

---

# Types of merges

"Index" refers to what the index should be

- 1:1 — index levels of both DataFrames are the same

- m:1 — The left DataFrame's index levels are a strict superset of the right DataFrame's index levels

- 1:m — The right DataFrame's index levels are a strict superset of the left DataFrame's index levels

- m:m — Both DataFrames overlap in a strict subset of both index levels
