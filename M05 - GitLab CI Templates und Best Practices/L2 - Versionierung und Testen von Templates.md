
# Versionierung und Testen von Templates

## Versionsmanagement für Templates in GitLab

Das Versionsmanagement von CI/CD-Templates ist ein entscheidender Bestandteil für die Wiederverwendung und Wartung von Pipelines. Durch die Versionierung von Templates können Änderungen im Laufe der Zeit verfolgt und verschiedene Versionen verwendet werden, ohne dass die Kompatibilität zwischen Projekten verloren geht.

### Schritte zur Versionierung von Templates:

1. **Template-Repository anlegen**:
   - Erstelle ein separates GitLab-Repository, in dem die CI/CD-Templates verwaltet werden. Dies kann als zentrales Repository für verschiedene Projekte dienen.

2. **Versionskontrolle durch Tags**:
   - Nutze Git-Tags, um stabile Versionen der Templates zu kennzeichnen:
   ```bash
   git tag v1.0
   git push origin v1.0
   ```
   - Tags ermöglichen es, spezifische Versionen eines Templates in anderen Projekten zu referenzieren.

3. **Verwendung von Versionen in Projekten**:
   - In den `.gitlab-ci.yml`-Dateien anderer Projekte können Templates wie folgt referenziert werden:
   ```yaml
   include:
     - project: 'namespace/template-repository'
       file: '/path/to/template.yml'
       ref: 'v1.0'
   ```
   - Durch den `ref`-Parameter kannst du sicherstellen, dass eine bestimmte Version des Templates verwendet wird.

## Testing von Templates für fehlerfreie Pipelines

Um sicherzustellen, dass CI/CD-Templates fehlerfrei funktionieren, ist es wichtig, diese vor der Verteilung gründlich zu testen. GitLab bietet verschiedene Möglichkeiten, Templates lokal oder auf separaten Testpipelines zu testen, bevor sie in Produktionsprojekten genutzt werden.

### Schritte zum Testen von Templates:

1. **Lokales Testen mit Docker**:
   - GitLab Runner kann lokal mit Docker betrieben werden, um Templates zu testen, ohne dass diese sofort in GitLab verwendet werden müssen.
   ```bash
   gitlab-runner exec docker <job-name>
   ```

2. **Testpipeline in separatem Projekt**:
   - Lege ein Testprojekt in GitLab an, um Templates in einer isolierten Umgebung zu testen. Führe die Pipeline mit dem Template durch und überprüfe die Logs auf Fehler:
   ```yaml
   include:
     - project: 'namespace/template-repository'
       file: '/path/to/template.yml'
       ref: 'v1.0'

   test-job:
     stage: test
     script:
       - echo "Testing the template"
   ```

3. **Automatisiertes Testing**:
   - Richte automatisierte Tests für die Templates ein. Sobald Änderungen an einem Template vorgenommen werden, kann eine Pipeline gestartet werden, um diese Änderungen zu validieren. Dies stellt sicher, dass Änderungen keine unerwarteten Fehler verursachen.

## Praktische Übung: Versionierung und Testen von CI/CD-Templates

Um das Gelernte anzuwenden, führen wir eine praktische Übung zur Versionierung und zum Testen von CI/CD-Templates durch.

### Übungsaufgabe 1: Versionierung von Templates
1. **Erstelle ein Repository** für CI/CD-Templates und füge dein erstes Template hinzu:
   ```yaml
   stages:
     - build

   build-template:
     stage: build
     script:
       - echo "Building the project from template..."
   ```

2. **Versioniere das Template**, indem du einen Tag setzt:
   ```bash
   git tag v1.0
   git push origin v1.0
   ```

3. **Nutze das Template in einem anderen Projekt**, indem du die Template-Datei in der `.gitlab-ci.yml` des neuen Projekts referenzierst:
   ```yaml
   include:
     - project: 'namespace/template-repository'
       file: '/templates/build-template.yml'
       ref: 'v1.0'
   ```

### Übungsaufgabe 2: Testen von Templates
1. **Erstelle eine Testpipeline** in einem separaten Testprojekt, um sicherzustellen, dass dein Template wie erwartet funktioniert.
2. **Ändere das Template** und führe Tests durch, um zu überprüfen, ob die Änderungen korrekt implementiert wurden.
3. **Erstelle automatisierte Tests**, die bei jeder Änderung des Templates ausgeführt werden und die Funktionalität sicherstellen.

## Fazit

Die Versionierung und das Testen von CI/CD-Templates sind wesentliche Schritte, um sicherzustellen, dass wiederverwendbare Pipelines stabil und fehlerfrei bleiben. Durch das korrekte Management von Template-Versionen und die Implementierung von Tests können Teams sicherstellen, dass ihre Automatisierung zuverlässig und skalierbar ist.
