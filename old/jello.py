from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,sys,time

sys.setrecursionlimit(10**6)

windowsize_x=500
windowsize_y=500

def polygon(list,color):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_POLYGON)
    for coor in list:
        glVertex2f(coor[0],coor[1])
    glEnd()
    
def line(list,color):
    glLineWidth(4)
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_LINE_LOOP)
    for coor in list:
        glVertex2f(coor[0],coor[1])
    glEnd()
    
def circle(r,center,color,degree=360):
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center[0],center[1])
    for i in range(0,degree+1):
        glVertex2f(r*math.cos(math.pi*i/180)+center[0],r*math.sin(math.pi*i/180)+center[1])
    glEnd()
    glutSwapBuffers()
    
def putpixel(x,y,color):
    glPointSize(3)
    glColor3f(color[0],color[1],color[2])
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glutSwapBuffers()
    
def boundaryfill(x,y,newcolor,bgcolor):
    currentcolor=glReadPixels(x+windowsize_x/2,y+windowsize_y/2,1.0,1.0,GL_RGB,GL_FLOAT,None)
    if(currentcolor[0][0][0]!=newcolor[0] or currentcolor[0][0][1]!=newcolor[1] or currentcolor[0][0][2]!=newcolor[2] ) and (currentcolor[0][0][0]!=bgcolor[0] or currentcolor[0][0][1]!=bgcolor[1] or currentcolor[0][0][2]!=bgcolor[2] ):
        putpixel(x,y,newcolor)
        boundaryfill(x-2,y,newcolor,bgcolor)
        boundaryfill(x+2,y,newcolor,bgcolor)
        boundaryfill(x,y+2,newcolor,bgcolor)
        boundaryfill(x,y-2,newcolor,bgcolor)


current_x=0
current_y=0

global_polygon_list=[]
local_polygon_list=[]
polygon_id=[]
polygon_color=[]

global_line_list=[]
local_line_list=[]
line_id=[]
line_color=[]

circle_radius=[]
circle_center=[]
circle_id=[]
circle_color=[]

overide=0
choice=69
state1=0
go_bit=0

pointer=[]

def click_callback(button,state,x,y):
    global current_x,current_y
    global pointer
    global overide,choice,state1
    global circle_id,circle_radius,circle_center,circle_color
    global polygon_id,polygon_color,local_polygon_list,global_polygon_list
    global line_id,line_color,local_line_list,global_line_list
    global go_bit
    mouse_x,mouse_y=x,glutGet(GLUT_WINDOW_HEIGHT)-y
    mouse_x=mouse_x-windowsize_x/2
    mouse_y=mouse_y-windowsize_y/2
    
    if (current_x!=mouse_x and current_y!=mouse_y):
        current_x=mouse_x
        current_y=mouse_y
        
        print(current_x,current_y)
        
        pointer.append([current_x,current_y])
        for coor in pointer:
            circle(3,coor,[0,0,1])
            
        if overide==0:
            choice=int(input("1.circle 2.polygon 3.line "))
            
        if choice==1 or overide==1:
            if state1==0:
                p_id=input("circle name:")
                circle_id.append(p_id)
                circle_center.append([current_x,current_y])
                state1=1
                overide=1
            else:
                circle_radius.append(math.sqrt(pow(circle_center[-1][0]-current_x,2)+pow(circle_center[-1][1]-current_y,2)))
                r=float(input("r:"))
                g=float(input("g:"))
                b=float(input("b:"))
                circle_color.append([r,g,b])
                state1=0
                overide=0
                pointer=[]
                
        if choice==2 or overide==2:
            if state1==0:
                p_id=input("polygon name:")
                polygon_id.append(p_id)
                local_polygon_list.append([current_x,current_y])
                state1=int(input("how many coordinates"))
                overide=2
            else:
                local_polygon_list.append([current_x,current_y])
                state1=state1-1
                if state1==1:
                    r=float(input("r:"))
                    g=float(input("g:"))
                    b=float(input("b:"))
                    global_polygon_list.append(local_polygon_list)
                    local_polygon_list=[]
                    polygon_color.append([r,g,b])
                    state1=0
                    overide=0
                    pointer=[]
                    
        if choice==3 or overide==3:
            if state1==0:
                p_id=input("line name:")
                line_id.append(p_id)
                local_line_list.append([current_x,current_y])
                state1=int(input("how many coordinates"))
                overide=3
            else:
                local_line_list.append([current_x,current_y])
                state1=state1-1
                if state1==1:
                    r=float(input("r:"))
                    g=float(input("g:"))
                    b=float(input("b:"))
                    global_line_list.append(local_line_list)
                    local_line_list=[]
                    line_color.append([r,g,b])
                    state1=0
                    overide=0
                    pointer=[]
                    
        if choice==4:
            go_bit=0
            boundaryfill(current_x,current_y,[1,0,0],[1,1,1])
            pointer=[]
            
        if choice==5:
            go_bit=1
            boundaryfill(current_x,current_y,[0,1,0],[1,1,1])
            pointer=[]
        
dx=15
def Display():
    global dx
    glutPostRedisplay()
    glutTimerFunc(1, Display, 0)
    
    glClear(GL_COLOR_BUFFER_BIT)
    

    
    if(go_bit==1):
        for i in range(0,len(polygon_color)):
            if(polygon_id[i]=="car"):
                for coor in global_polygon_list[i]:
                    coor[0]=coor[0]+dx
                    if(coor[0]>250):
                        dx=dx*-1
                    if(coor[0]<-250):
                        dx=dx*-1
        

    for i in range(0,len(polygon_color)):
        polygon(global_polygon_list[i],polygon_color[i])
            
    for i in range(0,len(line_color)):
        line(global_line_list[i],line_color[i])
        
    for i in range(0,len(circle_color)):
        circle(circle_radius[i],circle_center[i],circle_color[i])
    
                
    glutSwapBuffers()
    time.sleep(0.1)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(windowsize_x,windowsize_y)
    glutInitWindowPosition(0,0)
    glutCreateWindow("you are gay")
    glutDisplayFunc(lambda:Display())
    glutMouseFunc(click_callback)
    gluOrtho2D(-windowsize_x/2,windowsize_x/2,-windowsize_y/2,windowsize_y/2)
    glutMainLoop()
    
main()