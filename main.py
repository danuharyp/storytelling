import streamlit as st
from PIL import Image  # Import Image from Pillow (PIL)
from multipage import MultiPage
from pages import about, model, explain, app # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("California Housing Price Prediction")
image = Image.open('california.jpg') # replace california.png with your image
st.image(image, caption='California Housing', use_column_width=True)

# Add all your applications (pages) here
app.add_page("Home", app.app)
app.add_page("About the Data", about.app)
app.add_page("Model and Performance", model.app)
app.add_page("Explainability (SHAP)", explain.app)

# The main app
app.run()