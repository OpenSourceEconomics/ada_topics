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
title: Applied Data Analytics
defaults:
  layout: center
---

### Applied Data Analytics

<br>

# Data management with pandas

### Setting and renaming columns and indices

<br>


Hans-Martin von Gaudecker

---

# Why the Index is important

<div class="grid grid-cols-2 gap-4">
<div>

The dataframe from before

<table>
  <thead>
    <tr>
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>life_exp</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2002</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cuba</td>
      <td>Americas</td>
      <td>2007</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2002</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>Europe</td>
      <td>2007</td>
      <td>80.94</td>
    </tr>
  </tbody>
</table>


Same dataset, different Index

<table>
  <thead>
    <tr>
      <th></th>
      <th>continent</th>
      <th>life_exp</th>
    </tr>
    <tr>
      <th>country</th>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2">Cuba</th>
      <th>2002</th>
      <td>Americas</td>
      <td>77.16</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Americas</td>
      <td>78.27</td>
    </tr>
    <tr>
      <th rowspan="2">Spain</th>
      <th>2002</th>
      <td>Europe</td>
      <td>79.78</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>Europe</td>
      <td>80.94</td>
    </tr>
  </tbody>
</table>




</div>
<div>

<br/>
<br/>

- We have seen that pandas aligns new columns in a DataFrame by index
- Many other operations are aligned by index
- Using a meaningful index makes this even safer
- Index should be unique and not contain floats


</div>
</div>

---

# Setting and resetting the index


<div class="grid grid-cols-2 gap-4">
<div>

assume `df` is our gapminder example

```python
[1] df.index
RangeIndex(start=0, stop=4, step=1)

[1] df = df.set_index(["country", "year"])
    df.index
```
```txt
MultiIndex([( 'Cuba', 2002),
            ( 'Cuba', 2007),
            ('Spain', 2002),
            ('Spain', 2007)],
           names=['country', 'year'])
```
```python
[1] df = df.reset_index()
    df.index
RangeIndex(start=0, stop=4, step=1)
```


</div>
<div>

<br/>
<br/>

- `set_index` and `reset_index` are inverse functions
- `set_index` can take any column or list of columns
- Optional argument `drop=True` or `drop=False` determines what happens with the old
  index in `set_index`

</div>
</div>

---

# Renaming columns

<div class="flex gap-8">
<div>

assume `df` is our gapminder example

```python
[1] df.columns
```
```txt
Index(['country', 'continent', 'year',
 'life_exp'], dtype='string')
```

```python
[1] new_names = {
...     "life_exp": "life expectancy",
...     "country": "country name",
...     "continent": "continent name",
... }

[1] df = df.rename(columns=new_names)
    df.columns
```
```txt
Index(['country name', 'continent name',
 'year', 'life expectancy'], dtype='string')
```


</div>
<div>

<br/>
<br/>


- Dict can contain only the subset of variables that is actually renamed
- Renaming the index works the same way but is rarely needed
- Instead of a dict, you can provide a function that converts old names to new names!


</div>
</div>
