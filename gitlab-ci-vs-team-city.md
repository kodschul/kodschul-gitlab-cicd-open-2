# GitLab CI vs. TeamCity Vergleich

## 1. Plattform und Integration

- **GitLab CI**:

  - Nahtlos in GitLab integriert (Version Control, Issue Tracking, CI/CD).
  - YAML-basierte Pipelines direkt im Repository (`.gitlab-ci.yml`).

- **TeamCity**:
  - Eigenständiger CI/CD-Server, der mit verschiedenen VCS (Git, GitHub, Bitbucket) integriert werden kann.
  - Web-basierte Pipeline-Konfiguration mit DSL-Unterstützung (z.B. Kotlin DSL).

---

## 2. Konfigurationsdateien

### GitLab CI `.gitlab-ci.yml`

```yaml
stages:
  - build
  - test

build_job:
  stage: build
  script:
    - echo "Building the application"

test_job:
  stage: test
  script:
    - echo "Running tests"
```

- **Stichpunkte GitLab CI**:
  - Pipelines werden in einer `.gitlab-ci.yml` Datei versioniert.
  - Konfiguration direkt im Repository, wodurch Änderungen an der Pipeline nachvollziehbar sind.

### TeamCity Kotlin DSL

```kotlin
version = "2022.04"

project {
    buildType(Build)
}

object Build : BuildType({
    name = "Build"

    steps {
        script {
            scriptContent = "echo 'Building the application'"
        }
    }
})
```

- **Stichpunkte TeamCity**:
  - Build-Definitionen können mit Kotlin DSL in Code geschrieben werden.
  - Standardmäßig werden Pipelines über die Web-Oberfläche konfiguriert.

---

## 3. Benutzeroberfläche und Benutzerfreundlichkeit

- **GitLab CI**:
  - Vollständig integriert in die GitLab-Plattform.
  - Einfach zu bedienen für GitLab-Nutzer, keine separate Installation nötig.
- **TeamCity**:
  - Web-basierte Konfiguration, geeignet für komplexe Pipelines, aber steilere Lernkurve.
  - Erfordert Setup für VCS-Integration und Build Agents.

---

## 4. Skalierbarkeit und Ressourcenverwaltung

- **GitLab CI**:

  - Nutzt **GitLab Runner**, der auf verschiedenen Plattformen installiert werden kann (lokal, VM, Cloud).
  - Cloud-Runner (GitLab SaaS) und self-hosted Optionen verfügbar.

- **TeamCity**:
  - Verwendet **Build Agents** zur Ausführung von Builds, erfordert manuelles Setup.
  - Lizenziert nach Anzahl der Agenten, was bei vielen Builds kostspielig werden kann.

---

## 5. Build Pipelines (Stages und Jobs)

### GitLab CI Pipeline

```yaml
stages:
  - build
  - test

build_job:
  stage: build
  script:
    - echo "Building the application"

test_job:
  stage: test
  script:
    - echo "Running tests"
```

- **Stichpunkte GitLab CI**:
  - Pipelines bestehen aus **Stages** und **Jobs**.
  - Jobs innerhalb einer Stage laufen parallel, Stages laufen sequentiell.

### TeamCity Build Chain (via Web-UI)

- **Stichpunkte TeamCity**:
  - **Build Chains** definieren die Reihenfolge der Builds.
  - Build-Ketten sind detailliert, aber die Konfiguration ist komplexer als in GitLab.

---

## 6. Testintegration und Codeabdeckung

### GitLab CI Unit Test Integration

```yaml
test_job:
  stage: test
  script:
    - pytest --junitxml=report.xml
  artifacts:
    when: always
    reports:
      junit: report.xml
```

- **Stichpunkte GitLab CI**:
  - Automatische Test- und Codeabdeckungsberichte direkt in der Pipeline.
  - YAML-Konfiguration ermöglicht einfache Integration von Test-Tools wie `pytest`.

### TeamCity Unit Test Integration

```kotlin
steps {
    script {
        scriptContent = "pytest --junitxml=report.xml"
    }
}
```

- **Stichpunkte TeamCity**:
  - Detaillierte Testberichte und Codeabdeckung in der Oberfläche verfügbar.
  - Testintegration ähnlich wie in GitLab, erfordert jedoch Plugins für spezifische Tools.

---

## 7. Kosten und Lizenzierung

- **GitLab CI**:

  - Kostenlose Version verfügbar (GitLab Core), Premium-Funktionen sind kostenpflichtig.
  - Keine separate Lizenz für CI/CD erforderlich.

- **TeamCity**:
  - Kostenlose Version auf eine begrenzte Anzahl von **Build Agents** beschränkt.
  - Kostenpflichtige Lizenzen für mehr Agenten.

---

## 8. Sicherheit und Compliance

- **GitLab CI**:

  - Bietet integrierte Sicherheits- und Compliance-Tools (z.B. Dependency Scanning, DAST).
  - Native Unterstützung für DevSecOps.

- **TeamCity**:
  - Weniger native Sicherheitsfeatures, aber erweiterbar über Plugins.
  - Sicherheits- und Compliance-Tests müssen oft extern integriert werden.

---

## Fazit

- **GitLab CI** ist ideal für Teams, die bereits GitLab nutzen und eine nahtlose CI/CD-Integration wünschen. Es ist einfacher zu konfigurieren und eignet sich für kleinere und mittlere Projekte.
- **TeamCity** ist leistungsstärker und besser geeignet für größere, komplexe Projekte mit unterschiedlichen Anforderungen, erfordert jedoch mehr Setup und Wartung.
