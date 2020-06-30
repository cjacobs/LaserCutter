
import sys
sys.path.append("Fonts")
import asteroids

OFFSET = 14
SPACING = 18

font = asteroids.get_font()

def svg_header(width, height, title):
    return """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{}" height="{}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" version="1.1">
<title>{}</title>
""".format(width, height, title)

def svg_rect(x, y, w, h):
    return """<rect x="{}" y="{}" width="{}" height="{}" fill="none" stroke-width="1" stroke="black" />\n""".format(x, y, w, h)
    
def svg_text(x, y, text):
    result = """<path d=" """
    xpos = x
    ypos = y
    scale = 0.2
    charwidth = (asteroids.FONT_WIDTH+4)*scale
    for char in text:
        mode = "M"
        if char in font:
            path = font[char]
            for pt in path:
                if type(pt) is tuple:
                    result += "{} {},{} ".format(mode, xpos+pt[0]*scale, ypos+(asteroids.FONT_HEIGHT-pt[1])*scale)
                    mode = "L"
                else:
                    mode = pt

            xpos += charwidth
    result += """ " stroke="black" fill="none" stroke-width="0.5"/>\n"""
    return result
    # return """<text x="{}" y="{}" font-face="American typewriter" font-size="4">{}</text>\n""".format(x, y, text)

def svg_experiment(f, s, xpos, ypos):
    x = OFFSET + SPACING * xpos
    y = OFFSET + SPACING * ypos
    w = 10
    h = 10

    return svg_rect(x, y, w, h)

def svg_footer():
    return "</svg>\n"


#
# gcode
#

def gcode_header(width, height, title):
    return """
G21         ; Set units to mm
G90         ; Absolute positioning
M4          ; Laser on during motion only
"""

def gcode_rect(x, y, w, h, feed, spindle):
    return """G0 X{} Y{}
G1 X{} Y{} F{} S{}
G1 X{} Y{}
G1 X{} Y{}
G1 X{} Y{}
S 0
""".format(x, y, x+w, y, feed, spindle, x+w, y+w, x, y+w, x, y)
    
def gcode_text(x, y, text):
    feed = 200
    spindle = 20
    xpos = x
    ypos = y
    scale = 0.2
    charwidth = (asteroids.FONT_WIDTH+4)*scale

    result = "; F = {}, S = {}\n".format(feed, spindle)
    result += "G0 X{} Y{} F {} S {}\n".format(x, y, feed, spindle)
    for char in text:
        mode = "G0"
        if char in font:
            path = font[char]
            for pt in path:
                if type(pt) is tuple:
                    result += "{} X{} Y{}\n".format(mode, xpos+pt[0]*scale, ypos+(asteroids.FONT_HEIGHT-pt[1])*scale)
                    mode = "G1"
                elif pt == asteroids.FONT_UP:
                    mode = "G0"
                else:
                    print("Unknown font entry: {}".format(pt))

            xpos += charwidth
    result += "\n"
    return result

def gcode_experiment(f, s, xpos, ypos):
    x = OFFSET + SPACING * xpos
    y = OFFSET + SPACING * ypos
    w = 10
    h = 10

    return gcode_rect(x, y, w, h, f, s)

def gcode_footer():
    return "M5          ; Switch tool off\n"

if __name__ == "__main__":

    header = gcode_header
    text = gcode_text
    experiment = gcode_experiment
    footer = gcode_footer

    # header = svg_header
    # text = svg_text
    # experiment = svg_experiment
    # footer = svg_footer

    width = 200
    height = 200
    print(header(width, height, "hello"))

    fs = [50, 100, 150, 200, 250, 300, 400, 500]
    ss = [5, 10, 20, 50, 100, 200, 300, 400, 500]

    for xpos, f in enumerate(fs):
        print(text(OFFSET + xpos*SPACING - 2, 6, "F {}".format(f)))
    for ypos, s in enumerate(ss):
        print(text(0, OFFSET + ypos*SPACING + 4, "S {}".format(s)))

    for xpos, f in enumerate(fs):
        for ypos, s in enumerate(ss):
            print(experiment(f, s, xpos, ypos))

    print(footer())

