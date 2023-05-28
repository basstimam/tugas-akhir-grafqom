from ursina import *

app = Ursina()


bird = Entity(model='quad', texture='asset/Bird.png', scale=(1, 1), position=(-6, 0), eternal=True)
background1 = Entity(model='quad', texture='asset/Background.png', scale=(16, 7), eternal=True)
background2 = Entity(model='quad', texture='asset/Background.png', scale=(16, 7), eternal=True)
background2.x = 16

background_speed = 1 
moon = Entity(model='quad', texture='asset/Moon.png', scale=(1, 1), position=(6, 3), eternal=True)


bird_speed = 5  

def update():
    
    background1.x -= background_speed * time.dt
    background2.x -= background_speed * time.dt

    if background1.x <= -16:
        background1.x = background2.x + 16
    if background2.x <= -16:
        background2.x = background1.x + 16

    if held_keys['a']:
        bird.x -= bird_speed * time.dt
    if held_keys['d']:
        bird.x += bird_speed * time.dt
    if held_keys['w']:
        bird.y += bird_speed * time.dt
    if held_keys['s']:
        bird.y -= bird_speed * time.dt

app.run()
