'''
Goal is to use the scribe-canvas code to create a data structure
and write a function that creates and moves the scribe based on
the data sctructure. 
'''

from termcolor import colored
import os
import time
import math 

'''
Canvas
'''
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

'''
TerminalScribe (directions)
'''
class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)


# Asign canvas a Canvas size 30X30.
canvas = Canvas(30, 30)

# Scribe <3 function. 
scribes = [
    # upper right V
    {'degrees': 45, 'position': [15,10], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]},
    # upper left V
    {'degrees': -45, 'position': [15,10], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]},
    # lower right V
    {'degrees': 45, 'position': [15,19], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]},
    # lower left V
    {'degrees': -45, 'position': [15,19], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]},
    # outter /
    {'degrees': 45, 'position': [7,11], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]},
    # outter \
    {'degrees': -45, 'position': [23,11], 'instructions': [
        {'function':'forward', 'duration': 10}
        ]}
]

# Draw the function. 
for scribeData in scribes:
    scribeData['scribe'] = TerminalScribe(canvas)
    scribeData['scribe'].setDegrees(scribeData['degrees'])
    scribeData['scribe'].setPosition(scribeData['position'])

    # Flatten instructions:
    # Convert "{'left': 10}" to ['left', 'left', 'left'...]
    scribeData['instructions_flat'] = []
    for instruction in scribeData['instructions']:
        scribeData['instructions_flat'] = scribeData['instructions_flat'] + [instruction['function']]*instruction['duration']

maxInstructionLength = max([len(scribeData['instructions_flat']) for scribeData in scribes])

for i in range(maxInstructionLength):
    for scribeData in scribes:
        if i < len(scribeData['instructions_flat']):
            if scribeData['instructions_flat'][i] == 'forward':
                scribeData['scribe'].forward()
            elif scribeData['instructions_flat'][i] == 'drawSquare':
                scribeData['scribe'].drawSquare()
            elif scribeData['instructions_flat'][i] == 'up':
                scribeData['scribe'].up()
            elif scribeData['instructions_flat'][i] == 'down':
                scribeData['scribe'].down()
            elif scribeData['instructions_flat'][i] == 'left':
                scribeData['scribe'].left()
            elif scribeData['instructions_flat'][i] == 'right':
                scribeData['scribe'].right()


