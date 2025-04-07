import streamlit as st

def get_user_inputs():
    """
    Interface utilisateur pour choisir les paramètres du logo.
    """
    style_options = ["Cyberpunk", "Hacker Underground", "Futuriste sensible", "Dark Artistic", "Autre"]
    color_options = ["Rose néon", "Bleu digital", "Violet translucide", "Rouge profond", "Autre"]

    style = st.selectbox("Choisissez un style de logo :", style_options)
    color = st.selectbox("Sélectionnez la couleur dominante :", color_options)

    hidden_word = st.text_input("Mot à inclure de manière cachée :", value="TRHACKNON")

    default_prompt = f"""
Une œuvre d'art numérique représentant un cœur néon rose en forme de circuit imprimé, lumineux sur fond noir texturé. Autour, plusieurs personnages masqués façon Guy Fawkes, en capuche, certains sur ordinateur, d'autres dans l'ombre. Un personnage réconforte un homme triste, symbolisant l'empathie. Des ailes translucides violettes apparaissent en arrière-plan, comme une protection éthérée. Du code binaire, des effets glitch et un message “CAPITALISM IS PAST” s'intègrent à la scène. Le mot caché "{hidden_word}" est dissimulé dans les circuits. Ambiance cyberpunk underground sensible.
""".strip()

    user_prompt = st.text_area("Prompt image (modifiable)", value=default_prompt)

    return style, color, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée dans Streamlit.
    """
    st.image(image_url, caption="Image générée", use_column_width=True)
    st.markdown(f"[Voir l'image ici]({image_url})")
