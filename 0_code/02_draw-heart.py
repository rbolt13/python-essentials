'''
The goal is to draw a heart in the terminal. 
'''
from termcolor import colored
import os
import time

'''
Canvas
'''
class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

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
        self.framerate = 0.2
        self.pos = [1, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def rightLowerDiagnal(self):
        pos = [self.pos[0]+1, self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def rightUpperDiagnal(self):
        pos = [self.pos[0]+1, self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def leftLowerDiagnal(self):
        pos = [self.pos[0]-1, self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def leftUpperDiagnal(self):
        pos = [self.pos[0]-1, self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

# Define the vaibale 'canvas' to class Canvas of size 10x10
canvas = Canvas(10, 10)

'''
Deifine the variable 'scribe' to class TerminalScribe such that 
the canvas is the defined as the 10x10 canvas. 
'''
scribe = TerminalScribe(canvas)

'''
Draws a heart similar to this: 
 . .   . .
.   . .   .
.    .    .
 .       .
  .     .
   .   .
     .
'''
scribe.right()
scribe.right()
scribe.rightLowerDiagnal()
scribe.rightLowerDiagnal()
scribe.rightUpperDiagnal()
scribe.rightUpperDiagnal()
scribe.right()
scribe.right()
scribe.down()
scribe.down()
scribe.leftLowerDiagnal()
scribe.leftLowerDiagnal()
scribe.leftLowerDiagnal()
scribe.leftLowerDiagnal()
scribe.leftUpperDiagnal()
scribe.leftUpperDiagnal()
scribe.leftUpperDiagnal()
scribe.leftUpperDiagnal()
scribe.up()
scribe.up()