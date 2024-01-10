#working code

from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.6, -0.6)
    glVertex2f(0.6, -0.6)
    glVertex2f(0.0, 0.6)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow("PyOpenGL Triangle")
glutDisplayFunc(display)
glutMainLoop()
