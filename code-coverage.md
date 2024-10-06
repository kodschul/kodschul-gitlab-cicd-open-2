### 1. **JUnit Testberichte**

GitLab unterstützt die Anzeige von Testresultaten, wenn du deine Tests im JUnit-Format exportierst. Hier ein Beispiel, wie du in der `.gitlab-ci.yml` Testberichte generierst:

```yaml
test_job:
  stage: test
  script:
    - pytest --junitxml=report.xml # Beispiel mit pytest und JUnit Report
  artifacts:
    reports:
      junit: report.xml # Exportiere den JUnit-Bericht
```

- **JUnit-Berichte** werden nach dem Pipeline-Run im **"Test"** Tab des Jobs angezeigt.
- Zeigt an, welche Tests bestanden oder fehlgeschlagen sind.

### 2. **Code-Coverage-Berichte**

Du kannst die Code-Coverage-Ergebnisse sichtbar machen, indem du ein Coverage-Tool wie **pytest-cov** verwendest und die Ergebnisse in GitLab integrierst.

```yaml
test_job:
  stage: test
  script:
    - pytest --cov=my_project # Beispiel mit Coverage-Bericht
  coverage: '/TOTAL\s+\d+\s+\d+\s+(\d+)%/' # Regex, um Coverage aus den Logs zu extrahieren
```

- Die **Code Coverage** wird im Pipeline-Dashboard neben dem Job angezeigt.

### 3. **Artefakte für detaillierte Berichte**

Zusätzlich kannst du auch ausführliche Testreports als Artefakte speichern:

```yaml
test_job:
  stage: test
  script:
    - pytest --junitxml=report.xml
  artifacts:
    paths:
      - report.xml # Speichere die Testberichte als Artefakt
    expire_in: 1 week # Lege fest, wie lange das Artefakt gespeichert wird
```

- Die Berichte können als **Download** im Job-Artefaktbereich zur Verfügung gestellt werden.

### 4. **Erweiterte Testberichte**

Falls du Tools wie **SonarQube** verwendest, können diese auch in GitLab integriert werden, um erweiterte Berichte zur Code-Qualität und Coverage anzuzeigen.

### Sichtbarkeit:

- Testberichte sind nach der Pipeline-Ausführung im **"Test" Tab** des jeweiligen Jobs sichtbar.
- **Code Coverage** wird direkt im Pipeline-Dashboard und Merge-Request-Übersicht angezeigt, wenn es konfiguriert ist.
