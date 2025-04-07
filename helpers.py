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

    hidden_word = st.text_input("Quel mot voulez-vous inclure de manière cachée ?", value="TRHACKNON")

    user_prompt = st.text_area("Description du logo", value="Un logo {style} sombre et contrasté, inspiré d'Anonymous et de l'hacktivisme, incarne l'amour et la protection envers les femmes autistes hypersensibles. Fond noir texturé avec du code vert néon, un papillon digital aux ailes violettes translucides, symbolisant la beauté cachée dans la technologie. Des circuits imprimés et des reflets irisés ornent les ailes. Un masque de Guy Fawkes discret en arrière-plan, représentant la protection invisible. Le mot '{hidden_word}' est subtilement caché dans le code ou les circuits, un message secret pour les âmes sensibles. L’ambiance cyberpunk douce mais puissante évoque un sanctuaire numérique sûr, où l’hyper-perception est un don et non une malédiction. L’image doit inspirer courage et confiance, un lieu où les femmes autistes hypersensibles trouvent un refuge dans un monde caché et mystérieux.")

    return style, color, hidden_word, user_prompt

def show_image(image_url):
    """
    Affiche l'image générée par OpenAI dans l'interface.
    """
    st.image(image_url, caption="Image générée par OpenAI", use_column_width=True)
    st.markdown(f"**Lien de l'image générée** : [Voir l'image ici]({image_url})")
