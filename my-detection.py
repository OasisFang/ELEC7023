#!/usr/bin/env python3

import jetson.inference
import jetson.utils
import sys
import os  # Added os module to call xdg-open

# ==============================================================
# Loading the Detection Model
# ==============================================================
# Create a detectNet object to load the 91-class SSD-Mobilenet-v2 model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# ==============================================================
# Opening the Stream
# ==============================================================
# Note: The input path must be a specific image file, not a directory!
# It reads an image path from the command line argument, or uses a default image if none is provided.
input_path = sys.argv[1] if len(sys.argv) > 1 else "/home/nvidia/jetson-inference/data/images/humans_7.jpg"
camera = jetson.utils.videoSource(input_path) 

# Change output mode to save as a local image file instead of opening a display window
output_filename = "output.jpg"
display = jetson.utils.videoOutput(output_filename)

# ==============================================================
# Main Process Loop
# ==============================================================
while display.IsStreaming():
    # Capture the next image frame
    img = camera.Capture()
    
    if img is None: 
        continue
        
    # The detection network processes the image and returns a list of detections
    detections = net.Detect(img)
    
    # ==============================================================
    # Assignment 3 Requirements: PRINTING DATA TO TERMINAL
    # ==============================================================
    for i, detection in enumerate(detections):
        print(f"========== Detection {i+1} ==========")
        # Get the string name of the class
        class_name = net.GetClassDesc(detection.ClassID)
        
        print(f"ClassID:    {detection.ClassID} ({class_name})")
        print(f"Confidence: {detection.Confidence:.4f}")
        print(f"Left:       {detection.Left:.2f}")
        print(f"Top:        {detection.Top:.2f}")
        print(f"Right:      {detection.Right:.2f}")
        print(f"Bottom:     {detection.Bottom:.2f}")
        print(f"Width:      {detection.Width:.2f}")
        print(f"Height:     {detection.Height:.2f}")
        print(f"Area:       {detection.Area:.2f}")
        print(f"Center:     {detection.Center}")
        print("=====================================\n")

    # ==============================================================
    # Rendering & Saving
    # ==============================================================
    # This step saves the processed image with bounding boxes to output.jpg
    display.Render(img)
    
    # Since we are processing a single static image, break the loop after one frame
    if not camera.IsStreaming():
        break

# ==============================================================
# Display using xdg-open
# ==============================================================
print(f"Detection completed. Image saved to {output_filename}.")
print("Opening the image using xdg-open...")
os.system(f"xdg-open {output_filename}")