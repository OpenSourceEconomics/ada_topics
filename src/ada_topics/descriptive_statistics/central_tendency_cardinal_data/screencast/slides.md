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

# Descriptive Statistics

### Measures of Central Tendency: Cardinal data

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Cardinal data

Example:

- Variable: Age in years

- Possible values: 0, 1, 2, ...

- Observed values: 18, 22, 19, 29

<br/>
<br/>

---

# Distribution

<center>
<img src="/income_in_bins_bare.png" width=500>
</center>

<br/>
<br/>
<br/>




---

### Mode: Definition

The mode is the value that appears most frequently in the data.

### Mode: In practice

- Get a frequency distribution, take the maximum.
- Defined for any type of data (nominal, ordinal, cardinal).

### Mode: Corner cases

- If more values appear with the same highest frequency, the data is _multimodal_.
- If no value appears more than once, the data has _no mode_.



---

# Distribution with mode

<center>
<img src="/income_in_bins_mode.png" width=500>
</center>

<br/>
<br/>
<br/>

---


### Median: Definition

A value such that:
  - at least half of the observations are higher or equal than the value
  - at least half of the observations are lower or equal than the value

### Median: in practice

- Sort the data and find the _middle value_
- Even $N$ and distinct values at $N/2$ and $N/2 + 1$: Any value between the two, typically the average.
- Can be computed for any type of _ordered_ data (ordinal and cardinal).

<br/>
<br/>
<br/>

---

# Distribution with mode

<center>
<img src="/income_in_bins_median.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# Mode and median in pandas

<div class="grid grid-cols-7 gap-4">
<div class="col-span-3">

```python
[1] income.mode()
[1] 0    [0, 30,000)
    dtype: category


[2] income.median()
[2] TypeError: 'Categorical' with
    dtype category does not support
    reduction 'median'
```

</div>
<div class="col-span-4">

- Just call methods with the respective name

- Median only works for numerical data

- Reason is that it is not clear what should be returned if the
  median is not a category in the data.

<br/>
<br/>
<br/>
</div>
</div>
