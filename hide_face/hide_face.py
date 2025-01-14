import cv2
import os
from PIL import Image, ImageDraw
import numpy as np

# Function to detect faces using OpenCV's Haar Cascade Classifier
def detect_faces(image_path):
    # Load the Haar cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=6, minSize=(30, 30))
    return faces, img


# Function to overlay a smiley face
def overlay_smiley(img, faces):
    # Open image using PIL
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    
    # Define smiley face properties
    smiley_radius = 30
    smiley_color = (255, 255, 0)
    
    for (x, y, w, h) in faces:
        # Center of the face
        face_center = (x + w//2, y + h//2)
        
        # Draw a smiley face
        smiley_position = (face_center[0] - smiley_radius, face_center[1] - smiley_radius)
        draw.ellipse([smiley_position, (smiley_position[0] + 2*smiley_radius, smiley_position[1] + 2*smiley_radius)], fill=smiley_color)

        # Draw the eyes on the smiley face (position relative to face center)
        eye_radius = 5
        left_eye_position = (face_center[0] - 10, face_center[1] - 10)
        right_eye_position = (face_center[0] + 10, face_center[1] - 10)
        draw.ellipse([left_eye_position[0] - eye_radius, left_eye_position[1] - eye_radius, left_eye_position[0] + eye_radius, left_eye_position[1] + eye_radius], fill=(0, 0, 0))
        draw.ellipse([right_eye_position[0] - eye_radius, right_eye_position[1] - eye_radius, right_eye_position[0] + eye_radius, right_eye_position[1] + eye_radius], fill=(0, 0, 0))
    
    return np.array(pil_img)

# Function to process images in a folder
def process_images_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through the images in the folder
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        if os.path.isfile(image_path):
            faces, img = detect_faces(image_path)

            # If faces are detected, overlay a smiley face
            if len(faces) > 0:
                print(f"Faces detected in {filename}, processing...")
                modified_img = overlay_smiley(img, faces)

                # Save the modified image to the output folder
                output_path = os.path.join(output_folder, f"modified_{filename}")
                cv2.imwrite(output_path, cv2.cvtColor(modified_img, cv2.COLOR_RGB2BGR))
            else:
                print(f"No faces detected in {filename}, skipping.")

# Example usage
input_folder = "input_images"  # Path to the folder containing input images
output_folder = "output_images"  # Path to the folder where modified images will be saved

process_images_in_folder(input_folder, output_folder)