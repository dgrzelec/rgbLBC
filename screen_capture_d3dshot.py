import numpy as np
import d3dshot
from PIL import Image


d = d3dshot.create(capture_output='pil', frame_buffer_size=25)
d.display = d.displays[0]

def capture_rgb()->Image:
    return d.screenshot()

if __name__ == "__main__":
    im = d.screenshot()
    im.show()