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
- Any binned cardinal variable (e.g. low wealth (wealth lower than \$40k), middle wealth (wealth between \$40k and \$130k), wealth (wealth above $130k))

---

# Ordinal, non-numeric data

Example:

- Variable: Annual Income in Euros, binned

- Possible values: $[0, 30,000), [30,000, 60,000), [60,000, \infty)$

- Observed values: $[30,000, 60,000)$, $[0, 30,000)$, $[30,000, 60,000)$, $[0, 30,000)$,

---

# Distribution of observed income categories


<center>
<img src="/income_in_bins_bare.png" width=500>
</center>

<br/>
<br/>
<br/>




---

### Mode

- **Definition**: the mode is _the value that appears most frequently in the data_.

- If more values appear with the same highest frequency, the data is _multimodal_.

- If no value appears more than once, the data has _no mode_.

- The mode is computed by calculating the frequency of each possible realization and taking the most frequent one(s).

- The mode can be computed for any type of data (unordered, ordinal, and cardinal).

---

### Example Data

| GDP per capita (binned) | Frequency |
| ----------- | ----- |
| **low GDP per capita**           |  **4**    |
| middle GDP per capita           |   2   |
| high GDP per capita           | 3   |

<br>

- In our case, the mode is **low GDP per capita**.

---

### Median

- **Definition**: the median is the value such that:
  - at least half of the observations are higher or equal than the value
  - at least half of the observations are lower or equal than the value

- **Intuition**: the median is _the value that separates the higher half from the lower half of the data_.

- To compute the median sort the data and find the _middle value_ (what happens if the values are an even number?).

- Can be computed for any type of _ordered_ data (ordinal and cardinal).

---

### Example Data

| Country | GDP per capita (binned) |
| ----------- | ----- |
| Bolivia           | low GDP per capita     |
| Guatemala           | low GDP per capita     |
| Paraguay           | low GDP per capita   |
| Ecuador           | low GDP per capita   |
| **Colombia**           | **middle GDP per capita**   |
| Peru          | middle GDP per capita     |
| Brazil           | high GDP per capita   |
| Argentina           | high GDP per capita     |
| Chile           | high GDP per capita   |

<br>

- In our case, the median is **middle GDP per capita**.
