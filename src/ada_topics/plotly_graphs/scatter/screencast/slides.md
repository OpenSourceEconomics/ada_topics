---
theme: academic
coverDate: ""
class: text-center
highlighter: shiki
lineNumbers: false
info: Applied Data Analytics
drawings:
  persist: false
transition: fade
defaults:
  layout: center
---

### Applied Data Analytics

<br/>

# Visualisations with plotly

### Scatter plots

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Scatter plots

<div class="flex gap-10">
<div>

|     |     x |     y |
| --: | ----: | ----: |
|   0 | 75.87 | 71.84 |
|   1 | 78.62 | 73.34 |
|   2 | 80.37 | 75.34 |
| ... |   ... |   ... |
| 686 | 84.62 | 28.09 |
| 687 | 82.12 | 25.34 |
| 688 | 76.37 | 25.84 |

</div>
<div>

```python
fig = panda.plot.scatter(x="x", y="y")
fig.show()
```

<center>
<img src="/panda.svg" width=400>
</center>

</div>
</div>

---

<center>
<img src="/panda_to_star.gif" width=700>
</center>


Animation generated using the [Data Morph Python library](https://doi.org/10.5281/zenodo.7834197) and inspired by the paper “[Same Stats, Different Graphs: Generating Datasets with Varied Appearance and Identical Statistics through Simulated Annealing](https://damassets.autodesk.net/content/dam/autodesk/research/publications-assets/pdf/same-stats-different-graphs.pdf)” by Justin Matejka and George Fitzmaurice (ACM CHI 2017).

---

# Anscombe's Quartet

| dataset | mean(x) | std(x) | mean(y) | std(y) | corr(x,y) |
| :------ | ------: | -----: | ------: | -----: | --------: |
| I       |       9 |   3.32 |     7.5 |   2.03 |      0.82 |
| II      |       9 |   3.32 |     7.5 |   2.03 |      0.82 |
| III     |       9 |   3.32 |     7.5 |   2.03 |      0.82 |
| IV      |       9 |   3.32 |     7.5 |   2.03 |      0.82 |

---

<center>
<img src="/anscombe.svg" width=900>
</center>

---

<div class="flex gap-10">
<div>

```python
import seaborn as sns
import plotly.express as px
import pandas as pd

# Load Anscombe's quartet dataset
anscombe = sns.load_dataset("anscombe")

# Create scatter plots for each dataset
fig = px.scatter(
    anscombe,
    x="x",
    y="y",
    color="dataset",
    facet_col="dataset",
    title="Anscombe's Quartet",
    labels={"x": "X-axis", "y": "Y-axis"},
    width=900,
    height=300
)

# Show the plot
fig.show()
```

</div>
</div>
