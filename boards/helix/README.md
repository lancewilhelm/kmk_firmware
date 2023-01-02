# Helix

![Helix](https://camo.githubusercontent.com/15552bce07c6ad8e2a9c25054bada9f6a12239d009771b372d2c2ea7a91ed8b2/68747470733a2f2f692e696d6775722e636f6d2f5842416d796e4e2e6a7067)

A compact split ortholinear keyboard.

* Keyboard Maintainer: [yushakobo](https://github.com/yushakobo)
* Hardware Supported: Helix PCBs (probably rev2 only), Pro Micro RP2040 boards

Copy the `kb.py` and `main.py` files from your preferred keymap folder into your root directory of your keyboard as detailed in the [KMK instructions](http://kmkfw.io/docs/Getting_Started/).

## Microcontroller support

Update this line in `kb.py` to any supported microcontroller in `kmk/quickpin/pro_micro`:

```python
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins