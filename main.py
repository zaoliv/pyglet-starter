import pyglet
win = pyglet.window.Window() 
# Load the image
img = pyglet.image.load('assets/hero/Sliced/peace.png')
spr = pyglet.sprite.Sprite(img, x = 200, y = 200) 

# Start the even:
  pass

@win.event
def on_draw():0
win.clear()
img.blit(100, 150) # this is new line
    # draw the sprite
    spr.draw()
pyglet.clock.schedule(update)
pglet.app.run()
import pyglet # import the library
win= pyglet.window.Window() # create the window

# create a sprite
img= pyglet.image.load('assets/hero/peace.png')
smol_img = img.get_region(x=10, y=10, width=32, height=32)
spr = pyglet.sprite.Sprite(smol_img, x = 200, y = 200)

def update(dt)
pass

# Start the event loop
@win.event
def on_draw():
    win.clear()
    spr.draw()

    pyglet.clock.sedule(update)
    pyglet.app.run()