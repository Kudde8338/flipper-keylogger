import time
from pynput.keyboard import Key, Listener
from config import special_chars, special_keys, pass_keys

last_time = time.monotonic_ns() // 1_000_000


FILE_OUTPUT = "out/" + str(input("Please enter a name for your ducky script: ").replace(".", "").lower()) + ".txt"

def on_press(key):
    if key is Key.esc:
        return False

    ducky_delay = calculate_delay()
    write_file(ducky_delay)

    ducky_press = key_to_ducky(key)
    if ducky_press:
        write_file(ducky_press)

    print(f"Pressed: {format_key(key)}")

def key_to_ducky(key):
    ducky = ""
    char = getattr(key, "char", None)

    if key in pass_keys:
        pass
    elif key in special_keys:
        ducky = special_keys[key]
    elif char in special_chars:
        ducky = special_chars[char]
    elif char:
        ducky = f"STRING {char}"

    return ducky

def calculate_delay():
    # Calculate the time since last key press and append the delay
    global last_time
    now = time.monotonic_ns() // 1_000_000
    delta = max(now - last_time, 50)
    last_time = now
    return f"DELAY {delta}"

def write_file(string):
    with open(FILE_OUTPUT, "a") as f:
        f.write(f"{string}\n")

def format_key(key):
    char = getattr(key, "char", None)

    if char is not None:
        return char

    return str(key).replace("Key.", "").replace("_", " ").title()

with Listener(on_press=on_press) as listener:
    listener.join()