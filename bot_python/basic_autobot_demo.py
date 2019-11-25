# GIS Practicum Main Demo
# Will Wagner

import sys


import jetson.inference
import jetson.utils
import ctypes
import argparse

# import glViewport


def showClassification_GLWindow(net, camera):

    # Load the object detection model
    net = jetson.inference.detectNet(net, threshold=0.5)

    # Show the openGL window
    display = jetson.utils.glDisplay()

    while display.IsOpen():
        img, width, height = camera.CaptureRGBA()
        detections = net.Detect(img, width, height)
        display.RenderOnce(img, width, height)
        display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    for x in range ( len ( detections ) ):
        print (detections[x])



def showSegmentation_GLWindow(tfnet, camera):


    ignore_class = "void"
    filter_mode = "linear"
    alpha = 105
    width = 1280
    height = 720



    # parser.add_argument("--network", type=str, default="fcn-resnet18-voc", help="pre-trained model to load, see below for options")
    # parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
    # parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
    # parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")


    # Load the object detection model
    net = jetson.inference.segNet(tfnet, camera)

    # set the alpha blending value
    net.SetOverlayAlpha(alpha)


    # allocate the output images for the overlay & mask
    img_overlay = jetson.utils.cudaAllocMapped(width * height * 4 * ctypes.sizeof(ctypes.c_float))

    img_mask = jetson.utils.cudaAllocMapped(width/2 * height/2 * 4 * ctypes.sizeof(ctypes.c_float))

    # Show the openGL window
    display = jetson.utils.glDisplay()
    glViewport(0, 0, width, height)

    while display.IsOpen():

    	# capture the image
        img, width, height = camera.CaptureRGBA()

        # process the segmentation network
        net.Process(img, width, height, ignore_class)

        # generate the overlay and mask
        net.Overlay(img_overlay, width, height, filter_mode)
        net.Mask(img_mask, width/2, height/2, filter_mode)

        # render the images
        display.BeginRender()
        display.Render(img_overlay, width, height)
        display.Render(img_mask, width/2, height/2, width, height)
        display.EndRender()

        # update the title bar
        display.SetTitle("{:s} | Network {:.0f} FPS".format(net, net.GetNetworkFPS()))


#Main Loop
if __name__ == "__main__":

    # Installed object detection models
    nets = ["ssd-mobilenet-v2", "pednet", "fcn-resnet18-mhp", "fcn-resnet18-sun", "fcn-resnet18-deepscene"]

    # Define the camera to be used
    camera = jetson.utils.gstCamera(1280, 720, "0")
    # camera = jetson.utils.gstCamera(1920, 1080, "/dev/video0")

    
    main_menu = True
    
    #Main Menu
    while main_menu == True:
        print ("Main Menu")
        print ("1 - mobilenet-v2            -   Classification")
        print ("2 - pednet                  -   Classification Pedestrians")
        print ("3 - fcn-resnet18-mhp        -   Segmentation People")
        print ("4 - fcn-resnet18-sun        -   Segmentation Indoors")
        print ("5 - fcn-resnet18-deepscene  -   Segmentation Outdoors")
        print ("0 - Quit")
        
        try:
            demomode = int(input ("Select demo mode: "))
            
        except: 
            print ("Please choose from the menu.")

        if  0 < demomode <= 2:
            showClassification_GLWindow(nets [demomode-1], camera)

        elif  2 < demomode <= 9:
            showSegmentation_GLWindow(nets [demomode-1], camera)

        else:
            print ("Please choose from the menu.")  

        if demomode == 0:  
            main_menu = False

    

    



