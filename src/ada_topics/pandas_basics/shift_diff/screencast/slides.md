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

# Pandas basics

### Shifting and differencing rows

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Example: Gapminder data

<div class="grid grid-cols-2 gap-4">
<div>

MultiIndex: `country`, `year`

</div>
<div>

| country | year | continent | lifeExp |
| ------: | ---: | --------: | ------: |
|    Cuba | 1997 |  Americas |  76.151 |
|    Cuba | 2002 |  Americas |  77.158 |
|    Cuba | 2007 |  Americas |  78.273 |
|   Spain | 1997 |    Europe |   78.77 |
|   Spain | 2002 |    Europe |   79.78 |
|   Spain | 2007 |    Europe |  80.941 |

<br/>

</div>
</div>

---

# Shifting rows

<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] df.shift(1)
```

- Index remains the same

- Data is shifted by the number of<br/> rows specified in the argument

</div>
<div>

| country | year | continent | lifeExp |
| ------: | ---: | --------: | ------: |
|    Cuba | 1997 |       nan |     nan |
|    Cuba | 2002 |  Americas |  76.151 |
|    Cuba | 2007 |  Americas |  77.158 |
|   Spain | 1997 |  Americas |  78.273 |
|   Spain | 2002 |    Europe |   78.77 |
|   Spain | 2007 |    Europe |   79.78 |

<br/>

</div>
</div>

---

# Including a column with lags

<div class="grid grid-cols-2 gap-4">
<div>

```python
[2] df["lag_lifeExp"] = (
        df.shift(1)["lifeExp"]
    )
    df[["lifeExp", "lag_lifeExp"]]
```

</div>
<div>

| country | year | lifeExp | lag_lifeExp |
| ------: | ---: | ------: | ----------: |
|    Cuba | 1997 |  76.151 |         nan |
|    Cuba | 2002 |  77.158 |      76.151 |
|    Cuba | 2007 |  78.273 |      77.158 |
|   Spain | 1997 |   78.77 |      78.273 |
|   Spain | 2002 |   79.78 |       78.77 |
|   Spain | 2007 |  80.941 |       79.78 |

<br/>

</div>
</div>

---

# Combining groupby and shift

<div class="grid grid-cols-2 gap-4">
<div>

```python
[3] df.groupby("country").shift(1)
    df[["continent", "lifeExp"]]
```

- Essentially always necessary<br/>when your data has a MultiIndex

- Or should have one

</div>
<div>

| country | year | continent | lifeExp |
| ------: | ---: | --------: | ------: |
|    Cuba | 1997 |       nan |     nan |
|    Cuba | 2002 |  Americas |  76.151 |
|    Cuba | 2007 |  Americas |  77.158 |
|   Spain | 1997 |       nan |     nan |
|   Spain | 2002 |    Europe |   78.77 |
|   Spain | 2007 |    Europe |   79.78 |

<br/>

</div>
</div>

---

# Differencing rows

<div class="flex">
<div>

```python
[4] df.groupby("country").diff(1)
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    [clipped]

    TypeError: unsupported operand type(s) for -: 'str' and 'str'

```

<br/>

- Only defined for numerical data

</div>
</div>



---

# Differencing rows

<div class="grid grid-cols-7 gap-4">
<div class="col-span-4">

```python
[5]  df.groupby("country")[["lifeExp"]].diff(1)
```

</div>
<div class="col-span-3">

| country   |   year |   lifeExp |
|----------:|-------:|----------:|
| Cuba      |   1997 |   nan     |
| Cuba      |   2002 |     1.007 |
| Cuba      |   2007 |     1.115 |
| Spain     |   1997 |   nan     |
| Spain     |   2002 |     1.01  |
| Spain     |   2007 |     1.161 |

</div>
</div>
