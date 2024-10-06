# Anleitung: Self-hosted GitLab Runner mit Docker Compose

## Schritt 1: Installation von Docker und Docker Compose

Falls Docker und Docker Compose noch nicht installiert sind, folge diesen Schritten:

- **Docker installieren**:

  ```bash
  sudo apt update
  sudo apt install docker.io -y
  sudo systemctl start docker
  sudo systemctl enable docker
  ```

- **Docker Compose installieren**:
  ```bash
  sudo apt install docker-compose -y
  ```

## Schritt 2: Erstellen einer Docker Compose Datei

Erstelle ein Verzeichnis für die GitLab Runner-Konfiguration und wechsle in dieses Verzeichnis:

```bash
mkdir gitlab-runner
cd gitlab-runner
```

Erstelle dann die `docker-compose.yml`-Datei:

```bash
nano docker-compose.yml
```

Füge den folgenden Inhalt ein, um den GitLab Runner-Dienst zu definieren:

```yaml
version: "3"

services:
  gitlab-runner:
    image: gitlab/gitlab-runner:latest
    container_name: gitlab_runner
    restart: always
    volumes:
      - "./config:/etc/gitlab-runner" # Konfigurationsordner für den Runner
      - "/var/run/docker.sock:/var/run/docker.sock" # Für Docker-in-Docker
```

### Erklärung:

- Das offizielle GitLab Runner Docker-Image wird verwendet.
- Die Konfigurationsdateien werden im Verzeichnis `./config` auf deinem Host gespeichert.
- Der Docker-Socket wird gemountet, damit der Runner Docker für die Jobausführung verwenden kann.

## Schritt 3: Docker Compose starten

Starte den GitLab Runner mit Docker Compose:

```bash
docker-compose up -d
```

Der GitLab Runner wird nun im Hintergrund ausgeführt.

## Schritt 4: GitLab Runner registrieren

Jetzt musst du den Runner mit deinem GitLab-Projekt registrieren:

- **Token abrufen**:

  - Gehe in dein GitLab-Projekt.
  - Navigiere zu **Einstellungen > CI/CD > Runners**.
  - Unter **"Richte einen spezifischen Runner manuell ein"** findest du den **Registrierungs-Token**.

- **Runner registrieren**:
  Führe den folgenden Befehl aus, um den Runner im Container zu registrieren:

  ```bash
  docker exec -it gitlab_runner gitlab-runner register
  ```

  Folge den Anweisungen:

  - **GitLab URL**: Gib die URL deiner GitLab-Instanz ein (z.B. `https://gitlab.com`).
  - **Registrierungstoken**: Füge den Token aus deinem Projekt ein.
  - **Beschreibung**: Gib eine Beschreibung für den Runner ein (z.B. "Docker Runner").
  - **Tags**: Optional kannst du Tags hinzufügen, um den Runner bestimmten Jobs zuzuweisen.
  - **Executor**: Wähle `docker` als Executor.
  - **Standard-Docker-Image**: Gib ein Standard-Image für deine Jobs an (z.B. `alpine:latest` oder `python:3.9`).

## Schritt 5: Konfiguration des Runners anpassen

Nach der Registrierung wird eine Konfigurationsdatei im Ordner `config` unter `config/config.toml` erstellt. Diese Datei kann angepasst werden, um das Verhalten des Runners zu steuern.

Hier ist ein Beispiel für eine `config.toml`-Datei:

```toml
[[runners]]
  name = "docker-runner"
  url = "https://gitlab.com/"
  token = "dein-registrierungstoken"
  executor = "docker"
  [runners.custom_build_dir]
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = true  # Notwendig für Docker-in-Docker
    disable_entrypoint_overwrite = false
    oom_kill_disable = false
    disable_cache = false
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
    shm_size = 0
  [runners.cache]
    [runners.cache.s3]
    [runners.cache.gcs]
```

## Schritt 6: Den Runner in der Pipeline verwenden

Nachdem der Runner registriert ist, wird er im Abschnitt **Runners** deines GitLab-Projekts angezeigt. Du kannst ihn jetzt verwenden, um Jobs in deiner CI/CD-Pipeline auszuführen.

Beispiel einer `.gitlab-ci.yml`-Datei, um den Runner zu verwenden:

```yaml
stages:
  - build
  - test

build_job:
  stage: build
  script:
    - echo "Building the project"
  tags:
    - docker # Passende Tags für den Runner

test_job:
  stage: test
  script:
    - echo "Running tests"
  tags:
    - docker
```

Achte darauf, dass die **Tags** in der `.gitlab-ci.yml`-Datei den Tags entsprechen, die du bei der Runner-Registrierung verwendet hast.

## Schritt 7: Den Runner überwachen und verwalten

Du kannst die Aktivität des Runners direkt in GitLab unter **CI/CD > Runners** überwachen. Hier siehst du, ob der Runner aktiv ist und welche Jobs er ausgeführt hat.

## Schritt 8: Den Runner stoppen und neu starten

- Um den GitLab Runner zu **stoppen**, führe aus:

  ```bash
  docker-compose down
  ```

- Um den Runner **neu zu starten**, führe aus:
  ```bash
  docker-compose up -d
  ```
