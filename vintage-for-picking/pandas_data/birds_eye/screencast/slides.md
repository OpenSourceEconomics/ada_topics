---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Applied Data Analytics
drawings:
  persist: false
transition: fade
title: Applied Data Analytics
defaults:
  layout: center
---

### Applied Data Analytics

<br>

# Data management with pandas

### A bird's eye view of pandas

<br>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# What is pandas?

- Industry standard DataFrame library in Python
- Covers all you need for handling data
  - Loading datasets in many formats
  - Cleaning data
  - Generating variables
  - Reshaping datasets
  - Basic statistical operations
- Compatible with all plotting and statistics libraries

---

# What is a DataFrame?

<br/>

<div class="grid grid-cols-2 gap-12">
<div>

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>computer_use</th>
      <th>programming</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>United States</th>
      <td>0.754612</td>
      <td>0.074551</td>
    </tr>
    <tr>
      <th>Netherlands</th>
      <td>0.801328</td>
      <td>0.057847</td>
    </tr>
    <tr>
      <th>Germany</th>
      <td>0.71248</td>
      <td>0.058607</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>0.736921</td>
      <td>0.05632</td>
    </tr>
  </tbody>
</table>

</div>

<div>

- Tabular data format
- Variables are columns
- Observations are rows
- Can be manipulated in Python

</div>
</div>


---

# What is **modern** pandas?

- Pandas was created in 2008 and has some baggage
- With version 3.0 many things will improve
- We will enable some features right away using:

<br/>

```python
import pandas as pd

pd.options.mode.copy_on_write = True
pd.options.future.infer_string = True
pd.options.plotting.backend = "plotly"
```
