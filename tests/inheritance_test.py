import d3dshot
from d3dshot.d3dshot import D3DShot

class InheritTest(D3DShot):
    def __init__(self) -> None:
        co = d3dshot._validate_capture_output('pil')
        super().__init__(capture_output=co, frame_buffer_size=1)

if __name__=='__main__':
    print("main")
    # d = d3dshot.create(capture_output='pil', frame_buffer_size=1)

    instance = InheritTest()
    instance.screenshot()
