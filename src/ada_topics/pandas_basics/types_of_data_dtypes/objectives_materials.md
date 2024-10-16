# Types of data and data types

Please note that this page appears in both the chapters "Descriptive Statistics" and
"Pandas Basics". This is because the topic is relevant to both the general understanding
of data and the specific implementation in Pandas.

## Learning objectives

After working through this topic, you should be able to:

- determine the correct description of a given data column

  - nominal
  - cardinal
  - ordinal

- explain how these categories map into Pandas data types:

  - unordered categorical
  - floating point
  - integer
  - ordered categorical



## Materials

Here is the
[screencast](https://electure.uni-bonn.de/static/mh_default_org/engage-player/xxx).
These are the [slides](pandas_basics-types_of_data_dtypes.pdf).


## Decision tree

This is the decision tree for the "correct" form of data. Just because a variable
arrives as a number, it does not mean that you should think about it as numerical data.
Very often this happens when categories are encoded as numbers (e.g., 0, 1, 2 meaning $[0,
30,000)$, $[30,000, 60,000)$, $[60,000, \infty)$, which would be described in some metadata).

```{mermaid}
flowchart LR
    A -->|"`Yes`"| C("`Numerical?`")
    A(Ordered?) -->|No| B("`Unordered
    Categorical`")

    C -->|"`Yes`"| E("`Continuous?`")
    C -->|"`No`"| D("`Ordered
    Categorical`")

    E -->|"`Yes`"| G("`Floating
    point`")
    E -->|"`No`"| F("`Integer`")

    style A fill:#FFE5B4
    style C fill:#FFE5B4
    style E fill:#FFE5B4
```

Note that for numerical data, you still have to decide whether a variable is measured on
a cardinal or ordinal scale. Both are possible for continuous or discrete data, it is
not embedded in the Pandas data type.