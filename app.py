import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time

# Charger le CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appliquer le CSS personnalisé
local_css("style.css")

# Sidebar avec options
st.sidebar.title("Options")
style = st.sidebar.selectbox("Choisissez un style", ["Moderne", "Rétro", "Futuriste", "Naturel"])
color = st.sidebar.color_picker("Choisissez une couleur dominante", "#00f900")
hidden_word = st.sidebar.text_input("Entrez un mot caché", "")
user_prompt = st.sidebar.text_area("Décrivez l'image que vous souhaitez générer")

st.sidebar.markdown("**Résumé de vos choix**")
st.sidebar.write(f"Style : {style}")
st.sidebar.write(f"Couleur : {color}")
st.sidebar.write(f"Mot caché : {hidden_word}")
st.sidebar.write(f"Description : {user_prompt}")

# Affichage des Tabs
tab1, tab2 = st.tabs(["Générer", "Paramètres"])

with tab1:
    st.subheader("Générer une image")
    if st.button("Générer l'Image"):
        display_loader()  # Affichage du loader
        image_url = generate_image(user_prompt)
        show_image(image_url)

with tab2:
    st.subheader("Paramètres de personnalisation")
    size = st.slider("Sélectionner la taille de l'image", 100, 2000, 1024)
    st.write(f"Taille de l'image : {size}x{size}")
    st.write("Modifiez les paramètres ci-dessus pour personnaliser votre image.")

# Affichage d'un expander avec plus d'infos
with st.expander("Plus d'infos"):
    st.write("Voici des informations supplémentaires...")
    st.text("Vous pouvez ajouter des détails sur les images générées ou des conseils pour l'utilisateur.")

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://www.facebook.com/share/g/SpQ3RD4dqmVHwfFm/" target="_blank">Suivez-moi sur Facebook</a>
    </footer>
""", unsafe_allow_html=True)

# Fonction pour afficher un loader pendant le traitement
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)  # Simuler un délai pour l'exemple
