from manim import*
import numpy as np
import math
import itertools
##Sierpinski build up##
class Sierpinski_Build_Up(Scene):
    def construct(self):
        #n = NumberPlane()
        #self.add(n)
        WHITE_RED = "#FCDED7"
        self.color = itertools.cycle([WHITE_RED,RED_A,RED_B,RED_C,RED_D,RED_E])
        #colors = color_gradient(RED,WHITE)
        t1 = Triangle(color=WHITE,fill_opacity=1,stroke_width=0)
        t1.set_fill(WHITE_RED).scale(2.5)
        pos = [
        t1.get_vertices()[0],
        t1.get_vertices()[1],
        t1.get_vertices()[2],
        ]
        print(pos)
        self.play(Create(t1))

        for _ in range(7-1):
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


#########################################################################################################
## Testing Range Below ##




    
        


    
 