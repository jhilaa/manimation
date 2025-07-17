from manim import *

class Equation(Scene):
    def construct(self):
        eq1 = MathTex("x^2 + 2x + 1")
        eq2 = MathTex("(x + 1)^2")

        self.play(Write(eq1))
        self.wait(1)
        self.play(Transform(eq1, eq2))
        self.wait(1)
