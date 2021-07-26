from manim import*
from manim import*
import numpy as np
import math
import itertools

####CONFIGURATION###
WHITE_RED = "#FCDED7"
SIERPINSKI_COLOR = [WHITE_RED,RED_A,RED_B,RED_C,RED_D,RED_E]
sierpinski_order = 7


####Custom Mobject####
class sierpinski(VMobject):
    pass

class Kochcurve(VMpbject):
    pass

class BrowinanSnowflake(VMobject):
    pass

class MoveAndShift(Animation):
    def __init__(self, mob, targ_coord, ang, **kwargs):
        digest_config(self, kwargs)
        self.mobject = mob
        self.distance = targ_coord - mob.get_center()
        self.ang = ang

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(
            self.ang * alpha,
            about_point=self.mobject.get_center()
        )
        self.mobject.shift(
            self.distance * alpha
        )

#class Sierpinski_Build_Up(Animation):
#    def __init__(self, mob, **kwargs):
#        super().__init__(**kwargs)
#        digest_config(self, kwarg)
#        self.mobject = mob
    
#    def interpolate_mobject(self, alpha):
#        self.mobject =


####construct####
class Main_Scene(Scene):
    def construct(self):
        self.intro_to_fractal(self):
        self.intro_to_moi(self):

####sub_scene####
def intro_to_fractal(self):
    pass

def intro_to_moi(self):
    pass

##special animation construct####
def Sierpinski_Build_Up(self):
    self.color = itertools.cycle(SIERPINSKI_COLOR)
    t1 = Triangle(color=WHITE,fill_opacity=1,stroke_width=0)
    t1.set_fill(WHITE_RED).scale(2.5)
    pos = [
    t1.get_vertices()[0],
    t1.get_vertices()[1],
    t1.get_vertices()[2],
    ]
    print(pos)
    self.play(Create(t1))

    for _ in range(self.sierpinski_order-1):
        mark = t1.copy()
        mark.set_color(next(self.color))
        self.play(
            t1.animate.scale(1/2,about_point=pos[0]),
            rate_func=smooth,
            run_time=1.5,
            )
        a = VGroup(t1)
        for i in range(2):
            a.add(mark.copy().scale(1/2,about_point=pos[i+1])
                    )
        t1 = a
        self.play(Create(a[1:]),run_time=3)
        
    self.wait()



