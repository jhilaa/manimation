✅ 1. Créer un nouvel environnement virtuel avec Python 3.11
Ouvre PowerShell ou un terminal VS Code, place-toi dans le bon dossier :

cd "D:\Utilisateurs\julie\Dropbox\Ada Tech School\06 Projets\13 Manimations"

Puis crée un nouvel environnement avec Python 3.11 :
C:\Python311\python.exe -m venv .venv
(⚠️ adapte le chemin C:\Python311\python.exe si tu l’as installé ailleurs — tu peux aussi tester avec py -3.11 à la place)

✅ 2. Active l’environnement virtuel
Toujours dans ce même terminal :
.\.venv\Scripts\activate
Tu devrais voir ton invite changer en :

(.venv) PS D:\Utilisateurs\julie\...
✅ 3. Installer Manim (enfin sans erreur 😄)
powershell
Copier
Modifier
python -m pip install --upgrade pip
python -m pip install manim
Tu peux ensuite vérifier que tout est OK avec :

powershell
Copier
Modifier
manim -v
Tu dois voir quelque chose comme :

nginx
Copier
Modifier
Manim Community v0.18.0.post0
✅ 4. Ouvrir dans VS Code et lier l’environnement
Ouvre le dossier 13 Manimations dans VS Code

En bas à droite, clique sur l’interpréteur Python si ce n’est pas encore .venv

Ou fais Ctrl+Shift+P → Python: Select Interpreter → choisis .venv

Crée (ou vérifie) le fichier .vscode/tasks.json :

json
Copier
Modifier
{
"version": "2.0.0",
"tasks": [
{
"label": "Lancer Manim",
"type": "shell",
"command": ".venv\\Scripts\\manim.exe",
"args": [
"--renderer=opengl",
"-pql",
"${file}"
],
"group": {
"kind": "build",
"isDefault": true
}
}
]
}
✅ 5. Test final
Crée un fichier 00_test.py dans un sous-dossier

Colle-y un exemple minimal :

python
Copier
Modifier
from manim import \*

class HelloScene(Scene):
def construct(self):
text = Text("Hello, Manim!")
self.play(Write(text))
Ouvre ce fichier dans l’éditeur

Appuie sur Ctrl+B → une fenêtre vidéo doit apparaître 🎥
