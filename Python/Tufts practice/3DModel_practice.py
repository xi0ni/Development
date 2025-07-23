from ursina import *
from ursina.shaders import lit_with_shadows_shader
from math import sin, cos

app = Ursina(fullscreen=False)
window.editor_ui.disable()

goalkeeper = Entity(
    model="models/skibidi monkey.obj",
    scale=0.2,
    position=(2.5, 0.2, 0),
    rotation=(0, 90, 0),
    color=color.blue,
)

goalpost = Entity(
    model="models/goalpost.obj",
    texture="models/gtexture.jpg",
    texture_scale=(5, 5),
    scale=0.2,
    position=(4, 0.4, 0),
)

player = Entity(
    model="models/player.obj",
    texture="models/jtexture.jpg",
    texture_scale=(0.5, 0.5),
    scale=0.2,
    rotation=(0, 90, 0),
    position=(-1, 1, 0),
    color=color.red,
)

box = Entity(
    model="sphere",
    # color=color.red,
    # color=rgb(1, 0, 0),
    scale=0.3,
    texture="models/ball-01.jpg",
    texture_scale=(1, 1),
    rotation=(-45, 45, 0),
    position=(0, 0.2, 0),
    shader=lit_with_shadows_shader,
)
box.direction = 3
goalkeeper.direction = 1


floor = Entity(
    model="plane",
    scale=10,
    texture="grass",
    color=color.green,
    # rotation=(-45, 45, 0),
    shader=lit_with_shadows_shader,
)


dl = DirectionalLight(shadows=True)
dl.position = (0, 5, 0)
dl.look_at(box)

al = AmbientLight()
al.position = (2, 2, 2)
al.color = rgb(1, 1, 1)


def update():
    box.rotation_x += 2

    # box.x = sin(time.time())
    # box.position = (sin(4*time.time()),0,0)
    # box.x = (box.x + time.dt) % 4

    if box.x > 4 or box.x < -1:
        box.direction *= -1
    box.x += time.dt * box.direction

    if goalkeeper.z > 1 or goalkeeper.z < -1:
        goalkeeper.direction *= -1
    goalkeeper.z += time.dt * goalkeeper.direction

EditorCamera()

app.run()
