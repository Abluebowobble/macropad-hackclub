# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.modules.encoder import EncoderHandler


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Define your pins here!
KEYBOARD_PINS = [board.GP3, board.GP4, board.GP2, board.GP1, board.GP26, board.GP27]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# columns and rows defined here
keyboard.col_pins = tuple(KEYBOARD_PINS[1:])
keyboard.row_pins = tuple(KEYBOARD_PINS[:5])

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.MUTE]
]

# create encoder handler
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

# define encoders
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP17, board.GP15, None,), # encoder #1 
)

# define encoder function
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, ),)
]

# define RGB
rgb = RGB(pixel_pin=board.GP28, num_pixels=16)
keyboard.extensions.append(rgb)

# define OLED display
displayio.release_displays()

i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

splash = displayio.Group()
label_text = label.Label(terminalio.FONT, text="HACKPAD", color=0xFFFFFF)
label_text.x = 40
label_text.y = 16
splash.append(label_text)
display.show(splash)

# Start kmk!
if __name__ == '__main__':
    keyboard.go()