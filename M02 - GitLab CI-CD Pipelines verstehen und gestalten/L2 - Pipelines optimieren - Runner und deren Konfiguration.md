
# Pipelines optimieren: Runner und deren Konfiguration

## GitLab Runner: Arten und Anwendungsfälle

Ein GitLab Runner ist eine Anwendung, die CI/CD-Jobs von GitLab ausführt. Er kann auf verschiedenen Plattformen installiert werden und bietet unterschiedliche Ausführungsumgebungen. Es gibt zwei Hauptarten von GitLab Runnern:

1. **Shared Runner**:
   - Diese Runner stehen mehreren Projekten innerhalb einer GitLab-Instanz zur Verfügung. Sie sind ideal für kleinere Projekte oder Teams, die keine eigenen Runner verwalten wollen.

2. **Dedicated/Private Runner**:
   - Diese Runner sind für bestimmte Projekte oder Gruppen reserviert und bieten eine höhere Kontrolle über die Ausführungsumgebung. Sie eignen sich für größere Teams oder Projekte mit speziellen Anforderungen.

### Anwendungsfälle:
- **Shared Runner**: Für allgemeine Zwecke und kleinere Projekte, die keine spezielle Ausführungsumgebung benötigen.
- **Dedicated Runner**: Für Projekte mit spezifischen Anforderungen, z.B. wenn spezielle Software oder Libraries in der Pipeline benötigt werden.

## Installation und Konfiguration von GitLab Runner

Die Installation eines GitLab Runners ist relativ einfach und kann auf verschiedenen Betriebssystemen und Umgebungen erfolgen.

### Installation auf einem Linux-Server:

1. **GitLab Runner installieren**:
   ```bash
   sudo apt-get update
   sudo apt-get install gitlab-runner
   ```

2. **Runner registrieren**:
   Nach der Installation musst du den Runner bei einem GitLab-Projekt registrieren. Dies erfolgt mit dem folgenden Befehl:
   ```bash
   sudo gitlab-runner register
   ```
   Dabei wirst du aufgefordert, folgende Informationen anzugeben:
   - **GitLab URL**: Die URL deines GitLab-Servers (z.B. `https://gitlab.com`).
   - **Token**: Das Token für den Runner, das in den GitLab-Projekteinstellungen unter `CI / CD` > `Runner` zu finden ist.
   - **Executor**: Wähle den Executor-Typ, z.B. `shell`, `docker`, etc.

3. **Runner konfigurieren**:
   Die Konfiguration des Runners erfolgt in der Datei `/etc/gitlab-runner/config.toml`. Hier kannst du z.B. den Executor-Typ, Umgebungsvariablen und Caching-Optionen anpassen.

### Beispiel für die `config.toml`:
```toml
[[runners]]
  name = "my-runner"
  url = "https://gitlab.com/"
  token = "your-token"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.docker]
    image = "alpine:latest"
    privileged = true
    volumes = ["/cache"]
  [runners.cache]
    path = "/tmp/cache"
```

In diesem Beispiel wird ein Docker-Executor verwendet, der Builds in einer `alpine`-Umgebung ausführt. Caching wird aktiviert, um Zwischenergebnisse zu speichern und spätere Builds zu beschleunigen.

## Best Practices: Effiziente Pipeline-Strategien entwickeln

Um effiziente und performante Pipelines zu erstellen, gibt es einige Best Practices, die beachtet werden sollten:

### 1. **Parallele Jobs und Stages**:
   - Nutze die Möglichkeit, Jobs parallel auszuführen, um die Pipeline-Laufzeiten zu verkürzen. Jobs, die voneinander unabhängig sind, können gleichzeitig laufen.
   ```yaml
   test-job1:
     stage: test
     script:
       - run-tests.sh

   test-job2:
     stage: test
     script:
       - run-more-tests.sh
   ```

### 2. **Caching und Artifacts**:
   - Verwende Caching, um Abhängigkeiten oder Build-Artefakte zwischen verschiedenen Pipeline-Läufen zu speichern. Dies kann die Ausführungszeit von Builds erheblich reduzieren.
   ```yaml
   cache:
     paths:
       - node_modules/
   ```

### 3. **Spezifische Runner für bestimmte Aufgaben**:
   - Verwende spezielle Runner für Jobs, die besondere Anforderungen haben (z.B. Docker-Builds oder besondere Hardwareanforderungen). Dies kann helfen, die Ausführungsumgebung besser zu kontrollieren und Ressourcen effizienter zu nutzen.

### 4. **Vermeide unnötige Job-Ausführungen**:
   - Durch die Verwendung von `only` und `except` kannst du festlegen, dass bestimmte Jobs nur unter bestimmten Bedingungen ausgeführt werden. So sparst du Ressourcen, indem du z.B. Tests nur auf bestimmten Branches oder bei bestimmten Änderungen durchführst.
   ```yaml
   test-job:
     script:
       - npm test
     only:
       - main
   ```

### 5. **Fehler frühzeitig erkennen (Fail Fast)**:
   - Setze Jobs, die kritische Fehler früh im Prozess erkennen (z.B. Syntax-Checks oder Linting), an den Anfang der Pipeline. Dies spart Zeit, da die Pipeline bei einem Fehler frühzeitig abgebrochen wird.
   ```yaml
   lint-job:
     stage: lint
     script:
       - npm run lint
     allow_failure: false
   ```

## Fazit

GitLab Runner sind ein wichtiger Bestandteil der CI/CD-Pipelines und ermöglichen die Automatisierung des Entwicklungsprozesses. Durch eine sorgfältige Konfiguration und die Anwendung von Best Practices kannst du deine Pipelines effizienter gestalten und die Ressourcen optimal nutzen.
