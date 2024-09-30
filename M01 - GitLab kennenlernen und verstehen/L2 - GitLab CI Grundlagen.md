## Was ist Continuous Integration und Delivery?

**Continuous Integration (CI)** ist der Entwicklungsansatz, bei dem Codeänderungen häufig in das zentrale Repository integriert und automatisch getestet werden. Ziel ist es, potenzielle Konflikte frühzeitig zu erkennen und zu beheben. CI trägt dazu bei, die Qualität des Codes zu verbessern und die Bereitstellung neuer Features zu beschleunigen.

**Continuous Delivery (CD)** erweitert CI um die Automatisierung der Bereitstellung (Deployment) von Software. Durch CD wird sichergestellt, dass die Software jederzeit in einem zustellbaren Zustand ist und nach jedem erfolgreichen Build ausgeliefert werden kann.

### Vorteile von CI/CD
- Automatisierung wiederkehrender Aufgaben
- Erhöhte Codequalität durch frühzeitige Fehlererkennung
- Schnellere Iterationen durch kontinuierliche Tests und Deployments
- Reduzierung des manuellen Aufwands bei der Bereitstellung

## Grundlagen zu Pipelines in GitLab CI

Eine Pipeline ist eine Abfolge von Jobs, die auf verschiedenen Stages ausgeführt werden. Pipelines in GitLab bestehen typischerweise aus den folgenden Stages:

1. **Build**: Kompilieren des Quellcodes oder Erstellen eines Docker-Images.
2. **Test**: Ausführen automatisierter Tests zur Sicherstellung der Codequalität.
3. **Deploy**: Bereitstellung des Codes in einer Test-, Staging- oder Produktionsumgebung.

Jede Pipeline wird durch eine Datei namens `.gitlab-ci.yml` definiert, die sich im Wurzelverzeichnis des Projekts befindet.

Beispiel einer Pipeline mit mehreren Stages:
```yaml
stages:
  - build
  - test
  - deploy

build-job:
  stage: build
  script:
    - echo "Building the project"
    - make build

test-job:
  stage: test
  script:
    - echo "Running tests"
    - make test

deploy-job:
  stage: deploy
  script:
    - echo "Deploying the project"
    - make deploy
```

### Stages und Jobs
- **Stages**: Repräsentieren die verschiedenen Phasen im CI/CD-Prozess (z.B. build, test, deploy).
- **Jobs**: Jeder Stage sind Jobs zugeordnet, die nacheinander oder parallel ausgeführt werden. Ein Job enthält Anweisungen, die den Code kompilieren, testen oder bereitstellen.

## Der erste Blick auf das .gitlab-ci.yml-File

Die `.gitlab-ci.yml` Datei definiert die gesamte Pipeline. Sie ist in YAML geschrieben und beschreibt die Stages, Jobs und Skripte, die ausgeführt werden. Jede Datei kann für unterschiedliche Zwecke angepasst werden, um spezifische Anforderungen an Builds, Tests und Deployments zu erfüllen.

Beispiel für eine einfache `.gitlab-ci.yml`-Datei:
```yaml
stages:
  - build
  - test

build-job:
  stage: build
  script:
    - echo "Starting build process..."
    - npm install
    - npm run build

test-job:
  stage: test
  script:
    - echo "Running tests..."
    - npm test
```

In diesem Beispiel:
- Es gibt zwei Stages: **build** und **test**.
- Der `build-job` installiert die Abhängigkeiten und baut das Projekt.
- Der `test-job` führt die Tests aus, um sicherzustellen, dass der Code korrekt funktioniert.

### Häufige Direktiven in `.gitlab-ci.yml`
- `stages`: Definiert die verschiedenen Phasen der Pipeline.
- `script`: Gibt die Befehle an, die in einem Job ausgeführt werden.
- `only`: Beschränkt den Job auf bestimmte Branches oder Bedingungen (z.B. nur auf dem Hauptbranch).
- `artifacts`: Speichert Dateien, die nach der Ausführung eines Jobs für nachfolgende Jobs benötigt werden.

```yaml
artifacts:
  paths:
    - build/
```

Dies würde den Inhalt des `build`-Ordners nach Abschluss des Jobs speichern.

## Fazit

GitLab CI/CD ermöglicht es Teams, den Softwareentwicklungsprozess durch Automatisierung zu beschleunigen und die Qualität zu verbessern. Die Pipelines und das `.gitlab-ci.yml`-File bilden die Grundlage für diese Automatisierung und bieten eine flexible Möglichkeit, den Entwicklungszyklus effizient zu gestalten.
