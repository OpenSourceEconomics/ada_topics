# Planung

## Selbstlernphase

### Quiz

- Die Zahlungen des Bürgergelds implizieren Äquivalenzgewichte für verschiedene
  Haushalte. Diese sollen hier berechnet werden.

Machen Sie eine Kopie des Notebooks "Kinder & Bürgergeld" aus der Selbstlernphase zum
Thema "Grundsicherung für Familien mit Kindern". Sie müssen das Notebook an 2 Stellen
anpassen: 1. Setzen Sie die Kosten der Unterkunft und Heizkosten auf 0€. 2. Setzen Sie
das Alter aller Kinder auf 10 Jahre. In der Version der Präsenzphase haben die Kinder
unterschiedliche Alter. (Tipp: Sie können hier entweder die `.loc[...]` Methode oder
eine `.apply` Funktion verwenden.

Errechnen Sie für ein Haushaltseinkommen von 0 Euro, welche Äquivalenzgewichte vom
Bürgergeld impliziert werden. Vergessen Sie nicht das Kindergeld zum Bürgergeld
hinzuzurechnen. Gegeben, dass ein Erwachsener das Äquivalenzgewicht von 1 hat, was sind
dann bei einem Haushaltseinkommen von 0€ die vom Bürgergeld implizierten
Äquivalenzgewichte für die folgenden Haushaltstypen? Runden Sie auf zwei Dezimalstellen.

- 1E: (Lösung: 1)
- 1E, 1K: (Lösung: 1,85)
- 2E: (Lösung: 1,8)
- 2E, 1K: (Lösung: 2,53)
- 2E, 2K: (Lösung: 3,26)

**ACHTUNG: LÖSUNGEN IMMER NEU AUSRECHNEN**

Zum Vergleich die Werte der neuen OECD-Äquivalenzskala:

- 1E: 1
- 1E, 1K: 1,3
- 2E: 1,5
- 2E, 1K: 1,8
- 2E, 2K: 2,1.

## Präsenzphase

```{todo}
- [ ] Rentner aus Datensatz entfernen, z.B. hat `hh_id == 9401` ein negatives Einkommen
      nach vorgegebener Definition
```

| Zeit   | Inhalt                                            |
| ------ | ------------------------------------------------- |
| 8:45h  | Begrüßung                                         |
| 8:50h  | Notebook                                          |
|        | - Reform in GETTSIM                               |
|        | - Äquivalenzgewichte (Aufgabenstellung existiert) |
| 10:15h | Pause                                             |
| 11:30h | Pentabilities                                     |
| 11:40h | Besprechung der Ergebnisse                        |

### Details zu Aufgabe

### Fragen Feedbackrunde Studierende
