# Getting started with notebooks

## Learning Objectives

*(opening)*

After working through this screencast, you should be able to:

- Start a JupyterHub session from eCampus
- Open a notebook
- Find your way around the JupyterLab interface

*(executing)*

After working through this screencast, you should be able to:

- Understand the difference between Python and Markdown cells
- Execute notebook cells in various ways
- Restart the kernel

*(pitfalls)*

- Explain why linear execution of cells is important before considering something
  finished

*(markdown)*

- Write texts in Markdown using basic formatting

(copy a cheat sheet giving proper credit and include it)

## Materials

### Screencast on starting a JupyterHub client from eCampus

- Jupyter Notebooks are the main tool for data analytics in Python in the corporate
  world
- We use JupyterHub. There are other options, but you will be on your own.
- Ecampus page -> JupyterHub -> show contents -> start my server
- Describe user interface of JupyterLab (files on the left, and launch new things)
- To start: launch notebook and rename. Describe extension ipynb
- Notebooks are useful because:
  - you can have immediate feedback after running a cell
  - you can include nicely formatted text between python cells
  - All of this will be described in the next screencasts.
- Fill a cell with print("hello world") (mentioning that they don't need to understand
  the content) and show how to execute it
  - run cell
  - Shift-Enter
  - ctrl-Enter
- Create a new cell and show that you can move the order of cells - but explain that
  this is not common.

### Screencast on Markdown cells

- Describe why adding text between cells is useful
- Create a markdown cell and do the following
  - Insert title, subtitle, subsubtitle, ....
  - Insert unordered list (- .... - .... )
  - Insert ordered list (1. 1. 1. ...)
  - Write code in md

### Screencast on Python cells

- Create different python cells in which the following operations are performed:
  - 2+2
  - a = 2
  - a = 3 (reiterate that the variable is overwritten)
  - a (show the path dependency)
  - Restart kernel and show that a is not defined

## Quiz

Check all boxes that apply.

- F We will get support from the teaching team if running things on our own computer.
- T We can do everything that we do on JupyterHub also on our own computer if we install
  some freely available programmes.
- T We will get support from the teaching team if running things on JupyterHub.
- F JupyterHub is the only way to run the Python code required in this course.

The preferred way to execute a single notebook cell is...

- F by selecting 'Run' from the menu bar and then 'Run Selected Cell' from the drop-down
  menu.
- F by clicking on the 'fast-forward' button in the top row of the notebook tab
- F by clicking on the 'play' button in the top row of the notebook tab
- F by selecting 'Run' from the menu bar and then 'Restart kernel and run all cells'
  from the drop-down menu.
- T Selecting the cell and pressing 'Shift' (or 'ctrl') + 'Enter'.

In Jupyter Notebooks, the order in which cells are executed:

- F Is the order in which cells appear on the screen
- T Is determined by which cell you run first
- F Is always random
- T Is the order in which cells appear on the screen IF you restart the kernel and
  select "run all".
