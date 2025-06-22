import google.generativeai as genai

genai.configure(api_key="AIzaSyA-h4byyEwAD9dzlwuTmX0wtjIQ4_uqh5A")

models = genai.list_models()
for model in models:
    print(model.name)
