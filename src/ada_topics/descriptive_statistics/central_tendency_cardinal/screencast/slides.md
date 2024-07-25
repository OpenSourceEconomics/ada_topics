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

| Observation | GDP per capita ($)|
| ----------- | ----- |
| Argentina           | 13,731   |
| Bolivia           | 3,701   |
| Brazil           | 10,044   |
| Chile           | 17,093   |
| Colombia           | 6,980   |
| Ecuador           | 6,533   |
| Panama           | 18,662   |
| Paraguay           | 6,260   |
| Peru           | 7,790   |

---

### Mode

- **Definition**: the mode is _the value that appears most frequently in the data_.

- If more values appear with the same highest frequency, the data is _multimodal_.

-  If no value appears more than once, the data has _no mode_.

- The mode can be computed for any type of data (categorical, ordinal, and cardinal).

- In our case, there is no mode.

---

### Median

<div class="grid grid-cols-2 gap-4">
<div>

| Observation | GDP per capita ($) |
| ----------- | ----- |
| Bolivia           | 3,701    |
| Paraguay           | 6,260    |
| Ecuador           | 6,533    |
| Colombia        | 6,980    |
| Peru           | **7,790**   |
| Brazil           | 10,044    |
| Argentina           | 13,731    |
| Chile           | 17,093    |
| Panama           | 18,662    |

</div>
<div>


- **Intuition**: the median is _the value that separates the higher half from the lower half of the data_.

- To compute the median sort the data and find the _middle value_ (what happens if the values
  are an even number?).

- Can be computed for any type of _ordered_ data (numerical and ordinal).

- In our case, the median is observed at the 5th position, which is $7,790.

</div>
</div>

---

### Mean

  - **Definition**: The mean is _the sum of all the values in the sample divided by the total number of
  values_.

- In our case, it is computed by:

    $$
    \text{mean} = \frac{13,731 + 3,701 + 10,044 + ...}{9} = 10,088
    $$

- Can be computed *only* for cardinal data.

- The mean is more sensitive to outliers than the median and the mode. Why?

---

### Mean vs Median and Mode: sensitivity to outliers.

- The mean is more sensitive to outliers than the median and the mode.

- Imagine Panama's GDP per capita increasing to $1,000,000.

- The mean changes to $119,125.77, while the median and the mode remain the same ($7,790 and no mode).

---

### Summary

| Statistic | Sensitivity to outliers | Type of data | Aggregation to higher level |
| --------- | ----------------------- | ------------ | --------------------------- |
| Mean      | High                    | Numerical    | Sum of all values / N |
| Median    | Low                     | Numerical, ordinal | Middle value |
| Mode      | Low                     | Numerical, ordinal, categorical | Most frequent value |
