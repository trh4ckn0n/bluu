import streamlit as st

def get_user_inputs():
    """
    Fonction pour récupérer les choix de l'utilisateur via l'interface.
    """
    style = st.selectbox(
        "Choisissez un style de logo :",
        ["Cyberpunk", "Futuristic", "Hacker Underground", "Artistique", "Autre"],
        index=0
    )

    color = st.selectbox(
        "Sélectionnez la couleur dominante :",
        ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"],
        index=0
    )

    hidden_word = st.text_input("Quel mot voulez-vous inclure de manière cachée ?", value="Bluu Haxxor")

    user_prompt = st.text_area("Description du logo", value="Un logo cyberpunk avec des éléments numériques et un papillon...")

    return style, color, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée par OpenAI dans l'interface.
    """
    st.image(image_url, caption="Image générée par OpenAI", use_column_width=True)
    st.markdown(f"**Lien de l'image générée** : [Voir l'image ici]({image_url})")
