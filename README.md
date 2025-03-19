# Vision OCR Pro

![Banner](https://placehold.co/1200x300?text=Vision+OCR+Pro&font=montserrat)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-FF4B4B)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-0.1.29%2B-green)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 📑 Description

**Vision OCR Pro** est une application web intuitive qui utilise l'intelligence artificielle pour extraire et structurer le texte à partir d'images. Conçue pour maximiser la productivité, elle offre une alternative éthique et locale aux services cloud d'OCR traditionnels.

### 🔒 Confidentialité et Sécurité

- **Traitement 100% local** - Aucun document n'est envoyé sur des serveurs distants
- **Fonctionne hors connexion** - Idéal pour les environnements sécurisés
- **Contrôle total** - Vous maîtrisez où vont vos données

## ✨ Fonctionnalités

- **Reconnaissance précise** du texte dans les images
- **Préservation de la structure** des documents (titres, paragraphes, tableaux)
- **Support multi-langues**
- **Options de formatage variées** (texte structuré, brut, tableau)
- **Interface utilisateur intuitive**
- **Historique des extractions**
- **Export des résultats** en formats TXT et MD

## 📸 Captures d'écran

![image](https://github.com/user-attachments/assets/6fcebdaa-d125-4072-bf1e-334e0cd9a224)


![image](https://github.com/user-attachments/assets/6c04481c-33d3-47ae-bde2-7d6577542ec4)



## 🚀 Installation

### Prérequis

- Python 3.9+
- [Ollama](https://ollama.com/) installé et configuré

### Étapes d'installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Anasseyahnn/vision-ocr-pro.git
   cd vision-ocr-pro
   ```

2. Créez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Assurez-vous que le modèle Gemma-3 est installé dans Ollama :
   ```bash
   ollama pull gemma3:12b
   ```

## 💻 Utilisation

1. Démarrez l'application :
   ```bash
   streamlit run main1.py
   ```

2. Ouvrez votre navigateur et accédez à `http://localhost:8501`

3. Téléchargez une image contenant du texte

4. Configurez les options d'extraction selon vos besoins

5. Cliquez sur "Extraire le texte" et obtenez les résultats instantanément

## 📝 Guide d'utilisation

### Extraire du texte d'une image

1. Cliquez sur "Choisir l'image..." et sélectionnez une image (PNG, JPG, JPEG)
2. Configurez les options d'extraction :
   - **Format de sortie** : Texte structuré, Brut, ou Tableau
   - **Langue principale** : Auto-détection ou langue spécifique
   - **Détection de tableaux** : Activée ou désactivée
3. Cliquez sur "🔍 Extraire le texte"
4. Consultez les résultats dans les onglets "Texte formaté" ou "Texte brut"
5. Utilisez les boutons pour télécharger ou copier les résultats

### Personnalisation des modèles

L'application prend en charge plusieurs modèles d'IA pour l'extraction de texte :
- **gemma3:12b** - Modèle par défaut, excellent équilibre entre précision et vitesse
- **gemma3:8b** - Plus rapide, idéal pour les appareils moins puissants
- **llava:34b** - Plus précis pour les cas complexes, nécessite plus de ressources

## 🛠️ Fichiers du projet

```
vision-ocr-pro/
├── app.py                 # Application principale
├── requirements.txt       # Dépendances Python
├── assets/                # Images et ressources statiques
│   └── placeholder.png    # Image de placeholder
├── README.md              # Documentation              
```

## 📊 Performances

| Modèle | Temps moyen d'extraction | Précision | Consommation mémoire |
|--------|--------------------------|-----------|----------------------|
| gemma3:12b | ~3.5 secondes | 98% | ~8 GB |
| gemma3:8b | ~2.1 secondes | 95% | ~5 GB |
| llava:34b | ~6.2 secondes | 99% | ~15 GB |

## 🔧 Dépannage

### Problèmes courants

- **"Erreur de connexion à Ollama"** : Vérifiez qu'Ollama est bien lancé avec `ollama serve`
- **"Modèle non trouvé"** : Assurez-vous d'avoir téléchargé le modèle avec `ollama pull gemma3:12b`
- **"Mémoire insuffisante"** : Essayez un modèle plus léger comme gemma3:8b

### Logs

Les logs sont disponibles dans le terminal où vous avez lancé l'application.

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment vous pouvez contribuer :

1. Forkez ce dépôt
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 🙏 Remerciements

- [Streamlit](https://streamlit.io/) pour le framework d'interface utilisateur
- [Ollama](https://ollama.com/) pour l'exécution locale des modèles d'IA
- [Google](https://blog.google/technology/ai/gemma-open-models/) pour le modèle open source Gemma-3

---

<div align="center">
  <p>Développé avec ❤️ par <a href="https://github.com/Anasseyahnn">Anasse Yahanan</a></p>
  <p>⭐ N'oubliez pas de mettre une étoile à ce projet si vous l'avez trouvé utile! ⭐</p>
</div>
