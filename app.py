# Import required libraries
import streamlit as st
from PIL import Image, ImageEnhance, ImageOps

# Streamlit app title
st.title('Image Enhancement App')

# Upload image through file uploader with a default value
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is None:
    uploaded_file = 'Tolkien Fanart.png'

# Function to remove background using alpha blending
def remove_background(image):
    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Create a new image with a white background
    new_image = Image.new("RGBA", image.size, (255, 255, 255, 255))

    # Perform alpha blending to remove the background
    final_image = Image.alpha_composite(new_image, image)

    return final_image

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
        enhanced_image = ImageOps.grayscale(enhanced_image)

    # Display the enhanced image with zoom
    st.subheader("Enhanced Image")
    st.image(enhanced_image, caption='Enhanced Image.')

else:
    st.write("Please upload an image.")
