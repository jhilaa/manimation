from manim import *

class RepereAvecAxes(Scene):
    def construct(self):
        # Création du repère orthonormé
        axes = Axes(
            x_range=[-5, 5, 1],       # de -5 à 5 avec un pas de 1
            y_range=[-3, 3, 1],       # de -3 à 3 avec un pas de 1
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True}  # Ajoute les valeurs sur les axes
        )

        # Création d'un point (2, 1)
        point = Dot(axes.c2p(2, 1), color=RED)  # c2p = coordonnées cartésiennes → coordonnées pixel

        # Ajout d'un label pour le point
        label = MathTex(r"(2,\ 1)").next_to(point, UR, buff=0.2)

        # Animation
        self.play(Create(axes))
        self.wait(0.5)
        self.play(FadeIn(point), Write(label))
        self.wait(1)
