# script to export images from a font file
# usage: fontforge -script exportGlyphs.py font.ttf

import os
from fontforge import *
font = open(os.sys.argv[1])
for glyph in font:
    # if font[glyph].isWorthOutputting():
    if glyph in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or glyph in ['comma', 'period', 'quoteright']:
        font[glyph].export(font[glyph].glyphname + ".png", pixelsize=399)
