#working code

from OpenGL.GL import *
from OpenGL.GLUT import *


points = []

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    for x, y in points:
        # Convert integer coordinates to NDC
        x_ndc = (2 * x / 400) - 1.0  # Assuming a window size of 400x400
        y_ndc = 1.0 - (2 * y / 400)
        glVertex2f(x_ndc, y_ndc)
    glEnd()
    glFlush()


def main():
    x1 = int(input("Enter x1 value: "))
    y1 = int(input("Enter y1 value: "))
    x2 = int(input("Enter x2 value: "))
    y2 = (input("Enter y2 value: "))
    points.append((x1,y1))
    dy= y2-y1
    dx= x2-x1
    if abs(dx)>abs(dy):
        steps=abs(dx)
    else:
        steps=abs(dy)
    xinc=dx/steps
    yinc=dy/steps
    x=x1
    y=y1
    for i in range(steps):
        x=x+xinc
        y=y+yinc
        points.append((x,y))
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow("PyOpenGL__DDA")
    glutDisplayFunc(display)
    glutMainLoop()

main()