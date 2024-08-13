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
title: Applied Data Analytics
defaults:
  layout: center
---

### Applied Data Analytics

<br>

# Data management with pandas

### Functional data management

<br>


Hans-Martin von Gaudecker

---

# Example

consider this hypothetical survey about a programming course

<div class="grid grid-cols-2 gap-4">
<div>

```python
[1] raw = pd.read_csv("survey.csv")
    raw
```

<table>
  <thead>
    <tr>
      <th></th>
      <th>Q001</th>
      <th>Q002</th>
      <th>Q003</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>strongly disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>1</th>
      <td>strongly agree</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-77</td>
      <td>disagree</td>
      <td>R</td>
    </tr>
    <tr>
      <th>3</th>
      <td>agree</td>
      <td>-77</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-99</td>
      <td>-99</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>5</th>
      <td>nan</td>
      <td>strongly agree</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>6</th>
      <td>neutral</td>
      <td>strongly agree</td>
      <td> Python</td>
    </tr>
    <tr>
      <th>7</th>
      <td>disagree</td>
      <td>agree</td>
      <td>python</td>
    </tr>
    <tr>
      <th>8</th>
      <td>strongly disagree</td>
      <td>-99</td>
      <td>PYTHON</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-77</td>
      <td>-99</td>
      <td>Ypthon</td>
    </tr>
  </tbody>
</table>



</div>
<div>

<br/>
<br/>


From the metadata you know

- Q001: I am a coding genius
- Q001: I learned a lot
- Q003: What is your favourite language

<br/>

- -77 not readable
- -99 no reply


</div>
</div>
