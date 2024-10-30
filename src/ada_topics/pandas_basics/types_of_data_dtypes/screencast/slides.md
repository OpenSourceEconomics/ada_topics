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
# themeConfig:
#   paginationPagesDisabled: true
---

### Applied Data Analytics

<br/>

# Descriptive Statistics / Pandas

### Types of data and data types

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar


---

# Nominal (qualitative, categorical) data

Example

- Variable: Country of origin

- Possible values: Names of countries in Latin America

- Observed values: Argentina, Bolivia, Argentina

---
src: ./decision_tree.md
---

---

# Nominal (qualitative, categorical) data

<div class="grid grid-cols-2 gap-4">
<div>

### Examples

Country

Gender

Marital status

Industry classifier

</div>
<div>

### Pandas data type

```python
pd.Series(
  [
    "Argentina",
    "Bolivia",
    "Argentina",
  ],
  dtype=pd.CategoricalDtype(
    [
      "Argentina",
      ...
      "Peru",
    ],
    ordered=False
  )
)
```
<br/>
<br/>
<br/>
</div>
</div>



---

# Cardinal, continuous data

Example:

- Variable: Annual Income in Euros

- Possible values: Positive real numbers

- Observed values: 42,345 €, 53,724 €, 28,734 €

---
src: ./decision_tree.md
---

---

# Cardinal, continuous data

<div class="grid grid-cols-2 gap-4">
<div>

### Examples

Monetary quantities

Some utility measures

Weight

Lengths

Energy consumption

</div>
<div>

### Pandas data type

Floating point

```python

pd.Series(
  [
    42_345,
    53_724,
    28_734,
  ],
  dtype=float
)
```
<br/>
<br/>
<br/>
</div>
</div>


---

# Cardinal, discrete data

Example:

- Variable: Age in years

- Possible values: 0, 1, 2, ...

- Observed values: 18, 22, 19

---
src: ./decision_tree.md
---

---

# Cardinal, discrete data

<div class="grid grid-cols-2 gap-4">
<div>

### Examples

Age in years or months

Any count variable

<br/>

_Depending on the typical number of outcomes, we may treat variables as quasi-continuous._

</div>
<div>

### Pandas data type

Integer

```python

pd.Series(
  [
    18,
    22,
    19,
  ],
  dtype=int
)
```
<br/>
<br/>
<br/>
</div>
</div>


---

# Ordinal, non-numeric data

Example:

- Variable: Annual Income in Euros, binned

- Possible values: $[0, 30000), [30000, 60000), [60000, \infty)$

- Observed values: $[30000, 60000)$, $[30000, 60000)$, $[0, 30000)$,

---
src: ./decision_tree.md
---

---

# Ordinal, non-numeric data

<div class="grid grid-cols-2 gap-4">
<div>

### Examples

Binned cardinal data, whatever the label.
Here:
- "low", "medium", "high"
- 0, 1, 2

Labelled Likert scales ("0 disagree", "1", "2", "3", "4 agree")

Highest degree obtained

Social status / class

<br/>
<br/>

</div>
<div>

### Pandas data type

Ordered categorical

```python
pd.Series(
    [
        "[30000, 60000)",
        "[30000, 60000)",
        "[0, 30000)",
    ],
    dtype=pd.CategoricalDtype(
        [
            "[0, 30000)"
            "[30000, 60000)"
            "[60000, ∞)"
        ],
        ordered=True
    )
)
```


</div>
</div>

---

## Ordinal, numeric data

<br/>
<div class="grid grid-cols-2 gap-4">
<div>

### Examples

Unlabelled Likert scales

IQ

Some utility measures

</div>
<div>

### Pandas data type

Ordered categorical

Integer

Floating point

<br/>
<br/>
<br/>
</div>
</div>
