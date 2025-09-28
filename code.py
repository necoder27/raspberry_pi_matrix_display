import board
import displayio
import framebufferio
import rgbmatrix
import time
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from displayio import Bitmap

from screens.screen import BaseScreen
from screens.default_screen import DefaultScreen
from screens.cat_animation import CatAnimation

import get_greeting
import get_time_through_wifi

teeny_tiny_font = bitmap_font.load_font("fonts/Teeny-Tiny-Pixls-5.bdf", Bitmap)

displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=6,
    rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],
    addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20],
    clock_pin=board.GP11,
    latch_pin=board.GP12,
    output_enable_pin=board.GP13,
)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

main_group = displayio.Group()

# Default Screen
time_weather_group = displayio.Group()
row_group = displayio.Group()

# Cat Animation Screen

# default_screen = DefaultScreen(main_group, teeny_tiny_font, time_weather_group, row_group)
cat_animation_screen = CatAnimation(main_group, teeny_tiny_font)
display.root_group = cat_animation_screen.group


for item in main_group:
    main_group.remove(item)

while True:
    cat_animation_screen.update()
    time.sleep(0.2)
