# My SoME_Video

**[Moment of inertia of fractals geometry](https://github.com/thanniti/SoME_Video)**
this website contain my project workflow

## Workflow

### Intro to fractal
   1. Scene1
      - Creature ask "There are many type of fractals"
      - Show different variable of fractals
      - Focus on Sierpinski triagle , Van koch curve
   2. Scene2
      - Creature talk "There are many property of these fractals 
        but, the one that we gonna discuss in this video is the moment of inertia"
      - Show fractals spin around axes

### Intro to Moment of inertia  
   3. Scene3
      - fill screen with fractal spin in scene2
      - Creature ask "but what is moment of inertia"
      - Change fractal spinning in to disk
      - Creature disappear
      - Write def of moment of inertia
      - Write formula
    


```python
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
```
For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/thanniti/SoME_Video/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
