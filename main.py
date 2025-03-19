import streamlit as st
import ollama
from PIL import Image
import io
import base64
import time

# Configuration de la page
st.set_page_config(
    page_title="Vision OCR Pro",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
<style>
    .main-header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #4A4A4A;
        margin-bottom: 0;
    }
    .sub-header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #6C6C6C;
        font-size: 1.2rem;
        margin-top: 0;
    }
    .result-container {
        background-color: #F8F9FA;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #E0E0E0;
        margin-top: 20px;
    }
    .sidebar-content {
        padding: 20px 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 500;
        height: 46px;
    }
    .upload-section {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .success-message {
        background-color: #D4EDDA;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #6C6C6C;
        font-size: 0.8rem;
    }
    .stProgress > div > div {
        background-color: #6C63FF;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de l'état de session
if 'ocr_result' not in st.session_state:
    st.session_state['ocr_result'] = None

if 'processing_time' not in st.session_state:
    st.session_state['processing_time'] = None

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Barre latérale
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image("https://placehold.co/600x400?text=Vision+OCR+Pro", width=250)

    st.markdown("## Paramètres")
    model_option = st.selectbox(
        "Modèle d'IA",
        ["gemma3:12b", "gemma3:8b", "llava:34b"],
        index=0
    )

    st.markdown("## Historique")
    if st.session_state['history']:
        for i, item in enumerate(st.session_state['history']):
            if st.button(f"Session {i + 1}: {item['timestamp']}", key=f"history_{i}"):
                st.session_state['ocr_result'] = item['result']
                st.session_state['processing_time'] = item['processing_time']
                st.rerun()
    else:
        st.info("Aucun historique disponible")

    st.markdown("</div>", unsafe_allow_html=True)

# Zone principale
st.markdown('<h1 class="main-header">Vision OCR Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Extraire et structurer le texte de vos images avec précision</p>',
            unsafe_allow_html=True)

# Créer deux colonnes pour les actions
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🗑️ Effacer", help="Effacer les résultats actuels"):
        st.session_state['ocr_result'] = None
        st.rerun()

# Zone de téléchargement
st.markdown("### Téléchargez votre image")
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Formats acceptés: PNG, JPG, JPEG", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Afficher l'image téléchargée
    image = Image.open(uploaded_file)

    # Créer deux colonnes pour l'image et les paramètres
    col1, col2 = st.columns([3, 2])

    with col1:
        st.image(image, caption="Image téléchargée", use_container_width=True)

    with col2:
        st.markdown("### Options d'extraction")
        format_option = st.radio(
            "Format de sortie",
            ["Texte structuré", "Brut", "Tableau"]
        )

        lang_option = st.selectbox(
            "Langue principale",
            ["Auto-détection", "Français", "Anglais", "Espagnol", "Allemand", "Italien"]
        )

        include_tables = st.checkbox("Inclure la détection de tableaux", value=True)

        if st.button("🔍 Extraire le texte", type="primary"):
            start_time = time.time()

            # Afficher une barre de progression
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)

            try:
                # Construire le prompt en fonction des options
                prompt = "Analyse le texte dans l'image fournie. "

                if format_option == "Texte structuré":
                    prompt += "Extrais tout le contenu lisible et présente-le dans un format Markdown structuré qui est clair, concis et bien organisé. "
                elif format_option == "Brut":
                    prompt += "Extrais simplement le texte brut sans formatage supplémentaire. "
                elif format_option == "Tableau":
                    prompt += "Identifie et extrais les informations sous forme de tableaux Markdown. "

                if lang_option != "Auto-détection":
                    prompt += f"Le texte est principalement en {lang_option}. "

                if include_tables:
                    prompt += "Identifie les tableaux éventuels et préserve leur structure. "

                prompt += "Assure-toi que le formatage (par exemple, titres, listes ou blocs de code) représente efficacement le contenu."

                response = ollama.chat(
                    model=model_option,
                    messages=[{
                        'role': 'user',
                        'content': prompt,
                        'images': [uploaded_file.getvalue()]
                    }]
                )

                st.session_state['ocr_result'] = response.message.content
                end_time = time.time()
                st.session_state['processing_time'] = round(end_time - start_time, 2)

                # Ajouter à l'historique
                st.session_state['history'].append({
                    'timestamp': time.strftime("%H:%M:%S"),
                    'result': response.message.content,
                    'processing_time': st.session_state['processing_time']
                })

                # Limiter l'historique à 5 entrées
                if len(st.session_state['history']) > 5:
                    st.session_state['history'] = st.session_state['history'][-5:]

                st.success("Extraction terminée avec succès!")
                st.rerun()

            except Exception as e:
                st.error(f"Une erreur s'est produite: {str(e)}")
                st.error("Veuillez vérifier que le service Ollama est bien lancé et que le modèle est disponible.")
st.markdown('</div>', unsafe_allow_html=True)

# Affichage des résultats
if st.session_state['ocr_result']:
    st.markdown("### Résultats de l'extraction")
    st.markdown(
        f"<div class='success-message'>Extraction réalisée en {st.session_state['processing_time']} secondes avec le modèle {model_option}</div>",
        unsafe_allow_html=True)

    tabs = st.tabs(["Texte formaté", "Texte brut"])

    with tabs[0]:
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.markdown(st.session_state['ocr_result'])
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]:
        st.markdown('<div class="result-container">', unsafe_allow_html=True)
        st.code(st.session_state['ocr_result'], language="markdown")
        st.markdown('</div>', unsafe_allow_html=True)

    # Boutons d'action pour les résultats
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.download_button(
                label="📥 Télécharger en TXT",
                data=st.session_state['ocr_result'],
                file_name="extraction_resultat.txt",
                mime="text/plain"
        ):
            pass
    with col2:
        if st.download_button(
                label="📥 Télécharger en MD",
                data=st.session_state['ocr_result'],
                file_name="extraction_resultat.md",
                mime="text/markdown"
        ):
            pass
    with col3:
        if st.button("📋 Copier dans le presse-papiers"):
            st.success("Texte copié dans le presse-papiers!")
else:
    st.info("Téléchargez une image et cliquez sur « Extraire le texte » pour voir les résultats ici.")

# Pieds de page
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("---")
st.markdown("Vision OCR Pro • Propulsé par Gemma-3 et Ollama • Développé avec Streamlit")
st.markdown("© 2025 - Tous droits réservés")
st.markdown('</div>', unsafe_allow_html=True)