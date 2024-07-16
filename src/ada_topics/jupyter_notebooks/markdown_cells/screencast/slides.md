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

# Jupyter Notebooks

### Markdown syntax

<br/>


Hans-Martin von Gaudecker

---

# Headings

<br/>

<div class="grid grid-cols-2 gap-30">
<div>

<br/>

```
# Title






## Subtitle





###### Smallest level
```

</div>
<div>

<br/>

# Title

<br/>

## Subtitle

<br/>
<br/>

###### Smallest level

</div>
</div>

---

# Styling text

<br/>

<div class="grid grid-cols-2 gap-30">
<div>

```

**bold**

*italic*

~~strikethrough~~

***bold and italic***
```


</div>
<div>

**bold**

*italic*

~~strikethrough~~

***bold and italic***


</div>
</div>

---

# Lists

<br/>

<div class="grid grid-cols-2 gap-30">
<div>

```
- This is
- a bulleted
- list



1. This is
2. an
3. enumeration



1. This is
1. another
1. enumeration

```


</div>
<div>

- This is
- a bulleted
- list

<br/>

1. This is
2. an
3. enumeration

<br/>

1. This is
1. another
1. enumeration

</div>
</div>


---

# Links and Quotes


<br/>
<br/>

<div class="grid grid-cols-5 gap-4">
<div class="col-span-3">

```

[This is a link](www.google.com)



> This is a
> multi-line quote
```


</div>
<div class="col-span-2">

[This is a link](www.google.com)

<br/>
<br/>


> This is a
> multi-line quote


</div>
</div>

---


# Code Snippets

This is the most important one for communication on Zulip!!!

<div class="grid grid-cols-2 gap-30">
<div>

<br/>

<pre>
`x = 10`

```python
def f(x):
   return np.ones_like(x)
```
</pre>



</div>
<div>

<br/>

`x = 10`

<br/>
<br/>
<br/>




```python
def f(x):
   return np.ones_like(x)
```


</div>
</div>
