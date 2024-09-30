
# Artefakte: Ergebnisse nachhaltig sichern und bereitstellen

## Was sind Artefakte in GitLab CI?

Artefakte in GitLab CI sind Dateien oder Verzeichnisse, die während der Ausführung einer Pipeline erzeugt werden und für nachfolgende Jobs oder für die Bereitstellung wichtig sind. Sie ermöglichen die Übertragung von Zwischenergebnissen zwischen Jobs oder Pipelines und können genutzt werden, um beispielsweise Build-Artefakte, Testergebnisse oder Deployment-Pakete zu speichern.

### Beispiele für Artefakte:
- Kompilierte Programme oder ausführbare Dateien
- Testberichte und Coverage-Daten
- Log-Dateien oder Protokolle
- Docker-Images oder andere Container-Artefakte

## Artefakte im Repository sichern und nutzen

Die Sicherung von Artefakten erfolgt in GitLab CI durch die Konfiguration der `.gitlab-ci.yml` Datei. Hier kann festgelegt werden, welche Dateien oder Verzeichnisse nach der Ausführung eines Jobs als Artefakte gespeichert werden sollen.

### Beispiel: Artefakte in einer Pipeline definieren
In folgendem Beispiel wird der Build-Ordner als Artefakt gespeichert, damit er in nachfolgenden Jobs genutzt werden kann.

```yaml
stages:
  - build
  - test

build-job:
  stage: build
  script:
    - mkdir build
    - echo "Building project..." > build/output.txt
  artifacts:
    paths:
      - build/

test-job:
  stage: test
  script:
    - echo "Running tests..."
    - cat build/output.txt
```

### Erklärung:
- Der `build-job` erstellt ein Verzeichnis namens `build` und speichert eine Textdatei darin.
- Durch die `artifacts`-Direktive wird das Verzeichnis `build` als Artefakt gespeichert und steht dem `test-job` zur Verfügung.
- Im `test-job` wird der Inhalt der Datei `output.txt` aus dem `build`-Ordner ausgegeben.

Artefakte können auch für das Deployment genutzt werden, um Builds oder Pakete auf einen Server oder eine Produktionsumgebung zu übertragen.

## Praktische Übung: Artefakte effizient verwalten und deployen

Um die Verwaltung von Artefakten zu üben, kannst du folgende Aufgaben durchführen:

1. **Artefakte in einer Pipeline konfigurieren**:
   - Erstelle eine Pipeline, die Build-Artefakte speichert und in einem nachfolgenden Job verwendet. Verwende dazu die `artifacts`-Direktive in deiner `.gitlab-ci.yml` Datei.

   Beispiel:
   ```yaml
   stages:
     - build
     - deploy

   build-job:
     stage: build
     script:
       - echo "Compiling project..."
       - mkdir dist
       - echo "Build completed" > dist/build.txt
     artifacts:
       paths:
         - dist/

   deploy-job:
     stage: deploy
     script:
       - echo "Deploying project..."
       - cat dist/build.txt
   ```

2. **Artefakte zwischen verschiedenen Stages nutzen**:
   - Stelle sicher, dass Artefakte, die in einem Job erzeugt wurden, auch in späteren Stages zugänglich sind. Du kannst dies testen, indem du in einem Deploy-Job auf das Ergebnis eines Build-Jobs zugreifst.

3. **Artefakte zur Bereitstellung verwenden**:
   - In einem realen Szenario kannst du Artefakte wie kompilierte Anwendungen oder Docker-Images bereitstellen, indem du sie in eine Produktionsumgebung überträgst oder auf einem Server bereitstellst.

4. **Artefakte automatisch löschen**:
   - Du kannst GitLab so konfigurieren, dass Artefakte nach einer bestimmten Zeit automatisch gelöscht werden, um Speicherplatz zu sparen:
   ```yaml
   artifacts:
     expire_in: 1 week
   ```

   Dies würde die Artefakte eine Woche nach ihrer Erstellung automatisch entfernen.

## Fazit

Artefakte sind ein essenzieller Bestandteil von GitLab CI/CD, um Zwischenergebnisse und Build-Artefakte zu sichern und zwischen Jobs zu teilen. Durch die korrekte Verwaltung von Artefakten können Entwicklungsprozesse optimiert und die Bereitstellung von Software effizient gestaltet werden.
