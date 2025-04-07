import streamlit as st

def get_user_inputs():
    """
    Interface utilisateur pour choisir les paramètres du logo.
    """
    style = st.selectbox(
        "Choisissez un style de logo :",
        ["Cyberpunk", "Hacker Underground", "Futuriste sensible", "Dark Artistic", "Autre"],
        index=0
    )

    color = st.selectbox(
        "Sélectionnez la couleur dominante :",
        ["Rose néon", "Bleu digital", "Violet translucide", "Rouge profond", "Autre"],
        index=0
    )

    hidden_word = st.text_input("Mot à inclure de manière cachée :", value="TRHACKNON")

    user_prompt = st.text_area("Prompt image (modifiable)", value=f"""
A digital artwork showing a bright neon pink heart shaped like a circuit board, glowing against a textured black background. Surrounding it are multiple Guy Fawkes masked figures in hoodies, some watching screens, others standing in shadows. One character comforts a sad man, representing empathy in the hacker world. A pair of ethereal translucent wings in violet hover behind the heart, symbolizing protection and sensitivity. Binary code, glitch effects, and subtle graffiti fill the dark space. One masked figure stands in front of the phrase “CAPITALISM IS PAST”. The word "{hidden_word}" is hidden in the circuits or digital code. High contrast, emotional, underground hacker cyberpunk style, like a digital sanctuary for hypersensitive minds.
""".strip())

    return style, color, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée dans Streamlit.
    """
    st.image(image_url, caption="Image générée", use_column_width=True)
    st.markdown(f"[Voir l'image ici]({image_url})")
