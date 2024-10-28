# Script: Quantiles

Starter code:

```python
import pandas as pd

data = pd.Series([0.09, 0.35, 1, 1, 1.25, 1.57, 2.15, 2.3, 2.9])
data
```

Remind them of:

```python
data.median()
```

Exactly the same:

```python
data.quantile(0.5)
```

Quartiles -- will yield Series back

```python
data.quantile([0.25, 0.5, 0.75])
```

Terciles:

Do computation right in there

```python
data.quantile([1 / 3, 2 / 3])
```
