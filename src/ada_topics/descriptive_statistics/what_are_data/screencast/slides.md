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
# themeConfig:
#   paginationPagesDisabled: true
---

### Applied Data Analytics

<br/>

# Descriptive Statistics

### What do we mean by "data"?

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

<center>
<img src="/container-port.png" width=900>
</center>

---

# Computer Science Definition

A collection of values or information that can be processed by a computer.

- Unstructured data (images, videos, text documents, ...)

- Structured data (commonly: tables with rows and columns)

<br/>
<br/>
<br/>

---

# Statistical Definition

The actual values of variables obtained from samples or populations. These values can be
numerical or categorical.

- Sample vs. Population

- Numerical vs. Categorical

<br/>
<br/>
<br/>

---

# What could freight data look like?

- Notation often $x_{k, i}$ where $k$ indexes the variable and $i$ indexes the
  observation.

- So $i$ could be the name of the vessel

- $x_{1, i}$ could be the owner of the vessel $\in \{ \text{Mærsk}, \text{MSC},
  \text{CMA CGM}, \ldots \}$:

- $x_{2, i}$ could be the number of containers on the vessel

<br/>
<br/>
<br/>

---

# Tables

| `ship_name`  | `owner` | `n_containers` |
| ------------ | ------- | -------------- |
| Laura Mærsk  | Mærsk   | 1,926          |
| MSC Flaminia | MSC     | 2,356          |

a.k.a. labelled arrays, labelled matrices, Pandas DataFrames



<br/>
<br/>
<br/>

---

# Table columns


| `ship_name`  | `owner` |
| ------------ | ------- |
| Laura Mærsk  | Mærsk   |
| MSC Flaminia | MSC     |

<br/>

| `ship_name`  |`n_containers` |
| ------------ |-------------- |
| Laura Mærsk  |1,926          |
| MSC Flaminia |2,356          |

<br/>

a.k.a. labelled vectors, Pandas Series

Only one index to access elements — $x_{i}$

<br/>
<br/>
<br/>
