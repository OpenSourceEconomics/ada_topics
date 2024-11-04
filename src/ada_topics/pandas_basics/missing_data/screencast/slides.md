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

### Missing data

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# No income data for Bob and Derek

<div class="grid grid-cols-3 gap-4">
<div>
</div>
<div>

| Name    | Income |
| :------ | :----- |
| Alice   | 3000.0 |
| Bob     |        |
| Charlie | 5000.0 |
| Derek   |        |

<br/>
<br/>
<br/>

</div>
<div>
</div>
</div>

---

# Use pd.NA, take missings into account

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```python
[1] income = pd.Series(
        data=[3000.0, pd.NA, 5000.0, pd.NA],
        index=["Alice", "Bob", "Charlie", "Derek"],
        name="Income",
    )
    income

[1] Alice      3000.0
    Bob          <NA>
    Charlie    5000.0
    Derek        <NA>
    Name: Income, dtype: object
```
<br/>
<br/>
<br/>

</div>
<div class="col-span-2">

```python
[2] income.value_counts()
[2] 3000.0    1
    5000.0    1
    Name: count, dtype: int64

[3] income.value_counts(
      dropna=False
    )
[3] <NA>      2
    3000.0    1
    5000.0    1
    Name: count, dtype: int64
```
</div>
</div>


---

# Check for (non-)missing values

<div class="grid grid-cols-2 gap-20">
<div>

```python
[4] income.isna()

[4] Alice      False
    Bob         True
    Charlie    False
    Derek       True
    Name: Income, dtype: bool
```

<br/>
<br/>
<br/>
</div>
<div>

```python

[5] income.notna()

[5] Alice       True
    Bob        False
    Charlie     True
    Derek      False
    Name: Income, dtype: bool
```

<br/>
<br/>
<br/>
</div>
</div>

---

# Explicitly exclude missing data

```python
[6] income.loc[income.notna()]

[6] Alice      3000.0
    Charlie    5000.0
    Name: Income, dtype: object
```
<br/>
<br/>
<br/>

---

# Fill one value with missing data

```python
[7] income.loc["Bob"] = 1000.0
    income

[7] Alice      3000.0
    Bob        1000.0
    Charlie    5000.0
    Derek        <NA>
    Name: Income, dtype: object
```

This changes the existing Series.

---

# Fill all values with missing data

```python
[8] income_imputed = income.fillna(2000.0)
    income_imputed

[8] Alice      3000.0
    Bob        1000.0
    Charlie    5000.0
    Derek      2000.0
    Name: Income, dtype: object

[9] income

[9] Alice      3000.0
    Bob        1000.0
    Charlie    5000.0
    Derek        <NA>
    Name: Income, dtype: object

```

The existing Series is unchanged.
