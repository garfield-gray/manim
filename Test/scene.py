from manim import *


class StoC(Scene):
    def construct(self):
        self.add(TextMobject("StoC"))
        self.wait(2)
        self.play(FadeOut(self.mobjects[0]))
        circle = Circle(radius=1.5, color=BLUE)
        self.play(ShowCreation(circle))
        square = Square(side_length=1.5, color=RED)
        self.play(Transform(circle, square))
        self.play(FadeOut(square))
