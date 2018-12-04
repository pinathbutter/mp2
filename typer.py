import pyglet
import engine
from engine import Word
from engine import get_dictionary
from pyglet import clock
from pyglet.window import key

words = []  # contains word objects
pressed = []
score = 0
window = pyglet.window.Window(width = 1280, height = 720)
output = pyglet.text.Label('', font_size=28,
                          x=window.width//2, y=40,
                          anchor_x='center', anchor_y='center')


def check_input():  #checks input of user
    for word in words:
        if word.display.text == output.text:
            words.remove(word)
            
def create_blocks(time):  # instantiate words
    words.append(Word())

def draw():
    for word in words:
        word.draw_self()
        if word.display.y == 00:
            words.remove(word)
            
    output.draw()
    
    
        
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.BACKSPACE: # [Backspace]
        output.text = output.text[:-1] # Delete one letter from screen
    elif symbol == key.ENTER:
        check_input()
        output.text = ''
    else:
        pressed.append(symbol)
        output.text += chr(symbol)


@window.event
def on_draw():
    window.clear()
    draw()

clock.schedule_interval(create_blocks,2)
pyglet.app.run()
