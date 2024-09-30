
# Beispiele aus der Praxis: CI/CD mit Docker

## Best Practices für die Integration von Docker in CI/CD-Pipelines

Die Verwendung von Docker in CI/CD-Pipelines bietet eine hohe Flexibilität und Konsistenz, da jeder Job in einer isolierten Umgebung läuft. Hier sind einige Best Practices, um Docker effizient in GitLab CI zu integrieren:

1. **Nutze spezialisierte Docker-Images**:
   - Verwende Images, die spezifisch für deine Build-Umgebung sind. Dies reduziert den Aufwand für die Installation von Abhängigkeiten.
   ```yaml
   image: node:14
   stages:
     - build
     - test

   build-job:
     stage: build
     script:
       - npm install
       - npm run build
   ```

2. **Caches verwenden**:
   - Verwende Cache-Mechanismen, um den Build-Prozess zu beschleunigen und wiederholte Downloads von Abhängigkeiten zu vermeiden.
   ```yaml
   cache:
     paths:
       - node_modules/
   ```

3. **Mehrere Stages nutzen**:
   - Teile deine Pipeline in Stages auf, z.B. für Build, Test und Deployment. Dies ermöglicht eine bessere Trennung und übersichtlichere Pipelines.

4. **Saubere Container-Umgebungen**:
   - Verwende immer saubere Docker-Umgebungen, um sicherzustellen, dass keine unerwarteten Abhängigkeiten oder Artefakte aus früheren Builds vorhanden sind.

## Sicherheit und Optimierung von Docker-basierten Pipelines

Sicherheit spielt eine zentrale Rolle, wenn Docker in CI/CD-Pipelines eingesetzt wird. Hier sind einige Optimierungen und Sicherheitsaspekte, die berücksichtigt werden sollten:

1. **Vermeide den Einsatz von Root-Benutzern in Containern**:
   - Es ist eine Best Practice, Container nicht als `root` laufen zu lassen. Stelle sicher, dass dein Dockerfile einen spezifischen Benutzer definiert:
   ```dockerfile
   FROM node:14
   RUN useradd -ms /bin/bash appuser
   USER appuser
   ```

2. **Verwende minimalistische Basis-Images**:
   - Reduziere die Angriffsfläche, indem du möglichst kleine und spezialisierte Docker-Images verwendest (z.B. `alpine`).
   ```yaml
   image: node:14-alpine
   ```

3. **Regelmäßige Sicherheitsupdates**:
   - Stelle sicher, dass Docker-Images regelmäßig aktualisiert werden, um Sicherheitslücken zu schließen.

4. **Docker Layer Caching nutzen**:
   - Optimiere die Pipeline-Performance, indem du Caching für Docker-Layer verwendest. Dies beschleunigt Builds und reduziert die Ressourcennutzung.
   ```yaml
   docker:
     services:
       - docker:dind

   build-job:
     stage: build
     script:
       - docker build -t myapp .
   ```

5. **Umgang mit sensiblen Daten**:
   - Vermeide es, sensible Daten wie Zugangsdaten direkt in der Pipeline oder im Dockerfile zu hinterlegen. Verwende GitLab CI-Umweltvariablen oder Secrets für die sichere Handhabung.

## Praktische Übung: Docker-Container in GitLab CI verwenden

In dieser Übung wirst du lernen, wie man Docker-Container in GitLab CI einsetzt, um Builds und Tests durchzuführen.

### Schritte zur Implementierung einer Docker-basierten Pipeline:

1. **.gitlab-ci.yml Datei anlegen**:
   Erstelle eine `.gitlab-ci.yml` Datei im Root-Verzeichnis deines Projekts.
   ```yaml
   image: docker:20.10

   services:
     - docker:dind

   stages:
     - build
     - test

   variables:
     DOCKER_DRIVER: overlay2

   build-job:
     stage: build
     script:
       - docker build -t myapp .

   test-job:
     stage: test
     script:
       - docker run myapp npm test
   ```

2. **Docker Image in der Pipeline bauen**:
   In der `build-job` Stage wird ein Docker Image gebaut. Dies geschieht innerhalb der Docker-in-Docker (DinD) Umgebung.

3. **Container für Tests nutzen**:
   Der `test-job` startet das erstellte Docker-Image und führt die Tests innerhalb eines Containers aus. Dies stellt sicher, dass die Tests in einer konsistenten Umgebung ausgeführt werden.

### Optional: Push des Images in eine Registry

Falls du das erstellte Docker-Image in eine Registry wie die GitLab Container Registry pushen möchtest, kannst du folgende Erweiterung in die Pipeline integrieren:

```yaml
deploy-job:
  stage: deploy
  script:
    - docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" $CI_REGISTRY
    - docker tag myapp $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:latest
```

Hierbei wird das erstellte Docker-Image nach erfolgreichem Build in die Registry hochgeladen.

## Fazit

Die Integration von Docker in GitLab CI/CD ermöglicht flexible und skalierbare Pipelines, die in isolierten Containern laufen. Best Practices wie die Verwendung von spezialisierten Images, Sicherheitsrichtlinien und die Optimierung durch Caching tragen dazu bei, eine performante und sichere Pipeline zu gewährleisten.
