import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version='2023-04-04', authenticator=authenticator)
lt.set_service_url(url)

def englishToFrench(englishText):
    # a function to translate English to French
    frenchText = LanguageTranslatorV3.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    # a function to translate French to English
    englishText = LanguageTranslatorV3.translate(text=frenchText, model_id='fr-en').get_result()
    return englishText

