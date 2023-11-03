# Import required libraries
import streamlit as st
from PIL import Image, ImageEnhance
import cv2
import numpy as np

# Streamlit app title
st.title('Image Enhancement App')

# Upload image through file uploader with a default value
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is None:
    uploaded_file = 'Tolkien Fanart.png'

# Function to remove background from the image
def remove_background(image):
    # Convert PIL image to OpenCV format
    cv_image = np.array(image)
    # Convert RGB to BGR
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
    # Define a mask range for background color (white)
    lower_bound = np.array([200, 200, 200], dtype=np.uint8)
    upper_bound = np.array([255, 255, 255], dtype=np.uint8)
    # Create a mask and update the image to keep only the foreground
    mask = cv2.inRange(cv_image, lower_bound, upper_bound)
    result = cv2.bitwise_and(cv_image, cv_image, mask=mask)
    # Convert BGR back to RGB
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    # Convert NumPy array to PIL image
    result_image = Image.fromarray(result)
    return result_image

# Function to display the uploaded image
def display_image(image):
    st.image(image, caption='Uploaded Image.')
    st.write("")
    return image

# Check if an image has been uploaded
if uploaded_file is not None:
    # Read the image using PIL
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    uploaded_image = display_image(image)

    # Image enhancement options
    st.subheader("Image Enhancement Options")
    brightness = st.slider("Brightness", 0.0, 2.0, 1.0)
    contrast = st.slider("Contrast", 0.0, 2.0, 1.0)
    saturation = st.slider("Saturation", 0.0, 2.0, 1.0)
    grayscale = st.checkbox("Convert to Black & White")
    remove_bg = st.checkbox("Remove Background")

    # Apply enhancements to the image
    enhanced_image = ImageEnhance.Brightness(uploaded_image).enhance(brightness)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
    enhanced_image = ImageEnhance.Color(enhanced_image).enhance(saturation)

    # Remove background if the checkbox is selected
    if remove_bg:
        enhanced_image = remove_background(enhanced_image)

    # Convert to black and white if the checkbox is selected
    if grayscale:
        enhanced_image = enhanced_image.convert("L")

    # Display the enhanced image with zoom
    st.subheader("Enhanced Image")
    st.image(enhanced_image, caption='Enhanced Image.')

else:
    st.write("Please upload an image.")
