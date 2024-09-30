
# Die Architektur einer CI/CD-Pipeline

## Aufbau und Bestandteile des .gitlab-ci.yml-Files

Das `.gitlab-ci.yml`-File ist das Herzstück einer GitLab CI/CD-Pipeline. Es steuert, wie und wann die verschiedenen Phasen einer Pipeline ausgeführt werden. Jede Pipeline besteht aus einer Reihe von definierten Stages, Jobs und Steps, die der Automatisierung von Build-, Test- und Deployment-Prozessen dienen.

### Grundlegender Aufbau
Das `.gitlab-ci.yml`-File ist in YAML geschrieben und beginnt mit der Definition von Stages und den Jobs, die in diesen Stages ausgeführt werden sollen.

Beispiel eines einfachen `.gitlab-ci.yml`-Files:
```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Building the project..."

test-job:
  stage: test
  script:
    - echo "Running tests..."

deploy-job:
  stage: deploy
  script:
    - echo "Deploying the project..."
```

In diesem Beispiel gibt es drei Stages: **build**, **test** und **deploy**, und für jede Stage gibt es einen Job, der einen spezifischen Schritt im Entwicklungsprozess ausführt.

## Wichtige Schlüsselwörter: Stages, Jobs und Steps

### Stages
- **Stages** repräsentieren die Hauptphasen einer Pipeline, z.B. **build**, **test** und **deploy**.
- Alle Jobs in einer Stage werden entweder parallel oder seriell (abhängig von Abhängigkeiten) ausgeführt. Die Pipeline bewegt sich erst zur nächsten Stage, wenn alle Jobs der vorherigen Stage abgeschlossen sind.

Beispiel für die Definition von Stages:
```yaml
stages:
  - build
  - test
  - deploy
```

### Jobs
- **Jobs** sind die eigentlichen Aufgaben, die in einer Stage ausgeführt werden. Jeder Job enthält ein `script`, das die auszuführenden Befehle definiert.
- Jobs können zusätzliche Parameter enthalten, wie z.B. `only` (um Jobs nur unter bestimmten Bedingungen auszuführen) oder `artifacts` (um Dateien zwischen Jobs zu teilen).

Beispiel eines Jobs:
```yaml
build-job:
  stage: build
  script:
    - echo "Building the project..."
```

### Steps (Script)
- **Steps** sind die Befehle innerhalb eines Jobs, die nacheinander ausgeführt werden. Diese Befehle sind in der `script`-Sektion eines Jobs definiert.
- Steps können einfache Shell-Befehle, Skripte oder komplexere Aktionen wie das Erstellen von Docker-Containern oder das Ausführen von Tests umfassen.

Beispiel für mehrere Steps in einem Job:
```yaml
test-job:
  stage: test
  script:
    - echo "Running unit tests..."
    - echo "Checking code coverage..."
```

## Pipeline Builds und Trigger: Automatisierte Abläufe gestalten

### Builds
Ein **Build** ist eine vollständige Ausführung aller definierten Stages und Jobs in einer Pipeline. Jedes Mal, wenn neuer Code in ein Repository gepusht wird, startet GitLab automatisch einen neuen Build, der die Pipeline durchläuft.

Beispiel:
```yaml
build-job:
  stage: build
  script:
    - echo "Compiling code..."
```

### Trigger
**Trigger** steuern, wann eine Pipeline ausgeführt wird. Sie können manuell, automatisch durch Code-Änderungen oder durch externe Systeme ausgelöst werden.

#### Automatische Trigger durch `push`-Events
Jedes Mal, wenn Code in das Repository gepusht wird, wird die Pipeline automatisch ausgeführt. Du kannst jedoch den Trigger steuern, um beispielsweise Pipelines nur auf bestimmten Branches oder bei Merge Requests auszuführen.

Beispiel:
```yaml
test-job:
  stage: test
  script:
    - echo "Running tests..."
  only:
    - main
```
In diesem Fall wird der Job nur ausgeführt, wenn der Code in den `main`-Branch gepusht wird.

#### Manuelle Trigger
Du kannst auch manuelle Trigger in deine Pipelines integrieren, um bestimmte Jobs oder Pipelines nur bei Bedarf auszuführen.

```yaml
deploy-job:
  stage: deploy
  script:
    - echo "Deploying the project..."
  when: manual
```

In diesem Fall wird der `deploy-job` nur dann ausgeführt, wenn er manuell gestartet wird.

## Fazit

Die Architektur einer GitLab CI/CD-Pipeline bietet flexible und mächtige Tools zur Automatisierung von Build-, Test- und Deployment-Prozessen. Durch die richtige Definition von Stages, Jobs und Triggers kannst du komplexe Abläufe gestalten, die eine effiziente und fehlerfreie Softwareentwicklung sicherstellen.
