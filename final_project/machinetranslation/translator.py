"""
This module translates from english to french and from french to english
Makes use of IBM Watson Language Translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(some_text):
    """
    e2f
    """
    if some_text is None:
        return None
    translation = language_translator.translate(
        text=some_text, model_id="en-fr"
    ).get_result()
    translated_text = translation["translations"][0]["translation"]
    return translated_text

def frenchToEnglish(some_text):
    """
    f2e
    """
    if some_text is None:
        return None
    translation = language_translator.translate(
        text=some_text, model_id="fr-en"
    ).get_result()
    translated_text = translation["translations"][0]["translation"]
    return translated_text
