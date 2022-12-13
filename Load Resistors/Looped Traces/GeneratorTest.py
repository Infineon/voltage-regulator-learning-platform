# This script generates load resistors in by looping copper traces
# You can specify the number of resistors, the dimensions of the board and other parameters
# The Script will output everything to the file specified in FILENAME. Afterwards copy the
# content of FILENAME to the ende of the PCB File.

# Notes:
# This code is written for Python 3.9
# All distances in millimeters
# The coordinate system in Kicad starts in the top left corner:
#  x →
# y
# ↓

import sys
import os

# ---------------- User constants -------------------
# General
FILENAME = "output.txt"                     # Output file
NETNAMES = ["net 3", "net 3", "net 3"]      # Net names for the load resitors

# Thickness of the individual load resitors. Add more entries to generate more resistors
THICKNESS = [0.129, 0.129, 0.129]

# Board Specific
BOARDX = 100  # Board dimensions
BOARDY = 100
OFFSETX = 50  # Offset refers to top left corner
OFFSETY = 50
CLEARANCE = 0.13  # Between traces of the same net
LOAD_CLEARANCE = 0.2  # Between traces of different nets (how much do you trust the manufacturer?)
OUTLINE_CLEARANCE = 0.3  # Between traces and the edge
COPPER_THICKNESS = 35e-6  # Thickness of the copper layer

# Keepouts
# There are keepouts in each edge for mounting holes and a keepout in the top center for a connector
# You have to add clearance by yourself!
SCREW_KEEPOUT = 7.5  # Square keepout in the corners for the screw
CONNECTOR_KEEPOUT_X = 6.5  # 1/2 of the width of the connector
CONNECTOR_KEEPOUT_Y = 7.5  # Height of the connector

# --------------- Actual script ------------------------
COPPER_RESISTANCE = 1.68e-8  # Specific resistance
LOADNUM = len(THICKNESS)  # Number of load resistors
CONNECTOR_KEEPOUT_X_START = BOARDX / 2 - CONNECTOR_KEEPOUT_X
CONNECTOR_KEEPOUT_X_END = BOARDX / 2 + CONNECTOR_KEEPOUT_X

# Divide the effective board space into LOADNUM equal parts.
# Keep in mind that at the edges OUTLINE_CLEARANCE has to be subtracted
# whereas in the middle it is just LOAD_CLEARANCE
LOADWIDTH = (BOARDY - 2 * OUTLINE_CLEARANCE - (LOADNUM - 1) * LOAD_CLEARANCE) / LOADNUM


# Either pass coordinates with left, right, top, bottom OR
# y, left, right OR
# x, top, bottom
def add_track_top(coordinates, thickness, net):
    with open(FILENAME, "a") as pcb:
        mycoordinates = {'left': 0, 'right': 0, 'top': 0, 'bottom': 0}
        # Copy all entries that match from coordinates to mycoordinates
        for mykey in mycoordinates:
            if mykey in coordinates:
                mycoordinates[mykey] = coordinates[mykey]
        # If just x is given instead of left and right
        if 'x' in coordinates:
            mycoordinates['left'] = mycoordinates['right'] = coordinates['x']
        # If just y is given instead of top and bottom
        elif 'y' in coordinates:
            mycoordinates['top'] = mycoordinates['bottom'] = coordinates['y']
        pcb.write(
            "  (segment (start " + str("{:.4f}".format(mycoordinates['left'] + OFFSETX))
            + " " + str("{:.4f}".format(mycoordinates['top'] + OFFSETY))
            + ")  (end " + str("{:.4f}".format(mycoordinates['right'] + OFFSETX)) + " "
            + str("{:.4f}".format(mycoordinates['bottom'] + OFFSETY))
            + ") (width " + str("{:.4f}".format(thickness))
            + ") (layer F.Cu) (" + net + "))\n")


if __name__ == '__main__':
    print('Started\n')

    # Delete file if it exists to start with a blank file:
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    # Array which stores the length of each trace
    length = [0, 0, 0]
    # Coordinate dictionaries for vertical and horizontal traces
    vertical = {'x': 0, 'top': 0, 'bottom': 0}
    horizontal = {'left': 0, 'right': 0, 'y': 0}

    for counter in range(LOADNUM):
        # Set the start in x direction
        vertical['x'] = OUTLINE_CLEARANCE + LOADWIDTH * counter + THICKNESS[counter] / 2 + LOAD_CLEARANCE / 2
        # Reset the counter
        i = 0
        # Calculate new linespacing
        linespacing = THICKNESS[counter] + CLEARANCE
        # Iterate in x direction until the LOADWIDTH is reached
        while 1:
            right_edge = vertical['x'] + THICKNESS[counter] / 2  # Right edge of the current trace
            left_edge = vertical['x'] - THICKNESS[counter] / 2   # Left edge of the current trace
            # Screw keepouts:
            # In the area of the keepout
            if left_edge < SCREW_KEEPOUT or right_edge > BOARDY - SCREW_KEEPOUT:
                vertical['top'] = THICKNESS[counter] / 2 + SCREW_KEEPOUT
                vertical['bottom'] = BOARDY - THICKNESS[counter] / 2 - SCREW_KEEPOUT
            # At the edge of the keepout
            elif left_edge < SCREW_KEEPOUT + linespacing or right_edge > BOARDY - SCREW_KEEPOUT - linespacing:
                # Left screw holes (keepout ends):
                if vertical['x'] < BOARDX / 2:
                    # If the last horizontal line was at the top, make current trace longer at the bottom
                    if horizontal['y'] == vertical['top']:
                        vertical['bottom'] = BOARDY - OUTLINE_CLEARANCE - THICKNESS[counter] / 2
                    else:
                        vertical['top'] = OUTLINE_CLEARANCE + THICKNESS[counter] / 2
                # Right screw holes (keepout starts):
                else:
                    # If the last horizontal trace was at the top, make current trace shorter at the bottom
                    if horizontal['y'] == vertical['top']:
                        vertical['bottom'] = BOARDY - THICKNESS[counter] / 2 - SCREW_KEEPOUT
                    else:
                        vertical['top'] = THICKNESS[counter] / 2 + SCREW_KEEPOUT
            # Connector keepouts:
            # Below the connector
            elif CONNECTOR_KEEPOUT_X_START < right_edge and left_edge < CONNECTOR_KEEPOUT_X_END or \
                    (CONNECTOR_KEEPOUT_X_START - linespacing < right_edge and left_edge < CONNECTOR_KEEPOUT_X_END
                     and horizontal['y'] == vertical['bottom']) or \
                    (CONNECTOR_KEEPOUT_X_START < right_edge and left_edge < CONNECTOR_KEEPOUT_X_END + linespacing
                     and horizontal['y'] == vertical['top']):
                vertical['top'] = THICKNESS[counter] / 2 + CONNECTOR_KEEPOUT_Y
            # Beyond the keepouts
            else:
                vertical['top'] = OUTLINE_CLEARANCE + THICKNESS[counter] / 2
                vertical['bottom'] = BOARDY - OUTLINE_CLEARANCE - THICKNESS[counter] / 2

            # Add vertical trace
            add_track_top(vertical, THICKNESS[counter], NETNAMES[counter])
            # Increase counter because a vertical trace has been added
            i += 1
            # Calculate the new length
            length[counter] += vertical['bottom'] - vertical['top']

            # Horizontal
            horizontal['left'] = vertical['x']
            if i % 2:  # Alternate between top and bottom
                horizontal['y'] = vertical['bottom']
            else:
                horizontal['y'] = vertical['top']

            # Calculate new x position and also use it as the end position of the horizontal line
            vertical['x'] += linespacing
            horizontal['right'] = vertical['x']

            # Only add the horizontal line if there is still enough space
            if vertical['x'] + THICKNESS[counter] / 2 + LOAD_CLEARANCE / 2 > \
                    OUTLINE_CLEARANCE + LOADWIDTH * (counter + 1):
                break
            else:
                add_track_top(horizontal, THICKNESS[counter], NETNAMES[counter])

        # To calculate the resistance, the cross-sectional area is needed
        A = THICKNESS[counter] * COPPER_THICKNESS
        print("Length: " + str("{:.1f}".format(length[counter] / 1000)) + " m")
        print("Approximate resistance: " + str("{:.1f}".format(COPPER_RESISTANCE * length[counter] / A)) + " Ohm")
