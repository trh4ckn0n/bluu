import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time

st.set_page_config(page_title="Trhacknon's dalle tool", page_icon=":guardsman:", layout="wide")
st.header("Générateur d'Images et Interface Interactive")

# Fonction loader
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)

# Charger CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# Sidebar
st.sidebar.title("Options")

# Définir les choix possibles
style_choices = ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"]
color_choices = ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Rouge sombre", "Autre"]
background_choices = ["Noir profond", "Bleu nuit", "Violet galactique", "Vert binaire", "Autre"]

# Inputs avec fallback sécurisé
style = st.sidebar.selectbox("Choisissez un style", style_choices,
                             index=style_choices.index("Cyberpunk") if "Cyberpunk" in style_choices else 0,
                             key="style_selectbox")

color = st.sidebar.selectbox("Sélectionnez la couleur dominante", color_choices,
                             index=color_choices.index("Vert néon") if "Vert néon" in color_choices else 0,
                             key="color_selectbox")

background = st.sidebar.selectbox("Choisissez le fond", background_choices,
                                  index=background_choices.index("Noir profond") if "Noir profond" in background_choices else 0,
                                  key="background_selectbox")

hidden_word = st.sidebar.text_input("Quel mot voulez-vous inclure de manière cachée ?", key="hidden_word_input")
user_prompt = st.sidebar.text_area("Description du logo", key="user_prompt_textarea")
size = st.sidebar.slider("Taille de l'image", 256, 1024, 512, step=128, key="size_slider")

# Résumé visuel dans la sidebar
st.sidebar.markdown(f"""
<div style="font-family:'Press Start 2P'; border:1px solid #ff0000; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé</h2>
    <ul>
        <li><b>Style</b>: {style}</li>
        <li><b>Couleur</b>: {color}</li>
        <li><b>Fond</b>: {background}</li>
        <li><b>Mot caché</b>: {hidden_word}</li>
        <li><b>Description</b>: {user_prompt}</li>
        <li><b>Taille</b>: {size}x{size}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Section principale
tab = st.radio("Choisissez une section", ["Générer", "Paramètres"], key="tabs_radio")

if tab == "Générer":
    st.subheader("Générer une image")
    if st.button("Générer l'Image", key="generate_button"):
        display_loader()
        full_prompt = f"{style} style, {color} color, {background} background. Hidden word: {hidden_word}. {user_prompt}"
        image_url = generate_image(full_prompt, size)
        show_image(image_url)

elif tab == "Paramètres":
    st.subheader("Paramètres de personnalisation")
    st.write("Modifiez les paramètres dans la sidebar pour personnaliser l’image générée.")

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://t.me/@trhacknon" target="_blank">Contactez-moi sur Telegram</a>
    </footer>
""", unsafe_allow_html=True)
