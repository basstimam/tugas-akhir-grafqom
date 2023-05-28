from ursina import *
from ursina.shaders import lit_with_shadows_shader



app = Ursina()

#resolution
window.width = 1280
window.height = 720
window.fullscreen = False
window.exit_button.visible = True
window.title = 'Dragon Mystic Forest'



Sky(texture='sky_default')

ground = Entity(model='plane', scale=(100, 1, 100), color=color.white.tint(-.2), texture='textures/ground.jpg', texture_scale=(1,1), collider='box', shader=lit_with_shadows_shader)
tree = Entity(model='tree/scene.gltf', collider='mesh', scale=10, position=(-19, 11, 60), shader=lit_with_shadows_shader)
tree2 = Entity(model='tree/scene.gltf', collider='mesh', scale=10, position=(13, 11, 60), shader=lit_with_shadows_shader)
tree3 = Entity(model='old_dead_tree/scene.gltf', collider='mesh', scale=0.4, position=(15, 0, 30), shader=lit_with_shadows_shader)
tree4 = Entity(model='old_dead_tree/scene.gltf', collider='mesh', scale=0.4, position=(15, 0, -60), shader=lit_with_shadows_shader)
naga = Entity(model='scene.gltf', collider='mesh', scale=2, position=(0, 0, 0), shader=lit_with_shadows_shader)

tree3.rotation_x = 90
tree4.rotation_x = 90


camera.fov = 100



camera_pivot = Entity(parent=naga, y=8,)


def update():
    
    camera_pivot.rotation_y += time.dt * 30
    camera.position = camera_pivot.world_position + (camera_pivot.forward * -20)
    camera.look_at(camera_pivot, 'forward')




app.run()
