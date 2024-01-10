from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as numpy
import sys

wsize = 500
point = 10
sys.setrecursionlimit(1000)  # not needed anymore

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-wsize, wsize, -wsize, wsize)
    glMatrixMode(GL_PROJECTION)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 0.1, 0.2)
    # Use GL_POLYGON instead of beginPath and endPath
    glBegin(GL_POLYGON)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 400)
    glVertex2f(100, 400)
    glEnd()
    glFlush()

def setpixel(x, y, fillcolor=(0, 0, 0)):
    glColor3f(*fillcolor)
    glPointSize(point)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def getpixel(x, y):
    glReadBuffer(GL_FRONT)
    data = glReadPixels(x, wsize - y, 1, 1, GL_RGB, GL_FLOAT)
    return numpy.array([round(val, 1) for val in data[0][0]])

def flood_fill(x, y, old_color, new_color):
    # Use a stack to store pixels to be checked
    stack = [(x, y)]
    while stack:
        # Pop a pixel from the stack
        current_x, current_y = stack.pop()
        current_color = getpixel(current_x, current_y)
        
        # Check if pixel matches target color and skip previously filled
        if numpy.array_equal(current_color, old_color):
            setpixel(current_x, current_y, new_color)
            # Add adjacent pixels to the stack if they match
            if current_x + 1 < wsize and numpy.array_equal(getpixel(current_x + 1, current_y), old_color):
                stack.append((current_x + 1, current_y))
            if current_x - 1 >= 0 and numpy.array_equal(getpixel(current_x - 1, current_y), old_color):
                stack.append((current_x - 1, current_y))
            if current_y + 1 < wsize and numpy.array_equal(getpixel(current_x, current_y + 1), old_color):
                stack.append((current_x, current_y + 1))
            if current_y - 1 >= 0 and numpy.array_equal(getpixel(current_x, current_y - 1), old_color):
                stack.append((current_x, current_y - 1))

def mouse(btn, state, x, y):
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        old_color = getpixel(x, y)
        flood_fill(x, y, old_color, (0, 0, 0))

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(wsize, wsize)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Point")
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()

main()
