import d3dshot
from PIL import Image


d = d3dshot.create(capture_output='pil', frame_buffer_size=25) #capture_output='numpy' is faster, but downsampling method is to be found
d.display = d.displays[0]

def capture_rgb()->Image:
    return d.screenshot()

if __name__ == "__main__":
    im = d.screenshot()

    for i,display in enumerate(d.displays):
        print("[{}]".format(i),display)
    # im.show()