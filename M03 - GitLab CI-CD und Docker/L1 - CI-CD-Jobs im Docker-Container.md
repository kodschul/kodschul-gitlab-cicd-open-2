
# Grundlagen: CI/CD-Jobs im Docker-Container

## Docker und GitLab CI: Warum Containerisierung wichtig ist

Containerisierung mit Docker ermöglicht es, Anwendungen isoliert und reproduzierbar in einer Umgebung auszuführen. In GitLab CI/CD spielt Docker eine wichtige Rolle, da es die Ausführung von Jobs in genau definierten Umgebungen ermöglicht. Einige Vorteile der Containerisierung in CI/CD sind:

- **Isolierung**: Jeder CI-Job läuft in einem eigenen Container, der von den restlichen Jobs und der Host-Umgebung unabhängig ist.
- **Reproduzierbarkeit**: Docker-Container ermöglichen es, dasselbe Setup auf verschiedenen Systemen zu reproduzieren, unabhängig von den lokalen Umgebungen der Entwickler.
- **Flexibilität**: Durch die Verwendung verschiedener Docker-Images können CI-Jobs in unterschiedlichen Umgebungen (z.B. verschiedene Betriebssysteme, Programmiersprachen-Versionen) ausgeführt werden.

GitLab CI unterstützt die Ausführung von Pipelines in Docker-Containern und stellt dabei sicher, dass jede Pipeline dieselben Voraussetzungen erfüllt.

## Docker-Images in GitLab CI Pipelines erstellen

Ein häufiger Anwendungsfall in CI/CD-Pipelines ist das Erstellen eines Docker-Images. Dies kann notwendig sein, um Anwendungen in einem Docker-Container zu verpacken, der anschließend bereitgestellt wird. Hier ein Beispiel, wie ein Docker-Image in einer GitLab CI Pipeline erstellt werden kann.

### Beispiel `.gitlab-ci.yml` zum Erstellen eines Docker-Images:
```yaml
image: docker:latest

services:
  - docker:dind

stages:
  - build

variables:
  DOCKER_DRIVER: overlay2

before_script:
  - docker info

build-docker-image:
  stage: build
  script:
    - docker build -t mein-image:latest .
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
    - docker tag mein-image:latest $CI_REGISTRY/dein-projekt/mein-image:latest
    - docker push $CI_REGISTRY/dein-projekt/mein-image:latest
```

In diesem Beispiel:
- **`docker:latest`** wird als Basis-Image für die Pipeline verwendet.
- **`docker:dind`** (Docker in Docker) wird als Service gestartet, damit Docker-Befehle innerhalb der CI-Pipeline ausgeführt werden können.
- Der Job erstellt ein Docker-Image aus dem `Dockerfile` im Projektverzeichnis und pusht es in die GitLab Container Registry.

## Docker-Container in CI/CD-Pipelines starten und stoppen

Manchmal ist es notwendig, Docker-Container innerhalb von CI-Jobs zu starten und zu stoppen, beispielsweise für Integrationstests oder die Ausführung von Diensten. Auch hierfür kann Docker in GitLab CI verwendet werden.

### Beispiel `.gitlab-ci.yml` zum Starten eines Containers:
```yaml
image: docker:latest

services:
  - docker:dind

stages:
  - test

variables:
  DOCKER_DRIVER: overlay2

before_script:
  - docker info

test-container:
  stage: test
  script:
    - docker run -d --name test-container -p 8080:80 mein-image:latest
    - echo "Container gestartet, führe Tests aus..."
    - curl http://localhost:8080
    - docker stop test-container
    - docker rm test-container
```

In diesem Beispiel:
- Ein Docker-Container wird mit dem zuvor erstellten Image gestartet.
- Der Job testet, ob der Container korrekt läuft (in diesem Fall durch einen einfachen `curl`-Befehl).
- Nach den Tests wird der Container gestoppt und entfernt.

### Weitere nützliche Docker-Befehle in CI/CD:
- **docker-compose**: Mit Docker Compose können mehrere Container als ein Verbund gestartet werden. Dies kann in komplexeren Pipelines nützlich sein, in denen mehrere Services (z.B. Datenbank, Webserver) benötigt werden.
- **docker exec**: Dieser Befehl kann verwendet werden, um Kommandos innerhalb eines laufenden Containers auszuführen.

```yaml
services:
  - docker:dind

script:
  - docker exec -it test-container /bin/bash -c "ls /app"
```

Mit diesem Befehl wird ein Kommando (`ls /app`) innerhalb des Containers ausgeführt, was für Debugging-Zwecke nützlich sein kann.

## Fazit

Durch die Verwendung von Docker in GitLab CI/CD-Pipelines lassen sich reproduzierbare und isolierte Umgebungen schaffen. Docker ermöglicht es, Software zu bauen, zu testen und bereitzustellen, ohne dass die Entwicklerumgebung die Ergebnisse beeinflusst. Das Erstellen und Verwalten von Docker-Containern innerhalb von CI/CD-Pipelines ist eine Schlüsseltechnik für moderne DevOps-Workflows.
