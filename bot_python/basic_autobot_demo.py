# GIS Practicum Main Demo
# Will Wagner

import jetson.inference
import jetson.utils
import ctypes

# Installed object detection models
tfNets = ["ssd-mobilenet-v2", "pednet", "fcn-resnet18-mhp", "fcn-resnet18-sun", "fcn-resnet18-deepscene"]

# Define the camera to be used
camera = jetson.utils.gstCamera(1280, 720, "0")
# camera = jetson.utils.gstCamera(1920, 1080, "/dev/video0")



def showClassification_GLWindow(tfnet, camera):

    # Load the object detection model
    net = jetson.inference.detectNet(tfnet, threshold=0.5)

    # Show the openGL window
    display = jetson.utils.glDisplay()

    while display.IsOpen():
        img, width, height = camera.CaptureRGBA()
        detections = net.Detect(img, width, height)
        display.RenderOnce(img, width, height)
        display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))



def showSegmentation_GLWindow(tfnet, camera):

    ignore_class = "void"
    filter_mode = "linear"
    alpha = 105
    width = 1920
    height = 1080

    # Load the object detection model
    net = jetson.inference.segNet(tfnet, camera)

    # set the alpha blending value
    net.SetOverlayAlpha(alpha)

    # allocate the output images for the overlay & mask
    img_overlay = jetson.utils.cudaAllocMapped(width * height * 4 * ctypes.sizeof(ctypes.c_float))
    img_mask = jetson.utils.cudaAllocMapped(width/2 * height/2 * 4 * ctypes.sizeof(ctypes.c_float)) 

    # Show the openGL window
    display = jetson.utils.glDisplay()

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
        display.Render(img_mask, width/2, height/2, width)
        display.EndRender()

        # update the title bar
        display.SetTitle("{:s} | Network {:.0f} FPS".format(net, net.GetNetworkFPS()))


#Main Loop
while __name__ == "__main__":


    
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
            showClassification_GLWindow(tfNets [demomode-1], camera)

        elif  2 < demomode <= 9:
            showSegmentation_GLWindow(tfNets [demomode-1], camera)

        else:
            print ("Please choose from the menu.")  

        if demomode == 0:  
            main_menu = False

    

    break



