# uv run manim -pql demo.py CircleToSquare

from manim import *

class CircleToSquare(Scene):
    def construct(self):
        c = Circle()
        s = Square()

        self.play(Create(c))
        self.wait(0.5)
        self.play(Transform(c, s))
        self.wait(1)

