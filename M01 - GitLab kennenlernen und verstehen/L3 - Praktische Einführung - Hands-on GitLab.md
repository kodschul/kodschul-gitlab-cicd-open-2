
# Praktische Einführung: Hands-on GitLab

## Git Repository erstellen und initialisieren

GitLab bietet eine einfache Möglichkeit, ein Git Repository zu erstellen und mit der Versionskontrolle zu beginnen.

### Schritte zur Erstellung eines Git-Repositories:
1. **Neues Projekt in GitLab anlegen**:
   - Gehe auf die GitLab-Plattform und klicke auf "Neues Projekt".
   - Wähle die Option für ein leeres Repository und gib einen Projektnamen ein.

2. **Repository lokal klonen**:
   ```bash
   git clone https://gitlab.com/benutzername/dein-projekt.git
   cd dein-projekt
   ```

3. **Erste Datei hinzufügen und Commit ausführen**:
   ```bash
   echo "# Mein erstes GitLab-Projekt" >> README.md
   git add README.md
   git commit -m "Erstes Commit"
   git push origin main
   ```

### Repository-Struktur
Nachdem das Repository erstellt und lokal geklont wurde, kannst du Dateien und Ordner hinzufügen und Versionskontrolle durchführen.

## Erste einfache CI/CD Pipeline erstellen und ausführen

Um die Vorteile von CI/CD zu nutzen, kannst du eine einfache Pipeline in GitLab erstellen. Dies erfolgt durch das Hinzufügen einer `.gitlab-ci.yml` Datei im Wurzelverzeichnis deines Projekts.

### Beispiel einer minimalen Pipeline:
Erstelle eine Datei namens `.gitlab-ci.yml` und füge folgende Inhalte hinzu:
```yaml
stages:
  - build

build-job:
  stage: build
  script:
    - echo "Building the project..."
```

### Schritte zur Ausführung der Pipeline:
1. **Erstelle die Datei**:
   ```bash
   touch .gitlab-ci.yml
   ```

2. **Füge die Pipeline-Konfiguration ein**:
   ```yaml
   stages:
     - build

   build-job:
     stage: build
     script:
       - echo "Building the project..."
   ```

3. **Datei hinzufügen und pushen**:
   ```bash
   git add .gitlab-ci.yml
   git commit -m "Erste CI/CD Pipeline hinzugefügt"
   git push origin main
   ```

4. **Pipeline in GitLab ausführen**:
   - Sobald der Code in GitLab gepusht wird, startet GitLab automatisch die Pipeline. Du kannst den Status der Pipeline unter "CI / CD" > "Pipelines" in deinem Projekt einsehen.

## Praktische Übung: GitLab Umgebung erkunden

Um die Funktionen von GitLab zu erkunden, kannst du folgende Aufgaben durchführen:

1. **Erstelle einen neuen Branch**:
   - Branches helfen dabei, verschiedene Feature-Entwicklungen voneinander zu trennen.
   ```bash
   git checkout -b feature-branch
   git push origin feature-branch
   ```

2. **Erstelle einen Merge Request (MR)**:
   - Ein Merge Request ist ein zentraler Bestandteil der Zusammenarbeit in GitLab. Er ermöglicht es, Code-Änderungen zu überprüfen, bevor sie in den Hauptbranch gemerged werden.
   - Gehe zu "Merge Requests" > "Neuen Merge Request erstellen" und wähle deinen Branch aus.

3. **Erkunde das CI/CD Menü**:
   - Gehe in dein Projekt und navigiere zu "CI/CD" > "Pipelines", um die Ergebnisse der zuvor erstellten Pipeline zu überprüfen.
   - Du kannst detaillierte Logs für jeden Job einsehen, den Fortschritt der Pipeline überwachen und Fehlermeldungen analysieren.

4. **Experimentiere mit GitLab Features**:
   - Erkunde weitere Funktionen wie das integrierte Issue-Tracking, das Einrichten eines Wikis für die Dokumentation oder das Erstellen von Releases für deine Software.

## Fazit

Diese Einführung bietet einen praktischen Überblick über die Verwendung von GitLab zur Erstellung von Repositories und CI/CD-Pipelines sowie zur Erkundung der verschiedenen Werkzeuge, die GitLab für eine effiziente Softwareentwicklung bietet.
