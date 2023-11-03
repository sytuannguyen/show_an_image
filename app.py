# Import required libraries
import streamlit as st
from PIL import Image

# Streamlit app title
st.title('Image Loader App')

# Upload image through file uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Function to display the uploaded image
def display_image(image):
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    return

# Check if an image has been uploaded
if uploaded_file is not None:
    # Read the image using PIL
    image = Image.open(uploaded_file)
    # Display the uploaded image
    display_image(image)
else:
    st.write("Please upload an image.")

