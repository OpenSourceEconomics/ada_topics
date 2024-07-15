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

# Sample Statistics: Mean, Mode and Median

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

# Series of Data

*Great idea -- but let's move to a different screencast of how we think about data*

- Example: ...
- Def: Anything that can be measured (?)
- Math: Notation typically $$x_i$$, $$x_{k,i}$$ etc.
- Computer Science: Arrays, lists, **dataframes**, etc.
- Human eye / mind: Tables and plots

Objective: Understand all these are ways to represent the same thing

*Chapter for this is not obvious! "Background" or so?*

- Data can often be represented as a collection of observations of a variable.

- For example, think of the heights of students in a class. Call this variable $X$, and
  let $X_1, X_2, \ldots, X_N$ be the heights of the students in the class (who are a
  total of $N$ students).

- We can think of this as a dataset, or in statistical notation, a sample of size $N$.

---

# Representing a Series of Data

<!-- maybe this part is more for the histogram part?-->

---

# Sample Statistics

- Previous lecture: describe the data using a histogram.

- There are more succinct ways to describe the data. One of the most common ways is to
  use _sample statistics_.

- A _sample statistic_ is any number computed as a function of the values in the sample
  (the data).

- We will look at: _mean_, _mode_, and _median_.

---

# Mean

- The most commonly used.

- Defined as:

  $$
  \bar{X} = \frac{1}{N} \sum_{i=1}^N X_i
  $$

- The mean is _the sum of all the values in the sample divided by the total number of
  values_.

- Can be computed _only_ for numerical data. Why?

---

# Median

- Intuitively, the median is the value that separates the higher half from the lower half
  of the data.

- To compute the median:

  1. Sort the data.
  2. If the number of observations is odd, the median is the middle value.
  3. If the number of observations is even, the median is the average of the two middle
     values.

- It can be computed for any type of _ordered_ data (so numerical and ordinal data).

- Example with an histogram...

---

# Mode

- The mode is the value that appears most frequently in the data.

- A dataset can have multiple modes, or no mode at all. Examples with histograms.

- The mode can be computed for any type of data (numerical, ordinal, and categorical).

---

# Differences between Mean and Median: how they can be used to BS.

- Classic example of mean vs median income changes over the years?
