from manim import *
from manim.utils.space_ops import rotate_vector

class CercleSurArc(Scene):
    def construct(self):
        rayon = 1

        # Création des cercles
        centre = LEFT * rayon
        cercle1 = Circle(radius=rayon, color=BLUE).move_to(centre)
        cercle2 = Circle(radius=rayon, color=GREEN).next_to(cercle1, RIGHT, buff=0)
        cercle3 = Circle(radius=rayon, color=RED).next_to(cercle1, UP, buff=0)

        brace1 = Brace (cercle1, direction=LEFT, buff=0.2)
        brace1_text = brace1.get_text("1")
        brace2 = Brace (cercle2, direction=DOWN, buff=0.2)
        brace2_text = brace2.get_text("1")
        brace3 = Brace (cercle3, direction=LEFT, buff=0.2)
        brace3_text = brace3.get_text("1")

        self.play(Create(cercle1), Create(cercle2),Create(cercle3))
        self.wait(0.5)
        self.play(FadeIn(brace1_text), GrowFromCenter(brace1), FadeIn(brace2_text),  GrowFromCenter(brace2), FadeIn(brace3_text), GrowFromCenter(brace3))
        self.wait(0.5)

        # Arc autour du cercle1, angle négatif pour aller vers la droite
        arc_path = Arc(
            radius=2 * rayon,
            angle=-PI / 6,  # ➜ rotation horaire (vers la droite)
            start_angle=PI / 2,  # départ en haut
            arc_center=cercle1.get_center()
        )

                # Arc autour du cercle1, angle négatif pour aller vers la droite
        arc_path_back = Arc(
            radius=2 * rayon,
            angle=PI / 6,  # ➜ rotation anti-horaire (vers la gauche)
            start_angle=PI / 3,  # On reprend au point d'arrivée
            arc_center=cercle1.get_center()
        )

        self.play(
            MoveAlongPath(cercle3, arc_path),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)

        self.play(
            MoveAlongPath(cercle3, arc_path_back),
            run_time=2,
            rate_func=smooth
        )

        self.wait(1)

        self.play(
            MoveAlongPath(cercle3, arc_path),
            run_time=2,
            rate_func=smooth
        )
        
        self.wait(1)
