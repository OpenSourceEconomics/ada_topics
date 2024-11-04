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

# Basic Python

### Importing Modules

<br/>


Hans-Martin von Gaudecker and Aapo Stenhammar

---

# Contents

- What are libraries?

- Different ways to import libraries or parts of libraries

- Typical errors when importing


---

# Third party libraries

- Python is a general purpose programming language

- The base language you have seen so far is extended by libraries

  - Standard library (e.g. datetime)

  - Third party libraries (e.g. pandas, plotly)

- Libraries need to be imported to use them (and third party libraries need to be
  installed)



---

# Different ways to import

<div class="grid grid-cols-2 gap-4">
<div class="col-span-1">

```python
# Import entire library and rename it
import pandas as pd

# # # # # # # # # # # # # # # # # # # #
# Remaining things are just for
# being able to read others' code
# # # # # # # # # # # # # # # # # # # #

# Import an entire library
import pandas

# Import one function / object
from pandas import Series

# Import everything from a library
from pandas import *
```

</div>
<div class="col-span-1">

1. All that is needed in this course

   - `pandas` (pd)
   - `plotly.express` (px)
   - `plotly.graph_objects` (go)

1. Many functions needed, no convention

1. If one needs one-three specific things

1. Never, ever use

</div>
</div>


---

# What could go wrong?

```python
import paaaaaandas as pd

---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import paaaaaandas as pd

ModuleNotFoundError: No module named 'paaaaaandas'
```

<br/>

- Meaning: The library you asked for is not found

- Do you have a typo in the library name?

- Is the library installed in your environment?

<br/>
<br/>
<br/>
