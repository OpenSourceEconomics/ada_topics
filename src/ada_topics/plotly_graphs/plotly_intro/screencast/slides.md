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

### Introduction to plotly

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Frontends, backends, leaky abstractions

- Frontend: The user-facing part

- Backend: The part that does the work

- Leaky abstraction: The user needs to know about the backend

<br/>
<br/>
<br/>


---

# Plotting Series

- Frontend: Pandas

- Backend: Plotly

- Leaky abstraction: Many customisation options you'll find on the web are specific to
  the (default) matplotlib backend

<br/>
<br/>


---

# Setting plotly as the plotting backend

```python

import pandas as pd

pd.options.plotting.backend = "plotly"

```
<br/>

Just in case you wonder why you find this code in notebooks we provide

<br/>
<br/>
<br/>

---

# Example series

<div class="grid grid-cols-2 gap-4">
<div class="col-span-1">

```python

[1] continuous = pd.Series(
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
        name="cont"
    )

```

</div>
<div class="col-span-1">


```python

[2] continuous
[2] 0    1.57
    1    0.09
    2    1.00
    3    2.90
    4    1.25
    5    1.00
    6    0.35
    7    2.30
    8    2.15
    Name: cont, dtype: float64

```


<br/>
<br/>
</div>
</div>


---

# `continuous.plot()`

<center>
<img src="/line.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# `continuous.plot.line()`

<center>
<img src="/line.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# `continuous.plot.bar()`

<center>
<img src="/bar.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# `continuous.plot.hist()`

<center>
<img src="/hist.png" width=500>
</center>

<br/>
<br/>
<br/>

---

# `continuous.plot.hist(nbins=100)`

<center>
<img src="/hist_nbins100.png" width=500>
</center>

<br/>
<br/>
<br/>
