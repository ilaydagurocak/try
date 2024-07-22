from transformers import pipeline

def ai_detector(text):
    detector = pipeline('text-classification', model='roberta-base-openai-detector')
    result = detector(text)
    return result
