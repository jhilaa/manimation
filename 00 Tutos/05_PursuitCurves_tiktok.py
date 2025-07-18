from manim import *
import math

class TikTokShortTemplate(Scene):
    def construct(self):
        # Paramètres de base pour centrage vertical
        title = Text("Titre de la scène", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Contenu principal au centre
        content = Tex(r"\text{Une formule ou une animation ici}").scale(1.5)
        self.play(Write(content))

        self.wait(2)
        self.play(FadeOut(content), FadeOut(title))
        self.wait()

# Pour exporter en vertical :
# manim -pqh --config.pixel_height=1920 --config.pixel_width=1080 --config.frame_rate=30 fichier.py TikTokShortTemplate
