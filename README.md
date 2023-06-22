# CE-Projekt

## Setup

Clone das Repository und öffne es mit PyCharm oder einer anderen Python IDE. Die IDE sollte dich fragen, ob du dir eine
neue Conda Umgebung einrichten willst. Mach dies und lass dir eine aus der ``environment.yml`` Datei erstellen.

Solltest du bereits eine eigene Umgebung habe und die willst diese nutzen, stelle sicher, dass alle Pakete die du im
Code neu hinzugefügt hast auch in der ``environment.yml`` enthalten sind. So hat jeder die gleiche Version von den
Paketen und es kann nicht zu blöden Fehlern kommen, weil wir mit unterschiedlichen Versionen arbeiten.

Des Weiteren muss noch ``pip install pyqt6 pyside6`` installiert werden. Bei Problemen kann auch statt ``pip`` conda
verwendet werden, um die Bibliotheken zu installieren.

## Use

Um das Projekt zu starten, führe die ``__main__.py`` in ``craneSimulator/`` aus. Klicke auf **File > Open** und wähle
die Datei ``exampleCrane.xml`` aus. Diese enthält eine beispielhafte Konfiguration der Optionen, welche unter 
**Optionen** eingestellt werden können.

![img.png](resources/img.png)

## Update environment.yml

Um manuell installierte Pakete zu der environment.yml hinzuzufügen führe folgenden
Befehl ``conda env export --from-history > environment.yml`` in einer Konsole aus, mit der aktivierten Conda
Umgebung ``ce-project``. Schaue in der ``environment.yml`` Datei nach, diese sollte aktualisiert worden sein, entferne
die unterste Zeile mit dem ``prefix:`` und committe die Änderungen.

## Oder

Nutze die Python-Installation die schon auf deinem Rechner ist solange diese Numpy und PyQT6 hat
