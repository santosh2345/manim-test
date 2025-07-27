from manim import *

class SantoshAnimation(Scene):
    def construct(self):
        # Create the text "SANTOSH"
        title = Text("SANTOSH", font_size=72, color=BLUE)
        
        # Animation 1: Write the text letter by letter
        self.play(Write(title), run_time=3)
        self.wait(1)
        
        # Animation 2: Change color with a rainbow effect
        self.play(
            title.animate.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE),
            run_time=2
        )
        self.wait(1)
        
        # Animation 3: Scale and rotate
        self.play(
            title.animate.scale(1.5).rotate(PI/6),
            run_time=2
        )
        self.wait(1)
        
        # Animation 4: Move around the screen
        self.play(
            title.animate.shift(UP * 2),
            run_time=1.5
        )
        self.play(
            title.animate.shift(DOWN * 4),
            run_time=1.5
        )
        self.play(
            title.animate.shift(UP * 2),
            run_time=1.5
        )
        self.wait(1)
        
        # Animation 5: Create a circle around the text
        circle = Circle(radius=3, color=WHITE)
        self.play(Create(circle), run_time=2)
        self.wait(1)
        
        # Animation 6: Spin everything together
        group = VGroup(title, circle)
        self.play(
            Rotate(group, angle=2*PI, about_point=ORIGIN),
            run_time=3
        )
        self.wait(1)
        
        # Animation 7: Final transform - make text glow
        self.play(
            title.animate.set_stroke(color=YELLOW, width=3),
            circle.animate.set_color(GOLD),
            run_time=2
        )
        self.wait(2)
        
        # Animation 8: Fade out
        self.play(FadeOut(group), run_time=2)
        self.wait(1)