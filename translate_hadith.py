# This Python file uses the following encoding: utf-8
import http.client
import json
import googletrans 
import sys
import re
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

# Test the function
arabic_sentence = 'عَنْ أَمِيرِ الْمُؤْمِنِينَ أَبِي حَفْصٍ عُمَرَ بْنِ الْخَطَّابِ رَضِيَ اللهُ عَنْهُ قَالَ: سَمِعْتُ رَسُولَ اللَّهِ صلى الله عليه وسلم يَقُولُ: " إنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إلَى اللَّهِ وَرَسُولِهِ فَهِجْرَتُهُ إلَى اللَّهِ وَرَسُولِهِ، وَمَنْ كَانَتْ هِجْرَتُهُ لِدُنْيَا يُصِيبُهَا أَوْ امْرَأَةٍ يَنْكِحُهَا فَهِجْرَتُهُ إلَى مَا هَاجَرَ إلَيْهِ". رَوَاهُ إِمَامَا الْمُحَدِّثِينَ أَبُو عَبْدِ اللهِ مُحَمَّدُ بنُ إِسْمَاعِيل بن إِبْرَاهِيم بن الْمُغِيرَة بن بَرْدِزبَه الْبُخَارِيُّ الْجُعْفِيُّ [رقم:1]، وَأَبُو الْحُسَيْنِ مُسْلِمٌ بنُ الْحَجَّاج بن مُسْلِم الْقُشَيْرِيُّ النَّيْسَابُورِيُّ [رقم:1907] رَضِيَ اللهُ عَنْهُمَا فِي "صَحِيحَيْهِمَا" اللذَينِ هُمَا أَصَحُّ الْكُتُبِ الْمُصَنَّفَةِ.'
arabic_sentence = araby.strip_diacritics(arabic_sentence)

# dictionary  = translate_arabic_sentence(arabic_sentence)
dictionary = {'عن': 'About', 'أمير': 'Prince', 'المؤمنين': 'Believers', 'أبي': 'My Father', 'حفص': 'Hamper', 'عمر': 'Omar', 'بن': 'The son of', 'الخطاب': 'the speech', 'رضي': 'satisfied', 'الله': 'Allah', 'عنه': 'about him', 'قال': 'He said', 'سمعت': 'I heard', 'رسول': 'messenger', 'صلى': 'pray', 'عليه': 'on him', 'وسلم': 'Greet', 'يقول': 'Says', 'إنما': 'But', 'الأعمال': 'Business', 'بالنيات': 'With intentions', 'وإنما': 'But but', 'لكل': 'for every', 'امرئ': 'Person', 'ما': 'what', 'نوى': 'Intend', 'فمن': 'Not', 'كانت': 'She was', 'هجرته': 'Migrate', 'إلى': 'to me', 'ورسوله': 'And his Messenger', 'فهجرته': 'I migrate it', 'ومن': 'And from', 'لدنيا': 'Worldly', 'يصيبها': 'It affects it', 'أو': 'or', 'امرأة': 'woman', 'ينكحها': 'Blind it', 'هاجر': 'Emigrated', 'إليه': 'mechanism', 'رواه': 'Narrate', 'إماما': 'Imam', 'المحدثين': 'Modernist', 'أبو': 'Father', 'عبد': 'Slave', 'محمد': 'Mohammed', 'إسماعيل': 'Ismael', 'إبراهيم': 'Ibrahim', 'المغيرة': 'Heaving', 'بردزبه': 'Bardahbah', 'البخاري': 'Bukhari', 'الجعفي': 'Jaafi', 'رقم': 'number', '1': '1', 'وأبو': 'And Abu', 'الحسين': 'ELHussein', 'مسلم': 'Muslim', 'الحجاج': 'Pilgrims', 'القشيري': 'Al -Qushairi', 'النيسابوري': 'Nisaburi', '1907': '1907', 'عنهما': 'About them', 'في': 'in', 'صحيحيهما': 'Correct them', 'اللذين': 'who', 'هما': 'They', 'أصح': 'More correct', 'الكتب': 'Books', 'المصنفة': 'Classified'}
json_data = json.dumps(dictionary)
with open("dictionary.json", "w") as json_file:
    json.dump(dictionary, json_file)

with open("dictionary.json", "r") as file:
    data = json.load(file)
    print(data)
# print(dictionary)


# words_json = json.dumps(words_dict)

# # Set the headers for the Contentful API
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer <ACCESS_TOKEN>"
# }

# # Set the endpoint for the Contentful API
# endpoint = "https://api.contentful.com/spaces/u2mxtfs4ey3o/entries"

# # Post the JSON object to the Contentful API
# response = requests.post(endpoint, headers=headers, data=words_json)

# # Check the status code of the response
# if response.status_code == 200:
#     print("JSON object successfully posted to Contentful")
# else:
#     print("Error posting JSON object to Contentful: ", response.status_code)