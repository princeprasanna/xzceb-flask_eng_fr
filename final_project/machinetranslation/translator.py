import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_transator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

language_transator.set_service_url(url)

def english_to_french(english_text):
    """This method is used to translate text from English to French"""
    translation = language_transator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """This method is used to translate text from French to English"""
    translation = language_transator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text