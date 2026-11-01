from manim import *


class Test(Scene):
    def construct(self):
        lo = ValueTracker(0.9)
        r = ValueTracker(1)
        circle = always_redraw(
            lambda: Circle(radius=r.get_value(), stroke_width=2, stroke_color=YELLOW, stroke_opacity=0.9))
        line_radius = always_redraw(
            lambda: Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color=RED, stroke_width=2,
                         stroke_opacity=0.9))
        triangle = always_redraw(
            lambda: Polygon(circle.get_top(), circle.get_left(), circle.get_right(), stroke_color=LIGHT_PINK,
                            stroke_width=2, stroke_opacity=0.9))
        line_circumference = always_redraw(
            lambda: Line(start=LEFT * (r.get_value() * PI),
                         end=RIGHT * (r.get_value() * PI), stroke_color=YELLOW, stroke_width=2,
                         stroke_opacity=lo.get_value()).next_to(circle, DOWN, buff=0.3))

        self.play(Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle))
        self.wait(2)
        lo.set_value(0)
        self.add(line_circumference)
        self.play(r.animate.set_value(2), run_time=2)
        self.wait()
        target_line = Line(start=LEFT * (2 * PI),
                           end=RIGHT * (2 * PI),
                           stroke_color=YELLOW,
                           stroke_width=2,
                           stroke_opacity=0.9
                           ).next_to(circle, DOWN, buff=0.3)
        self.play(ReplacementTransform(circle.copy(), target_line))
        self.play(lo.animate.set_value(0.9))
        self.remove(target_line)
        self.wait()


class Banana(Scene):
    def construct(self):
        banana = SVGMobject("banana.svg")
        txt = Text("yoink", fill_color=YELLOW, fill_opacity=0.9)
        cursor = Rectangle(width=0.1, height=0.5, fill_color=DARK_GRAY, fill_opacity=0.9)
        black_out = Square(side_length=0, fill_color=BLACK, stroke_color=BLACK, stroke_width=0, fill_opacity=0)
        banana.set_fill(YELLOW, opacity=1)
        banana.set_stroke(WHITE, width=2)
        banana.scale(3)
        self.play(DrawBorderThenFill(banana), run_time=4)
        self.wait(2)
        self.play(Transform(banana, black_out), run_time=0.1)
        self.play(FadeOut(banana), run_time=0.5)
        self.play(TypeWithCursor(txt, cursor), run_time=0.5)

        self.wait()


class Math(Scene):
    def construct(self):
        rectangle = Rectangle(stroke_width=4, stroke_color=WHITE, stroke_opacity=0.9).move_to(UL)
        math = MathTex("\\frac {3} {4} = 0.75").set_color_by_gradient(GREEN, PINK)
        math.add_updater(lambda x: x.move_to(rectangle.get_center()))
        self.play(Create(rectangle), run_time=1)
        self.play(Write(math), run_time=2)
        self.play(rectangle.animate.shift(1 * UP, 1 * RIGHT), run_time=2)
        self.wait()
