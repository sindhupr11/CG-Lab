from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x = 0
y = 0
a = 0
def line(x,y):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3f(1,1,1)
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(50,50)
    glVertex2f(150+x,150+y)
    glEnd()
    glFlush()

def display():
    global x,y
    line(x,y)

def animate(value):
    global x,y,a
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,0)
    a += 1
    x = 50 * math.cos(math.radians(a*3))
    y = math.sqrt(100**2 - x**2)  

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    gluOrtho2D(-500, 500, -500, 500)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

main()