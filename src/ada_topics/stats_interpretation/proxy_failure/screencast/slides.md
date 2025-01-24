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

# Data analysis — Interpretation challenges

### Proxy failure

<br/>

Hans-Martin von Gaudecker and Aapo Stenhammar

---

# [Rats (Hanoi, 1902)](https://en.wikipedia.org/wiki/Great_Hanoi_Rat_Massacre)

- Needed to reduce rat population

- Wanted to provide incentives for killing rats

- Payment upon delivering rat tail

---

# The world before the incentive scheme

```mermaid {theme: 'neutral', scale: 1.15, htmlLabels: false}
flowchart LR
    Ag(Citizens) ~~~ ActP( )
    Ag --> ActG(Kill rats)
    ActP ~~~ Principal(Govt.)
    ActG ~~~ Principal
    ActG --> G(Reduce rat<br/>population)
    ActP ~~~ Proxy(Rat tails)
    ActG --> Proxy
    Principal ~~~ G
    G ~~~ Proxy
    Proxy --> Principal ~~~ Ag

    style ActP  fill-opacity:0, stroke-opacity:0;
```

---

# The world with the incentive scheme

```mermaid {theme: 'neutral', scale: 1.15, htmlLabels: false}
flowchart LR
    Ag(Citizens) ~~~ ActP( )
    Ag --> ActG(Kill rats)
    ActP ~~~ Principal(Govt.)
    ActG ~~~ Principal
    ActG --> G(Reduce rat<br/>population)
    ActP ~~~ Proxy(Rat tails)
    ActG --> Proxy
    Principal ~~~ G
    G ~~~ Proxy
    Proxy --> Principal --> Ag

    style ActP  fill-opacity:0, stroke-opacity:0;
```

---

# The world with the incentive scheme

```mermaid {theme: 'neutral', scale: 1.15, htmlLabels: false}
flowchart LR
    Ag(Citizens) --> ActP(Cut rats'<br/>tails off)
    Ag --> ActG(Kill rats)
    ActP ~~~ Principal(Govt.)
    ActG ~~~ Principal
    ActP --> G
    ActG --> G(Reduce rat<br/>population)
    ActP --> Proxy(Rat tails)
    ActP ~~~ Proxy(Rat tails)
    ActG --> Proxy
    Principal ~~~ G
    G ~~~ Proxy
    Proxy --> Principal --> Ag
```



---

# Goodhart's law

In the formulation by Marilyn Strathern:

<br/>

_<span style="color:#CD7F32;">When a measure becomes a target, it ceases to be a good measure.</span>_

<br/>

Causal model for how the world works changes when we let agents act upon it.


---

# Principal observes

```mermaid {theme: 'neutral', scale: 1.25, htmlLabels: false}
flowchart LR
    Ag(Agent) ~~~ ActP( )
    Ag --> ActG(Action: G)
    ActP ~~~ Principal(Principal)
    ActG ~~~ Principal
    ActG --> G(Goal)
    ActP ~~~ Proxy(Proxy)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal ~~~ Ag

    style ActP  fill-opacity:0, stroke-opacity:0;
```

---

# Principal incentivises proxy measure
```mermaid {theme: 'neutral', scale: 1.25, htmlLabels: false}
flowchart LR
    Ag(Agent) ~~~ ActP( )
    Ag --> ActG(Action: G)
    ActP ~~~ Principal(Principal)
    ActG ~~~ Principal
    ActG --> G(Goal)
    ActP ~~~ Proxy(Proxy)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag

    style ActP  fill-opacity:0, stroke-opacity:0;
```

---

# Principal incentivises proxy measure

```mermaid {theme: 'neutral', scale: 1.25, htmlLabels: false}
flowchart LR
    Ag(Agent) --> ActP(Action: P)
    Ag --> ActG(Action: G)
    ActP ~~~ Principal(Principal)
    ActG ~~~ Principal
    ActG -->  G(Goal)
    ActP --> Proxy(Proxy)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag
```

---

# Education

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
flowchart LR
    Ag(Teachers) --> ActP(Teach to<br/>the test)
    Ag --> ActG(Teach<br/>holistically)
    ActP ~~~ Principal(School<br/>authority)
    ActG ~~~ Principal
    ActG -->  G(Critical<br/>thinking)
    ActP --> Proxy(Standardised<br/>tests)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag
```

---

# Policing

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
flowchart LR
    Ag(Police) --> ActP(Arrest party<br/>people<br/>for drugs)
    Ag --> ActG(Arrest serious<br/>criminals)
    ActP ~~~ Principal(Govt.)
    ActG ~~~ Principal
    ActG -->  G(Reduce crime)
    ActP --> Proxy(No. of<br/>arrests)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag
```

---

# Phillips curve

```mermaid {theme: 'neutral', scale: 1, htmlLabels: false}
flowchart LR
    Ag(Central<br/>Bank) --> ActP(Very low interest<br/>rates)
    Ag --> ActG(Moderate<br/>interest rates)
    ActP ~~~ Principal(Govt.)
    ActG ~~~ Principal
    ActG -->  G(Reduce<br/>unemployment)
    ActP --> Proxy(Inflation)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag
```

---

# Clicks

```mermaid {theme: 'neutral', scale: 1.15, htmlLabels: false}
flowchart LR
    Ag(Website<br/>designer) --> ActP(Clickbait<br/>links)
    Ag --> ActG(Interesting<br/>links)
    ActP ~~~ Principal(Firm)
    ActG ~~~ Principal
    ActG -->  G(Purchase<br/>product)
    ActP --> Proxy(Click<br/>on link)
    Principal ~~~ G
    G --> Proxy
    Proxy --> Principal --> Ag
```

---

# Bottom line

- Quantification is important

- Measurement is important

- But beware when applying it to control complex systems!

  _<span style="color:#CD7F32;">Ideas of one principal vs. creativity of many agents!</span>_
