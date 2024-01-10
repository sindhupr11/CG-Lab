from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)
    glMatrixMode(GL_PROJECTION)

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 0.1, 0.2)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(0.0,0.0)
    glEnd()
    glFlush()

def main():
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Point")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    init()
    glutMainLoop()

main()
