# This script places load resistors
# To use it, place the components in the schematic and annotate them as shown in the example.
# Import the changes to the PCB and use this script to align the components.

# Notes:
# This code is written for Python 3.9
# All distances in millimeters
# The coordinate system in Kicad starts in the top left corner


#!/usr/bin/env python
from pcbnew import *

OFFSETX = 50  # Offset refers to top left corner
OFFSETY = 50

BOARDX = 100
BOARDY = 100

# Resistors per Load
NUMX = 5
NUMY = 9

# Resistor Size including Pad
SIZEX = 3.6
SIZEY = 7.4

# Keepouts
TOP_KEEPOUT = 10
BOT_KEEPOUT = 8

# Spacing
#SPACEX = (BOARDX - SIZEX)/(NUMX*3-1)     #6.5
SPACEX = 6.7
SPACEY = (BOARDY - SIZEY - TOP_KEEPOUT - BOT_KEEPOUT) / (NUMY-1)
print("SPACEX: " + str(SPACEX) + "\n")
print("SPACEY: " + str(SPACEY) + "\n")

STARTX = OFFSETX + SPACEX / 2.0
STARTY = OFFSETY + TOP_KEEPOUT + SIZEY / 2.0

# Load the board
pcb = GetBoard()

for loadnum in range(0,3):
    # Iterate in x direction
    for i in range(0,NUMX):
        # Iterate in y direction
        for j in range(0, NUMY):
            # Find the component
            c = pcb.FindModuleByReference("R" + str((loadnum+1)*100+NUMY*i+j+1))
            # Place the resistor
            c.SetPosition(wxPointMM(STARTX + SPACEX*i + loadnum*BOARDX/3.0 , STARTY + SPACEY*j)) #(BOARDX-SPACEX)/3.0 statt 33
            # Rotate it (angle in 1/10 degreee)
            c.SetOrientation(-90 * 10)
            #print("R" + str(NUMY*i+j+1) + " placed.\n")
    Refresh()