from manim import *

class CarreVersCercle(Scene):
    def construct(self):
        carre = Square()
        carre.set_fill(BLUE, opacity=0.5)

        cercle = Circle()
        cercle.set_fill(RED, opacity=0.5)

        self.play(Create(carre))
        self.wait(1)
        self.play(Transform(carre, cercle))
        self.wait(1)
        self.play(FadeOut(cercle))
