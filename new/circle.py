from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3f(1,1,1)
    glPointSize(10)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,361,1):
        theta = math.radians(i)
        x = 50 * math.cos(theta)
        y = 50 * math.sin(theta)
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