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
marp: true
---

## Applied Data Analytics

<br>

# Pandas

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
    )income.isna()
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
[2] Income
    3000.0    1
    5000.0    1
    Name: count, dtype: int64

[3] income.value_counts(
      dropna=False
    )
[3] Income
    <NA>      2
    3000.0    1
    5000.0    1
    Name: count, dtype: int64
```
</div>
</div>


---

# Checking for (non-)missing values

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

# Explicitly excluding missing data

```python
[6] income.loc[income.isna()]

[6] Alice       True
    Bob        False
    Charlie     True
    Derek      False
    Name: Income, dtype: bool
```
