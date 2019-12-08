import jetson.inference
import jetson.utils

import keyboard

# load the object detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

camera = jetson.utils.gstCamera(1280, 720, "0")

# Show the OpenGL Display
display = jetson.utils.glDisplay()


def continuous_cap(display):
    while display.IsOpen():

        img, width, height = camera.CaptureRGBA()
        detections = net.Detect(img, width, height)
        display.RenderOnce(img, width, height)
        display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
        


def cap_screen (display):

    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    print ("Detections: {:.s}".format(detections))


while __name__ == "__main__":

        # try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('c'):  
                cap_screen(display)
        #         # break  # finishing the loop
        # except:
        #     break  # if user pressed a key other than the given key the loop will break


#     if keyboard.is_pressed('c'):  
#         cap_screen(display)