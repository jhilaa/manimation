from manim import *

class HelloScene(Scene):
    def construct(self):
        texte = Text("Coucou Manim !", font_size=72)
        self.play(Write(texte))
        self.wait(1)
        # Garde la fenêtre ouverte à la fin
        # input("Appuyez sur Entrée pour fermer...")

class NewScene(Scene):
    def construct(self):
        texte = Text("2ème chance", font_size=72)
        self.play(Write(texte))
        self.wait(1)
        # Garde la fenêtre ouverte à la fin
        input("Appuyez sur Entrée pour fermer...")

