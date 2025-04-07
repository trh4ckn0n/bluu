import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time

st.set_page_config(page_title="Trhacknon's dalle tool", page_icon=":guardsman:", layout="wide")
st.header("Générateur d'Images et Interface Interactive")

# Appliquer le CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Affichage loader
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)

# Récupération des choix
style, color, background, hidden_word, user_prompt = get_user_inputs()

# Sidebar
st.sidebar.title("Options")
style = st.sidebar.selectbox("Style", ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"], index=0, key="style_selectbox")
if style == "Autre":
    style = st.sidebar.text_input("Style personnalisé", value=style, key="custom_style")

color = st.sidebar.selectbox("Couleur dominante", ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"], index=0, key="color_selectbox")
if color == "Autre":
    color = st.sidebar.text_input("Couleur personnalisée", value=color, key="custom_color")

background = st.sidebar.selectbox("Couleur de fond", ["Noir texturé", "Gris foncé métallique", "Bleu nuit", "Rouge sombre", "Autre"], index=0, key="background_selectbox")
if background == "Autre":
    background = st.sidebar.text_input("Fond personnalisé", value=background, key="custom_background")

hidden_word = st.sidebar.text_input("Mot caché", value=hidden_word, key="hidden_word_input")
user_prompt = st.sidebar.text_area("Prompt complet", value=user_prompt, key="user_prompt_textarea")

# Résumé
st.sidebar.markdown(f"""
<div style="font-family:'Press Start 2P'; border:1px solid #ff0000; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé de vos choix</h2>
    <ul>
        <li><b>Style</b>: {style}</li>
        <li><b>Couleur</b>: {color}</li>
        <li><b>Fond</b>: {background}</li>
        <li><b>Mot caché</b>: {hidden_word}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Résumé principal
st.markdown(f"""
<div style="font-family:'Press Start 2P'; border:1px solid #7CFC0099; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé de vos choix</h2>
    <ul>
        <li><b>Style</b>: {style}</li>
        <li><b>Couleur</b>: {color}</li>
        <li><b>Fond</b>: {background}</li>
        <li><b>Mot caché</b>: {hidden_word}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Tabs
tab = st.radio("Choisissez une section", ["Générer", "Paramètres"], key="tabs_radio")

if tab == "Générer":
    st.subheader("Générer une image")
    if st.button("Générer l'Image", key="generate_button"):
        display_loader()
        image_url = generate_image(user_prompt, size=size)
        show_image(image_url)

elif tab == "Paramètres":
    st.subheader("Paramètres de personnalisation")
    size = st.slider("Taille de l'image", 100, 2000, 1024, key="size_slider")
    st.write(f"Taille actuelle : {size}x{size}")

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://t.me/@trhacknon" target="_blank">Contact Telegram</a>
    </footer>
""", unsafe_allow_html=True)
