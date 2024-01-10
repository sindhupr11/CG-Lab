from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as numpy
import sys

wsize = 500
point = 10
sys.setrecursionlimit(1000)

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0,wsize,wsize,0)
    glMatrixMode(GL_PROJECTION)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 0.1, 0.2)
    glPointSize(point)
    glBegin(GL_POLYGON)
    glVertex2f(100,100)
    glVertex2f(400,100)
    glVertex2f(400,400)
    glVertex2f(100,400)
    glEnd()
    glFlush()

def setpixel(x,y,fillcolor=(0,0,0)):
    glColor3f(*fillcolor)
    glPointSize(point)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
    
def getpixel(x, y):
    data = glReadPixels(x, wsize - y, 1, 1, GL_RGB, GL_FLOAT)
    return numpy.array([round(val, 1) for val in data[0][0]])

def flood(x,y,oldcolor,newcolor):
    color = getpixel(x,y)
    if numpy.array_equal(color, oldcolor):
        setpixel(x,y,newcolor)
        flood(x+10,y,oldcolor,newcolor)
        flood(x-10,y,oldcolor,newcolor)
        flood(x,y+10,oldcolor,newcolor)
        flood(x,y-10,oldcolor,newcolor)

def mouse(btn,state,x,y):
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        oldcolor = getpixel(x,y)
        flood(x,y,oldcolor,(0,0,0))

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    init()
    glutMainLoop()

main()