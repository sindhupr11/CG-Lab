from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin


radius = 100
center_x = 100.0
center_y = 100.0
num_segments = 1000

X = 0
Y = 0
def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3f(1,1,1)
    glPointSize(1)
    glBegin(GL_QUADS)
    glVertex2f(X,Y)
    glVertex2f(X+100,Y)
    glVertex2f(X+100,Y+100)
    glVertex2f(X,Y+100)
    glEnd()
    glFlush()

def main():
    glutInit() #1
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) #2
    glutInitWindowSize(500,500) #3
    glutInitWindowPosition(100,100) #4
    glutCreateWindow("Point") #5
    glutDisplayFunc(showscreen) #6
    glutIdleFunc(showscreen) # 7
    gluOrtho2D(-500, 500, -500, 500) #8
    glClearColor(0, 0, 0, 1) #9
    glutMainLoop() #10

main()