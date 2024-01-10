from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

# Global variables
candle_height = 300
flame_height = 100
flame_intensity = 1.0

def draw_candle():
    glColor3f(1.0, 0.8, 0.9)  # Candle color
    glBegin(GL_QUADS)
    glVertex2f(-100, 100)
    glVertex2f(100, 100)
    glVertex2f(100, -candle_height)
    glVertex2f(-100, -candle_height)
    glEnd()

def draw_flame():
    global flame_intensity, blink_factor
    blink_factor = random.uniform(0.5, 1.0)
    flicker = random.uniform(1.9, 1.0)
    flame_intensity = max(0.0, flame_intensity - 0.005 * flicker)

    glColor4f(1.0, 0.7, 0.1, flame_intensity * blink_factor)  # Flame color
    glBegin(GL_TRIANGLES)
    glVertex2f(-50, 125)
    glVertex2f(50, 125)
    glVertex2f(0, candle_height + flame_height * flame_intensity + 25)
    glEnd()

def draw_wick():
    glColor3f(0.2, 0.2, 0.2)  # Wick color
    glBegin(GL_QUADS)
    glVertex2f(-15, 100)
    glVertex2f(15, 125)
    glVertex2f(15, 125)
    glVertex2f(-15, 100)
    glEnd()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_candle()
    draw_flame()
    draw_wick()

    glutSwapBuffers()

def update_frame(_):
    glutTimerFunc(16, update_frame, 0)  # Schedule the next update
    glutPostRedisplay()

def main():
    # Initialize GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow(b"Candle Animation")
    glutReshapeWindow(500, 500)

    # Enable transparency
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Set the clear color to black
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Set up the orthographic projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

    # Set up the main loop
    glutDisplayFunc(draw_scene)
    glutTimerFunc(0, update_frame, 0)  # Schedule the first update
    glutMainLoop()

main()
