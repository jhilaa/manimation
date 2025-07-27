from manim import *
import random

class MonteCarloPiRepere(Scene):
    def construct(self):
        # Nombre de points à générer
        nb_points = 500

        # Création du repère
        axes = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False, "numbers_to_include": [-1, 0, 1]},
        )
        self.play(Create(axes))

        # Cercle unité centré en (0, 0)
        cercle = Circle(radius=axes.x_axis.unit_size, color=BLUE).move_to(axes.c2p(0, 0))
        self.play(Create(cercle))

        # Texte de l’estimation de pi
        pi_text = MathTex(r"\pi \approx").to_corner(UL)
        value_text = DecimalNumber(0, num_decimal_places=4).next_to(pi_text, RIGHT)
        self.add(pi_text, value_text)

        inside = 0
        points_to_add = []

        # Simulation
        for i in range(nb_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            # Point dans le cercle ?
            if x**2 + y**2 <= 1:
                color = GREEN
                inside += 1
            else:
                color = RED

            dot = Dot(point=axes.c2p(x, y), radius=0.03, color=color)
            points_to_add.append(dot)

            # Affichage tous les 50 points
            if i % 50 == 0 and i > 0:
                self.play(*[FadeIn(p) for p in points_to_add[-50:]], run_time=0.3)
                pi_estimate = 4 * inside / (i + 1)
                value_text.set_value(pi_estimate)

        # Affiche la valeur finale
        final_pi = 4 * inside / nb_points
        value_text.set_value(final_pi)
        self.wait(2)
