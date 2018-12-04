import pyglet
import random as r
from pyglet import clock

""" Functions """
def get_dictionary():  # load dictionary and filter based on requirements
    file = open("dictionary_small.txt")
    dictionary = []
    for word in file:
        dictionary.append(word.rstrip())

    for word in dictionary:
        if len(word) <= 2:
            dictionary.remove(word)
    return dictionary

def check_input(input1):  # check if input of user is present in the screen
    for word in words:
        if word.display.text == input1:
            words.remove(word)   #remove word from screen
            score += 1   #update score

            

""" Classes """
class Word():  # blueprint for block of words
    
    def __init__(self):
        self.display = pyglet.text.Label(r.choice(get_dictionary()),font_name='Times New Roman'
                ,font_size=32,x = r.randint(1, 1190), y = 700)

        def update_self(dt):
            self.display.y -= 0.25
        clock.schedule_interval(update_self,1/60)

    def draw_self(self):
        self.display.draw()

