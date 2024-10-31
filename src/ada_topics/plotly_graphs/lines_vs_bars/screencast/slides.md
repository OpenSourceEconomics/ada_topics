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

### Line graphs vs. bar charts

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Picking the right graph

All kinds of data:

- Histograms: Bar charts, potentially stacked

Cardinal data:

- Levels of variable with fractional scale: Bar charts (including zeros!)

- Changes: Line charts

Never

- Pie charts

---

# Example (from [plotly docs](https://plotly.com/python/line-charts/))

```python
import plotly.express as px

df = px.data.gapminder()
df = df.query("continent=='Africa' & pop > 10_000_000")
df = df[["country", "year", "lifeExp"]]
life_exp = df.pivot(index='year', columns='country', values='lifeExp')
life_exp = life_exp.dropna(axis="columns", how="any")

life_exp.round(1)
```

<div class="grid grid-cols-2 gap-4">
<div>

- Take the gapminder dataset used in the plotly library

- No need to understand the data wrangling at this point

</div>
<div>

- Reduce to African countries with population over 10 million

- Select columns for country, year, and life expectancy

- Reshape the data

- Remove countries with missing data (e.g., Cameroon crossed 10M threshold in 1990s)
<br/>
<br/>
<br/>
</div>
</div>

---

| year | Congo, Dem. Rep. | Egypt | Ethiopia | Nigeria | South Africa |
| ---: | ---------------: | ----: | -------: | ------: | -----------: |
| 1952 |             39.1 |  41.9 |     34.1 |    36.3 |           45 |
| 1957 |             40.7 |  44.4 |     36.7 |    37.8 |           48 |
| 1962 |             42.1 |    47 |     40.1 |    39.4 |           50 |
| 1967 |             44.1 |  49.3 |     42.1 |      41 |         51.9 |
| 1972 |               46 |  51.1 |     43.5 |    42.8 |         53.7 |
| 1977 |             47.8 |  53.3 |     44.5 |    44.5 |         55.5 |
| 1982 |             47.8 |    56 |     44.9 |    45.8 |         58.2 |
| 1987 |             47.4 |  59.8 |     46.7 |    46.9 |         60.8 |
| 1992 |             45.5 |  63.7 |     48.1 |    47.5 |         61.9 |
| 1997 |             42.6 |  67.2 |     49.4 |    47.5 |         60.2 |
| 2002 |               45 |  69.8 |     50.7 |    46.6 |         53.4 |
| 2007 |             46.5 |  71.3 |     52.9 |    46.9 |         49.3 |

---

# Features of the data

- Homogenous data

  - All entries are life expectancies

  - This fact is implicit, cannot tell from the table

  - Contrast with survey data on sex, age, income, etc.

- Cardinal data on a fractional scale

- No missing values

---

# Out-of-the-box bar chart

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = life_exp.plot.bar(
  title='Life expectancy in large African countries'
)
fig.show()
```

</div>
<div>

<img src="/bar-naive.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>


---

# Plot levels as bars

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = life_exp.mean().plot.bar(
    title='Life expectancy in large African, 1950-2010 average'
)
fig.update_layout(showlegend=False)
fig.show()
```

Note that bars have to start at zero!

</div>
<div>

<img src="/bar-average.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>


---

# Plot changes as lines

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = life_exp.plot.line(
    title='Life expectancy in large African countries over time'
)
fig.show()
```

Focus on changes, hence focus the scale of the y-axis on the relevant range

</div>
<div>

<img src="/line-changes-over-time.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>
