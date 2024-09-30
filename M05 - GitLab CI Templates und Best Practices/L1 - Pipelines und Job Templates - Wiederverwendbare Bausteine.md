
# Pipelines und Job Templates: Wiederverwendbare Bausteine

## Was sind CI/CD Templates und warum sind sie wichtig?

CI/CD Templates in GitLab sind vorgefertigte Konfigurationen für Pipelines und Jobs, die wiederverwendet werden können. Sie helfen dabei, Standards zu setzen und sich wiederholende Aufgaben zu vereinfachen, indem sie einmal erstellt und mehrfach in verschiedenen Projekten oder Pipelines genutzt werden können.

### Vorteile von Templates:
- **Wiederverwendbarkeit**: Einmal definierte Jobs und Pipelines können in mehreren Projekten verwendet werden, ohne sie jedes Mal neu erstellen zu müssen.
- **Konsistenz**: Templates ermöglichen es Teams, gleiche Standards für alle Projekte anzuwenden.
- **Zeitersparnis**: Sie sparen Zeit, da wiederkehrende Aufgaben durch automatisierte und standardisierte Templates ersetzt werden.

## Erstellung und Nutzung von Pipeline und Job Templates

### Erstellung eines Job Templates

Ein Job Template wird in einer eigenen `.yml` Datei definiert, die du dann in anderen Pipelines einbinden kannst. Hier ein Beispiel für ein Template, das den Build-Prozess definiert:

```yaml
# build_template.yml
.build-template:
  stage: build
  script:
    - echo "Building the project..."
    - make build
```

Dieses Template definiert einen generischen Build-Job, der später in anderen Projekten verwendet werden kann.

### Nutzung des Job Templates in einer Pipeline

In einer Pipeline kannst du das erstellte Template wie folgt referenzieren:

```yaml
stages:
  - build

include:
  - local: 'build_template.yml'

build-job:
  extends: .build-template
```

Durch die `extends`-Direktive kannst du auf das definierte Template zugreifen und es in deiner Pipeline nutzen. Das Template wird eingebunden und der Job `build-job` verwendet alle Definitionen aus `.build-template`.

### Erstellung eines Pipeline Templates

Neben Job Templates können auch komplette Pipelines als Templates erstellt werden, um sie in verschiedenen Projekten zu nutzen. Hier ein Beispiel für ein Pipeline Template:

```yaml
# pipeline_template.yml
stages:
  - build
  - test

build-job:
  stage: build
  script:
    - echo "Building the project..."

test-job:
  stage: test
  script:
    - echo "Running tests..."
```

Dieses Pipeline-Template definiert eine Pipeline mit zwei Stages (build und test). Es kann ebenfalls in anderen Projekten eingebunden werden.

### Nutzung eines Pipeline Templates

Ähnlich wie bei den Job Templates kannst du ein Pipeline-Template einbinden:

```yaml
include:
  - local: 'pipeline_template.yml'
```

Durch diese `include`-Direktive wird das Pipeline-Template in die aktuelle `.gitlab-ci.yml` Datei eingefügt und direkt verwendet.

## Praktische Übung: Eigene Templates erstellen und testen

### Schritt 1: Eigenes Job Template erstellen

Erstelle eine neue Datei `custom_job_template.yml` im Root-Verzeichnis deines Projekts mit folgendem Inhalt:

```yaml
.custom-job-template:
  stage: deploy
  script:
    - echo "Deploying the project..."
    - ./deploy.sh
```

### Schritt 2: Nutzung des Job Templates

In der `.gitlab-ci.yml`-Datei deines Projekts referenziere das erstellte Template:

```yaml
stages:
  - deploy

include:
  - local: 'custom_job_template.yml'

deploy-job:
  extends: .custom-job-template
```

### Schritt 3: Pipeline testen

Nachdem du das Template erstellt und eingebunden hast, führe die Pipeline durch das Pushen der Änderungen aus:

```bash
git add custom_job_template.yml .gitlab-ci.yml
git commit -m "Job Template für Deployment hinzugefügt"
git push origin main
```

Gehe in deinem GitLab-Projekt zur CI/CD Pipeline-Seite, um zu sehen, wie die Pipeline das neue Template verwendet.

### Schritt 4: Anpassung und Wiederverwendung

Passe das Template nach Bedarf an und binde es in anderen Projekten ein. Dies ist besonders nützlich, wenn du standardisierte Jobs wie Builds, Tests oder Deployments in mehreren Projekten einheitlich nutzen möchtest.

## Fazit

Templates sind eine mächtige Möglichkeit, um Pipelines und Jobs in GitLab effizient zu gestalten. Sie helfen dabei, Arbeitsprozesse zu standardisieren und zu automatisieren, und ermöglichen die Wiederverwendung von bewährten CI/CD-Konfigurationen in verschiedenen Projekten. Durch die Übung hast du gelernt, wie du eigene Templates erstellst, nutzt und testest.
