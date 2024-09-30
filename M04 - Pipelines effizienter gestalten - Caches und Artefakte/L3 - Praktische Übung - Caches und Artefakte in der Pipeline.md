
# Praktische Übung: Caches und Artefakte in der Pipeline

## Implementierung von Caches und Artefakten in einer laufenden Pipeline

In GitLab CI/CD können **Caches** und **Artefakte** verwendet werden, um die Effizienz und Performance der Pipelines zu verbessern. Caches speichern häufig verwendete Abhängigkeiten zwischen Jobs, während Artefakte Build-Ergebnisse für spätere Stages oder für die Benutzer bereitstellen.

### Caches implementieren
Caches können verwendet werden, um Abhängigkeiten wie Node Modules, Maven-Repositories oder andere Bibliotheken zwischen verschiedenen Pipeline-Läufen wiederzuverwenden.

Beispiel einer Pipeline mit Cache:
```yaml
stages:
  - build
  - test

build-job:
  stage: build
  cache:
    paths:
      - node_modules/
  script:
    - npm install
    - npm run build

test-job:
  stage: test
  cache:
    paths:
      - node_modules/
  script:
    - npm test
```
In diesem Beispiel wird der `node_modules`-Ordner zwischengespeichert, um zu vermeiden, dass npm-Abhängigkeiten in jedem Pipeline-Lauf neu installiert werden müssen.

### Artefakte implementieren
Artefakte ermöglichen das Speichern von Dateien, die nach einem Job generiert wurden, und die Bereitstellung dieser Dateien für nachfolgende Stages oder für den Download.

Beispiel einer Pipeline mit Artefakten:
```yaml
stages:
  - build
  - deploy

build-job:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/

deploy-job:
  stage: deploy
  script:
    - echo "Deploying..."
    - ls dist/
  artifacts:
    when: on_success
```
In diesem Beispiel wird der `dist/`-Ordner nach dem Build-Prozess als Artefakt gespeichert und in der Deploy-Stage verwendet.

## Fehleranalyse: Häufige Probleme und ihre Lösung

### Problem 1: Cache wird nicht korrekt verwendet
- **Fehlerbeschreibung**: Der Cache wird zwischen verschiedenen Pipelines nicht verwendet, was zu langen Installationszeiten führt.
- **Lösung**: Stelle sicher, dass der Cache korrekt definiert ist und dass die Cache-Key-Einstellungen korrekt sind, insbesondere wenn der Cache für mehrere Jobs verwendet wird.
  ```yaml
  cache:
    key: "$CI_COMMIT_REF_SLUG"
    paths:
      - node_modules/
  ```

### Problem 2: Artefakte werden nicht gespeichert
- **Fehlerbeschreibung**: Artefakte sind nach dem Job nicht verfügbar oder wurden nicht richtig gespeichert.
- **Lösung**: Überprüfe, ob die Artefakte korrekt definiert sind und ob der Pfad, den du als Artefakt speichern möchtest, existiert.
  ```yaml
  artifacts:
    paths:
      - build/
  ```

### Problem 3: Pipeline schlägt bei der Verwendung von Caches/Artefakten fehl
- **Fehlerbeschreibung**: Die Pipeline bricht ab, wenn auf Caches oder Artefakte zugegriffen wird.
- **Lösung**: Stelle sicher, dass die entsprechenden Verzeichnisse tatsächlich in vorherigen Jobs erstellt wurden und die Berechtigungen korrekt sind.

## Optimierung der Performance durch Caching und Artefakt-Management

Caching und Artefakte spielen eine entscheidende Rolle bei der Optimierung der Performance von Pipelines. Hier sind einige Ansätze zur Verbesserung der Effizienz:

1. **Gezieltes Caching**: Vermeide es, große oder unnötige Dateien zu cachen. Nutze den Cache für Build-Abhängigkeiten und Bibliotheken, die sich selten ändern.
   - Beispiel:
     ```yaml
     cache:
       paths:
         - .m2/repository/
     ```

2. **Strategischer Einsatz von Artefakten**: Artefakte sollten nur dann gespeichert werden, wenn sie in späteren Stages benötigt werden oder wenn sie für den Benutzer relevant sind. Überflüssige Artefakte können Speicherplatz verschwenden und die Pipeline verlangsamen.

3. **Cache Invalidierung**: Manchmal müssen Caches invalidiert werden, wenn sich Abhängigkeiten ändern. Dies kann durch den Einsatz dynamischer Cache-Schlüssel erreicht werden.
   ```yaml
   cache:
     key: "$CI_COMMIT_REF_SLUG"
     paths:
       - node_modules/
   ```

4. **Artefakte zeitlich begrenzen**: Um Speicherplatz zu sparen, können Artefakte mit einer Ablaufzeit versehen werden:
   ```yaml
   artifacts:
     expire_in: 1 week
   ```

Durch eine effiziente Nutzung von Caches und Artefakten kannst du die Laufzeiten deiner Pipeline erheblich verkürzen und die Gesamteffizienz steigern.

## Fazit

Die Implementierung von Caches und Artefakten in GitLab CI/CD Pipelines ermöglicht es, den Entwicklungsprozess zu beschleunigen und ressourcenschonender zu gestalten. Durch gezielte Optimierungen und Fehleranalysen können häufige Probleme gelöst und die Performance der Pipeline maximiert werden.
