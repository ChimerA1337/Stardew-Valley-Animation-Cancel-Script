# Stardew Valley Animation Cancel Script

import threading
from pynput import mouse, keyboard
from time import sleep

keyCon = keyboard.Controller()
mouseCon = mouse.Controller()

k = keyboard.Key
m = mouse.Button

held = threading.Event()

def animationCancel():
    mouseCon.press(m.left)
    sleep(0.05)
    mouseCon.release(m.left)

    sleep(0.125)

    keyCon.press(k.shift_r)
    keyCon.press(k.delete)
    keyCon.press('R')
    sleep(0.05)
    keyCon.release(k.shift_r)
    keyCon.release(k.delete)
    keyCon.release('R')

    #sleep(0.03)

def worker():
    while True:
        held.wait()
        sleep(0.01)
        animationCancel()

def onPress(key):
    match key:
        case k.space:
            held.set()
        case k.insert:
            held.clear()
            return False

def onRelease(key):
    if key == k.space:
        held.clear()

threading.Thread(target=worker, daemon=True).start()
with keyboard.Listener(
    on_press = onPress,
    on_release = onRelease
    ) as listener:
    listener.join()