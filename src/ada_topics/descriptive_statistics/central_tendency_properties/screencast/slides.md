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

### Measures of Central Tendency: More properties

<br>

Hans-Martin von Gaudecker and Aapo Stenhammar

---



### Mean vs Median: sensitivity to outliers.

- The mean is more sensitive to outliers than the median. Why?

- After ranking as the top tourist destination for the next year, Guatemala's GDP per capita is expected to spike to approximately $10,000

- The mean changes to $9,125, while the median remains more stable ($7,790)

- Note: if the shock would have affected a country in the top half of the distribution, the median wouldn't have changed

---

### Summary

| Statistic | Sensitivity to outliers | Type of data | Aggregation to higher level |
| --------- | ----------------------- | ------------ | --------------------------- |
| Mean      | High                    | Cardinal    | Sum of all values / N |
| Median    | Low                     | Cardinal, ordinal | Middle value |
| Mode      | Low                     | Cardinal, ordinal, categorical | Most frequent value |
