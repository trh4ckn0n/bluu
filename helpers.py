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

    color = st.selectbox(
        "Sélectionnez la couleur dominante :",
        ["Vert néon", "Rose fluorescent", "Bleu électrique", "Violet translucide", "Autre"],
        index=0
    )

    hidden_word = st.text_input("Quel mot voulez-vous inclure de manière cachée ?", value="TRHACKNON")

    # Prompt auto-généré basé sur l'image montrée
    user_prompt = st.text_area("Prompt pour DALL·E", value=f"""
A dark cyberpunk alley at night, filled with masked hackers riding dirt bikes and scooters, all wearing hoodies and Guy Fawkes masks. Neon wires and glowing cables hang above, casting a vibrant blue, pink, and red glow across the scene. Some hackers sit with laptops, others wheelie through puddles, all surrounded by an electric, chaotic atmosphere. The environment is gritty and urban, inspired by underground activism and digital rebellion. Cartoon-style hacker mascots stand in corners, giving attitude, dressed in dark hooded gear with neon accents. Subtle graffiti and digital circuit textures line the walls. The word "{hidden_word}" is hidden somewhere in the scene as graffiti or digital code. Comic-book style, highly detailed, vibrant contrast, with glitch and digital distortion effects to enhance the underground cyber feel.
""".strip())

    return style, color, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée dans l'interface Streamlit.
    """
    st.image(image_url, caption="Image générée par OpenAI", use_column_width=True)
    st.markdown(f"**Lien de l'image générée** : [Voir l'image ici]({image_url})")
