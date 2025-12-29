import streamlit as st
import os
import tempfile
from anonym import anonymize_image

# Streamlit page configuration
st.set_page_config(page_title="IA APP", page_icon=":camera:", layout="centered", initial_sidebar_state="collapsed")
# Page title and uploader
st.image("assets/anonym.jpg", width=400)
st.header("Anonimización de imagenes con IA (OpenCV + Deep Learning)")
st.subheader("Sube la imagen")
upl_image=st.file_uploader("Selecciona una imagen...", type=["png","jpg","jpeg"], accept_multiple_files=False)
# Output file name
file_name="processed_image.png"

# Process the uploaded image
if upl_image is not None:
    # Display the uploaded image
    st.image(upl_image, caption="Imagen subida", width=400)
    anonym_button=st.button(label="Anonimizar")
    # Anonymize button action
    if anonym_button:
             try:
                # Save the uploaded image to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                    tmp_file.write(upl_image.read())
                    file_path = tmp_file.name
                # Anonymize the image
                tmp_final_img = anonymize_image(file_name, file_path)
                # Display the anonymized image
                st.image(tmp_final_img, caption="Imagen anonimizada", width=400)
                with open(file_name, "rb") as f:
                    image_data = f.read()
                # Download button for the anonymized image
                st.download_button(
                    label="Descargar imagen anonimizada",
                    data=image_data,
                    file_name=file_name
                )
                os.remove(file_name)
                # Clean up the temporary file
             except:
                 # Display an error message if processing fails
                st.error("Error al procesar la imagen. Por favor, intenta con otra imagen.")
