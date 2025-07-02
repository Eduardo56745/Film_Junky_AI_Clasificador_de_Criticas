import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

# Cargar modelo y vectorizador
logistic_model = joblib.load('model.pkl')
tfidf_vectorizer = joblib.load('vectorizer.pkl')

# Función de normalización


def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)


# Interfaz de Streamlit
st.header("🎬 Clasificador de Sentimientos de Reseñas 🎭")

user_input = st.text_area("✍️ Escribe una reseña en inglés:")

if st.button("🔍 Predecir"):
    if not user_input.strip():
        st.warning("⚠️ Por favor, escribe una reseña válida.")
    else:
        norm_text = normalize_text(user_input)
        vectorized = tfidf_vectorizer.transform([norm_text])
        prediction = logistic_model.predict(vectorized)[0]
        probabilities = logistic_model.predict_proba(vectorized)[0]

        st.subheader("✅ Resultado:")
        sentiment = 'Positivo 😊' if prediction == 1 else 'Negativo 😠'
        st.write(f"**Sentimiento predicho:** {sentiment}")

        pos_prob = probabilities[1] * 100
        neg_prob = probabilities[0] * 100

        st.write(f"**Probabilidad Positiva:** {pos_prob:.2f}%")
        st.progress(probabilities[1])

        st.write(f"**Probabilidad Negativa:** {neg_prob:.2f}%")
        st.progress(probabilities[0])
