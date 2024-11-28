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

### Concatenating Series / DataFrames

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Similar data, different sources

- Imports for each country

- The same survey questions for different years

- ...

→ Stack data on top of each other to obtain a single Series or DataFrame

---

# Concatenating Series / DataFrames

<div class="grid grid-cols-2 gap-30">
<div>

<br/>

| country | year | lifeExp |
| :------ | ---: | ------: |
| Cuba    | 2002 |  77.158 |
| Cuba    | 2007 |  78.273 |

<br/>
<br/>

| country | year | lifeExp |
| :------ | ---: | ------: |
| Spain   | 2002 |   79.78 |
| Spain   | 2007 |  80.941 |

<br/>
</div>
<div>

<br/>
<br/>
<br/>

| country | year | lifeExp |
| :------ | ---: | ------: |
| Cuba    | 2002 |  77.158 |
| Cuba    | 2007 |  78.273 |
| Spain   | 2002 |   79.78 |
| Spain   | 2007 |  80.941 |

<br/>
<br/>
</div>
</div>

---

# Syntax

- `cuba` holds a Series or DataFrame with data from Cuba

- `spain` holds a Series or DataFrame with data from Cuba

<br/>
<div class="flex">
<div>

```python
stacked = pd.concat([cuba, spain])
```

</div>
</div>

---

# Careful with the index!

<div class="grid grid-cols-2 gap-30">
<div>

<br/>

|     | country | year | lifeExp |
| --: | :------ | ---: | ------: |
|   0 | Cuba    | 2002 |  77.158 |
|   1 | Cuba    | 2007 |  78.273 |

<br/>
<br/>

|     | country | year | lifeExp |
| --: | :------ | ---: | ------: |
|   0 | Spain   | 2002 |   79.78 |
|   1 | Spain   | 2007 |  80.941 |

<br/>
</div>
<div>

<br/>
<br/>
<br/>

|     | country | year | lifeExp |
| --: | :------ | ---: | ------: |
|   0 | Cuba    | 2002 |  77.158 |
|   1 | Cuba    | 2007 |  78.273 |
|   0 | Spain   | 2002 |   79.78 |
|   1 | Spain   | 2007 |  80.941 |

<br/>
<br/>
</div>
</div>
