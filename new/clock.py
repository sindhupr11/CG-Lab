from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

ROTATE_X = [0, 0, 0]  # s,m,h
ROTATE_Y = [350, 300, 200]
LENGTH = [350, 300, 200]
THETA = [0, 0, 0]

def line(x,y):
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(5)

    glBegin(GL_POINTS)
    nums = 1000
    for i in range(nums):
        theta = 2 * i * math.pi / nums
        x = 300 * math.cos(theta) 
        y = 300 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    for i in range(0, 3):
        line(ROTATE_X[i], ROTATE_Y[i])
    
    glFlush()
    glutSwapBuffers()

def animate(value):
    global x, y
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)

    for i in range(0, 3):
        ROTATE_X[i] = LENGTH[i] * math.sin(math.radians(THETA[i]))
        ROTATE_Y[i] = LENGTH[i] * math.cos(math.radians(THETA[i]))
    if THETA[0] >= 360:
        THETA[0] = 0
        THETA[1] += 1
    else:
        THETA[0] += 0.1
    if THETA[1] >= 360:
        THETA[1] = 0
        THETA[2] += 1
    if THETA[2] >= 360:
        THETA[2] = 0

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Clock")
    glutDisplayFunc(draw)
    glutTimerFunc(0, animate, 0)
    gluOrtho2D(-500, 500, -500, 500)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

if __name__ == "__main__":
    main()