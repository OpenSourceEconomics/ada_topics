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

# Statistics — Basics & location

### Absolute and relative differences

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

<div class="grid grid-cols-2 gap-20">
<div>

# Interval scales

- Continuous

- Well-defined differences (cardinal)

- No true zero point

- Example: Degrees Celsius, cardinal utility

<br/>
<br/>
<br/>
</div>
<div>

# Ratio scales

- Continuous

- Well-defined differences (cardinal)

- True zero point

- Examples: Weight, income, wealth, inflation, ...

<br/>
<br/>
<br/>
</div>
</div>


---

<div class="grid grid-cols-2 gap-20">
<div>

# Absolute diff's

$$
\Delta_\text{abs} x = x_\text{new} - x_\text{old}
$$

<br/>

- Works for interval scales and ratio scales

<br/>
<br/>
<br/>
</div>
<div>

# Relative diff's

$$
\Delta_\text{rel} x = \frac{x_\text{new} - x_\text{old}}{x_\text{old}}
$$

- Works for ratio scales only

- Hard to interpret if $x$ takes on non-positive values

<br/>

</div>
</div>

Which to pick depends on what is useful in a particular context!

<br/>
<br/>


---

# Taking logarithms

$$
\Delta_\text{abs} \log(x) = \log(x_\text{new}) - \log(x_\text{old}) \approx \Delta_\text{rel} x
$$

- Possible for ratio scales with strictly positive values

- Strategy: Transform the data, then work with absolute differences

- Useful for plotting when you are interested in relative differences

- Not very intuitive for many people (including me)!

  So if possible, use original labels.

---

<img src="/income_nbins_100.svg" class="rounded" width="600">

---

<img src="/log_income_nbins_100.svg" class="rounded" width="600">
