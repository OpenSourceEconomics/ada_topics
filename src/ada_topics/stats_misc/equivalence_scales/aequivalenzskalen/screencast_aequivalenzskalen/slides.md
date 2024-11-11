---
theme: default
# apply any windi css classes to the current slide
class: text-center
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
# some information about the slides, markdown enabled
info: |
  ## Finanz- und Sozialpolitik SoSe 2022/23
# persist drawings in exports and build
drawings:
  persist: false
# page transition
transition: fade
# use UnoCSS
css: unocss
defaults:
  layout: center
---

# Äquivalenzskalen

## Finanz- und Sozialpolitik

Hans-Martin von Gaudecker

---

## Verschiedene Haushalte vergleichen

Ökonomisch: Wie bildet man Skaleneffekte ab?

- Wohnung
- Haushaltseinrichtung
- Essen
- Urlaub
- Mobilität
- ...

---

## Äquivalenzskalen

$$\textrm{Gewicht}(\textrm{HH}_i) = f\big(N^\textrm{Erwachsene}_i, N^\textrm{Kinder}_i\big)$$

- Eigenschaften:

  - $f(1, 0) = 1$
  - $0 < \Delta f / \Delta N < 1$
  - $\Delta^2 f / \Delta N \Delta N \leq 0$
  - $\Delta f / \Delta N^\textrm{Erwachsene} \geq \Delta f / \Delta N^\textrm{Kinder}$

---

## Die neue OECD-Skala

| Beschreibung                     | Gewicht |
| -------------------------------- | ------- |
| Erster Erwachsener               | 1,0     |
| Jeder weitere Person ab 14 Jahre | 0,5     |
| Jedes Kind                       | 0,3     |
