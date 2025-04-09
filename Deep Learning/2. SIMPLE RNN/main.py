from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb

word_index = imdb.get_word_index()

model = load_model('simple_rnn_model.h5')

# Function to preprocess user input
def preprocess_text(text):
    """Preprocess the input text for the model."""
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]  # +3 to account for padding
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)  # Pad to the same length as training data
    return padded_review

### Designing the streamlit app
import streamlit as st

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment.")

user_input = st.text_area("Movie Review")

if st.button("Predict Sentiment"):

    preprocessed_input = preprocess_text(user_input)

    prediction = model.predict(preprocessed_input)
    
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'


    ### Display the result
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Prediction Score: {prediction[0][0]}')
else:
    st.write('Please enter a movie review.')