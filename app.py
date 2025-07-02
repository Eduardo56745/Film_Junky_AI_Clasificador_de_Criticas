import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Descarga recursos de nltk si es necesario
nltk.download('stopwords')
nltk.download('wordnet')

# Cargar modelo y vectorizador
logistic_model = joblib.load('model.pkl')
tfidf_vectorizer = joblib.load('vectorizer.pkl')

# Función de normalización


def normalize_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)


# Interfaz de Streamlit
st.title("Clasificador de Sentimientos de Reseñas")

user_input = st.text_area("Escribe una reseña en inglés:")

if st.button("Predecir"):
    if user_input.strip() == "":
        st.warning("Por favor, escribe una reseña.")
    else:
        norm_text = normalize_text(user_input)
        vectorized = tfidf_vectorizer.transform([norm_text])
        prediction = logistic_model.predict(vectorized)[0]
        probabilities = logistic_model.predict_proba(vectorized)[0]

        st.subheader("Resultado:")
        st.write(
            f"**Sentimiento predicho:** {'Positivo 😊' if prediction == 1 else 'Negativo 😠'}")
        st.write(f"**Probabilidad Positiva:** {probabilities[1]:.2f}")
        st.write(f"**Probabilidad Negativa:** {probabilities[0]:.2f}")
