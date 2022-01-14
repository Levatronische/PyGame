import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

WIDTH, HEIGHT = 1920, 1080


first_map = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
             [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
             ]

small_map = [
    [(5, 90), (4, 0), (4, 0), (3, 90), (2, 0)],
    [(5, 0), (3, 0), (3, 0), (0, 0), (3, 0)],
    [(3, 0), (2, 180), (1, 0), (3, 90), (4, 270)],
    [(3, 0), (0, 0), (3, 0), (0, 0), (3, 0)],
    [(2, 180), (3, 90), (4, 180), (3, 90), (2, 270)]
]

test_map = [
    [(5, 90), (4, 0), (2, 0)],
    [(2, 90), (4, 180), (4, 270)],
    [(2, 180), (3, 90), (2, 270)]
]

cam_loc = [0, 0]
cam_ang_xy = [0, 0]
key_loc = [0, 0]

time_play = 0.0

x_speed = 0.1
y_speed = 0.1

d_x = 0
d_y = 0

forward_backward = 0
right_left = 0

v_coll_list = [(-7, 7, 6.7, 7), (-7, 7, -7, -6.7), (-5, -1, -5.3, -5), (-5, -1, 5, 5.3), (1, 5, 5, 5.3), (1, 5, 0.7, 1),
               (1, 5, -1, -0.7)]

h_coll_list = [(-7, 7, 6.7, 7), (-7, 7, -7, -6.7), (-5, 5, -1, -0.7), (-5, 5, -5.7, -5), (1, 5, 0.7, 1), (1, 5, 5, 5.3),
               (-7, -1, 0.7, 1), (1, 4, 0.7, 1),
               (-7, -1, 5, 5.3), (1, 4, 5, 5.3)]



def check_h_coll(cam_loc_x, cam_loc_y):
    global h_coll_list
#    print(cam_loc_x, cam_loc_y)
    for i in h_coll_list:
        if i[0] <= cam_loc_x <= i[1]:
            if i[2] <= cam_loc_y <= i[3]:
                print("coll h")
                return True
    return False


def check_v_coll(cam_loc_x, cam_loc_y):
    global v_coll_list
    print(cam_loc_x, cam_loc_y)
    for i in v_coll_list:
        if i[0] <= cam_loc_y <= i[1]:
            if i[2] <= cam_loc_x <= i[3]:
                print("coll v")
                return True
    return False




def prepare_map(g_map):
    global key_loc
    rx = 0
    ry = 0
    y_origin_map = len(g_map)
    x_origin_map = len(g_map[0])
    cell = [-1, -1]
    while cell[0] == -1:
        ry = random.randint(0, y_origin_map - 1)
        rx = random.randint(0, x_origin_map - 1)
        if g_map[ry][rx][0] != 0 and g_map[ry][rx][0] != 1 and g_map[ry][rx][0] != 2 and g_map[ry][rx][0] != 3 \
                and g_map[ry][rx][0] != 4:
            cell = [rx, ry]
    y_origin_map = (len(g_map) - 1) // 2
    x_origin_map = (len(g_map[0]) - 1) // 2
    y_pos = y_origin_map
    x_pos = -x_origin_map
    key_loc = [(x_pos + rx) * 6, (y_pos - ry) * 6]


def loadTexture():
    texture_surface = pygame.image.load('Tex_Map.jpg')
    texture_data = pygame.image.tostring(texture_surface, "RGBA")
    width = texture_surface.get_width()
    height = texture_surface.get_height()
    glEnable(GL_TEXTURE_2D)
    tex_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return tex_id


def wall_x_helper(origin_loc=None):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0], origin_loc[1], 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1, 0, -2)
    glTexCoord2f(0.25, 0.0)
    glVertex3f(1, 0, -2)
    glTexCoord2f(0.25, 0.5)
    glVertex3f(1, 0, 2)
    glTexCoord2f(0.0, 0.5)
    glVertex3f(-1, 0, 2)
    glEnd()
    glPopMatrix()


def wall_y_helper(origin_loc=None):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0], origin_loc[1], 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(0, 1, -2)
    glTexCoord2f(0.25, 0.0)
    glVertex3f(0, -1, -2)
    glTexCoord2f(0.25, 0.5)
    glVertex3f(0, -1, 2)
    glTexCoord2f(0.0, 0.5)
    glVertex3f(0, 1, 2)
    glEnd()
    glPopMatrix()


def floor_helper():
    glColor4f(0.8, 0.8, 0.8, 1)
    glBegin(GL_QUADS)
    glTexCoord2f(0.5, 0.0)
    glVertex3f(-3, -3, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(3, -3, -2)
    glTexCoord2f(1.0, 0.5)
    glVertex3f(3, 3, -2)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(-3, 3, -2)
    glEnd()


def X_way(origin_loc=None):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0] * 6, origin_loc[1] * 6, 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    wall_x_helper([2, 1])
    wall_x_helper([2, -1])
    wall_x_helper([-2, 1])
    wall_x_helper([-2, -1])
    wall_y_helper([1, 2])
    wall_y_helper([-1, 2])
    wall_y_helper([1, -2])
    wall_y_helper([-1, -2])
    floor_helper()
    glPopMatrix()


def T_way(origin_loc=None, rot=0):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0] * 6, origin_loc[1] * 6, 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glRotatef(rot, 0, 0, 1)
    wall_x_helper([2, 1])
    wall_x_helper([0, 1])
    wall_x_helper([-2, 1])
    wall_x_helper([-2, -1])
    wall_x_helper([2, -1])
    wall_y_helper([1, -2])
    wall_y_helper([-1, -2])
    floor_helper()
    glPopMatrix()


def L_way(origin_loc=None, rot=0):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0] * 6, origin_loc[1] * 6, 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glRotatef(rot, 0, 0, 1)
    wall_x_helper([-2, 1])
    wall_x_helper([0, 1])
    wall_x_helper([-2, -1])
    wall_y_helper([1, 0])
    wall_y_helper([1, -2])
    wall_y_helper([-1, -2])
    floor_helper()
    glPopMatrix()


def H_way(origin_loc=None, rot=0):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0] * 6, origin_loc[1] * 6, 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glRotatef(rot, 0, 0, 1)
    wall_x_helper([0, 1])
    wall_y_helper([-1, 0])
    wall_y_helper([1, 0])
    wall_y_helper([1, -2])
    wall_y_helper([-1, -2])
    floor_helper()
    glPopMatrix()


def I_way(origin_loc=None, rot=0):
    if origin_loc is None:
        origin_loc = [0, 0]

    glPushMatrix()
    glTranslatef(origin_loc[0] * 6, origin_loc[1] * 6, 0)
    glColor4f(0.8, 0.8, 0.8, 1)
    glRotatef(rot, 0, 0, 1)
    wall_y_helper([-1, 2])
    wall_y_helper([-1, 0])
    wall_y_helper([-1, -2])
    wall_y_helper([1, 2])
    wall_y_helper([1, 0])
    wall_y_helper([1, -2])

    floor_helper()
    glPopMatrix()


def do_timer(do):
    global time_play
    hours = int(time_play // 3600)
    minutes = int(time_play // 60) - 60 * hours
    seconds = int(time_play) - 60 * minutes - 3600 * hours
    milliseconds = str(time_play % 1)[2:4]
    if do:
        time_play += 0.01
    return f"{hours}:{minutes}:{seconds}.{milliseconds}0"


def draw_map(g_map):
    y_origin_map = (len(g_map) - 1) // 2
    x_origin_map = (len(g_map[0]) - 1) // 2
    y_pos = y_origin_map
    for y in g_map:
        x_pos = -x_origin_map
        for x in y:
            if x[0] == 1:
                X_way([x_pos, y_pos])
            elif x[0] == 2:
                L_way([x_pos, y_pos], x[1])
            elif x[0] == 3:
                I_way([x_pos, y_pos], x[1])
            elif x[0] == 4:
                T_way([x_pos, y_pos], x[1])
            elif x[0] == 5:
                H_way([x_pos, y_pos], x[1])
            x_pos += 1
        y_pos -= 1


pygame.init()
display = (WIDTH, HEIGHT)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.4, 0.4, 0.4, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.6, 0.5, 0.3, 1])

sphere = gluNewQuadric()

glMatrixMode(GL_PROJECTION)
gluPerspective(90, (display[0] / display[1]), 0.01, 500)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -2, 0,
          0, 0, 0,
          0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)
pygame.mouse.set_visible(False)
up_down_angle = 0
left_right_angle_world = 0
left_right_angle = 0
paused = False
run = True
in_start = True

loadTexture()

have_key = False

prepare_map(test_map)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.mouse.set_visible(True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

        if paused:
            pygame.mouse.set_visible(True)
            do_timer(False)

    if not paused:

        if (key_loc[0] + 1.5 >= cam_loc[0] >= key_loc[0] - 1.5) \
                and (key_loc[1] + 1.5 >= cam_loc[1] >= key_loc[1] - 1.5):
#            print("Key")
            have_key = True

        keypress = pygame.key.get_pressed()
        pygame.mouse.set_visible(False)
        do_timer(True)
        glLoadIdentity()

        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        glPushMatrix()

        glLoadIdentity()

        if in_start:
            glTranslatef(0, 0, 2)
            in_start = False

        d_x = 0
        d_y = 0

        forward_backward = 0
        right_left = 0

        if keypress[pygame.K_w] or keypress[pygame.K_UP]:
#            glTranslatef(0, 0, 0.1)
            d_x += math.sin(math.radians(left_right_angle)) * x_speed
            d_y += math.cos(math.radians(left_right_angle)) * y_speed
            forward_backward += 0.1
        if keypress[pygame.K_s] or keypress[pygame.K_DOWN]:
#            glTranslatef(0, 0, -0.1)
            d_x += math.sin(math.radians(left_right_angle)) * -x_speed
            d_y += math.cos(math.radians(left_right_angle)) * -y_speed
            forward_backward += -0.1
        if keypress[pygame.K_d] or keypress[pygame.K_LEFT]:
#            glTranslatef(-0.1, 0, 0)
            d_x += math.sin(math.radians(90 - left_right_angle)) * x_speed
            d_y += math.cos(math.radians(90 - left_right_angle)) * -y_speed
            right_left += -0.1
        if keypress[pygame.K_a] or keypress[pygame.K_RIGHT]:
#            glTranslatef(0.1, 0, 0)
            d_x += math.sin(math.radians(90 - left_right_angle)) * -x_speed
            d_y += math.cos(math.radians(90 - left_right_angle)) * y_speed
            right_left += 0.1

        if check_h_coll(cam_loc[0] + d_x, cam_loc[1] + d_y):
            d_y = 0
            d_x = 0
            if right_left != 0:
                right_left = 0
            if forward_backward != 0:
                forward_backward = 0

        if check_v_coll(cam_loc[0] + d_x, cam_loc[1] + d_y):
            d_y = 0
            d_x = 0
            if right_left != 0:
                right_left = 0
            if forward_backward != 0:
                forward_backward = 0


        glTranslatef(right_left, 0, forward_backward)

        cam_loc[0] += d_x
        cam_loc[1] += d_y

        left_right_angle_world += mouseMove[0] * 0.1
        left_right_angle = left_right_angle_world - (left_right_angle_world // 360) * 360
#        print(f"ang:{left_right_angle}, x:{cam_loc[0]}, y:{cam_loc[1]}")

        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glPopMatrix()

        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #
        #
#        X_way()
#        T_way([2, 0])
#        L_way([4, 0])
#        I_way([6, 0])
#        H_way([8, 0])
        draw_map(test_map)
        #
        #

        #
        #
        glPushMatrix()

        glColor4f(1, 0.843, 0, 1)

        glTranslatef(key_loc[0], key_loc[1], 0)

        if not have_key:
            gluSphere(sphere, 1, 32, 64)

        glPopMatrix()
#        print(cam_loc)
        glPushMatrix()
        glColor4f(0.545, 0, 1, 1)
        if have_key:
            glColor4f(0.545, 0, 1, 1)
            gluSphere(sphere, 1, 32, 64)
            if (0 + 1.5 >= cam_loc[0] >= 0 - 1.5) \
                    and (0 + 1.5 >= cam_loc[1] >= 0 - 1.5):
                print(f"you win!!! time: {do_timer(False)}")
                run = False
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
