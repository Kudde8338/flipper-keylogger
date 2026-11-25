from pynput.keyboard import Key

special_chars = {
    # Swedish
    "å": "ALTCHAR 0229",
    "Å": "ALTCHAR 0197",
    "ä": "ALTCHAR 0228",
    "Ä": "ALTCHAR 0196",
    "ö": "ALTCHAR 0246",
    "Ö": "ALTCHAR 0214",

    # Danish
    "æ": "ALTCHAR 0230",
    "Æ": "ALTCHAR 0198",
    "ø": "ALTCHAR 0248",
    "Ø": "ALTCHAR 0216",

    # French and Spanish
    "é": "ALTCHAR 0233",
    "è": "ALTCHAR 0232",
    "ê": "ALTCHAR 0234",
    "ë": "ALTCHAR 0235",
    "É": "ALTCHAR 0201",
    "È": "ALTCHAR 0200",
    "á": "ALTCHAR 0225",
    "à": "ALTCHAR 0224",
    "í": "ALTCHAR 0237",
    "ó": "ALTCHAR 0243",
    "ú": "ALTCHAR 0250",
    "ñ": "ALTCHAR 0241",
    "Ñ": "ALTCHAR 0209",

    # German
    "ü": "ALTCHAR 0252",
    "Ü": "ALTCHAR 0220",
    "ß": "ALTCHAR 0223",

    # European
    "ç": "ALTCHAR 0231",
    "Ç": "ALTCHAR 0199",
    "¿": "ALTCHAR 0191",
    "¡": "ALTCHAR 0161"
}
special_keys = {
    Key.space: "SPACE",
    Key.enter: "ENTER",
    Key.backspace: "BACKSPACE",
    Key.up: "UP",
    Key.down: "DOWN",
    Key.left: "LEFT",
    Key.right: "RIGHT",
    Key.tab: "TAB",
    Key.delete: "DELETE",
    Key.home: "HOME",
    Key.end: "END",
    Key.page_up: "PAGEUP",
    Key.page_down: "PAGEDOWN"
}

pass_keys = [
    Key.shift,
    Key.shift_r,
    Key.caps_lock,
    Key.f1,
    Key.f2,
    Key.f3,
    Key.f4,
    Key.f5,
    Key.f6,
    Key.f7,
    Key.f8,
    Key.f9,
    Key.f10,
    Key.f11,
    Key.f12,
    Key.f13,
    Key.f14,
    Key.f15,
    Key.f16,
    Key.f17,
    Key.f18,
    Key.f19,
    Key.f20,
    Key.f21,
    Key.f22,
    Key.f23,
    Key.f24
]