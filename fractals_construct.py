from functools import reduce

from manimlib.constants import *
# from manimlib.for_3b1b_videos.pi_creature import PiCreature
# from manimlib.for_3b1b_videos.pi_creature import Randolph
# from manimlib.for_3b1b_videos.pi_creature import get_all_pi_creature_modes
from manimlib.mobject.geometry import Circle
from manimlib.mobject.geometry import Polygon
from manimlib.mobject.geometry import RegularPolygon
from manimlib.mobject.types.vectorized_mobject import VGroup
from manimlib.mobject.types.vectorized_mobject import VMobject
from manimlib.utils.bezier import interpolate
from manimlib.utils.color import color_gradient
from manimlib.utils.config_ops import digest_config
from manimlib.utils.space_ops import center_of_mass
from manimlib.utils.space_ops import compass_directions
from manimlib.utils.space_ops import rotate_vector
from manimlib.utils.space_ops import rotation_matrix


def rotate(points, angle=np.pi, axis=OUT):
    if axis is None:
        return points
    matrix = rotation_matrix(angle, axis)
    points = np.dot(points, np.transpose(matrix))
    return points


def fractalify(vmobject, order=3, *args, **kwargs):
    for x in range(order):
        fractalification_iteration(vmobject)
    return vmobject


def fractalification_iteration(vmobject, dimension=1.05, num_inserted_anchors_range=list(range(1, 4))):
    num_points = vmobject.get_num_points()
    if num_points > 0:
        # original_anchors = vmobject.get_anchors()
        original_anchors = [
            vmobject.point_from_proportion(x)
            for x in np.linspace(0, 1 - 1. / num_points, num_points)
        ]
        new_anchors = []
        for p1, p2, in zip(original_anchors, original_anchors[1:]):
            num_inserts = random.choice(num_inserted_anchors_range)
            inserted_points = [
                interpolate(p1, p2, alpha)
                for alpha in np.linspace(0, 1, num_inserts + 2)[1:-1]
            ]
            mass_scaling_factor = 1. / (num_inserts + 1)
            length_scaling_factor = mass_scaling_factor**(1. / dimension)
            target_length = get_norm(p1 - p2) * length_scaling_factor
            curr_length = get_norm(p1 - p2) * mass_scaling_factor
            # offset^2 + curr_length^2 = target_length^2
            offset_len = np.sqrt(target_length**2 - curr_length**2)
            unit_vect = (p1 - p2) / get_norm(p1 - p2)
            offset_unit_vect = rotate_vector(unit_vect, np.pi / 2)
            inserted_points = [
                point + u * offset_len * offset_unit_vect
                for u, point in zip(it.cycle([-1, 1]), inserted_points)
            ]
            new_anchors += [p1] + inserted_points
        new_anchors.append(original_anchors[-1])
        vmobject.set_points_as_corners(new_anchors)
    vmobject.set_submobjects([
        fractalification_iteration(
            submob, dimension, num_inserted_anchors_range)
        for submob in vmobject.submobjects
    ])
    return vmobject


class Sierpinski(VMobject):
    order = 5,
    num_subparts = 3,
    height = 4,
    colors = [RED, WHITE],
    stroke_width = 1,
    fill_opacity = 1,
    

    def init_colors(self):
        VMobject.init_colors(self)
        self.set_color_by_gradient([RED, WHITE])

    def init_points(self):
        order_n_self = self.get_order_n_self(5)
        if self.order == 0:
            self.set_submobjects([order_n_self])
        else:
            self.set_submobjects(order_n_self.submobjects)
        return self

    def get_order_n_self(self, order):
        if order == 0:
            result = self.get_seed_shape()
        else:
            lower_order = self.get_order_n_self(order - 1)
            subparts = [
                lower_order.copy()
                for x in range(3)
            ]
            self.arrange_subparts(*subparts)
            result = VGroup(*subparts)

        result.set_height(4)
        result.center()
        return result

    def get_seed_shape(self):
        return Polygon(
            RIGHT, np.sqrt(3) * UP, LEFT,
        )

    def arrange_subparts(self, *subparts):
        tri1, tri2, tri3 = subparts
        tri1.move_to(tri2.get_corner(DOWN + LEFT), UP)
        tri3.move_to(tri2.get_corner(DOWN + RIGHT), UP)




