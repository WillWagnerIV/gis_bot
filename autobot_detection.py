import jetson.inference
import jetson.utils

# load the object detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

camera = jetson.utils.gstCamera(1280, 720, "0")

# Show the OpenGL Display
display = jetson.utils.glDisplay()

while display.IsOpen():
	# main loop will go here

    img, width, height = camera.CaptureRGBA()
    detections = net.Detect(img, width, height)
    display.RenderOnce(img, width, height)
    display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
    display
