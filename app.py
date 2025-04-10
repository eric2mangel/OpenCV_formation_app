import streamlit as st
import numpy as np
from PIL import Image
import image_processing as ip  # Importez le fichier de traitement d'image
import cv2

def main():
    st.sidebar.title("Menu OpenCV")

    uploaded_file = st.sidebar.file_uploader("Importer une image", type=["jpg", "jpeg", "png"])

    st.title("Manipulation d'Images avec OpenCV")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image_array = np.array(image)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Image Originale", use_container_width=True)

        st.sidebar.subheader("Appliquer un effet")
        effect_type = st.sidebar.selectbox("Choisir un effet", ["Aucun", "Flou", "Canny"])

        if effect_type == "Flou":
            st.sidebar.subheader("Paramètres du flou")
            blur_radius = st.sidebar.slider("Rayon du flou", 0, 20, 5)
            processed_image = ip.apply_blur(image_array, blur_radius)
            with col2:
                st.image(processed_image, caption=f"Image avec flou (rayon: {blur_radius})", use_container_width=True)
            st.session_state.processed_image = processed_image
            st.session_state.processed_caption = f"Image avec flou (rayon: {blur_radius})"

        elif effect_type == "Canny":
            st.sidebar.subheader("Paramètres de Canny")
            threshold1 = st.sidebar.slider("Seuil 1", 0, 255, 100)
            threshold2 = st.sidebar.slider("Seuil 2", 0, 255, 200)
            processed_image = ip.apply_canny(cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY), threshold1, threshold2)
            with col2:
                st.image(processed_image, caption=f"Image avec détection de bords Canny (seuil 1: {threshold1}, seuil 2: {threshold2})", use_container_width =True)
            st.session_state.processed_image = processed_image
            st.session_state.processed_caption = f"Image avec détection de bords Canny (seuil 1: {threshold1}, seuil 2: {threshold2})"

        elif effect_type == "Aucun":
            if 'processed_image' in st.session_state:
                with col2:
                    st.info("L'image traitée apparaîtra ici.")
                del st.session_state.processed_image
                del st.session_state.processed_caption
            else:
                with col2:
                    st.info("L'image traitée apparaîtra ici.")

        elif 'processed_image' in st.session_state:
            with col2:
                st.image(st.session_state.processed_image, caption=st.session_state.processed_caption, use_container_width=True)
        else:
            with col2:
                st.info("L'image traitée apparaîtra ici.")


    else:
        st.info("Veuillez importer une image depuis le menu sur le côté.")

if __name__ == "__main__":
    main()