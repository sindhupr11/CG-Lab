from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

wsize = 500
polygon = [(100,100),(100,400),(400,400), (400,100)]
point = 10
filled = False

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    if filled:
        glColor3f(0.1,1.0,2.0)
        glPointSize(point)
        glBegin(GL_POLYGON)
        for x,y in polygon:
            glVertex2f(x,y)
        glEnd()
        glFlush()
    else:
        glColor3f(1.0, 0.1, 0.2)
        glPointSize(point)
        glBegin(GL_POLYGON)
        for x,y in polygon:
            glVertex2f(x,y)
        glEnd()
        glFlush()



def scanline():
    global filled
    min_y = min(polygon, key=lambda p: p[1])[1]
    max_y = max(polygon, key=lambda p: p[1])[1]

    for y in range(min_y, max_y):
        intersections = []
        for i in range(len(polygon)):
            x1,y1 = polygon[i]
            x2,y2 = polygon[(i+1)%len(polygon)]
            if y1 > y2 :
                x1,y1,x2,y2 = x2,y2,x1,y1
            if y1 <= y < y2:
                if y1 != y2:
                    x = int(x1 + (y-y1)*(x2-x1)/(y2-y1))
                    intersections.append(x)
                else:
                    intersections.append(x1)
        intersections.sort()
        for i in range(0,len(intersections),2):
            x1 = intersections[i]
            x2 = intersections[i+1]
            glColor3f(0.1,1.0,2.0)
            glPointSize(point)
            glBegin(GL_LINES)
            glVertex2f(x1,y)
            glVertex2f(x2,y)
            glEnd()
        glFlush()
        glutPostRedisplay()
    filled = True

def mouse(btn,state,x,y):
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        scanline()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(wsize,wsize)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Point")
    glClearColor(0.0,0.1,0.0,1.0)
    gluOrtho2D(0,wsize,wsize,0)
    glutDisplayFunc(draw)
    glutMouseFunc(mouse)
    glutMainLoop()

main()
