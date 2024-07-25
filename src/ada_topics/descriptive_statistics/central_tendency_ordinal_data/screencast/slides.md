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
- Any binned cardinal variable (e.g. low income (income lower than \$40k), middle income (income between \$40k and \$130k), income (income above $130k))

---

### Example Data


| Observation | GDP per capita (binned) |
| ----------- | ----- |
| Argentina           | high GDP per capita     |
| Bolivia           | low GDP per capita     |
| Brazil           | middle GDP per capita   |
| Chile           | high GDP per capita   |
| Colombia           | low GDP per capita   |
| Ecuador           | low GDP per capita     |
| Panama           | high GDP per capita   |
| Paraguay           | low GDP per capita   |
| Peru           | middle GDP per capita   |

---

### Mode

- **Definition**: the mode is _the value that appears most frequently in the data_.

- If more values appear with the same highest frequency, the data is _multimodal_.

- If no value appears more than once, the data has _no mode_.

- The mode is computed by calculating the frequency of each possible realization and taking the most frequent one(s).

- The mode can be computed for any type of data (categorical, ordinal, and cardinal).

---

### Example Data

| Value | Frequency |
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

| Observation | GDP per capita (binned) |
| ----------- | ----- |
| Bolivia           | low GDP per capita     |
| Paraguay           | low GDP per capita   |
| Ecuador           | low GDP per capita   |
| Colombia           | low GDP per capita   |
| **Peru**          | **middle GDP per capita**     |
| Brazil           | middle GDP per capita   |
| Argentina           | high GDP per capita     |
| Chile           | high GDP per capita   |
| Panama           | high GDP per capita   |

<br>

- In our case, the median is **middle GDP per capita**.
