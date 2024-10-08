---
theme: academic
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Applied Data Analytics, Winter Term 2024/2025
drawings:
  persist: false
transition: fade
defaults:
  layout: center
---

## Applied Data Analytics

<br>

# Sample Statistics: Mean, Mode and Median

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar


---

# Series of Data

- Data can often be represented as a collection of observations of a variable.

- For example, think of the heights of students in a class. Call this variable $X$, and
let $X_1, X_2, \ldots, X_N$ be the heights of the students in the class (who are a total
of $N$ students).

- We can think of this as a dataset, or in statistical notation, a sample of size $N$.

---

# Representing a Series of Data

<!-- maybe this part is more for the histogram part?-->

---

# Sample Statistics

- Previous lecture: describe the data using a histogram.

- There are more succinct ways to describe the data. One of the most common ways is to
use *sample statistics*.

- A *sample statistic* is any number computed as a function of the values in the sample
    (the data).

- We will look at: *mean*, *mode*, and *median*.

---

# Mean

- The most commonly used.

- Defined as:
    $$
    \bar{X} = \frac{1}{N} \sum_{i=1}^N X_i
    $$

- The mean is *the sum of all the values in the sample divided by the total number of
    values*.

- Can be computed *only* for numerical data. Why?

---

# Median

- Intuitively, the median is the value that separates the higher half from the lower half
    of the data.

- To compute the median:
    1. Sort the data.
    2. If the number of observations is odd, the median is the middle value.
    3. If the number of observations is even, the median is the average of the two middle
        values.

- It can be computed for any type of *ordered* data (so numerical and ordinal data).

- Example with an histogram...

---

# Mode

- The mode is the value that appears most frequently in the data.

- A dataset can have multiple modes, or no mode at all. Examples with histograms.

- The mode can be computed for any type of data (numerical, ordinal, and categorical).

---

# Differences between Mean and Median...

- Classic example of mean vs median income changes over the years?
- Hint at the idea that the mean is more sensitive to outliers than the median.
- Hint at the fact that averages are more precise if you have many people.
