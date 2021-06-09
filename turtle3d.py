import copy
from vpython import *


class Turtle3D:
    def __init__(self):
        # paràmetres de l'escena
        scene.height = scene.width = 1000
        scene.autocenter = True
        scene.caption = """\nTo rotate "camera", drag with right button or Ctrl-drag.\nTo zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.\n  On a two-button mouse, middle is left + right.\nTo pan left/right and up/down, Shift-drag.\nTouch screen: pinch/extend to zoom, swipe or two-finger rotate.\n"""
        self.rgb = vec(1, 0, 0)
        self.turtle = cone(pos=vector(0, 0, 0),
                           axis=vector(1, 0, 0),
                           radius=1,
                           color=color.red)
        self.draw = True
        self.vector_module = 0
        self.direction = self.turtle.axis

    def __rotate(self, rot_matrix):
        mult = self.matrix_multiplication(rot_matrix,
                                          [[self.turtle.axis.x],
                                           [self.turtle.axis.y],
                                           [self.turtle.axis.z]])
        self.direction = vec(mult[0][0], mult[1][0], mult[2][0])
        self.turtle.axis = self.direction/sqrt(pow(self.direction.x, 2) +
                                               pow(self.direction.y, 2) +
                                               pow(self.direction.z, 2))

    def __paint_sphere(self):
        if self.draw:
            sphere(pos=self.turtle.pos, radius=0.1, color=self.rgb)

    def left(self, angle):
        self.__rotate(self.rotate_y(radians(angle)))

    def right(self, angle):
        self.__rotate(self.rotate_y(radians(-angle)))

    def up(self, angle):
        self.__rotate(self.rotate_z(radians(angle)))

    def down(self, angle):
        self.__rotate(self.rotate_z(radians(-angle)))

    def forward(self, mida):
        self.vector_module = mida
        self.__paint_sphere()
        initial = copy.copy(self.turtle.pos)
        self.turtle.pos = initial + mida*self.direction
        if self.draw:
            cylinder(pos=initial, axis=self.turtle.pos-initial,
                     radius=0.1, color=self.rgb)
        self.__paint_sphere()

    def backward(self, mida):
        self.vector_module = mida
        self.__paint_sphere()
        initial = copy.copy(self.turtle.pos)
        self.turtle.pos = initial + -mida*self.direction
        if self.draw:
            cylinder(pos=initial, axis=self.turtle.pos-initial,
                     radius=0.1, color=self.rgb)
        self.__paint_sphere()

    def home(self):
        self.turtle.pos = vec(0, 0, 0)
        self.turtle.axis = vector(1, 0, 0)
        self.direction = self.turtle.axis
        self.vector_module = 0

    def hide(self):
        self.draw = False

    def show(self):
        self.draw = True

    def color(self, col):
        self.rgb = vec(col[0], col[1], col[2])

    @staticmethod
    def rotate_y(theta):
        return [[cos(theta), 0, sin(theta)],
                [0, 1, 0],
                [-sin(theta), 0, cos(theta)]]

    @staticmethod
    def rotate_z(theta):
        return [[cos(theta), -sin(theta), 0],
                [sin(theta), cos(theta), 0],
                [0, 0, 1]]

    @staticmethod
    def matrix_multiplication(rot, pos):
        result = [[0], [0], [0]]
        for i in range(len(rot)):
            for k in range(len(pos)):
                result[i][0] += rot[i][k] * pos[k][0]
        return result
