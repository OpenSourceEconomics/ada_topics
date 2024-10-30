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

### Logarithmic scales

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Example data

|    x |    y |
| ---: | ---: |
|    1 |    1 |
|    2 |    2 |
|    3 |    3 |
|    ⋮ |    ⋮ |
|  999 |  999 |
| 1000 | 1000 |

---

# linear x, linear y scales

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = series.plot.line()
fig.update_layout(
    showlegend=False,
    xaxis_title="x (linear scale)",
    yaxis_title="y (linear scale)",
)
fig.show()
```

</div>
<div>

<img src="/lin-lin.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# logarithmic x, linear y scales

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = series.plot.line()
fig.update_layout(
    showlegend=False,
    xaxis_type="log",
    xaxis_title="x (logarithmic scale)",
    yaxis_title="y (linear scale)",
)
fig.show()
```

</div>
<div>

<img src="/log-lin.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# linear x, logarithmic y scales

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = series.plot.line()
fig.update_layout(
    showlegend=False,
    xaxis_type="linear",
    yaxis_type="log",
    xaxis_title="x (linear scale)",
    yaxis_title="y (logarithmic scale)",
)
fig.show()
```

</div>
<div>

<img src="/lin-log.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# logarithmic x, logarithmic y scales

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = series.plot.line()
fig.update_layout(
    showlegend=False,
    xaxis_type="log",
    yaxis_type="log",
    xaxis_title="x (logarithmic scale)",
    yaxis_title="y (logarithmic scale)",
)
fig.show()
```

</div>
<div>

<img src="/log-log.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# Histogram: Linear


<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = income.plot.hist(nbins=100)
fig.update_layout(
    showlegend=False,
    yaxis_title="Number of observations",
    xaxis_title="Annual income (€)",
)
fig.show()
```

</div>
<div>

<img src="/income.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# Histogram with automatic log scale

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = income.plot.hist(nbins=100)
fig.update_layout(
    showlegend=False,
    yaxis_title="Number of observations",
    xaxis_title="Annual income (log €)",
    xaxis_type="log",
)
fig.show()
```

</div>
<div>

<img src="/log-income-wrong-bins.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>

---

# Histogram with non-human labels

<div class="grid grid-cols-2 gap-4">
<div>

```python
fig = np.log(income).hist(nbins=100)
fig.update_layout(
    showlegend=False,
    yaxis_title="Number of observations",
    xaxis_title="Annual income (log €)",
)
fig.show()
```

</div>
<div>

<img src="/log-income-wrong-labels.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>



---

# Histogram with manual labels

<div class="grid grid-cols-2 gap-4">
<div>

```python
xtickvals = pd.Series([1000, 5_000, 10_000, 50_000, 100_000, 300_000])
fig = np.log(income).hist(nbins=100)
fig.update_layout(
    showlegend=False,
    yaxis_title="Number of observations",
    xaxis_title="Annual income (log €)",
    xaxis_tickvals=np.log(xtickvals),
    xaxis_ticktext=xtickvals,
)
fig.show()
```

</div>
<div>

<img src="/log-income.svg" class="rounded" width="400">

<br/>
<br/>
<br/>
</div>
</div>
