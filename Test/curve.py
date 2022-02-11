from manim import *


class crv(Scene):
    def construct(self):
        text =  TextMobject("Hey!")
        self.play(Write(text), run_time=3)
        self.wait(0.5)
        self.play(FadeOut(text), run_time=1)
        ax = Axes(x_range=(-10, 10), y_range=(-10, 10))
        self.get_graph(lambda x: x**2, color=RED)
        c = ax.plot(lambda x: x**2, color=RED)
        self.play(ShowCreation(ax), run_time=2)
        self.wait(0.5)
        self.play(ShowCreation(c), run_time=2)

