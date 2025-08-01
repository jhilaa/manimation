from manim import *
from manim.utils.space_ops import rotate_vector

class CercleSurArc(Scene):
    def construct(self):
        rayon = 1.3
        Line.set_default(stroke_width=2)
        Circle.set_default(stroke_width=2)
        Dot.set_default(stroke_width=1)
        DashedLine.set_default(stroke_width=2)
        standard_color = WHITE
        self.all_objs = VGroup()  # Groupe global pour zoom final

        # ---- CERCLE 0 (référence grise, en arrière-plan) ----
        cercle0 = DashedVMobject(Circle(radius=rayon, color=GREY), dashed_ratio=0.5, num_dashes=60).shift(UP*1.3 + LEFT)
        cercle0.z_index = -1
        cercle0.set_opacity(0)
        centre0 = Dot(color=GREY, radius=0.03).move_to(cercle0.get_center())
        self.add(cercle0, centre0)
        self.all_objs.add(cercle0, centre0)

        # ---- CERCLE 1 ----
        cercle1 = Circle(radius=rayon, color=standard_color).shift(UP*1.3 + LEFT)
        centre1 = Dot(color=standard_color, radius=0.03).move_to(cercle1.get_center())
        self.add(centre1)
        self.all_objs.add(cercle1, centre1)

        # ---- CERCLE 2 ----
        cercle2 = Circle(radius=rayon, color=standard_color).next_to(cercle1, DOWN, buff=0)
        centre2 = Dot(color=standard_color, radius=0.03).move_to(cercle2.get_center())
        self.add(centre2)
        self.all_objs.add(cercle2, centre2)

        # ---- CERCLE 3 ----
        cercle3 = Circle(radius=rayon, color=standard_color).next_to(cercle2, RIGHT, buff=0)
        centre3 = Dot(color=standard_color, radius=0.03).move_to(cercle3.get_center())
        #centre3.add_updater(lambda d: d.move_to(cercle3.get_center()))
        self.add(centre3)
        self.all_objs.add(cercle3, centre3)

        # ---- BRACES ----
        brace0 = VGroup(
        Brace(cercle0, direction=LEFT, buff=0.2, color=standard_color),
        Brace(cercle0, direction=LEFT, buff=0.2, color=standard_color).get_text("1").set_color(standard_color)
        )

        brace1 = always_redraw(lambda: VGroup(
        (b := Brace(cercle1, direction=LEFT, buff=0.2, color=standard_color)),
         b.get_text("1").set_color(standard_color)
        ))

        brace2 = VGroup(
        Brace(cercle2, direction=LEFT, buff=0.2, color=standard_color),
        Brace(cercle2, direction=LEFT, buff=0.2, color=standard_color).get_text("1").set_color(standard_color)
        )

        brace3 = VGroup(
        Brace(cercle3, direction=DOWN, buff=0.2, color=standard_color),
        Brace(cercle3, direction=DOWN, buff=0.2, color=standard_color).get_text("1").set_color(standard_color)
        )
        self.all_objs.add(brace1, brace2, brace3)

        # ---- APPARITION ----
        self.play(
            Create(cercle1),
            Create(cercle2),
            Create(cercle3),
            cercle0.animate.set_opacity(1),
            run_time=1.5
        )
        self.wait(0.2)
        centre1.add_updater(lambda d: d.move_to(cercle1.get_center()))
        centre2.add_updater(lambda d: d.move_to(cercle2.get_center()))
        centre3.add_updater(lambda d: d.move_to(cercle3.get_center()))
        
        self.play(
            FadeIn(brace0),
            FadeIn(brace1),
            FadeIn(brace2),
            FadeIn(brace3)
        )
        self.wait(0.5)

        # ---- ANIMATION SUR ARC ----
        arc_path = Arc(radius=2 * rayon, angle=-PI / 6, start_angle=PI / 2, arc_center=cercle2.get_center())
        arc_path_back = Arc(radius=2 * rayon, angle=PI / 6, start_angle=PI / 3, arc_center=cercle2.get_center())

        self.play(MoveAlongPath(cercle1, arc_path), run_time=2)
        self.wait()
        self.play(MoveAlongPath(cercle1, arc_path_back), run_time=2)
        self.wait()

        # ---- ON MASQUE LES ACCOLADES
        self.play(
            FadeOut(brace0),
            FadeOut(brace1),
            FadeOut(brace2),
            FadeOut(brace3)
        )
        self.wait()

        # ---- SEGMENTS DYNAMIQUES ----
        segment1 = always_redraw(lambda: Line(cercle1.get_center(), cercle2.get_center(), color=standard_color))
        segment2 = always_redraw(lambda: Line(cercle2.get_center(), cercle3.get_center(), color=standard_color))
        segment3 = always_redraw(lambda: Line(cercle3.get_center(), cercle1.get_center(), color=standard_color))
        self.all_objs.add(segment1, segment2, segment3)
        self.wait()

        # ---- REPERES DYNAMIQUES ----
        dashedLine_cercle0 = always_redraw(lambda: DashedLine(
            cercle0.get_center() - RIGHT * 2,
            cercle0.get_center() + RIGHT * 4,
            color=GREY
        ))
        dashedLine_cercle1 = always_redraw(lambda: DashedLine(
            cercle1.get_center() - RIGHT * 3,
            cercle1.get_center() + RIGHT * 3,
            color=standard_color
        ))

        # ---- DOUBLE ARROW ----
        x_pos = cercle3.get_center()[0]
        delta = 0.2
        def double_fleche_redraw ():
            start_point = [x_pos + delta, dashedLine_cercle0.get_y(), 0]
            end_point   = [x_pos + delta, dashedLine_cercle1.get_y(), 0]
            da = DoubleArrow(start=start_point, end=end_point, buff=0, color=standard_color, tip_length=0.2) 
            return da
        double_fleche = always_redraw(lambda: double_fleche_redraw () )

        #-----------------------
        self.play(Create(dashedLine_cercle0), Create(dashedLine_cercle1), GrowArrow(double_fleche))
        # ---- Déplacement final de cercle1 seul ----
        self.play(MoveAlongPath(cercle1, arc_path), run_time=2)
        # ------
        label_x = MathTex("x").next_to(double_fleche, RIGHT, buff=0.1).set_color(standard_color)
        self.play(FadeIn(label_x))
        self.all_objs.add(dashedLine_cercle0, dashedLine_cercle1, double_fleche, label_x)
        self.wait(4)

        # On met tout en gris pour préparer la solution
        standard_color = GREY
        self.all_objs_solution = VGroup().add(cercle0,cercle1,cercle2,cercle3,centre0,centre1,centre2,centre3,dashedLine_cercle0,dashedLine_cercle1)
        self.play(self.all_objs_solution.animate.set_color(standard_color), run_time=1.5)
        # ---- ZOOM CENTRAL ----
        #self.play(self.all_objs.animate.scale(2.5).move_to(ORIGIN), run_time=2)
        #self.wait()

        # ---- DÉZOOM FINAL ----
        self.wait(2)
        #self.play(self.all_objs.animate.scale(0.4).move_to(ORIGIN), run_time=2)
        self.wait(4)
