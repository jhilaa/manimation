from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Crée un carré
        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        # Crée un cercle
        circle = Circle()
        circle.set_fill(RED, opacity=0.5)

        # Anime l’apparition du carré
        self.play(Create(square))
        self.wait(1)

        # Transforme le carré en cercle
        self.play(Transform(square, circle))
        self.wait(1)

        # Fait disparaître le cercle
        self.play(FadeOut(square))
