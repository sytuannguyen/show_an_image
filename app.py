# Import required libraries
import streamlit as st
from PIL import Image, ImageEnhance

# Streamlit app title
st.title('Image Enhancement App')

# Upload image through file uploader with a default value
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is None:
    uploaded_file = 'Tolkien Fanart.png'
    
# Function to display the uploaded image
def display_image(image, zoom):
    st.image(image, caption='Uploaded Image.', use_column_width=True, clamp=True, width=int(image.width * zoom))
    st.write("")
    return image

# Check if an image has been uploaded
if uploaded_file is not None:
    # Read the image using PIL
    image = Image.open(uploaded_file)
    
    # Display the uploaded image with zoom
    uploaded_image = display_image(image, zoom_level)

    # Image enhancement options
    st.subheader("Image Enhancement Options")
    brightness = st.slider("Brightness", 0.0, 2.0, 1.0)
    contrast = st.slider("Contrast", 0.0, 2.0, 1.0)
    saturation = st.slider("Saturation", 0.0, 2.0, 1.0)
    grayscale = st.checkbox("Convert to Black & White")

    # Apply enhancements to the image
    enhanced_image = ImageEnhance.Brightness(uploaded_image).enhance(brightness)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
    enhanced_image = ImageEnhance.Color(enhanced_image).enhance(saturation)

    # Convert to black and white if the checkbox is selected
    if grayscale:
        enhanced_image = enhanced_image.convert("L")

    # Display the enhanced image with zoom
    st.subheader("Enhanced Image")
    st.image(enhanced_image, caption='Enhanced Image.'))

else:
    st.write("Please upload an image.")
