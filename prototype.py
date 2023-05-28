from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

# Create a window
Sky(texture='sky_default')


ground = Entity(model='plane', scale=(100, 1, 100), color=color.white.tint(-.2), texture='textures/ground.jpg', texture_scale=(1,1), collider='box', shader=lit_with_shadows_shader)
tree = Entity(model='tree/scene.gltf', collider='mesh', scale=10, position=(-19, 11, 60), shader=lit_with_shadows_shader)
tree2 = Entity(model='tree/scene.gltf', collider='mesh', scale=10, position=(13, 11, 60), shader=lit_with_shadows_shader)
tree3 = Entity(model='old_dead_tree/scene.gltf', collider='mesh', scale=0.4, position=(15, 0, 30), shader=lit_with_shadows_shader)
tree4 = Entity(model='old_dead_tree/scene.gltf', collider='mesh', scale=0.4, position=(15, 0, -60), shader=lit_with_shadows_shader)
main = Entity(model='scene.gltf', collider='mesh', scale=2, position=(0, 0, 0), shader=lit_with_shadows_shader)

tree3.rotation_x = 90
tree4.rotation_x = 90


# Create a camera

camera.position = (0, 5, -10)
camera.rotation = (8, 0, 0)
camera.fov = 120
camera.height = 5


def update():
 
    if held_keys['a']:
      main.rotation_y -= time.dt * 50
      
    if held_keys['d']:
      main.rotation_y += time.dt * 50

    if held_keys['w']:
      
      main.position -= main.forward * time.dt * 10
    if held_keys['s']:
       main.position += main.forward * time.dt * 10

    if held_keys['space']:
      main.position += main.up * time.dt * 10

    if held_keys['shift']:
      main.position -= main.up * time.dt * 10
    
      




app.run()