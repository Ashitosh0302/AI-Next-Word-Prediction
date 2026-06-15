# 🧠 AI Next Word Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?style=flat-square&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat-square&logo=streamlit)
![Model](https://img.shields.io/badge/Model-LSTM_RNN-purple?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Shakespeare_Hamlet-teal?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

```text
╔════════════════════════════════════════════════════════════╗
║  Project     : AI Next Word Prediction                     ║
║  Model       : LSTM RNN Language Model                     ║
║  Dataset     : Shakespeare Hamlet Text                     ║
║  Framework   : TensorFlow / Keras + Streamlit              ║
║  Author      : ASHITOSH                                    ║
╚════════════════════════════════════════════════════════════╝
```

---

## 📌 Project Overview

**AI Next Word Prediction** is a deep learning NLP project that predicts the next word for a given text sequence. The model is trained on Shakespeare's *Hamlet* text using an LSTM-based Recurrent Neural Network.

The project includes:

- 🧠 A trained LSTM next-word prediction model
- 🔤 A saved tokenizer for text-to-sequence conversion
- 📚 Hamlet text dataset
- 📓 Training and experimentation notebook
- 🚀 A deployable Streamlit web application

---

## ✨ Features

- ✅ Predicts the next likely word from user input
- ✅ Uses n-gram sequence generation for language modeling
- ✅ Pads sequences before model inference
- ✅ Uses a trained Keras `.h5` model
- ✅ Provides a simple Streamlit UI
- ✅ Ready for local running and Streamlit Cloud deployment

---

## 🗂️ Project Directory

```text
LSTM_RNN_imple/
├── .streamlit/
│   └── config.toml
├── app.py
├── experiments.ipynb
├── hamlet.txt
├── next_word_prediction_model.h5
├── README.md
├── requirements.txt
├── runtime.txt
└── tokenizer.pickle
```

---

## 🛠️ Tech Stack

| Badge | Library | Purpose |
|-------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) | Python | Core language |
| ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat-square&logo=tensorflow) | TensorFlow | Deep learning framework |
| ![Keras](https://img.shields.io/badge/Keras-API-red?style=flat-square&logo=keras) | Keras | Model building API |
| ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square&logo=streamlit) | Streamlit | Web app interface |
| ![NumPy](https://img.shields.io/badge/NumPy-Array-green?style=flat-square&logo=numpy) | NumPy | Numerical operations |
| ![Pandas](https://img.shields.io/badge/Pandas-Data-purple?style=flat-square&logo=pandas) | Pandas | Data manipulation |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-Plot-blue?style=flat-square) | Matplotlib | Visualization |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square&logo=scikit-learn) | Scikit-learn | Utilities |
| ![NLTK](https://img.shields.io/badge/NLTK-NLP-yellow?style=flat-square) | NLTK | Text / corpus tools |

---

## 🧪 Model Information

The model pipeline follows these steps:

| Step | Description |
|------|-------------|
| `1` | Collect Hamlet text data using NLTK / Gutenberg |
| `2` | Tokenize text with `tensorflow.keras.preprocessing.text.Tokenizer` |
| `3` | Create n-gram input sequences from each line of text |
| `4` | Pad all sequences to a fixed length |
| `5` | Split data into predictors and labels |
| `6` | Convert labels into categorical vectors |
| `7` | Train an LSTM RNN model |
| `8` | Save the trained model and tokenizer for inference |

### 🏗️ Model Architecture

```text
┌─────────────────────────────────────────┐
│       Embedding(total_words, 100)       │  ← Word vectors
├─────────────────────────────────────────┤
│    LSTM(150, return_sequences=True)     │  ← Sequence layer 1
├─────────────────────────────────────────┤
│             Dropout(0.2)               │  ← Regularization
├─────────────────────────────────────────┤
│              LSTM(100)                  │  ← Sequence layer 2
├─────────────────────────────────────────┤
│   Dense(total_words, activation=       │
│              "softmax")                │  ← Output probabilities
└─────────────────────────────────────────┘
```
---

## 🚀 Starting Commands

### 1. Clone or Open the Project

```bash
cd "LSTM_RNN_imple"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Windows with TensorFlow support:

```bash
py -3.11 -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit App

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 💡 How Prediction Works

When the user enters text:

| Step | Action |
|------|--------|
| `1` | Input text is converted into token IDs |
| `2` | Token list is trimmed if longer than model input length |
| `3` | Sequence is padded |
| `4` | LSTM model predicts probabilities for all known words |
| `5` | Word with highest probability is returned as the next word |

**Example:**

```text
┌─────────────────────────────────┐
│  Input  : to be or not to      │
│  Output : be                   │
└─────────────────────────────────┘
```

---

## 👨‍💻 Author

> ![Author](https://img.shields.io/badge/Author-ASHITOSH-blue?style=flat-square&logo=github)