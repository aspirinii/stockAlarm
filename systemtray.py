from pystray import MenuItem as item
import pystray
from PIL import Image

def action():
    pass

image = Image.open("cat.png")
menu = (item('Start', action), item('Stop', lambda : icon.stop()))
icon = pystray.Icon("What", image, "Cat", menu)
icon.run()
