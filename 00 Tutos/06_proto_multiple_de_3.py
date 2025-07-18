from manim import *

class CubeRowsLeftAligned(Scene):
    def construct(self):
        rows = [5, 6, 7]  # nombre de cubes par rangée
        colors = [RED, GREEN, BLUE]  # une couleur par ligne
        cube_size = 0.4
        spacing = 0.4
        vertical_spacing = 0.6

        all_rows = VGroup()

        for i, (nb_cubes, color) in enumerate(zip(rows, colors)):
            row = VGroup()
            for j in range(nb_cubes):
                square = Square(side_length=cube_size, color=color, fill_color=color, fill_opacity=0.5)
                square.move_to(LEFT * 5 + RIGHT * j * spacing)  # aligné à gauche
                row.add(square)
            row.shift(DOWN * i * vertical_spacing)
            all_rows.add(row)

        self.play(Create(all_rows))
        #
        # second_row = all_rows[1]
        # last_square = second_row[-1]
        # self.play(last_square.animate.shift(UP * vertical_spacing))
        #
        first_row = all_rows[0]
        second_row = all_rows[0]
        third_row = all_rows[2]
        last_square = third_row[-1]
        self.play(last_square.animate.shift(UP * 2 * vertical_spacing + LEFT * spacing))
        third_row.remove(last_square)
        first_row.add(last_square)

        self.play(first_row.animate.shift(DOWN * (vertical_spacing-cube_size)), third_row.animate.shift(UP * (vertical_spacing - cube_size)))
        #self.play(third_row.animate.shift(UP * (vertical_spacing - cube_size)))
        self.wait(2)
