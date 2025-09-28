from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from displayio import Bitmap

teeny_tiny_font = bitmap_font.load_font("fonts/Teeny-Tiny-Pixls-5.bdf", Bitmap)

text = label.Label(
    teeny_tiny_font,
    text="good night",
    color=0xFF0000,
    x=5,
    y=7
)

def get_greeting():
    return text
