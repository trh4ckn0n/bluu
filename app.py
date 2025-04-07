import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time

st.set_page_config(page_title="Trhacknon's dalle tool", page_icon=":guardsman:", layout="wide")
st.header("Générateur d'Images et Interface Interactive")

# Fonction pour afficher un loader personnalisé
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)

# Charger le CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appliquer le CSS personnalisé
local_css("style.css")

# Valeur par défaut pour la taille
if "size" not in st.session_state:
    st.session_state.size = 1024

# Récupérer les entrées utilisateur depuis helpers.py
style, color, background, hidden_word, user_prompt = get_user_inputs()

# SIDEBAR
st.sidebar.title("Options")

style = st.sidebar.selectbox("Choisissez un style", 
                             ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"],
                             index=["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"].index(style), 
                             key="style_selectbox")

color = st.sidebar.selectbox("Sélectionnez la couleur dominante", 
                             ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"],
                             index=["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"].index(color),
                             key="color_selectbox")

background = st.sidebar.selectbox("Background", 
                                  ["Noir profond", "Galaxy", "Grille matrix", "Futur industriel", "Autre"],
                                  index=["Noir profond", "Galaxy", "Grille matrix", "Futur industriel", "Autre"].index(background),
                                  key="background_selectbox")

hidden_word = st.sidebar.text_input("Quel mot voulez-vous inclure de manière cachée ?", value=hidden_word, key="hidden_word_input")

user_prompt = st.sidebar.text_area("Description du logo", value=user_prompt, key="user_prompt_textarea")

# Résumé visuel
st.sidebar.markdown(f"""
<div style="font-family:'Press Start 2P'; border:1px solid #ff0000; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé</h2>
    <ul>
        <li><b>Style</b>: {style}</li>
        <li><b>Couleur</b>: {color}</li>
        <li><b>Background</b>: {background}</li>
        <li><b>Mot caché</b>: {hidden_word}</li>
        <li><b>Description</b>: {user_prompt}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Titre principal
st.markdown("Créons quelque chose de magnifique et puissant ensemble.")

# Affichage du même résumé dans le corps
st.markdown(f"""
<div style="font-family:'Press Start 2P';border:1px solid #7CFC0099; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé</h2>
    <ul>
        <li><b>Style</b>: {style}</li>
        <li><b>Couleur</b>: {color}</li>
        <li><b>Background</b>: {background}</li>
        <li><b>Mot caché</b>: {hidden_word}</li>
        <li><b>Description</b>: {user_prompt}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Choix de l'onglet
tab = st.radio("Choisissez une section", ["Générer", "Paramètres"], key="tabs_radio")

if tab == "Paramètres":
    st.subheader("Paramètres de personnalisation")
    st.session_state.size = st.slider("Taille de l'image", 256, 1024, st.session_state.size, step=256, key="size_slider")
    st.write(f"Taille sélectionnée : {st.session_state.size}x{st.session_state.size}")
    st.write("Modifiez les options dans la colonne de gauche pour personnaliser votre image.")

elif tab == "Générer":
    st.subheader("Générer une image")
    if st.button("Générer l'Image", key="generate_button"):
        display_loader()
        image_url = generate_image(user_prompt, size=st.session_state.size)
        show_image(image_url)

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://t.me/@trhacknon" target="_blank">Contact Telegram</a>
    </footer>
""", unsafe_allow_html=True)
