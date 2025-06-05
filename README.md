# 🎬 Clasificador de Sentimiento para Reseñas de Películas

Proyecto desarrollado para **Film Junky Union** 🍿, una comunidad dedicada a los amantes del cine clásico 🎞️. El objetivo principal fue construir un sistema inteligente 🤖 capaz de detectar automáticamente reseñas **positivas o negativas** utilizando técnicas de **Procesamiento de Lenguaje Natural (NLP)** 🧾.

Este proyecto fue parte de mi formación como **Data Scientist** en **TripleTen** y está disponible como una aplicación web interactiva.

---

## 🔗 Prueba la App

🟢 ¡El modelo está en línea! Puedes probarlo en esta app hecha con **Streamlit** y desplegada en **Render**:

👉 [https://ai-clasificador-de-criticas.onrender.com/](https://ai-clasificador-de-criticas.onrender.com/)

> ⏳ *Nota: Puede tomar unos segundos cargar si ha estado inactiva.*

---

## 📌 Objetivo del Proyecto

Clasificar automáticamente reseñas de películas en inglés del sitio IMDB 🗃️ como **positivas** o **negativas**, facilitando la moderación de contenido en plataformas de discusión y mejorando la experiencia de los usuarios cinéfilos.

---

## ⚙️ Proceso de Desarrollo

### 🧼 Procesamiento de Texto
- Conversión a minúsculas y limpieza de caracteres especiales.
- Lematización con **SpaCy**.
- Eliminación de *stopwords* usando **NLTK**.

### 🧠 Vectorización
- Representación de texto con **TF-IDF** para resaltar las palabras más informativas.

### 🤖 Modelado
Se entrenaron y compararon los siguientes algoritmos:
- **Regresión Logística** (mejor desempeño)
- **Gradient Boosting**
- **LightGBM**

### 📊 Evaluación
- **F1-score (test):** 0.88 🏆  
- **ROC AUC:** 0.95  
- **APS:** 0.95

El modelo de Regresión Logística demostró una excelente capacidad de generalización 🧪 y superó el umbral de calidad mínimo para producción (0.85).

---

## 🧰 Tecnologías Utilizadas

- Python 🐍
- Pandas & NumPy
- Scikit-learn 📊
- LightGBM ⚡
- NLTK & SpaCy
- Matplotlib & Seaborn
- Streamlit 🌐
- Render (para el despliegue)

---

## 🚀 Aplicaciones Reales

- **Moderación de contenido** 🛡️: filtrado automático de reseñas negativas o inapropiadas.
- **Sistemas de recomendación** 🎯: análisis del sentimiento para mejorar las recomendaciones personalizadas.
- **Expansión multilingüe** 🌍: posibilidad de escalar a otros idiomas y dominios.

---

## ✨ Conclusión

Este proyecto integra habilidades clave en NLP, modelado predictivo y despliegue web. A través de una solución funcional y accesible, demuestra cómo el análisis automatizado de sentimientos puede mejorar plataformas centradas en la comunidad cinéfila 🎥👥.

---

📫 ¿Comentarios o sugerencias? ¡Estoy abierto a feedback!
