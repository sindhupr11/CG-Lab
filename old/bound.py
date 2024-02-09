from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as numpy
import sys
import math

wsize = 500
point = 10
sys.setrecursionlimit(1000000)


def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(point)
    glLineWidth(10)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100,100)
    glVertex2f(400,100)
    glVertex2f(400,400)
    glVertex2f(100,400)
    glEnd()
    glFlush()

def getpixel(x, y):
    data = glReadPixels(x, wsize - y, 1, 1, GL_RGB, GL_FLOAT)
    return numpy.array([round(val, 1) for val in data[0][0]])

def setpixel(x,y,fillcolor=(1,1,0)):
    glColor3f(*fillcolor)
    glPointSize(point)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def bound(x, y, new, bcol):
  if not (100 <= x <= 400 and 100 <= y <= 400):
    return
  dist = math.sqrt(((x - 250)**2) + ((y - 250)**2))
  if dist <= 200:
    old = getpixel(x, y)
    if (old != bcol).any():
      setpixel(x, y, new)
      bound(x + 10, y, new, bcol)
      bound(x, y + 10, new, bcol)
      bound(x - 10, y, new, bcol)
      bound(x, y - 10, new, bcol)



def mouse(btn,state,x,y):
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        bcol = (1,1,1)
        new = (1,1,0)
        bound(x, y, new, bcol)
        
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0,wsize,wsize,0)
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    glutMainLoop()

main()