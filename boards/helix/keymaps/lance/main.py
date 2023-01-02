from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.modules.modtap import ModTap
from kmk.modules.capsword import CapsWord
from kmk.modules.cg_swap import CgSwap
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledData, OledReactionType
from storage import getmount

keyboard = KMKKeyboard()

# RGB backlight support
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=32, hue_default=80, sat_default=255, val_default=80)
keyboard.extensions.append(rgb)

# Split keyboard support
split_side = SplitSide.LEFT
split_side = SplitSide.RIGHT
split = Split(
    use_pio=True,
    uart_flip=True,
    data_pin=keyboard.data_pin
    )
keyboard.modules.append(split)

# ModTap support for that right shift/enter
modtap = ModTap()
keyboard.modules.append(modtap)

# OLED support
oled_flip = False
# Flip the OLEDs based on the side that they are on
flip_based_on_side = True
if flip_based_on_side:
    oled_flip = False
    root_name = str(getmount('/').label)
    if root_name.endswith('R'):
        oled_flip = not oled_flip

# Display two different images based on the side
imgs = ['left.bmp']
different_imgs_per_side = True
if different_imgs_per_side:
    root_name = str(getmount('/').label)
    if root_name.endswith('R'):
        imgs = ['right.bmp']

oled_display_data = OledData(image={0:OledReactionType.LAYER, 1:imgs})
oled_ext = Oled(oled_display_data, toDisplay=OledDisplayMode.IMG, flip=oled_flip) 
keyboard.extensions.append(oled_ext)

# Layer support``
layers_ext = Layers()
keyboard.modules.append(layers_ext)

# Capsword and CG_Swap modules
caps_word = CapsWord()
cg_swap = CgSwap()
keyboard.modules.append(caps_word)
keyboard.modules.append(cg_swap)

# Media key support
keyboard.extensions.append(MediaKeys())

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.MO(3)

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUD
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD
RGB_SPI = KC.RGB_ANI
RGB_SPD = KC.RGB_AND

RESET = KC.RESET
DEBUG = KC.DEBUG

CG_TOGG = KC.CG_TOGG

ENT_SFT = KC.MT(KC.ENT, KC.RSFT)

keyboard.keymap = [
    [  # QWERTY
        KC.GRV,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                       KC.N6,  KC.N7,  KC.N8,    KC.N9,   KC.N0,  KC.DEL,
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                       KC.Y,    KC.U,   KC.I,     KC.O,    KC.P, KC.BSPC,
        KC.ESC,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                       KC.H,    KC.J,   KC.K,     KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.LBRC,  KC.RBRC,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, ENT_SFT,
        KC.CW,   ADJUST, KC.LALT, KC.LGUI, KC.LCTL,   LOWER,   LOWER,   KC.SPC,   RAISE,   RAISE, KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT
    ],
    [  # LOWER
        _______, _______, _______, _______, _______, _______,                   _______, _______, _______, _______, _______, _______,
        _______,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                     KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, _______,
        _______, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                   KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, _______,
        _______, KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE, _______, _______, KC.MINS,  KC.EQL, KC.LBRC, KC.RBRC, KC.BSLS, _______,
        XXXXXXX, _______, _______, _______, _______, _______, _______, _______,  ADJUST,  ADJUST, XXXXXXX, KC.MPRV, KC.MPLY, KC.MNXT
    ],
    [  # RAISE
        KC.F1,     KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,                     KC.F7,   KC.F8,   KC.F9,  KC.F10,  KC.F11,  KC.F12,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   KC.PGUP, KC.HOME,   KC.UP,  KC.END, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX, _______,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, _______,
        XXXXXXX, _______, _______, _______, _______,  ADJUST,  ADJUST, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ],
    [  # ADJUST
        RESET,     DEBUG, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, RGB_TOG, RGB_VAI, RGB_SAI, RGB_HUI, RGB_SPI,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, RGB_VAD, RGB_SAD, RGB_HUD, RGB_SPD,                   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, CG_TOGG, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ]
]

if __name__ == '__main__':
    print('HELIX, I CHOOSE YOU!')
    keyboard.go()