from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as numpy
import math
import sys

wsize = 500
point = 10
sys.setrecursionlimit(1000000)

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(0,wsize,wsize,0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 0.1, 0.2)
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glPointSize(point)
    glBegin(GL_POLYGON)
    for i in range(1000):
        theta=2.0*math.pi*i/1000
        x=250+100*math.cos(theta)
        y=250+100*math.sin(theta)
        glVertex2f(x,y)
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
    glutInitDisplayMode( GLUT_RGB)
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    init()
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    
    glutMainLoop()

main()