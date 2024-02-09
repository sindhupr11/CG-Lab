from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

k = 0
l = 0
ang = 0

def cir(x,y):
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for i in range(1000):
        theta = math.radians(i)
        x1 = x + 30 * math.cos(theta) 
        y1 = y + 30 * math.sin(theta)
        glVertex2f(x1,y1)
    glEnd()
    glFlush()

def line(x,y):
    glColor3f(1,0,0)
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    global k,l
    cir(0 + k,-300 + l)
    line(0 + k,-300 + l)
    glutSwapBuffers()

def animate(value):
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), animate, 0)
    global ang, k, l
    ang += 1      
    k = 100 * math.cos(math.radians(ang*3))  
    l = -math.sqrt(100**2 - k**2)  

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Clock")
    glutDisplayFunc(draw)
    glutTimerFunc(0,animate,0)
    gluOrtho2D(-500,500,-500,500)
    glClearColor(0,0,0,1)
    glutMainLoop()

main()