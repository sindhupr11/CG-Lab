from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin


radius = 100
center_x = 100.0
center_y = 100.0
num_segments = 1000

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3f(1,1,1)
    glPointSize(1)
    glBegin(GL_POINTS)
    for i in range(num_segments):
        theta = 2.0 * 3.1415926 * i / num_segments
        x = radius * cos(theta) + center_x
        y = radius * sin(theta) + center_y
        glVertex2f(x, y)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    glutDisplayFunc(showscreen)
    glutIdleFunc(showscreen)
    gluOrtho2D(-500, 500, -500, 500)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

main()