from manim import *
from manim.utils.space_ops import rotate_vector

class CercleSurArc(Scene):
    def construct(self):
        rayon = 1

        # Création des cercles
        centre = LEFT * rayon
        cercle1 = Circle(radius=rayon, color=WHITE).move_to(centre)
        cercle2 = Circle(radius=rayon, color=WHITE).next_to(cercle1, RIGHT, buff=0)
        cercle3 = Circle(radius=rayon, color=WHITE).next_to(cercle1, UP, buff=0)

        # Brace 1
        brace1 = Brace(cercle1, direction=LEFT, buff=0.2, color=WHITE)
        brace1_text = brace1.get_text("1").set_color(WHITE)

        # Brace 2
        brace2 = Brace(cercle2, direction=DOWN, buff=0.2, color=WHITE)
        brace2_text = brace2.get_text("1").set_color(WHITE)

        # Brace 3 + texte + groupe + updater propre
        brace3 = Brace(cercle3, direction=LEFT, buff=0.2, color=RED)
        brace3_text = brace3.get_text("1").set_color(RED)
        brace3_group = VGroup(brace3, brace3_text)
        # Updater du groupe : suit le Y de cercle3, X fixe
        brace3_group_x = brace3_group.get_x()
        brace3_group.add_updater(lambda g: g.move_to([brace3_group_x, cercle3.get_y(), 0]))

        # Création des cercles
        self.play(Create(cercle1), Create(cercle2), Create(cercle3))
        self.wait(0.5)
        #self.play(cercle3.animate.set_color(RED))
        #self.wait(0.5)
        self.play(
            cercle3.animate.set_color(RED),
            FadeIn(brace1_text), GrowFromCenter(brace1),
            FadeIn(brace2_text), GrowFromCenter(brace2),
            FadeIn(brace3_group)
        )
        self.wait(0.5)

        # Définition des arcs
        arc_path = Arc(
            radius=2 * rayon,
            angle=-PI / 6,
            start_angle=PI / 2,
            arc_center=cercle1.get_center()
        )
        arc_path_back = Arc(
            radius=2 * rayon,
            angle=PI / 6,
            start_angle=PI / 3,
            arc_center=cercle1.get_center()
        )

        self.play(MoveAlongPath(cercle3, arc_path), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(MoveAlongPath(cercle3, arc_path_back), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(MoveAlongPath(cercle3, arc_path), run_time=2, rate_func=smooth)
        self.wait(1)

        # Zoom final
        all_objs = VGroup(cercle1, cercle2, cercle3, brace1, brace1_text, brace2, brace2_text, brace3, brace3_text)
        self.play(all_objs.animate.scale(2.5).move_to(ORIGIN), run_time=2)
        self.wait(1)

        
        # Ligne horizontale depuis la base de brace3 (vers la droite)
        ligne_brace3 = DashedLine(
            brace3.get_bottom() - RIGHT * 1,
            brace3.get_bottom() + RIGHT * 12,
            color=RED
        )

        # Ligne horizontale depuis le haut de brace2 (vers la droite)
        ligne_brace1 = DashedLine(
            brace1.get_top() - RIGHT * 1,
            brace1.get_top() + RIGHT * 12,
            color=WHITE
        )
        self.play(Create(ligne_brace3), Create(ligne_brace1))
        self.wait(1)

        # Position X de la flèche : légèrement avant la fin des dashlines
        x_pos = cercle3.get_center()[0]

        # Points de départ et d’arrivée
        start_point = [x_pos, ligne_brace1.get_y(), 0]
        end_point   = [x_pos, ligne_brace3.get_y(), 0]

        # Ligne verticale avec flèche
        ligne_verticale = DoubleArrow(
            start=start_point,
            end=end_point,
            buff=0,
            stroke_width=2,
            color=YELLOW,
            tip_length=0.2
        )

        # Légende "x"
        label_x = MathTex("x").next_to(ligne_verticale, RIGHT, buff=0.1).set_color(YELLOW)
        # Animation de tracé de la ligne (comme un "expand")
        self.play(GrowArrow(ligne_verticale), FadeIn(label_x))
        self.wait(6)