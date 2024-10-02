from manim import *

class MyFirstScene(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait(1)
