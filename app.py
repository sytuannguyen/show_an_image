# Import required libraries
import streamlit as st
from PIL import Image, ImageEnhance, ImageOps

# Streamlit app title
st.title('Image Loader App')

# Upload image through file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Function to display the uploaded image
def display_image(image):
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    return

# Function to enhance the image based on user options
def enhance_image(image, enhancement_factor, rotation_angle, flip_horizontal, flip_vertical):
    # Enhance image brightness and contrast
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(enhancement_factor)
    
    # Rotate image
    image = image.rotate(rotation_angle)
    
    # Flip image horizontally and vertically based on user choice
    if flip_horizontal:
        image = ImageOps.mirror(image)
    if flip_vertical:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    
    return image

# Check if an image has been uploaded
if uploaded_file is not None:
    # Read the image using PIL
    original_image = Image.open(uploaded_file)
    
    # User options for image enhancement
    enhancement_factor = st.slider('Enhance Brightness/Contrast:', 0.1, 2.0, 1.0)
    rotation_angle = st.slider('Rotate Image (degrees):', 0, 360, 0)
    flip_horizontal = st.checkbox('Flip Horizontal')
    flip_vertical = st.checkbox('Flip Vertical')
    
    # Enhance the image based on user options
    enhanced_image = enhance_image(original_image, enhancement_factor, rotation_angle, flip_horizontal, flip_vertical)
    
    # Display the original and enhanced images
    st.subheader('Original Image:')
    display_image(original_image)
    
    st.subheader('Enhanced Image:')
    display_image(enhanced_image)
else:
    st.write("Please upload an image.")
