# This Python file uses the following encoding: utf-8
import http.client
import json
import googletrans 
import sys
import re
import arabic_reshaper
import pyarabic.araby as araby
import io

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

print("stripping diacritics")
# Test the function
arabic_sentence = '''
عَنْ أَبِي عَبْدِ الرَّحْمَنِ عَبْدِ اللَّهِ بْنِ مَسْعُودٍ رَضِيَ اللهُ عَنْهُ قَالَ: حَدَّثَنَا رَسُولُ اللَّهِ صلى الله عليه و سلم -وَهُوَ الصَّادِقُ الْمَصْدُوقُ-: "إنَّ أَحَدَكُمْ يُجْمَعُ خَلْقُهُ فِي بَطْنِ أُمِّهِ أَرْبَعِينَ يَوْمًا نُطْفَةً، ثُمَّ يَكُونُ عَلَقَةً مِثْلَ ذَلِكَ، ثُمَّ يَكُونُ مُضْغَةً مِثْلَ ذَلِكَ، ثُمَّ يُرْسَلُ إلَيْهِ الْمَلَكُ فَيَنْفُخُ فِيهِ الرُّوحَ، وَيُؤْمَرُ بِأَرْبَعِ كَلِمَاتٍ: بِكَتْبِ رِزْقِهِ، وَأَجَلِهِ، وَعَمَلِهِ، وَشَقِيٍّ أَمْ سَعِيدٍ؛ فَوَاَللَّهِ الَّذِي لَا إلَهَ غَيْرُهُ إنَّ أَحَدَكُمْ لَيَعْمَلُ بِعَمَلِ أَهْلِ الْجَنَّةِ حَتَّى مَا يَكُونُ بَيْنَهُ وَبَيْنَهَا إلَّا ذِرَاعٌ فَيَسْبِقُ عَلَيْهِ الْكِتَابُ فَيَعْمَلُ بِعَمَلِ أَهْلِ النَّارِ فَيَدْخُلُهَا. وَإِنَّ أَحَدَكُمْ لَيَعْمَلُ بِعَمَلِ أَهْلِ النَّارِ حَتَّى مَا يَكُونُ بَيْنَهُ وَبَيْنَهَا إلَّا ذِرَاعٌ فَيَسْبِقُ عَلَيْهِ الْكِتَابُ فَيَعْمَلُ بِعَمَلِ أَهْلِ الْجَنَّةِ فَيَدْخُلُهَا".
'''
arabic_sentence = araby.strip_diacritics(arabic_sentence)
reshaped_text = arabic_reshaper.reshape(arabic_sentence)
print("translating")
dictionary  = translate_arabic_sentence(reshaped_text)
# APPEND
print("appending JSON")
with open('dictionary.json', 'a', encoding='utf8') as file:
    # use json.dump to write the new data to the file
    json.dump(dictionary, file, indent=None, ensure_ascii=False)
    # add a newline character to write the next item on a new line
    file.write('\n')
# print(dictionary)
