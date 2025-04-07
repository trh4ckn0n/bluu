import streamlit as st
from logo_generator import generate_image
from helpers import get_user_inputs, show_image
import time

# Fonction pour normaliser les couleurs
def normalize_color(color_input):
    color_map = {
        "vert": "Vert néon",
        "rose": "Rose fluorescent",
        "bleu": "Bleu électrique",
        "violet": "Violet translucide",
        "rouge": "Rouge vif",
        "jaune": "Jaune solaire",
        "cyan": "Cyan électrique",
        "orange": "Orange fluo",
        "blanc": "Blanc éclatant",
        "gris": "Gris métallisé",
    }
    return color_map.get(color_input.lower(), color_input)  # Retirer la normalisation directe pour "Autre"

# Configurer la page
st.set_page_config(page_title="Trhacknon's dalle tool", page_icon=":guardsman:", layout="wide")
st.header("Générateur d'Images et Interface Interactive")

# Fonction pour afficher un loader personnalisé
def display_loader():
    with st.spinner("Génération de l'image..."):
        time.sleep(3)  # Simuler un délai pour l'exemple

# Charger le CSS personnalisé
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appliquer le CSS personnalisé
local_css("style.css")

# Récupérer les entrées de l'utilisateur depuis helpers.py
style, color, background, hidden_word, user_prompt = get_user_inputs()

# Sidebar avec options
st.sidebar.title("Options")
style = st.sidebar.selectbox("Choisissez un style", 
                             ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"],
                             index=["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"].index(style), 
                             key="style_selectbox")

color = st.sidebar.selectbox("Sélectionnez la couleur dominante", 
                             ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", 
                              "Rouge vif", "Jaune solaire", "Cyan électrique", "Orange fluo", 
                              "Blanc éclatant", "Gris métallisé", "Autre"],
                             index=["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", 
                                    "Rouge vif", "Jaune solaire", "Cyan électrique", "Orange fluo", 
                                    "Blanc éclatant", "Gris métallisé", "Autre"].index(color),
                             key="color_selectbox")

background = st.sidebar.selectbox("Choisissez la couleur du fond", 
                                  ["Noir texturé", "Gris foncé métallique", "Bleu nuit", "Rouge sombre", "Autre"],
                                  index=["Noir texturé", "Gris foncé métallique", "Bleu nuit", "Rouge sombre", "Autre"].index(background),
                                  key="background_selectbox")

hidden_word = st.sidebar.text_input("Quel mot voulez-vous inclure de manière cachée ?", value=hidden_word, key="hidden_word_input")

user_prompt = st.sidebar.text_area("Description du logo", value=user_prompt, key="user_prompt_textarea")

# Normaliser les couleurs si l'option "Autre" est choisie
if color.lower() != "autre":
    color = normalize_color(color)
if background.lower() != "autre":
    background = normalize_color(background)

# Si l'utilisateur choisit "Autre", afficher un champ de texte pour que l'utilisateur saisisse sa propre couleur
if color.lower() == "autre":
    color = st.sidebar.text_input("Spécifiez votre propre couleur", value=color, key="color_input")

if background.lower() == "autre":
    background = st.sidebar.text_input("Spécifiez votre propre couleur de fond", value=background, key="background_input")

# Appliquer les couleurs au style
st.markdown(f"""
    <style>
        body {{
            background-color: {background};
            color: {color};
        }}
    </style>
""", unsafe_allow_html=True)

# Afficher un résumé des choix dans la sidebar
st.sidebar.markdown("""
<div style="font-family:'Press Start 2P'; border:1px solid #ff0000; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé de vos choix</h2>
    <ul>
        <li><b>Style</b>: {}</li>
        <li><b>Couleur</b>: {}</li>
        <li><b>Fond</b>: {}</li>
        <li><b>Mot caché</b>: {}</li>
        <li><b>Description</b>: {}</li>
    </ul>
</div>
""".format(style, color, background, hidden_word, user_prompt), unsafe_allow_html=True)

# Section principale
st.markdown("Créons quelque chose de magnifique et puissant ensemble.")
st.markdown("""
<div style="font-family:'Press Start 2P'; border:1px solid #7CFC0099; border-radius:8px; padding:16px; margin:16px 0; background-color:#000000; color:#fff;">
    <h2>Résumé de vos choix</h2>
    <ul>
        <li><b>Style</b>: {}</li>
        <li><b>Couleur</b>: {}</li>
        <li><b>Fond</b>: {}</li>
        <li><b>Mot caché</b>: {}</li>
        <li><b>Description</b>: {}</li>
    </ul>
</div>
""".format(style, color, background, hidden_word, user_prompt), unsafe_allow_html=True)

# Utilisation d'un radio button pour simuler des onglets
tab = st.radio("Choisissez une section", ["Générer", "Paramètres"], key="tabs_radio")

if tab == "Générer":
    st.subheader("Générer une image")
    if st.button("Générer l'Image", key="generate_button"):
        display_loader()  # Affichage du loader
        # Formuler le prompt complet
        full_prompt = f"{style} style, {color} color, {background} background. Hidden word: {hidden_word}. {user_prompt}"
        image_url = generate_image(full_prompt)
        show_image(image_url)

elif tab == "Paramètres":
    st.subheader("Paramètres de personnalisation")
    size = st.slider("Sélectionner la taille de l'image", 100, 2000, 1024, key="size_slider")
    st.write(f"Taille de l'image : {size}x{size}")
    st.write("Modifiez les paramètres ci-dessus pour personnaliser votre image.")

# Footer
st.markdown("""
    <footer style="text-align: center; padding: 10px; font-size: 12px; color: #888;">
        Créé avec ❤️ par trhacknon | <a href="https://t.me/@trhacknon" target="_blank">Contactez-moi sur Telegram</a>
    </footer>
""", unsafe_allow_html=True)
