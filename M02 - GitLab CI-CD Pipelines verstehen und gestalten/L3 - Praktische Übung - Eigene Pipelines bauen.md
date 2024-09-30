
# Praktische Übung: Eigene Pipelines bauen

## Erstellen einer mehrstufigen CI/CD-Pipeline

Eine mehrstufige CI/CD-Pipeline in GitLab hilft dabei, den Entwicklungsprozess in klare Phasen zu unterteilen. Typische Stages sind Build, Test und Deploy, die nacheinander ausgeführt werden.

### Beispiel einer mehrstufigen Pipeline:
Erstelle oder bearbeite die Datei `.gitlab-ci.yml` im Wurzelverzeichnis deines Projekts und füge die folgenden Inhalte hinzu:
```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Building the project..."
    - make build

test-job:
  stage: test
  script:
    - echo "Running tests..."
    - make test

deploy-job:
  stage: deploy
  script:
    - echo "Deploying the project..."
    - make deploy
  environment:
    name: production
    url: https://production.example.com
```

### Schritte zur Implementierung:
1. **Definiere die Stages**: Jede Pipeline besteht aus mehreren Stages (z.B. `build`, `test`, `deploy`), die nacheinander ausgeführt werden.
2. **Erstelle Jobs für jede Stage**: Jobs sind die spezifischen Aufgaben innerhalb jeder Stage. Im obigen Beispiel gibt es einen Build-, Test- und Deploy-Job.
3. **Environment-Definition**: Der `deploy-job` definiert auch ein Ziel-Environment, das auf der Produktionsumgebung basiert.

Pushe die Datei in dein Repository, um die Pipeline in GitLab auszuführen:
```bash
git add .gitlab-ci.yml
git commit -m "Mehrstufige CI/CD-Pipeline hinzugefügt"
git push origin main
```

## Einbindung von GitLab Runner in die Pipeline

Ein GitLab Runner führt die Jobs deiner Pipeline aus. Es kann sich um eine lokale Maschine oder einen Cloud-Server handeln.

### Schritte zur Einbindung eines GitLab Runners:
1. **GitLab Runner Installation**:
   - Installiere den GitLab Runner auf deiner Maschine:
   ```bash
   sudo apt-get install gitlab-runner
   ```

2. **Runner registrieren**:
   - Um den Runner in dein GitLab-Projekt zu integrieren, registriere ihn:
   ```bash
   sudo gitlab-runner register
   ```
   - Gib die URL deiner GitLab-Instanz und den Token des Projekts ein, um den Runner zu verknüpfen.

3. **Runner-Typ auswählen**:
   - GitLab Runner unterstützt verschiedene Executor-Typen wie Shell, Docker und Kubernetes. Wähle den Executor, der für dein Projekt geeignet ist:
   ```bash
   Please enter the executor: shell, docker, etc.
   ```

4. **Runner für spezifische Pipelines verwenden**:
   - Du kannst den Runner in deiner `.gitlab-ci.yml` Datei direkt ansprechen:
   ```yaml
   build-job:
     stage: build
     script:
       - make build
     tags:
       - mein-runner
   ```

Der Job `build-job` wird nur auf dem Runner mit dem Tag `mein-runner` ausgeführt.

## Fehleranalyse und Optimierung von Pipelines

Manchmal schlagen Pipelines fehl, und es ist wichtig, den Grund zu identifizieren und zu beheben. GitLab bietet verschiedene Tools zur Fehleranalyse und Optimierung.

### Fehleranalyse:
1. **Logs überprüfen**:
   - Navigiere in GitLab zu "CI / CD" > "Pipelines" und wähle die fehlerhafte Pipeline aus.
   - Überprüfe die Ausgabe der Logs für jeden Job, um festzustellen, wo der Fehler aufgetreten ist.

2. **Fehlerhafte Schritte finden**:
   - Innerhalb der Logs wird der Fehler detailliert beschrieben. Häufige Ursachen sind fehlende Abhängigkeiten, Syntaxfehler oder fehlerhafte Befehle.

3. **Rerun-Option**:
   - GitLab bietet die Möglichkeit, fehlgeschlagene Jobs direkt aus der Pipeline-Ansicht erneut auszuführen, ohne die gesamte Pipeline neu zu starten.

### Optimierung:
1. **Cache verwenden**:
   - Um den Build-Prozess zu beschleunigen, kannst du Caching in der Pipeline verwenden:
   ```yaml
   cache:
     paths:
       - node_modules/
   ```

2. **Parallelisierung von Jobs**:
   - Jobs in der gleichen Stage können parallel ausgeführt werden. Nutze dies, um die Gesamtzeit der Pipeline zu reduzieren:
   ```yaml
   test-job-1:
     stage: test
     script:
       - make test-part1

   test-job-2:
     stage: test
     script:
       - make test-part2
   ```

3. **Artifacts für nachfolgende Stages**:
   - Speichere wichtige Dateien (z.B. Build-Ergebnisse) als Artifacts, um sie in nachfolgenden Stages verfügbar zu machen:
   ```yaml
   build-job:
     stage: build
     script:
       - make build
     artifacts:
       paths:
         - build/
   ```

## Fazit

Durch das Erstellen und Optimieren von mehrstufigen Pipelines kannst du den Entwicklungsprozess erheblich beschleunigen. Die Einbindung von GitLab Runnern und die Fehleranalyse-Tools ermöglichen es, Probleme schnell zu erkennen und zu beheben.
