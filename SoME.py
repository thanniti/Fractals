from manim import*
import numpy as np
import math
import itertools
##Sierpinski build up##
class Sierpinski1(Scene):
    def construct(self):
        #n = NumberPlane()
        #self.add(n)
        self.color = itertools.cycle([RED,ORANGE,GREEN])
        t1 = Triangle(fill_color=next(self.color),color=WHITE,fill_opacity=1,stroke_width=0)
        pos = [
        t1.get_vertices()[0],
        t1.get_vertices()[1],
        t1.get_vertices()[2],
        ]
        print(pos)
        self.play(DrawBorderThenFill(t1))

        for _ in range(5-1):
            mark = t1.copy()
            self.play(
                t1.animate.scale(1/2,about_point=pos[0]),
                rate_func=smooth,
                run_time=2,
                )
            a = VGroup(t1)
            for i in range(2):
                a.add(mark.copy().scale(1/2,about_point=pos[i+1])

                    )
            t1 = a
            self.play(DrawBorderThenFill(a[1:]),run_time=3)
        
        self.wait()


#########################################################################################################
## Testing Range Below ##
from manim import*
class Test(Scene):
def getTri(self, color='#8B5F65'):
    tri = Triangle()
    tri.set_color(color)
def construct(self):
    tri = self.getTri()
    self.play(Write(tri))


    
        


    
 