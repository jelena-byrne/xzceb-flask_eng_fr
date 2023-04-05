import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version??}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def englishToFrench(englishText):
    # a function to translate English to French
    englishText = input("Please enter text you would like to translate to French: /n")
    frenchText = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText

def frenchToEnglish(frenchText):
    # a function to translate French to English
    frenchText = input("Please enter text you would like to translate to English: /n")
    englishText = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    return englishText

