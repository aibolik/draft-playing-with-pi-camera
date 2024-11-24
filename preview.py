from picamera2 import Picamera2, Preview
import time

try:
    camera = Picamera2()
    camera.start_preview(Preview.QTGL)
    config = camera.create_preview_configuration()
    camera.configure(config)
    camera.start()
    time.sleep(120)
except Exception as e:
    print(f"An error occured: {e}")
