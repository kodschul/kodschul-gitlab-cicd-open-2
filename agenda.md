### 1. **Grundlagen der GitLab-Pipelines**

- **Einführung in GitLab CI/CD**: Was ist CI/CD und wie funktioniert es in GitLab? Unterschiede zu bisherigen Tools wie TeamCity.
- **Aufbau einer einfachen Pipeline**: Wie man eine Pipeline in GitLab erstellt, von der Konfiguration der `.gitlab-ci.yml`-Datei bis zur Ausführung eines einfachen Jobs.
- **Automatisierung der Pipelines**: Was bedeutet Automatisierung und wie kann man wiederkehrende Prozesse in GitLab Pipelines automatisieren?
- **Erweiterung bestehender Pipelines**: Wie kann man bestehende Pipelines erweitern und in ein Gesamtkonzept integrieren? (z.B. durch stages, jobs, und dependencies)

### 2. **Fehlerbehebung bei GitLab-Pipelines**

- **Log-Analyse und Fehlerursachen finden**: Wie findet man heraus, warum ein Job in der Pipeline fehlschlägt? GitLab Logs verstehen und analysieren.
- **Typische Fehlerquellen in GitLab Pipelines**: Häufige Probleme und Best Practices zur Behebung.
- **Benachrichtigungen und Monitoring**: Automatisierte Benachrichtigungen bei Fehlern und Monitoring der Pipelines.

### 3. **Integration von Tests**

- **Automatisierte Unit Tests in Pipelines**: Wie man Unit Tests in die GitLab-Pipelines integriert. Konfiguration von Test-Suites und deren Ausführung innerhalb von Pipelines.
- **Beispiel für eine Testintegration**: Schritt-für-Schritt Aufbau einer Pipeline, die Unit Tests automatisiert ausführt.
- **Fehlerbehebung bei Tests**: Wie man fehlerhafte Tests in der Pipeline identifiziert und behebt. Vergleich mit TeamCity: Wo werden fehlerhafte Tests in GitLab angezeigt?

### 4. **Code Coverage und Qualitätssicherung**

- **Tools zur Codeabdeckung**: Welche Tools (z.B. `coverage.py` für Python oder `Jacoco` für Java) man mit GitLab CI integrieren kann, um die Codeabdeckung zu überprüfen.
- **Automatisierte Code Coverage Reports**: Wie man die Codeabdeckung in GitLab Pipelines misst und visualisiert. Vergleich mit TeamCity und entsprechende Ansichten in GitLab (z.B. Job Logs, Test Coverage Reports).
- **Testberichte und -analyse**: Automatische Generierung von Testberichten und deren Sichtbarmachung in der GitLab-Oberfläche.

### 5. **Erstellung einer Dokumentation für Pipelines**

- **Dokumentation der Schritte und Prozesse**: Wie man eine verständliche und nachhaltige Dokumentation für Pipelines erstellt. Was muss dokumentiert werden, damit alle IT-Mitarbeiter Änderungen vornehmen können?
- **Best Practices für Pipelines in der Teamarbeit**: Wie sichergestellt wird, dass alle Teammitglieder auf dem gleichen Stand sind und Änderungen leicht nachvollziehbar bleiben.

### 6. **Spezifische Unterschiede zu TeamCity**

- **Vergleich GitLab CI vs. TeamCity**: Unterschiede und Gemeinsamkeiten zwischen GitLab und TeamCity, insbesondere im Hinblick auf automatisierte Tests und Code Coverage.
- **Migration von TeamCity nach GitLab CI**: Tipps und Strategien für den Übergang von TeamCity zu GitLab, um die alten Workflows in das neue System zu übertragen.

### 7. **Praxisübungen**

- **Hands-on Session**: Praktische Übung, um eine vollständige GitLab-Pipeline zu erstellen, Unit Tests zu integrieren und die Ergebnisse zu analysieren.
- **Debugging-Szenarien**: Üben der Fehleranalyse und -behebung in Pipelines mit typischen Fehlerszenarien.
- **Erstellen und Erweitern einer Dokumentation**: Übung zur Erstellung einer einfachen Anleitung zur Pipeline-Konfiguration für Teammitglieder.
