from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Window dimensions
window_width = 500
window_height = 500

# Coordinates of the window (clipping rectangle)
xmin, xmax = -100, 100
ymin, ymax = -100, 100

# Coordinates of the line
x1, y1 = -150, -50
x2, y2 = 50, 150

# Region codes for Cohen-Sutherland algorithm
TOP = 1
BOTTOM = 2
RIGHT = 4
LEFT = 8
accept = False

# Function to clip a line using Cohen-Sutherland algorithm
def clip_line(x1, y1, x2, y2):
    global accept
    code1 = 0
    code2 = 0

    # Assign region codes to the endpoints
    if x1 < xmin:
        code1 |= LEFT
    elif x1 > xmax:
        code1 |= RIGHT
    if y1 < ymin:
        code1 |= BOTTOM
    elif y1 > ymax:
        code1 |= TOP

    if x2 < xmin:
        code2 |= LEFT
    elif x2 > xmax:
        code2 |= RIGHT
    if y2 < ymin:
        code2 |= BOTTOM
    elif y2 > ymax:
        code2 |= TOP

    accept = False
    done = False

    while not done:
        if (code1 | code2) == 0:
            # Line is completely inside the window
            accept = True
            done = True
        elif (code1 & code2) != 0:
            # Line is completely outside the window
            done = True
        else:
            # Line needs clipping
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Calculate the intersection point with the clipping boundary
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Update the endpoint that was outside
            if code_out == code1:
                x1, y1 = x, y
            else:
                x2, y2 = x, y

            # Recalculate the region codes for the new endpoint
            code1 = 0
            code2 = 0

            if x1 < xmin:
                code1 |= LEFT
            elif x1 > xmax:
                code1 |= RIGHT
            if y1 < ymin:
                code1 |= BOTTOM
            elif y1 > ymax:
                code1 |= TOP

            if x2 < xmin:
                code2 |= LEFT
            elif x2 > xmax:
                code2 |= RIGHT
            if y2 < ymin:
                code2 |= BOTTOM
            elif y2 > ymax:
                code2 |= TOP

    return accept, x1, y1, x2, y2

# Function to draw the window and line
def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 1.0, 0.0)  # Green for the window
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    glEnd()
    draw_line(x1, y1, x2, y2)

def draw_line(x1, y1, x2, y2):
    glColor3f(1.0, 0.0, 0.0)  # Red for the line
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

    glutSwapBuffers()

# Function to handle mouse clicks
def mouse(btn, state, x, y):
    global x1, y1, x2, y2
    global accept
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        accept, x1, y1, x2, y2 = clip_line(x1, y1, x2, y2)
        if not accept:
            glutPostRedisplay()  # Redraw the scene

# Initialization
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(window_width, window_height)
glutCreateWindow("Line Clipping")
glutDisplayFunc(draw)
glutMouseFunc(mouse)
glutMainLoop()
