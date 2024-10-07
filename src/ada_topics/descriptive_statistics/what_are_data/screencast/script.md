# Script: What do we mean by "data"?

## Intro

- Since a lot of programming: Computer Science Definition, as you may encounter versions
  of it when searching the web.

- Statistical

## Picture

- CS: Many different pixels, each with RGB color value

- Statistical: Lists of freight that is inside the containers along with their weight

- Human sensory and cognitive system: Can process all kinds of information

  - On this picture, see patterns of container ships. Cognitive system may realize that
    it is AI-generated because of nonsense letters

  - Cognitive system may read from tables and graphs on the freight that something is
    wrong with one of the containers, alert the drug police

- So let's start with CS def and then think about typical data formats

## CS def

- Lots of progress with unstructured data in recent years

- But will focus on structured data

## Statistical def

- Conditions on this being structured data

- Sometimes observe only a few people (say we interviewed some), sometimes the entire
  population that is relevant.

- Much of statistics is about the question how we can learn from samples about
  populations, but that will be for the next course, we'll be loose about that

- We will think a lot about the type of data though, different types of numerical and
  categorical data

- So what could freight data for the previous picture look like?

# What could freight data look like?

- $k$ and $i$ could be counters or labels

- Usually counters when you see abstract notation, but labels to keep sane when working
  with actual data

- Owner is a categorical variable

- Number of containers is numerical (integer)

# Tables

- Now back to computer

- Label: We have a meaningful name for each row and column

- Arrays / Tables / Matrices: Depends on the tool you look at, important is that we keep
  the label.

- Pandas DataFrames: Will be the particular incarnation we will work with

- First column has the labels, then two columns with data

- Start with data columns this week, in Pandas: Series

# Table columns

Obvious

# Wrapping up

- We will work with what computer scientists call structured data

- We will not think much about formal rules to draw inference from samples to
  populations

- We will think a lot about the type of data, different types of numerical and
  categorical data

- We will work a lot with Tables or DataFrames, but start with Table Columns or Series,
  i.e. one-dimensional data
