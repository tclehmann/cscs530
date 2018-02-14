import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed()

width = 100
height = 100

def init():
    global time, agx, agy, ugx, ugy, orient, orient1, config, nextConfig

    time = 0
    
    config = SP.zeros([height,width])
    agy = RD.randrange(height)
    agx = RD.randrange(width)
    orient = RD.choice(["L","R","U","D"])
    ugy = RD.randrange(height)
    ugx = RD.randrange(width)
    orient1 = RD.choice(["L","R","U","D"])

    nextConfig = SP.zeros([height,width])

def draw():
    if orient == "L":
        display = "<"
    elif orient == "R":
        display = ">"
    elif orient == "U":
        display = "^"
    elif orient == "D":
        display = "v"
        
    if orient1 == "L":
        display1 = "<"
    elif orient1 == "R":
        display1 = ">"
    elif orient1 == "U":
        display1 = "^"
    elif orient1 == "D":
        display1 = "v"
        
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.scatter(agx, agy, c = "r", marker = display)
    PL.scatter(ugx, ugy, c = "b", marker = display1)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    global time, agx, agy, nextagx, nextagy, ugx, ugy, nextugx, nextugy, orient, nextorient, orient1, nextorient1, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y,x]
            if x == agx and y == agy and state == 1: #If the cell the first ant is on is black
                #Turn right and find next cell forward based on orientation
                if orient == "L":
                    nextorient = "U"
                    nextagx = agx
                    nextagy = (agy + 1)%height
                elif orient == "R":
                    nextorient = "D"
                    nextagx = agx
                    nextagy = (agy - 1)%height
                elif orient == "U":
                    nextorient = "R"
                    nextagx = (agx + 1)%width
                    nextagy = agy
                elif orient == "D":
                    nextorient = "L"
                    nextagx = (agx - 1)%width
                    nextagy = agy
                state = 0  #Switch states
                next
            elif x == agx and y == agy and state == 0: #If the cell the first ant is on is white
                #Turn left and find next cell forward based on orientation
                if orient == "L":
                    nextorient = "D"
                    nextagx = agx
                    nextagy = (agy - 1)%height
                elif orient == "R":
                    nextorient = "U"
                    nextagx = agx
                    nextagy = (agy + 1)%height
                elif orient == "U":
                    nextorient = "L"
                    nextagx = (agx - 1)%height
                    nextagy = agy
                elif orient == "D":
                    nextorient = "R"
                    nextagx = (agx + 1)%height
                    nextagy = agy
                state = 1  #Switch states
                next
            
            if x == ugx and y == ugy and state == 1: #If the cell the second ant is on is black
                #Turn right and find next cell forward based on orientation
                if orient1 == "L":
                    nextorient1 = "U"
                    nextugx = ugx
                    nextugy = (ugy + 1)%height
                elif orient1 == "R":
                    nextorient1 = "D"
                    nextugx = ugx
                    nextugy = (ugy - 1)%height
                elif orient1 == "U":
                    nextorient1 = "R"
                    nextugx = (ugx + 1)%width
                    nextugy = ugy
                elif orient1 == "D":
                    nextorient1 = "L"
                    nextugx = (ugx - 1)%width
                    nextugy = ugy
                state = 0  #Switch states
                next
            elif x == ugx and y == ugy and state == 0: #If the cell the second ant is on is white
                #Turn left and find next cell forward based on orientation
                if orient1 == "L":
                    nextorient1 = "D"
                    nextugx = ugx
                    nextugy = (ugy - 1)%height
                elif orient1 == "R":
                    nextorient1 = "U"
                    nextugx = ugx
                    nextugy = (ugy + 1)%height
                elif orient1 == "U":
                    nextorient1 = "L"
                    nextugx = (ugx - 1)%height
                    nextugy = ugy
                elif orient1 == "D":
                    nextorient1 = "R"
                    nextugx = (ugx + 1)%height
                    nextugy = ugy
                state = 1  #Switch states
                next
                
            nextConfig[y,x] = state

    config, nextConfig = nextConfig, config
    orient, agx, agy = nextorient, nextagx, nextagy
    orient1, ugx, ugy = nextorient1, nextugx, nextugy

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
