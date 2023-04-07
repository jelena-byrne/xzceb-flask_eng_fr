""" translation program using Python and IBM Watson Language Translator"""

# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# initiating the Watson Language Translator instance:
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-04-07', authenticator=authenticator)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com')


def englishToFrench(englishText):
    """ a function to translate English to French """
    if englishText is None:
        # handling empty input from user:
        return None
    fr_translated_text = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    # isolate the written translation in the dictionary object returned
    frenchText = fr_translated_text["translations"][0]["translation"]
    return frenchText


def frenchToEnglish(frenchText):
    """ a function to translate French to English """
    if frenchText is None:
        # handling empty input from user:
        return None
    en_translated_text = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result()
    # isolate the written translation in the dictionary object returned
    englishText = en_translated_text["translations"][0]["translation"]
    return englishText


def main():
    """ main function to call on translation functions listed above """
    # Capture the text user wants to translate:
    englishText = input(
        "Please enter text you would like to translate to French: ")
    print(englishToFrench(englishText))
    # Capture the text user wants to translate:
    frenchText = input(
        "Please enter text you would like to translate to English: ")
    print(frenchToEnglish(frenchText))


if __name__ == "__main__":
    main()
