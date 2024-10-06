### 1. **Pipeline- und Job-Übersicht**

Wenn eine Pipeline fehlschlägt, zeigt GitLab eine klare Übersicht über den Status der Pipeline und ihrer Jobs an:

- **Grüne Häkchen**: Der Job ist erfolgreich.
- **Rotes X**: Der Job ist fehlgeschlagen.
- **Gelbes Ausrufezeichen**: Der Job wurde übersprungen oder manuell gestoppt.

**Navigiere zur Pipeline**:

- Gehe in deinem GitLab-Projekt zu **CI/CD > Pipelines**.
- Klicke auf die spezifische Pipeline, die fehlgeschlagen ist.
- Du siehst eine Übersicht der **Stages** und **Jobs**, und fehlgeschlagene Jobs sind mit einem roten X markiert.

### 2. **Job-Log öffnen**

Jeder Job in GitLab CI hat ein **detailliertes Log**, das alle ausgeführten Schritte und die Ausgabe der Befehle enthält. Um die Logs einzusehen:

- Klicke auf den fehlgeschlagenen **Job** in der Pipeline-Übersicht.
- Du wirst auf die **Job-Detail-Seite** weitergeleitet, wo du das vollständige **Log** des Jobs findest.

### 3. **Log-Analyse: Wichtige Bereiche**

Die **Job-Logs** enthalten viele Informationen. Hier sind die wichtigsten Bereiche, auf die du achten solltest:

#### a. **Zusammenfassung der Job-Ausführung**

Am Anfang des Logs findest du eine Zusammenfassung der Pipeline-Konfiguration:

- Die verwendete **GitLab Runner-Version**.
- Die **Stages** und **Jobs** der Pipeline.
- Den verwendeten **Docker-Image** oder die Umgebung, in der der Job ausgeführt wird.

#### b. **Fehlerhaftes Skript oder Befehl**

Suche im Log nach der genauen Stelle, an der der Fehler auftritt. Typische Fehlermeldungen sind:

- **Syntaxfehler** in Skripten oder Konfigurationsdateien.
- **Exit codes**: Ein nicht-Null-Exit-Code deutet auf einen Fehler hin.
  - Beispiel: `exit code 1` oder `exit code 127` (fehlendes Programm).
- **Timeouts**: Der Job könnte fehlschlagen, wenn ein Befehl zu lange dauert und ein Timeout erreicht wird.

Beispielhafte Fehlermeldungen:

```bash
ERROR: Command "pytest" not found
```

```bash
/bin/sh: 1: npm: not found
```

#### c. **Artefakte und Cache**

Prüfe, ob der Job auf notwendige **Artefakte** oder **Zwischenergebnisse** zugreift:

- Fehler beim Abrufen von Artefakten oder beim Zugriff auf Caches können zu Build-Problemen führen.

Beispiel:

```bash
ERROR: Downloading artifacts from coordinator... not found
```

#### d. **Build-Umgebung und Abhängigkeiten**

Überprüfe, ob alle notwendigen **Abhängigkeiten** (Pakete, Libraries, Docker-Images) korrekt installiert sind:

- Fehlschlag bei Abhängigkeiten oder fehlende Installationen von Paketen.

Beispiel:

```bash
Could not resolve dependencies for project
```

#### e. **Log-Filter**

GitLab bietet eine Filterfunktion, mit der du nach bestimmten Fehlermeldungen oder Text suchen kannst. Nutze diese Funktion, um schneller zu den relevanten Fehlermeldungen zu gelangen.

### 4. **Verstehen von Exit-Codes**

Viele Jobs in GitLab CI schlagen aufgrund eines **nicht-Null Exit-Codes** fehl. Hier sind einige häufige Exit-Codes:

- **0**: Erfolgreiche Ausführung (keine Fehler).
- **1**: Allgemeiner Fehler.
- **127**: Befehl nicht gefunden (z.B. falscher Pfad oder fehlendes Programm).

Beispiel:

```bash
Script failed with exit code 1
```

In diesem Fall zeigt das Log oft direkt den Befehl an, der den Exit-Code erzeugt hat.

### 5. **Pipeline-Ansicht und Retries**

- GitLab zeigt für jeden Job eine **"Retry"**-Option an. Wenn ein Job fehlschlägt, kannst du ihn erneut ausführen, um zu sehen, ob der Fehler reproduzierbar ist.
- Nutze auch die **"Play"**-Schaltfläche, um manuelle Jobs oder fehlerhafte Jobs erneut zu starten.

### 6. **Erweiterte Fehleranalyse**

GitLab ermöglicht es, **zusätzliche Informationen** in den Logs anzuzeigen:

- **Debug-Mode**: Du kannst die Pipeline im Debug-Modus ausführen, um detailliertere Logs zu erhalten. Dies ist besonders nützlich, wenn du detaillierte Informationen zur Laufzeitumgebung oder den verwendeten Docker-Containern benötigst.

In der `.gitlab-ci.yml` Datei kannst du `CI_DEBUG_TRACE` aktivieren:

```yaml
variables:
  CI_DEBUG_TRACE: "true"
```

Dies sorgt dafür, dass GitLab jeden Befehl und seine Ausgabe detaillierter protokolliert.

### 7. **Tipps zur Fehlerbehebung**

- **Fehlende Abhängigkeiten**: Wenn ein Job fehlschlägt, weil eine Abhängigkeit nicht gefunden wurde, stelle sicher, dass du das richtige Docker-Image verwendest oder installiere die Abhängigkeiten im `before_script`.

  Beispiel:

  ```yaml
  before_script:
    - apt-get update && apt-get install -y python3
  ```

- **Timeouts**: Wenn Jobs aufgrund von Zeitüberschreitungen fehlschlagen, kannst du das Timeout erhöhen, indem du die `timeout`-Anweisung verwendest.

  Beispiel:

  ```yaml
  job_name:
    script:
      - long_running_command
    timeout: 1h
  ```

- **Fehlgeschlagene Tests**: Wenn Unit-Tests oder Integrationstests fehlschlagen, kannst du die detaillierten Test-Logs analysieren. GitLab unterstützt Berichte wie **JUnit**:

  ```yaml
  test_job:
    script:
      - pytest --junitxml=report.xml
    artifacts:
      reports:
        junit: report.xml
  ```

- **Caching-Probleme**: Wenn der Cache nicht richtig funktioniert, kannst du den Cache neu generieren lassen:
  ```yaml
  cache:
    key: "$CI_COMMIT_REF_NAME"
    paths:
      - node_modules/
  ```

### 8. **Zusammenfassung**

- **Logs** sind der wichtigste Ausgangspunkt für die Fehleranalyse in GitLab CI.
- Identifiziere die Stelle im Log, an der der Fehler auftritt, und achte auf Exit-Codes, fehlende Abhängigkeiten, Zeitüberschreitungen und Artefakte.
- Nutze die **Retry-Option** und den **CI_DEBUG_TRACE**-Modus, um detaillierte Informationen zu erhalten.
- Stelle sicher, dass alle notwendigen Abhängigkeiten installiert und ordnungsgemäß konfiguriert sind.

Durch systematische Log-Analyse kannst du die Ursache von Fehlern in GitLab Pipelines schnell identifizieren und beheben.
