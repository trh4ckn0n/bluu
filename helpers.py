import streamlit as st

def get_user_inputs():
    """
    Récupère les choix de l'utilisateur via l'interface Streamlit.
    """
    style = st.selectbox(
        "Choisissez un style de logo :",
        ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"],
        index=0
    )
    if style == "Autre":
        style = st.text_input("Entrez votre style personnalisé :", value="")

    color = st.selectbox(
        "Sélectionnez la couleur dominante :",
        ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"],
        index=0
    )
    if color == "Autre":
        color = st.text_input("Entrez votre couleur personnalisée :", value="")

    background = st.selectbox(
        "Choisissez la couleur du fond :",
        ["Noir texturé", "Gris foncé métallique", "Bleu nuit", "Rouge sombre", "Autre"],
        index=0
    )
    if background == "Autre":
        background = st.text_input("Entrez votre couleur de fond personnalisée :", value="")

    hidden_word = st.text_input("Quel mot voulez-vous inclure de manière cachée ?", value="TRHACKNON")

    user_prompt = st.text_area("Prompt pour DALL·E", value=f"""
Une œuvre d'art numérique représentant un cœur néon {color} en forme de circuit imprimé, lumineux sur fond {background}. Autour, plusieurs personnages masqués façon Guy Fawkes, en capuche, certains sur ordinateur, d'autres dans l'ombre. Un personnage réconforte un homme triste, symbolisant l'empathie. Des ailes translucides {color} apparaissent en arrière-plan, comme une protection éthérée. Du code binaire, des effets glitch et un message “CAPITALISM IS PAST” s'intègrent à la scène. Le mot caché "{hidden_word}" est dissimulé dans les circuits. Ambiance {style.lower()} sensible.
""".strip())

    return style, color, background, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée dans l'interface Streamlit.
    """
    st.image(image_url, caption="Image générée par OpenAI", use_column_width=True)
    st.markdown(f"**Lien de l'image générée** : [Voir l'image ici]({image_url})")
