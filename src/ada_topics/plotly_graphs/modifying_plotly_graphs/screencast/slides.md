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
defaults:
  layout: center
# themeConfig:
#   paginationPagesDisabled: true
---

### Applied Data Analytics

<br/>

# Visualisations with plotly

### Modifying plotly graphs

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Motivation

Clearly communicating what is on your graph is absolutely crucial for
readers to understand what is in it!

- Title

- Axis labels, including units (!!!)

- _(Legends)_

- Bonus: Additional features, like vertical lines

<br/>
<br/>
<br/>


---

# Example series

<div class="grid grid-cols-2 gap-4">
<div class="col-span-1">

```python

[1] monthly_income = pd.Series(
        [
            1.57,
            0.09,
            1,
            2.9,
            1.25,
            1,
            0.35,
            2.3,
            2.15
        ],
    )

```

</div>
<div class="col-span-1">


```python

[2] monthly_income
[2] 0    1.57
    1    0.09
    2    1.00
    3    2.90
    4    1.25
    5    1.00
    6    0.35
    7    2.30
    8    2.15
    dtype: float64

```


<br/>
<br/>
</div>
</div>


---

```python
monthly_income.plot.hist()
```

<center>
<img src="/hist.png" width=500>
</center>

<br/>
<br/>
<br/>

---

```python
monthly_income.plot.hist(nbins=100)
```

<center>
<img src="/hist_nbins100.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# Adding a title

```python
monthly_income.plot.hist(
    nbins=100,
    title="Distribution of monthly income (1,000s of Euros)",
)
```

---

# Adding a title

<center>
<img src="/hist_nbins100_title.png" width=500>
</center>

<br/>
<br/>
<br/>


---

# Removing the legend

```python
fig = monthly_income.plot.hist(
    nbins=100,
    title="Distribution of monthly income (1,000s of Euros)",
)
fig.update_layout(showlegend=False)
fig
```

<br/>

1. Assign the figure to a new variable

2. Call the `.update_layout()` method

<br/>
<br/>
<br/>


---

# Removing the legend

<center>
<img src="/hist_nbins100_title_nolegend.png" width=500>
</center>

<br/>
<br/>
<br/>



---

# Making the axes nice

```python
fig = monthly_income.plot.hist(
    nbins=100,
    title="Distribution of monthly income",
)
fig.update_layout(
    showlegend=False,
    xaxis_title="Monthly income in 1,000s of Euros",
    yaxis_title="Number of observations",
    yaxis_tickvals=[0, 1, 2],
)
fig
```

<br/>

1. Sensible titles for x- and y-axes

2. Sensible ticks for y-axis

<br/>
<br/>
<br/>

---

# Making the axes nice

<center>
<img src="/hist_final.png" width=500>
</center>

<br/>
<br/>
<br/>



---

# Adding the mean

```python
fig = monthly_income.plot.hist(
    nbins=100,
    title="Distribution of monthly income",
)
fig.update_layout(
    showlegend=False,
    xaxis_title="Monthly income in 1,000s of Euros"
    yaxis_title="Number of observations",
    yaxis_tickvals=[0, 1, 2],
)
fig.add_vline(x=monthly_income.mean(), line_width=3, line_color="red")
fig
```

<br/>

Call the `.add_vline()` method on the graph object

<br/>
<br/>
<br/>

---

# Adding the mean

<center>
<img src="/hist_final_with_mean.png" width=500>
</center>

<br/>
<br/>
<br/>
