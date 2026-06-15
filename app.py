from pathlib import Path
import pickle

import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "next_word_prediction_model.h5"
TOKENIZER_PATH = BASE_DIR / "tokenizer.pickle"


st.set_page_config(
    page_title="AI Next Word Prediction",
    page_icon="🧠",
    layout="centered",
)


@st.cache_resource
def load_prediction_assets():
    model = load_model(MODEL_PATH)
    with TOKENIZER_PATH.open("rb") as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer


def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]

    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]

    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding="pre")
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = int(np.argmax(predicted, axis=1)[0])

    return tokenizer.index_word.get(predicted_word_index)


model, tokenizer = load_prediction_assets()

st.title("🧠 AI Next Word Prediction")
st.caption("LSTM RNN language model trained on Shakespeare's Hamlet text.")

input_text = st.text_input(
    "Enter a sequence of words",
    placeholder="Example: to be or not to",
)

if st.button("Predict Next Word", type="primary"):
    if input_text.strip():
        max_sequence_len = model.input_shape[1] + 1
        next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
        if next_word:
            st.success(f"Predicted next word: **{next_word}**")
        else:
            st.warning("Could not predict the next word.")
    else:
        st.info("Please enter a sequence of words.")
