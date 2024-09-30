
# Pipeline Caches: Performance-Booster für deine Pipelines

## Was sind Pipeline Caches und wie funktionieren sie?

Pipeline Caches sind ein leistungsfähiges Werkzeug in CI/CD-Systemen, das darauf abzielt, den Build-Prozess zu beschleunigen. Sie ermöglichen es, Dateien oder Abhängigkeiten zwischen verschiedenen Jobs oder Pipelines zu speichern und wiederzuverwenden, sodass diese nicht bei jedem Durchlauf neu erstellt oder heruntergeladen werden müssen.

### Funktionsweise:
- Ein Cache speichert Dateien oder Verzeichnisse, die während eines Jobs generiert werden (z.B. Node.js-Abhängigkeiten, kompilierte Dateien oder Docker-Layer).
- Bei einem späteren Pipeline-Durchlauf können diese Dateien wiederverwendet werden, wodurch die Ausführungszeit der Jobs erheblich reduziert wird.
- Caches sind besonders nützlich für große Projekte mit umfangreichen Build-Prozessen oder externen Abhängigkeiten, die regelmäßig wiederverwendet werden.

Beispiel:
```yaml
cache:
  key: dependencies
  paths:
    - node_modules/
```
In diesem Beispiel wird der Inhalt des `node_modules`-Ordners nach dem Job zwischengespeichert und in zukünftigen Jobs wiederverwendet.

## Best Practices: Caches in CI/CD richtig nutzen

### 1. **Caches effizient einsetzen**
   - Verwende Caches für große, sich selten ändernde Dateien oder Abhängigkeiten, die über mehrere Jobs hinweg konstant bleiben.
   - Setze Cache-Keys, um den Cache nur zu verwenden, wenn sich die entsprechenden Dateien nicht geändert haben.

### 2. **Verwende eindeutige Cache-Keys**
   - Verwende eindeutige Cache-Keys, die auf den Inhalt eines Verzeichnisses oder eines Abhängigkeitsmanagers basieren, um sicherzustellen, dass nur relevante Caches wiederverwendet werden.
   - Beispiel für einen Cache-Key auf Basis der `package-lock.json` Datei:
     ```yaml
     cache:
       key: "$CI_COMMIT_REF_SLUG-$CI_JOB_NAME"
       paths:
         - node_modules/
     ```

### 3. **Caches regelmäßig aktualisieren**
   - Caches sollten regelmäßig invalidiert werden, um sicherzustellen, dass veraltete oder fehlerhafte Abhängigkeiten nicht wiederverwendet werden. Dies kann z.B. über ein Ablaufdatum geschehen.
   - Beispiel:
     ```yaml
     cache:
       key: dependencies
       paths:
         - node_modules/
       policy: pull-push
       expire_in: 1 week
     ```

### 4. **Caches zwischen Jobs teilen**
   - Caches können zwischen verschiedenen Jobs in derselben Pipeline oder sogar zwischen Pipelines geteilt werden. Dies ist besonders nützlich, wenn verschiedene Stages wie Build, Test und Deploy die gleichen Abhängigkeiten nutzen.
   - Beispiel:
     ```yaml
     build-job:
       stage: build
       cache:
         paths:
           - node_modules/

     test-job:
       stage: test
       cache:
         paths:
           - node_modules/
     ```

## Praktische Übung: Implementierung von Caches in der Pipeline

### Schritt 1: Cache in der .gitlab-ci.yml Datei hinzufügen
In dieser Übung fügen wir einen Cache zu einem einfachen Node.js-Projekt hinzu. Ziel ist es, die `node_modules` nach dem ersten Build zu speichern und in den folgenden Jobs wiederzuverwenden.

```yaml
stages:
  - build
  - test

cache:
  key: "$CI_COMMIT_REF_SLUG"
  paths:
    - node_modules/

build-job:
  stage: build
  script:
    - npm install

test-job:
  stage: test
  script:
    - npm test
```

### Schritt 2: Pipeline ausführen
- Push die `.gitlab-ci.yml` Datei in dein GitLab-Projekt.
- GitLab wird die Pipeline ausführen und den Cache für `node_modules` beim ersten Durchlauf speichern.
- Bei den folgenden Pipeline-Durchläufen wird der Cache verwendet, um die Installationszeit für Abhängigkeiten zu verkürzen.

### Schritt 3: Cache-Überprüfung
- Gehe zu deinem GitLab-Projekt unter **CI/CD** > **Pipelines** und überprüfe die Logs des `build-job` und `test-job`.
- Du wirst sehen, dass der Cache beim ersten Lauf erstellt und bei den nachfolgenden Läufen wiederverwendet wird.

## Fazit

Pipeline Caches sind ein einfaches und effektives Mittel, um die Laufzeit von CI/CD-Pipelines zu reduzieren. Durch das Speichern und Wiederverwenden von Dateien und Abhängigkeiten können wiederkehrende Aufgaben wie das Installieren von Abhängigkeiten oder das Kompilieren von Code deutlich beschleunigt werden. Mit den Best Practices und der praktischen Übung kannst du Caches effizient in deinen Projekten einsetzen.
