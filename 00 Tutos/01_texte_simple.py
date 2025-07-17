from manim import *

class TexteSimple(Scene):
    def construct(self):
        texte = Text("Bonjour Manim !", font_size=72)
        self.play(Write(texte))
        self.wait(1)
