import pyglet # import the library
win = pyglet.window.Window() # create the window

# Create some text
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)

# Create a sprite
img = pyglet.image.load('assets/hero/Old hero.png')
# spr = pyglet.sprite.Sprite(img, x=50, y=50)

# Start the event loop
def update(dt):
  pass

@win.event
def on_draw():
    win.clear()
    img.blit(200, 100)
    img.blit(400, 100)
    # spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()
