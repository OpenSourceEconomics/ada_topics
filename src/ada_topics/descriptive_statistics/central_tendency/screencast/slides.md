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

### Measures of Central Tendency: Mean, Mode and Median

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

### Example Data

TODO: Make the median and mode different; add final slides.

| Observation | Value |
| ----------- | ----- |
| 0           | 1     |
| 1           | 1     |
| 2           | 1.5   |
| 3           | 1.5   |
| 4           | 2.5   |
| 5           | 1     |
| 6           | 0.5   |
| 7           | 2     |
| 8           | 2.5   |

<!--Would be ideal to use some actual data, but no more than 5 obs and need repeated value for mode -->
<!-- I think with 5 obs. there is not a very interesting histogram we can plot... -->

---

### Mode

<div class="grid grid-cols-2 gap-4">
<div>

<img src="mode.png" class="rounded" style="width: 85%; height: 85%; margin: auto"/>

</div>
<div>

<br>

- **Intuition**: the mode is _the value that appears most frequently in the data_.

- If more values appear with the same frequency, the data is _multimodal_.

- If no value appears more than once, the data has _no mode_.

- The mode can be computed for any type of data (numerical, ordinal, and categorical).

- In our case, the mode is 1.

</div>
</div>

---

### Median


<div class="grid grid-cols-2 gap-4">
<div>

<img src="median.png" class="rounded" style="width: 85%; height: 85%; margin: auto"/>

</div>
<div>

<br>

- **Intuition**: the median is _the value that separates the higher half from the lower half of the data_.

- To compute the median sort the data and find the _middle value_ (what happens if the values
  are an even number?).

- Can be computed for any type of _ordered_ data (numerical and ordinal).

- In our case, the median is 1.5.

</div>
</div>

---

### Median: alternative explanation

<div class="grid grid-cols-2 gap-4">
<div>

| Observation | Value |
| ----------- | ----- |
| 6           | 0.5   |
| 0           | 1     |
| 1           | 1     |
|    5        | 1     |
| **2**           | **1.5**   |
| 3           | 1.5   |
| 7           | 2     |
| 4           | 2.5   |
| 8           | 2.5   |

</div>
<div>


- **Intuition**: the median is _the value that separates the higher half from the lower half of the data_.

- To compute the median sort the data and find the _middle value_ (what happens if the values
  are an even number?).

- Can be computed for any type of _ordered_ data (numerical and ordinal).

- In our case, the median is observed at the 5th position, which is 1.5.

</div>
</div>

---

### Mean


- The **mean** is _the sum of all the values in the sample divided by the total number of
  values_.

- In our case, it is computed by:

    $$
    \text{mean} = \frac{1 + 1 + 1.5 + 1.5 + 2.5 + 1 + 0.5 + 2 + 2.5}{9} = 1.5
    $$

- Can be computed *only* for numerical data.

- The mean is more sensitive to outliers than the median and the mode. Why?

---

### Mean vs Median and Mode: sensitivity to outliers.

- The mean is more sensitive to outliers than the median and the mode.

- Imagine to add an observation with value 1000 to our data.

- The mean changes to 113.5, while the median and the mode remain the same (1.5 and 1).

---

| Statistic | Sensitivity to outliers | Type of data | Aggregation to higher level |
| --------- | ----------------------- | ------------ | --------------------------- |
| Mean      | High                    | Numerical    | Sum of all values / N |
| Median    | Low                     | Numerical, ordinal | Middle value |
| Mode      | Low                     | Numerical, ordinal, categorical | Most frequent value |

---
