import contentful
import sys
import io
import http.client
import json
import googletrans 
import re
from decouple import config

spaceId = config('CONTENTFUL_SPACE_ID')
accessKey = config('CONTENTFUL_ACCESS_KEY')



# Make sure print() uses utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="UTF-8")

def translate_arabic_sentence(sentence):
    # Split the sentence into words
    words = re.findall(r'\b\w+\b', sentence)
    
    # Initialize empty dictionary
    translation_dict = {}
    
    # Use Google Translate to translate each word
    translator = googletrans.Translator()
    for word in words:
        translation = translator.translate(word, src='ar', dest='en').text
        translation_dict[word] = translation
    
    return translation_dict

entryID = "53sOzBeTB6U1nYLpq88liy"
client = contentful.Client(spaceId, accessKey)



print(translate_arabic_sentence( client.entry(entryID).arabic_matn ))

entries = client.entries()
# goes through all the entries and checks if they have an arabic dictionary
# if it doesnt it translates the arabic_matn and eventually will post into the arabic_dict field
# in JSON format so that we can use it in the page
# the problem is that the computer currently cant read the arabic we have in the matn field
# we need to pull from sunnah.com and get the unformatted arabic which works better
for entry in entries:
    if getattr(entry, 'arabic_dict', '') == "":
        print("dict is empty")
        # print(translate_arabic_sentence(getattr(entry, 'arabic_matn', '')))
    else:
        print("FILLED")