from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x = 0
y = 0
tr = 1

def draw():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1, 0, 0)
    glPointSize(10)
    glBegin(GL_QUADS)
    glVertex2f(-500 + x, -100 +y)
    glVertex2f(-500 + x, 100 +y)
    glVertex2f(-100 + x, 100 +y)
    glVertex2f(-100 + x, -100 +y)
    glEnd()

    glColor3f(0,1,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        k = 50 * math.cos(theta) -450 + x
        l = 50 * math.sin(theta) -100 + y
        glVertex2f(k, l)
    glEnd()

    glColor3f(1,1,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        k = 50 * math.cos(theta) -150 + x
        l = 50 * math.sin(theta) -100 + y
        glVertex2f(k, l)
    glEnd()
    glFlush()

def animate(value):
    glutPostRedisplay()
    global x
    if x < 500:
        x += tr
    else:
        x = 0
    glutTimerFunc(int(100 / 60), animate, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car")
    glutDisplayFunc(draw)
    glutTimerFunc(100, animate, 0)
    gluOrtho2D(-500, 500, -500, 500)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()


