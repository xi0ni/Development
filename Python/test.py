from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina(fullscreen=False)
window.editor_ui.disable()

box = Entity(
    model="cube",
    scale=2,
    texture="models/rabbit_fur.png",
    texture_scale=(10, 10),
    rotation=(-45, 45, 0),
    position=(0, 2.5, 0),
    shader=lit_with_shadows_shader,
)
box.direction = 1  # Set direction once

floor = Entity(
    model="plane",
    scale=10,
    texture="grass",
    color=color.green,
    shader=lit_with_shadows_shader,
    collider='mesh',
)

dl = DirectionalLight(shadows=True)
dl.position = (0, 5, 0)
dl.look_at(box)

al = AmbientLight()
al.position = (2, 2, 2)
al.color = rgb(1, 1, 1)

def update():
    box.rotation_x += 5
    if box.x > 4 or box.x < -1:
        box.direction *= -1
    box.x += time.dt * box.direction

EditorCamera()
app.run()
