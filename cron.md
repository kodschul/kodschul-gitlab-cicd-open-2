# Anleitung zur Erstellung eines Pipeline-Schedules in GitLab

## 1. Pipeline-Schedule erstellen

1. **Gehe zu deinem Projekt in GitLab** und navigiere zu **CI/CD > Schedules**.
2. Klicke auf **New schedule**, um einen neuen Zeitplan für deine Pipeline zu erstellen.

## 2. Pipeline-Schedule konfigurieren

3. **Fülle die folgenden Felder aus**:

   - **Description**: Gib eine Beschreibung für den Zeitplan ein, z.B. "Nächtlicher Build" oder "Wöchentlicher Test".
   - **Cron Pattern**: Verwende ein Cron-Format, um die Häufigkeit der Pipeline-Ausführung festzulegen (mehr dazu unten).
     - Beispiele für Cron-Syntax:
       - `0 0 * * *` → Täglich um Mitternacht
       - `30 2 * * 1` → Jeden Montag um 02:30 Uhr
       - `0 0 * * 0` → Jeden Sonntag um Mitternacht
   - **Timezone**: Wähle die Zeitzone aus, in der die Pipeline ausgeführt werden soll (z.B. "Europe/Berlin").

4. **Weitere Optionen**:

   - **Target branch**: Wähle den Branch, auf dem die geplante Pipeline ausgeführt werden soll (z.B. `main`, `develop`).
   - **Variables**: Du kannst zusätzliche Umgebungsvariablen definieren, die nur bei diesem Pipeline-Schedule verwendet werden sollen (z.B. `SCHEDULED_BUILD=true`).

5. Klicke auf **Save pipeline schedule**, um den Zeitplan zu speichern.

## 3. Cron-Syntax: Erklärung und Beispiele

Die **Cron-Syntax** besteht aus fünf Feldern, die den Zeitpunkt der Pipeline-Ausführung festlegen:

```
*    *    *    *    *
│    │    │    │    │
│    │    │    │    └─── Tag der Woche (0 - 7) (Sonntag = 0 oder 7)
│    │    │    └──────── Monat (1 - 12)
│    │    └───────────── Tag des Monats (1 - 31)
│    └────────────────── Stunde (0 - 23)
└─────────────────────── Minute (0 - 59)
```

### Beispiele für gängige Cron-Syntax:

- `0 0 * * *` → Täglich um Mitternacht.
- `30 2 * * 1` → Jeden Montag um 02:30 Uhr.
- `0 0 * * 0` → Jeden Sonntag um Mitternacht.
- `0 18 * * *` → Täglich um 18:00 Uhr.

## 4. Pipeline-Schedule verwalten und bearbeiten

- Um einen bestehenden Pipeline-Schedule zu bearbeiten, gehe erneut zu **CI/CD > Schedules** und klicke auf den Namen des bestehenden Zeitplans. Dort kannst du den Zeitplan bearbeiten oder löschen.
- Du kannst mehrere Schedules für dasselbe Projekt erstellen, um unterschiedliche Pipelines zu verschiedenen Zeiten auszuführen (z.B. tägliche Tests, wöchentliche Deployments).

## Fazit

Mit GitLabs Pipeline-Schedules kannst du deine CI/CD-Pipelines automatisieren und zu festen Zeiten ausführen lassen, ohne manuell eingreifen zu müssen. Achte darauf, dass du die richtige **Cron-Syntax** verwendest und den Ziel-Branch sowie die Umgebungsvariablen entsprechend deiner Anforderungen konfigurierst.

### Wichtige Hinweise zur Cron-Syntax:

- **Minutenfeld (erste Stelle)**: Bestimmt die Minute der Ausführung (z.B. `0` für die volle Stunde).
- **Stundenfeld (zweite Stelle)**: Bestimmt die Stunde der Ausführung (z.B. `18` für 18:00 Uhr).
- **Tag des Monats (dritte Stelle)**: Gibt an, an welchem Tag des Monats die Pipeline ausgeführt wird.
- **Monat (vierte Stelle)**: Gibt den Monat der Ausführung an.
- **Wochentag (fünfte Stelle)**: Bestimmt, an welchem Wochentag die Pipeline läuft (z.B. `1` für Montag).

Mit dieser Anleitung kannst du in GitLab mühelos einen **Pipeline-Schedule** erstellen und die Ausführung deiner Pipelines automatisieren!
