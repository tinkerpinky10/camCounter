# import PiCamera class from picamera module to access physical camera 
from picamera import PiCamera
import time

#create an object from PiCamera class, which will initialize itself
camera = PiCamera()
time.sleep(2)
camera.resultion = (1280, 720)
camera.vflip = True
camera.contrast = 10
camera.image_effect = "watercolor"


camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
