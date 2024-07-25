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

### Ordinal Data

Ordinal data is a categorical data type where
- the variables have natural, ordered categories and
- the distances between the categories are not known/defined

Examples of ordinal data are:
- Likert scale (e.g. strongly agree, agree, neither agree nor disagree, disagree, strongly disagree)
- Education level (e.g. primary education, secondary education, higher education)
- Any binned cardinal variable (e.g. low income (income lower than \$40k), middle income (income between \$40k and \$130k), high income (income above $130k))

---

### Example Data


| Observation | Value |
| ----------- | ----- |
| 0           | low income     |
| 1           | high income     |
| 2           | high income   |
| 3           | low income   |
| 4           | low income   |
| 5           | middle income     |
| 6           | low income   |
| 7           | middle income   |
| 8           | high income   |

<!--Would be ideal to use some actual data, but no more than 5 obs and need repeated value for mode -->
<!-- I think with 5 obs. there is not a very interesting histogram we can plot... -->

---

### Mode

- **Definition**: the mode is _the value that appears most frequently in the data_.

- If more values appear with the same highest frequency, the data is _multimodal_.

- If no value appears more than once, the data has _no mode_.

- The mode is computed by calculating the frequency of each possible realization and taking the most frequent one(s).

- The mode can be computed for any type of data (categorical, ordinal, and cardinal).

---


| Value | Frequency |
| ----------- | ----- |
| **low income**           |  **4**    |
| middle income           |   2   |
| high income           | 3   |


- In our case, the mode is *low income*.

---

### Median

- **Definition**: the median is the value such that:
  - at least half of the observations are higher or equal than the value
  - at least half of the observations are lower or equal than the value

- **Intuition**: the median is _the value that separates the higher half from the lower half of the data_.

- To compute the median sort the data and find the _middle value_ (what happens if the values are an even number?).

- Can be computed for any type of _ordered_ data (ordinal and cardinal).

---


| Observation | Value |
| ----------- | ----- |
| 0           | low income     |
| 3           | low income   |
| 4           | low income   |
| 6           | low income   |
| **5**          | **middle income**     |
| 7           | middle income   |
| 1           | high income     |
| 2           | high income   |
| 8           | high income   |

- In our case, the median is *middle income*.

---
