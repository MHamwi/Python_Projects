from googletrans import Translator

def translate_arabic_to_english(text):
    translator = Translator()
    
    try:
        translation = translator.translate(text, src='ar', dest='en')
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    arabic_text = "مرحبًا، كيف حالك؟"
    
    translated_text = translate_arabic_to_english(arabic_text)
    
    if translated_text:
        print(f"Arabic: {arabic_text}")
        print(f"English: {translated_text}")
    else:
        print("Translation failed.")