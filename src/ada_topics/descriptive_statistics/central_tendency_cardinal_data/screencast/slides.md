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

# Descriptive Statistics

### Measures of Central Tendency: Cardinal data

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Cardinal data

Example:

- Variable: Age in years

- Possible values: 0, 1, 2, ...

- Observed values: 18, 22, 19, 31

<br/>
<br/>

---

# Distribution

<center>
<img src="/age_bare.png" width=500>
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

# Distribution with median

<center>
<img src="/age_median.png" width=500>
</center>

<br/>
<br/>
<br/>



---

### Mean: Definition

The mean is _the sum of all the values in the sample divided by the total number of values_

$$
\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

### Mean: in practice

- Sum up all values and divide by the number of observations

- Is influenced by all observations, median only by the middle one(s)

<br/>
<br/>
<br/>

---

# Distribution with mean

<center>
<img src="/age_mean.png" width=500>
</center>

<br/>
<br/>
<br/>


---

# Distribution with median and mean

<center>
<img src="/age_median_mean.png" width=500>
</center>


<br/>
<br/>
<br/>




---

# Median and mean in pandas

<div class="grid grid-cols-7 gap-4">
<div class="col-span-3">

```python
[1] age.median()
[1] np.float64(20.5)

[2] age.mean()
[2] np.float64(22.5)

```

</div>
<div class="col-span-4">

- Just call methods with the respective name

- Median gives the average of the two middle values for even $N$

<br/>
<br/>
<br/>
</div>
</div>

---

### Median vs Median: sensitivity to outliers.

- The median is less sensitive to outliers than the mean.

- Reason is that it is influenced by all observations, while the median only by the
  middle one(s).

- Example: Observed values: 18, 22, 19, <span style="color:red;">22</span>

---

# Distribution

<center>
<img src="/age_other_bare.png" width=500>
</center>

<br/>
<br/>
<br/>


---

# Distribution with median and mean

<center>
<img src="/age_other_median_mean.png" width=500>
</center>

<br/>
<br/>
<br/>
