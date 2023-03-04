from fastapi import FastAPI

from src.data_models import InputRequest, Response
from src.load_models import load_models
from src.text_preprocessor import TextPreprocessor

CLASS_MAPPING = {
    0: "non-harmful",
    1: "cyberbullying",
    2: "hate-speech",
}

app = FastAPI()

model, vectorizer = load_models("models")
preprocessor = TextPreprocessor()


@app.post("/detect-hate-speech", response_model=Response)
def get_prediction(input: InputRequest):
    text = input.text
    text_preprocessed = preprocessor.preprocess(text)
    text_vectorized = vectorizer.transform([text_preprocessed])
    prediction = model.predict(text_vectorized)[0]
    return Response(predicted_class=CLASS_MAPPING[prediction])
